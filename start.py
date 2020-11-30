import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Zamknij', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Zamknij program')
        exitAct.triggered.connect(qApp.quit)

        poziomyAct = QAction(
            QIcon('sugar-blood-level.png'), '&Dodaj pomiar', self)
        poziomyAct.setShortcut('Ctrl+C')
        poziomyAct.setStatusTip('Dodaj nowy pomiar poziomu cukru')

        pokazPoziomy = QAction(QIcon('wyniki.png'),
                               '&Sprawdź moje pomiary', self)
        pokazPoziomy.setShortcut('Ctrl+S')
        pokazPoziomy.setStatusTip('Wyświetl wszystkie poziomy cukru')

        wagaZapisz = QAction(QIcon('waga.png'), '&Dodaj nową wagę', self)
        wagaZapisz.setStatusTip(
            'Dodaj wagę ciała, aby mieć kontrolę nad masą ciała. Zalecane jest co tygodniowe ważenie.')

        wagaPokaz = QAction(QIcon('wynikiwazenia.png'),
                            '&Pokaż wyniki ważenia', self)
        wagaZapisz.setStatusTip(
            'Sprawdź swoje wyniki ważenia, kontroluj wagę poprzez swoje BMI')

        bmiPolicz = QAction(QIcon('bmi.png'), '&Policz BMI', self)
        bmiPolicz.setStatusTip(
            'Sprawdź swoje BMI i bądź na bierząco z wynikami. Kontrola wagi przy cukrzycy jest bardzo ważna')

        self.statusBar()

        menubar = self.menuBar()
        cukierMenu = menubar.addMenu('&Cukier')
        cukierMenu.addAction(poziomyAct)
        cukierMenu.addAction(pokazPoziomy)

        wagaMenu = menubar.addMenu('&Waga')
        wagaMenu.addAction(wagaZapisz)
        wagaMenu.addAction(wagaPokaz)
        wagaMenu.addAction(bmiPolicz)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('sugar-blood-level.png'))
        self.setWindowTitle('Simple menu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
