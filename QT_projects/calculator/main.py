import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import*
from form import*

app = QApplication([])
window = QMainWindow()
ui = Ui_Widget()
ui.setupUi(window)
window.show()



#numlock tanıtımı
def method0():
    text=ui.label.text()
    ui.label.setText(text+"0")

def method1():
    text=ui.label.text()
    ui.label.setText(text+"1")

def method2():
    text=ui.label.text()
    ui.label.setText(text+"2")

def method3():
    text=ui.label.text()
    ui.label.setText(text+"3")

def method4():
    text=ui.label.text()
    ui.label.setText(text+"4")

def method5():
    text=ui.label.text()
    ui.label.setText(text+"5")

def method6():
    text=ui.label.text()
    ui.label.setText(text+"6")

def method7():
    text=ui.label.text()
    ui.label.setText(text+"7")

def method8():
    text=ui.label.text()
    ui.label.setText(text+"8")

def method9():
    text=ui.label.text()
    ui.label.setText(text+"9")





#matematik operatörleri tanıtımı
def method_topla():
    text=ui.label.text()
    ui.label.setText(text+"+")

def method_cikar():
    text=ui.label.text()
    ui.label.setText(text+"-")

def method_carp():
    text=ui.label.text()
    ui.label.setText(text+"*")

def method_bol():
    text=ui.label.text()
    ui.label.setText(text+"/")

def method_sil():
    ui.label.setText("")

def method_gor():
    text=ui.label.text()
    try:
        ans=eval(text)
        ui.label.setText(str(ans))
    except:
        ui.label.setText("hata")


#butonları tıklanabiilir kılmak
ui.btn0.clicked.connect(method0)
ui.btn1.clicked.connect(method1)
ui.btn2.clicked.connect(method2)
ui.btn3.clicked.connect(method3)
ui.btn4.clicked.connect(method4)
ui.btn5.clicked.connect(method5)
ui.btn6.clicked.connect(method6)
ui.btn7.clicked.connect(method7)
ui.btn8.clicked.connect(method8)
ui.btn9.clicked.connect(method9)

ui.topla.clicked.connect(method_topla)
ui.cikar.clicked.connect(method_cikar)
ui.bol.clicked.connect(method_bol)
ui.carp.clicked.connect(method_carp)

ui.sil.clicked.connect(method_sil)
ui.gor.clicked.connect(method_gor)










sys.exit(app.exec())

