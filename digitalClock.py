# PyQt5 Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel , QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    
  def initUI(self):
    pass
  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  clock = DigitalClock()
  clock.show()
  sys.exit(app.exec_())