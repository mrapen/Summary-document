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
        self.ui.btn_open_file.clicked.connect(self.OpenFile)
        self.ui.btn_summarize.clicked.connect(self.Summarize)
    

    def OpenFile(self):
        file_path = QFileDialog.getOpenFileName(self, "Open File", "", "All files (*);;PDF file (*.pdf);; DOC files (*.doc);; DOCX files (*.docx)")[0]
        self.ui.le_path.setText(str(file_path))
        self.document = ConvertToText(file_path)

    def Summarize(self):
        summary: str = SummarizeWithGPT(self.document, self.ui.te_prompt_1.toPlainText(), self.ui.te_prompt_2.toPlainText(), self.ui.te_prompt_3.toPlainText(), self.ui.te_prompt_4.toPlainText())
        summary_file = QFileDialog.getSaveFileName(self,"Save File","","All Files(*);;Text Files(*.txt)")[0]
        if summary is not None:
            with open(summary_file, "w+", encoding='utf-8') as file:
                file.write(summary)
        else:
            print("Summary is None. Check your summary generation logic.")

        
