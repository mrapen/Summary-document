import g4f
import src.config as cfg
import copy

def SummarizeWithGPT(document: list[str],
                     document_type: str,
                     analysis_purpose: str,
                     response_format: str,
                     additional_requirements: str,
                     prompt_lang: str)->str:
    
    if len(document) == 0 or document_type == "" or analysis_purpose == "" or response_format == "" or additional_requirements == "":
        return

    summ_frag = ""

    msg = copy.deepcopy(cfg.message[prompt_lang]["Message"][0])
    msg["content"] = msg["content"] \
        .format(document_type,analysis_purpose,response_format,additional_requirements)
    
    frag = copy.deepcopy(cfg.message[prompt_lang]["Fragment"][0])
    for chunk in document:
        cf = copy.deepcopy(frag)
        cf["content"] = cf["content"].format(chunk)
        response = g4f.ChatCompletion.create(
            model=cfg.engine,
            messages=[msg,cf],
            stream=True
        )
        for part in response:
            summ_frag += part
        summ_frag += "\f"
        
    summ = copy.deepcopy(cfg.message[prompt_lang]["Summarize"][0])
    summ["content"] = summ["content"].format(summ_frag)
    res = g4f.ChatCompletion.create(
        model=cfg.engine,
        messages=[msg, summ],
    )

    output = ""
    for part in res:
        output += part

    return output
    
