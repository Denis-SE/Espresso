from PyQt5 import uic
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee')
        self.cur = self.con.cursor()
        self.button.clicked.connect(self.cof)
        self.boxes = [['ID', self.cBox0], ['name_of_the_variety', self.cBox1], ['degree_of_roasting', self.cBox2],
                      ['ground_or_in_grains', self.cBox3], ['description_of_the_taste', self.cBox4],
                      ['price', self.cBox5], ['packing_volume', self.cBox6]]

    def cof(self):
        line = []
        for box in self.boxes:
            if box[1].currentText() != 'None':
                line = [box[0], box[1].currentText()]
                break
        if len(line) > 0:
            text = self.cur.execute(f"""SELECT * FROM cofe WHERE {line[0]} = ?""", (line[1], )).fetchall().__str__()
            self.espresso_label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
