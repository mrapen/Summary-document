from PySide6.QtWidgets import QMainWindow, QFileDialog
from src.design.ui_mainwin import Ui_MainWindow
from src.convert import ConvertToText
from src.chatgpt import SummarizeWithGPT


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.document: list[str]
        self.summary: str
        self.ui.btn_open_file.clicked.connect(self.OpenFile)
        self.ui.btn_summarize.clicked.connect(self.Summarize)
        self.ui.btn_save_summary.clicked.connect(self.SaveSummary)
    

    def OpenFile(self):
        file_path = QFileDialog.getOpenFileName(self, "Open File", "", "All files (*);;PDF file (*.pdf);; DOCX files (*.docx);; TXT files (*.txt)")[0]
        if file_path == "": return
        self.ui.le_path.setText(str(file_path))
        self.document = ConvertToText(file_path)
        

    def Summarize(self):
        prompt_1 = self.ui.te_prompt_1.toPlainText()
        prompt_2 = self.ui.te_prompt_2.toPlainText()
        prompt_3 =  self.ui.te_prompt_3.toPlainText()
        prompt_4 =  self.ui.te_prompt_4.toPlainText()
        lang = self.ui.cb_prompt_lang.currentText()

        self.summary = SummarizeWithGPT(self.document, prompt_1, prompt_2, prompt_3, prompt_4, lang)
        self.ui.te_response.setText(self.summary)
        

    def SaveSummary(self):
        summary_file = QFileDialog.getSaveFileName(self,"Save File","","All Files(*);;Text Files(*.txt)")[0]
        if summary_file == "": return
        if self.summary is not None:
            with open(summary_file, "w+", encoding='utf-8') as file:
                file.write(self.summary)
        else:
            print("Summary is None. Check your summary generation logic.")

        
