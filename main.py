import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Circle Drawer')

        self.button = QPushButton('Draw Circle', self)
        self.button.clicked.connect(self.drawCircle)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def paintEvent(self, event):
        if hasattr(self, 'circle_data'):
            painter = QPainter(self)
            color, x, y, diameter = self.circle_data
            painter.setBrush(color)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(x - diameter / 2, y - diameter / 2, diameter, diameter)

    def drawCircle(self):
        diameter = random.randint(50, 150)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(0, 400)
        y = random.randint(0, 400)

        self.circle_data = (color, x, y, diameter)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleDrawer()
    ex.show()
    sys.exit(app.exec_())
