#baan jae
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 0, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.setPen(QColor(1,0,1))
        p.drawPolygon([QPoint(0,0), QPoint(0,100), QPoint(50,50)])
        p.end()

def main():
    app = QApplication(sys.argv)
    
    w=Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())