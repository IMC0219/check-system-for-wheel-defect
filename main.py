# your_main_window.py
import sys
from PySide6.QtWidgets import QMainWindow,QApplication
from PySide6.QtCore import Slot
from ui_wizardpage import Ui_WizardPage  # 导入转换后的UI类
from windowlogic import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.setWindowTitle("Your Application Name")  # 设置窗口标题
    window.resize(800, 600)  # 可选：设置初始大小
    window.show()
    
    sys.exit(app.exec())