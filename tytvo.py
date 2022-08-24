from sys import *
from PyQt5. QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QLabel, QVBoxLayout,QHBoxLayout,  QLineEdit,QRadioButton,QButtonGroup
from PyQt5 import QtGui

price1 = 250
price11 = 0
class BeginWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Магазин чогось")
        self.resize(1200,1200)
        # self.setStyleSheet("background-color: rgb(240, 100, 185);")
        self.v = QVBoxLayout()
        self.text1 = QLabel(self)
        self.text1.setText("Привіт, дякуємо що завітали до нас,\n вам спочатку потрібно пройти капчу \n щоб перейти до нашого магазину,\n бажаємо вам приємних покупок!!!")
        self.text1.show()
        self.v.addWidget(self.text1,alignment = Qt.AlignCenter)
        self.text1.setFont(QtGui.QFont("callibri",25))
        

        self.but = QPushButton(self)
        self.but.setText("Натисніть щоб почати проходження капчі")
        self.but.show()
        self.v.addWidget(self.but,alignment = Qt.AlignCenter) 
        self.but.setFont(QtGui.QFont("callibri",25))
        self.setLayout(self.v)

class KapckaWin(QWidget):
    def __init__(self):
        super(KapckaWin,self).__init__()
        self.setWindowTitle("КАПЧА")
        self.resize(400,300)
        self.h = QHBoxLayout(self)
        self.v1 = QVBoxLayout(self)
        self.v2 = QVBoxLayout(self)
        self.v3 = QVBoxLayout(self)
        self.b = QLabel()
        self.v1.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b = QLabel()
        self.v1.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b = QLabel()
        self.v1.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b = QLabel()
        self.v3.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b = QLabel()
        self.v3.addWidget(self.b, alignment = Qt.AlignCenter)


        self.b = QLabel()
        self.v3.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b = QLabel("У вас є одна спроба!!!")
        self.v2.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b = QLabel("Хто зайвий?")
        self.v2.addWidget(self.b, alignment = Qt.AlignCenter)
        self.b.setFont(QtGui.QFont("Courier New",25))


        self.b = QLabel()
        self.v2.addWidget(self.b, alignment = Qt.AlignCenter)

        self.picture = QtGui.QPixmap("1_cat_for_kapca.png")
        self.picture1 = QtGui.QPixmap("2_cat_for_kapca.png")
        self.picture2 = QtGui.QPixmap("dog.png")
        self.pic = QLabel()
        self.pic1 = QLabel()
        self.pic2 = QLabel()
        self.pic.setPixmap(self.picture)
        self.pic1.setPixmap(self.picture1)
        self.pic2.setPixmap(self.picture2)

        self.v1.addWidget(self.pic,alignment=Qt.AlignLeft)
        self.v3.addWidget(self.pic1,alignment=Qt.AlignRight)
        self.v2.addWidget(self.pic2,alignment=Qt.AlignCenter)
        


        self.but1 = QRadioButton()
        self.v1.addWidget(self.but1,alignment = Qt.AlignLeft)
        self.but1.setFont(QtGui.QFont("callibri",25))

        self.but2 = QRadioButton()
        self.v2.addWidget(self.but2,alignment = Qt.AlignCenter)
        self.but2.setFont(QtGui.QFont("callibri",25))


        self.but3 = QRadioButton()
        self.v3.addWidget(self.but3,alignment = Qt.AlignRight)
        self.but3.setFont(QtGui.QFont("callibri",25))

        self.b = QLabel()
        self.v1.addWidget(self.b, alignment = Qt.AlignCenter)
        
        self.b = QLabel()
        self.v3.addWidget(self.b, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.h.addLayout(self.v1)
        self.h.addLayout(self.v2)
        self.h.addLayout(self.v3)
        self.setLayout(self.h)
class Store(QWidget):
    def __init__(self):
        super(Store,self).__init__()
        self.setWindowTitle("Store")
        self.resize(1400,1200)

        self.h1 = QHBoxLayout(self)

        self.v1 = QVBoxLayout(self)
        self.v2 = QVBoxLayout(self)
        self.v3 = QVBoxLayout(self)    
        self.v4 = QVBoxLayout(self) 
        self.v5 = QVBoxLayout(self) 


        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)



        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)


        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)


        self.picture1 = QtGui.QPixmap("gta5.png")#1
        self.picture2 = QtGui.QPixmap("Forza.png")#2
        self.picture3 = QtGui.QPixmap("sot.png")#3
        self.picture4 = QtGui.QPixmap("r6.png")#4

        self.pic1 = QLabel()
        self.pic2 = QLabel()
        self.pic3 = QLabel()
        self.pic4 = QLabel()

        self.pic1.setPixmap(self.picture1)
        self.pic2.setPixmap(self.picture2)
        self.pic3.setPixmap(self.picture3)
        self.pic4.setPixmap(self.picture4)

        self.v1.addWidget(self.pic1,alignment=Qt.AlignCenter)#1
        self.v2.addWidget(self.pic2,alignment=Qt.AlignCenter)#2
        self.v3.addWidget(self.pic3,alignment=Qt.AlignCenter)#3
        self.v4.addWidget(self.pic4,alignment=Qt.AlignCenter)#4

        self.but1 = QPushButton(str(price1)+"$")
        self.v1.addWidget(self.but1,alignment = Qt.AlignCenter)#1

        self.but2 = QPushButton(str(price1)+"$")
        self.v2.addWidget(self.but2,alignment = Qt.AlignCenter)#2

        self.but3 = QPushButton(str(price1)+"$")
        self.v3.addWidget(self.but3,alignment = Qt.AlignCenter)#3

        self.but4 = QPushButton(str(price1)+"$")
        self.v4.addWidget(self.but4,alignment = Qt.AlignCenter)#4

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        

        self.picture5 = QtGui.QPixmap("dt.png")#11
        self.picture6 = QtGui.QPixmap("kb.png")#22
        self.picture7 = QtGui.QPixmap("str.png")#33
        self.picture8 = QtGui.QPixmap("ark.png")#44

        self.pic5 = QLabel()
        self.pic6 = QLabel()
        self.pic7 = QLabel()
        self.pic8 = QLabel()

        self.pic5.setPixmap(self.picture5)
        self.pic6.setPixmap(self.picture6)
        self.pic7.setPixmap(self.picture7)
        self.pic8.setPixmap(self.picture8)

        self.v1.addWidget(self.pic5,alignment=Qt.AlignCenter)#11
        self.v2.addWidget(self.pic6,alignment=Qt.AlignCenter)#22
        self.v3.addWidget(self.pic7,alignment=Qt.AlignCenter)#33
        self.v4.addWidget(self.pic8,alignment=Qt.AlignCenter)#44

        self.but5 = QPushButton(str(price1)+"$")
        self.v1.addWidget(self.but5,alignment = Qt.AlignCenter)#11

        self.but6 = QPushButton(str(price1)+"$")
        self.v2.addWidget(self.but6,alignment = Qt.AlignCenter)#22

        self.but7 = QPushButton(str(price1)+"$")
        self.v3.addWidget(self.but7,alignment = Qt.AlignCenter)#33

        self.but8 = QPushButton(str(price1)+"$")
        self.v4.addWidget(self.but8,alignment = Qt.AlignCenter)#44

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)


        self.picture9 = QtGui.QPixmap("dn2.png")#111
        self.picture10 = QtGui.QPixmap("etr2.png")#222
        self.picture11 = QtGui.QPixmap("rdr2.png")#333
        self.picture12 = QtGui.QPixmap("gdw.png")#444

        self.pic9 = QLabel()
        self.pic10 = QLabel()
        self.pic11 = QLabel()
        self.pic12 = QLabel()

        self.pic9.setPixmap(self.picture9)
        self.pic10.setPixmap(self.picture10)
        self.pic11.setPixmap(self.picture11)
        self.pic12.setPixmap(self.picture12)

        self.v1.addWidget(self.pic9,alignment=Qt.AlignCenter)#111
        self.v2.addWidget(self.pic10,alignment=Qt.AlignCenter)#222
        self.v3.addWidget(self.pic11,alignment=Qt.AlignCenter)#333
        self.v4.addWidget(self.pic12,alignment=Qt.AlignCenter)#444

        self.but9 = QPushButton(str(price1)+"$")
        self.v1.addWidget(self.but9,alignment = Qt.AlignCenter)#111

        self.but10 = QPushButton(str(price1)+"$")
        self.v2.addWidget(self.but10,alignment = Qt.AlignCenter)#222

        self.but11 = QPushButton(str(price1)+"$")
        self.v3.addWidget(self.but11,alignment = Qt.AlignCenter)#333

        self.but12 = QPushButton(str(price1)+"$")
        self.v4.addWidget(self.but12,alignment = Qt.AlignCenter)#444

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)



        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

    
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel("Ціна вашого кошика")
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1.setFont(QtGui.QFont("Courier New",15))

        self.pokupka = 0
        self.price = QLabel(str(self.pokupka))
        self.v5.addWidget(self.price, alignment = Qt.AlignCenter)#888
        self.price.setFont(QtGui.QFont("Courier New",15))
        

        self.but13 = QPushButton("Buy")
        self.v5.addWidget(self.but13,alignment = Qt.AlignCenter)#888
        self.but13.setFont(QtGui.QFont("Courier New",15))

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)


        self.h1.addLayout(self.v1)
        self.h1.addLayout(self.v2)
        self.h1.addLayout(self.v3)
        self.h1.addLayout(self.v4)
        self.h1.addLayout(self.v5)
        self.setLayout(self.h1)

class Skam(QWidget):
    def __init__(self):
        super(Skam,self).__init__()
        self.setWindowTitle("Оплата")
        self.resize(600,600)
        self.h1 = QHBoxLayout(self)
        self.v0 = QVBoxLayout(self)
        self.v1 = QVBoxLayout(self)
        self.v2 = QVBoxLayout(self)
        self.v3 = QVBoxLayout(self)
        self.v4 = QVBoxLayout(self)

        self.b1 = QLabel()
        self.v0.addWidget(self.b1, alignment = Qt.AlignCenter)
        
        self.b1 = QLabel()
        self.v0.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.ed1 = QLineEdit("Номер карти")
        self.v1.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(400)
        self.ed1.setMaxLength(16)

        self.ed1 = QLineEdit("Ім'я")
        self.v3.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(400)

        self.ed1 = QLineEdit("Дата")
        self.v1.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(300)
        self.ed1.setMaxLength(4)

        self.ed1 = QLineEdit("CVV")
        self.v3.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(300)
        self.ed1.setMaxLength(3)

        self.but0 = QPushButton("-->Сюди<--")
        self.v2.addWidget(self.but0,alignment = Qt.AlignBottom)


        
        

        # self.b1 = QLabel()
        # self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.h1.addLayout(self.v0)
        self.h1.addLayout(self.v1)
        self.h1.addLayout(self.v2)
        self.h1.addLayout(self.v3)
        self.h1.addLayout(self.v4)
        
        self.setLayout(self.h1)

class Skam1(QWidget):
    def __init__(self):
        super(Skam1,self).__init__()
        self.setWindowTitle("Єх")
        self.resize(600,600)
        self.h1 = QVBoxLayout(self)

        self.rr = QLabel("Ми вкрали ваші гроші :)\n Виражаємо величезну подяку вам за ваші гроші!!!")
        self.h1.addWidget(self.rr,alignment = Qt.AlignCenter)
        self.rr.setFont(QtGui.QFont("Courier New",15))

        self.but = QPushButton("Sad :(")
        self.h1.addWidget(self.but,alignment = Qt.AlignBottom)

        self.setLayout(self.h1)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')
        
        self.v1 = QVBoxLayout(self)
        self.setLayout(self.v1)
    def show_window_1(self):
        self.w1 = BeginWin()
        self.w1.but.clicked.connect(self.show_window_2)
        self.w1.but.clicked.connect(self.w1.close)
        self.w1.show()
    def click1(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but1.setVisible(False)
    def click2(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but2.setVisible(False)
    def click3(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but3.setVisible(False)
    def click4(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but4.setVisible(False)
    def click5(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but5.setVisible(False)
    def click6(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but6.setVisible(False)
    def click7(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but7.setVisible(False)
    def click8(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but8.setVisible(False)
    def click9(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but9.setVisible(False)
    def click10(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but10.setVisible(False)
    def click11(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but11.setVisible(False)
    def click12(self):
        self.w3.pokupka += 250
        self.w3.price.setText(str(self.w3.pokupka)+"$")
        self.w3.but12.setVisible(False)


    def show_window_2(self):
        self.w2 = KapckaWin()
        self.w2.show()
        self.w2.but1.clicked.connect(self.show_window_1)
        self.w2.but2.clicked.connect(self.show_window_3)
        self.w2.but3.clicked.connect(self.show_window_1)
        self.w2.but1.clicked.connect(self.w2.close)
        self.w2.but2.clicked.connect(self.w2.close)
        self.w2.but3.clicked.connect(self.w2.close)
    def show_window_3(self):
        self.w3 = Store()
        self.w3.show()
        self.w3.but1.clicked.connect(self.click1)
        self.w3.but2.clicked.connect(self.click2)
        self.w3.but3.clicked.connect(self.click3)
        self.w3.but4.clicked.connect(self.click4)
        self.w3.but5.clicked.connect(self.click5)
        self.w3.but6.clicked.connect(self.click6)
        self.w3.but7.clicked.connect(self.click7)
        self.w3.but8.clicked.connect(self.click8)
        self.w3.but9.clicked.connect(self.click9)
        self.w3.but10.clicked.connect(self.click10)
        self.w3.but11.clicked.connect(self.click11)
        self.w3.but12.clicked.connect(self.click12)

        self.w3.but13.clicked.connect(self.show_window_4)
        self.w3.but13.clicked.connect(self.w3.close)

    def show_window_4(self):
        self.w4 = Skam()
        self.w4.show()
        
        self.w4.but0.clicked.connect(self.show_window_5)
        self.w4.but0.clicked.connect(self.w4.close)
    def show_window_5(self):
        self.w5 = Skam1()
        self.w5.show()
        self.w5.but.clicked.connect(self.w5.close)
        
app = QApplication(argv)
w = MainWindow()
w.show_window_1()
exit(app.exec_())





