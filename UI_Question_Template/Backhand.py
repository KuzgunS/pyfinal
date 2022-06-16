"""@package docstring
    Backhand module for connections and functions of UI.
"""

from UI import Ui_MainWindow # in the same directory, import Ui_MainWindow class in the file and module Image_Operator
from PyQt5 import QtWidgets

class Operate(QtWidgets.QMainWindow):
 
 
    def __init__(self):
        """The constructor"""
        super(Operate,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        

        self.ui.comboBox_run_settings.activated[str].connect(self.onActivated)
        self.ui.lineEdit_number.textChanged[str].connect(self.onChanged)
        self.ui.pushButton_run.clicked.connect(self.run)

    def onActivated(self,text):
            self.choice=text
            print(self.choice)
            self.ui.label_status.setText(self.choice + " option is chosen")


    def onChanged(self,text):
        try:
            self.input_text=int(text)   
            print(self.input_text)
        except ValueError:
            print("ERROR: you need to enter integer only")
            self.ui.label_status.setText("Value Error m8")

    def run(self):
        self.calculate_primes(self.input_text)
        self.list_to_string(self.primes)
        if self.choice == "Print the text box":
            self.print_text_box()
        elif self.choice == "Write to file":
            self.print_file()
            

    def print_text_box(self):
        self.ui.textEdit_primes.setText(self.my_str)
    
    def print_file(self):
        filename = "primes_until_"+ str(self.input_text)+ ".txt"
        outfile = open(filename,'w')
        outfile.write("XDD\n")
        outfile.write(self.my_str + "\n")
        outfile.close()
        
    def calculate_primes(self,upper_limit):
        n=upper_limit
        self.primes = []
        for i in range (2, n+1):
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                self.primes.append(i)
        print(self.primes)

    def list_to_string(self,list):
        self.my_str = '\n'.join([str(item) for item in list]) 