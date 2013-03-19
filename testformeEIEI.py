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
        p.setBrush(QColor(255, 0, 0))
        p.drawPolygon([
            QPoint( 100, 100), QPoint(100, 200),
            QPoint(200, 200), QPoint(200, 100),
        ])
        
        p.end()

def main():
    app = QApplication(sys.argv)
    
    w=Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())