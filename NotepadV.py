import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QPushButton,QVBoxLayout,QFileDialog,QLabel



class Notepad(QWidget):
    def __init__(self):
        super(Notepad,self).__init__()
        self.text = QTextEdit(self)
        self.clr = QPushButton('Clear')
        self.opn = QPushButton('Open')
        self.save = QPushButton('Save')
        self.lbl = QLabel('Clean')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr)
        layout.addWidget(self.opn)
        layout.addWidget(self.save)
        layout.addWidget(self.lbl)

        self.clr.clicked.connect(self.clear_text)
        self.opn.clicked.connect(self.opn_file)
        self.save.clicked.connect(self.sv_file)
        self.text.textChanged.connect(self.text_length)
        self.text.textChanged.connect(self.clr_statue)

        self.setLayout(layout)
        self.setWindowTitle("Nemopad")

        self.show()

    def clear_text(self):
        self.text.clear()

    def opn_file(self):
        path = QFileDialog.getOpenFileName(self,'select a file','')
        try:
            if path:
                file = open(path[0],'r')
                text = file.readlines()
                text_to_print = ''
                for line in text:
                    text_to_print+=line
                self.text.setText(text_to_print)
        except:
            print('You did not choose a file')

    def sv_file(self):
        try:
            path = QFileDialog.getSaveFileName(self,'name the file','')
            with open(path[0],'w') as f:
                text = self.text.toPlainText()
                f.write(text)
        except:
            print('You did not save yet!')

    def text_length(self):
        text = self.text.toPlainText()
        self.lbl.setText('Letters: {}'.format(len(text)))

    def clr_statue(self):
        txt = self.text.toPlainText()
        if len(txt) == 0:
            self.clr.setEnabled(False)
        else:
            self.clr.setEnabled(True)

app = QApplication(sys.argv)
window = Notepad()
sys.exit(app.exec_())