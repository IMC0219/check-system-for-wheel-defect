# your_main_window.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from ui_wizardpage import Ui_WizardPage  # 导入转换后的UI类

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WizardPage()
        self.ui.setupUi(self)  # 直接设置UI
        
        # 剩余逻辑同上...
        self.ui.pushButton.clicked.connect(self.handle_click)

    @Slot()
    def handle_click(self):
        print("Button clicked!")