import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

    # ********** menu ustawienia
        rejestracja = QAction(QIcon('icons/user.png'), '&Rejestracja użytkownika', self)
        rejestracja.setStatusTip('Rejestracja nie jest przymusowa, jednak zarejestrowany użytkownik będzie miał więcej uprawnień')

        lekarz = QAction(QIcon('icons/lekarz.png'), '&Rejestracja lekarza', self)
        lekarz.setStatusTip('Dzięki rejestracji lekarza będziesz mógł wysyłać raporty pomiarów cukru swojemu lekarzowi')

        exitAct = QAction(QIcon('icons/exit.png'), '&Zamknij', self)
        exitAct.setStatusTip('Zamknij program')
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

    # ********** menu cukier
        poziomyAct = QAction(
            QIcon('icons/sugar-blood-level.png'), '&Dodaj pomiar', self)
        poziomyAct.setStatusTip('Dodaj nowy pomiar poziomu cukru')
        poziomyAct.setShortcut('Ctrl+D')

        pokazPoziomy = QAction(QIcon('icons/wyniki.png'),
                               '&Sprawdź moje pomiary', self)
        pokazPoziomy.setStatusTip('Wyświetl wszystkie poziomy cukru')

    # ************ menu waga
        wagaZapisz = QAction(QIcon('icons/waga.png'), '&Dodaj nową wagę', self)
        wagaZapisz.setStatusTip(
            'Dodaj wagę ciała, aby mieć kontrolę nad masą ciała. Zalecane jest co tygodniowe ważenie.')
        wagaZapisz.setShortcut('Ctrl+W')

        wagaPokaz = QAction(QIcon('icons/wynikiwazenia.png'),
                            '&Pokaż wyniki ważenia', self)
        wagaZapisz.setStatusTip(
            'Sprawdź swoje wyniki ważenia, kontroluj wagę poprzez swoje BMI')

        bmiPolicz = QAction(QIcon('icons/bmi.png'), '&Policz BMI', self)
        bmiPolicz.setStatusTip(
            'Sprawdź swoje BMI i bądź na bierząco z wynikami. Kontrola wagi przy cukrzycy jest bardzo ważna')
        bmiPolicz.setShortcut('Ctrl+B')

    # ************* menu raporty
        raporty = QAction(QIcon('icons/raport.png'), '&Raport graficzny', self)
        raporty.setStatusTip('Zobacz swoje graficzne raporty z zapisu wyników mierzenia cukru')

        raportyDrukuj = QAction(QIcon('icons/drukuj.png'), '&Drukuj raport', self)

        self.statusBar()

        menubar = self.menuBar()
        cukierMenu = menubar.addMenu('&Cukier')
        cukierMenu.addAction(poziomyAct)
        cukierMenu.addAction(pokazPoziomy)

        wagaMenu = menubar.addMenu('&Waga')
        wagaMenu.addAction(wagaZapisz)
        wagaMenu.addAction(wagaPokaz)
        wagaMenu.addAction(bmiPolicz)

        raportyMenu = menubar.addMenu('&Raporty')
        raportyMenu.addAction(raporty)
        raportyMenu.addAction(raportyDrukuj)

        fileMenu = menubar.addMenu('&Ustawienia')
        fileMenu.addAction(rejestracja)
        fileMenu.addAction(lekarz)
        fileMenu.addAction(exitAct)

    # *********** Geometria okna
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icons/sugar-blood-level.png'))
        self.setWindowTitle('Simple menu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
