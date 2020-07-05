import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QAction,qApp, QApplication, QWidget, QTextEdit,\
    QPushButton,QVBoxLayout, QHBoxLayout, QLabel,QFileDialog

class Note(QWidget):
    def __init__(self):
        super(Note, self).__init__()
        self.text = QTextEdit(self)
        self.text.setPlaceholderText("Type Here...")
        self.clr = QPushButton("Clear")
        self.opn = QPushButton("Open")
        self.sv = QPushButton("Save")
        self.lbl = QLabel("Clean")

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr)
        h_layout.addWidget(self.opn)
        h_layout.addWidget(self.sv)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.lbl)

        self.clr.clicked.connect(self.clr_text)
        self.opn.clicked.connect(self.opn_file)
        self.sv.clicked.connect(self.sv_file)
        self.text.textChanged.connect(self.text_length)
        self.text.textChanged.connect(self.clr_statue)

        self.setLayout(v_layout)
        self.setWindowTitle("Notepad")

        self.show()

    def clr_text(self):
        self.text.clear()

    def opn_file(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'select a file', '')
            if path:
                file = open(path[0],'r')
                file_text = file.readlines()
                text_to_prnt = ''
                for line in file_text:
                    text_to_prnt+= line
                self.text.setText(text_to_prnt)
        except:
            pass

    def sv_file(self):
        try:
            path = QFileDialog.getSaveFileName(self, 'pick a name', '')
            if path:
                with open(path[0],'w') as f:
                    f.write(self.text.toPlainText())
        except:
            pass

    def text_length(self):
        txt = self.text.toPlainText()
        self.lbl.setText("Letters: {}".format(len(txt)))

    def clr_statue(self):
        txt = self.text.toPlainText()
        if len(txt) == 0:
            self.clr.setEnabled(False)
        else:
            self.clr.setEnabled(True)

class menubar(QMainWindow):
    def __init__(self):
        super(menubar, self).__init__()
        self.setWindowIcon(QIcon('image/edit.png'))

        self.form_widget = Note()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        # make a menu bar
        bar = self.menuBar()
        # make main menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')
        # make actions of menus
        new_action = QAction('New',self)
        new_action.setShortcut('Ctrl+N')
        opn_action = QAction('Open',self)
        opn_action.setShortcut('Ctrl+O')
        sav_action = QAction('Save',self)
        sav_action.setShortcut('Ctrl+S')
        qut_action = QAction('Quit',self)
        qut_action.setShortcut('Ctrl+Q')

        find_action = QAction('find...',self)
        find_action.setShortcut('Ctrl+F')
        rplc_action = QAction('replace...',self)
        rplc_action.setShortcut('Ctrl+R')
        # put actions in their menus
        file.addAction(new_action)
        file.addAction(opn_action)
        file.addAction(sav_action)
        file.addAction(qut_action)
        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(rplc_action)

        # actions signals and slots
        file.triggered.connect(self.respond)

        self.setWindowTitle('MenuTry')
        self.resize(400,300)

        self.show()

    def respond(self,q):
        signal = q.text()
        if signal == 'New':
            self.form_widget.clr_text()
        elif signal == 'Save':
            self.form_widget.sv_file()
        elif signal == 'Open':
            self.form_widget.opn_file()
        elif signal == 'Quit':
            qApp.quit()




app = QApplication(sys.argv)
win = menubar()
sys.exit(app.exec_())



