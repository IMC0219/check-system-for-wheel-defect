# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import QMainWindow, QFileDialog, QGraphicsPixmapItem,QGraphicsScene,QWizardPage
from PySide6.QtGui import QPixmap, QImage
from ui_wizardpage import Ui_WizardPage
from model_api import YOLOv8Detector
import cv2

class MainWindow(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WizardPage()  # 自动生成的UI类
        self.ui.setupUi(self)

        # 连接信号槽
        self.ui.image_input_button.clicked.connect(self.load_image)
        self.ui.check_start_button.clicked.connect(self.run_detection)

        # 初始化图像显示场景
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def load_image(self):
        """加载轮毂图像"""
        path, _ = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")
        if path:
            # 使用OpenCV读取（保留原始数据用于检测）
            self.cv_image = cv2.imread(path)

            # 转换为Qt可显示格式
            rgb_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qt_image = QImage(rgb_image.data, w, h, ch*w, QImage.Format_RGB888)

            # 显示图像
            self.scene.clear()
            pixmap = QPixmap.fromImage(qt_image)
            self.scene.addPixmap(pixmap)
            self.ui.graphicsView.fitInView(self.scene.itemsBoundingRect())

    def run_detection(self):
        """执行缺陷检测（示例）"""
        # 获取检测参数（实际项目中从UI控件读取）
        threshold_conf = self.ui.SpinBox_conf.value()
        threshold_iou = self.ui.SpinBox_iou.value()

        # 调用检测算法（伪代码）
        defects = YOLOv8Detector.detect(self.cv_image)

        # 绘制检测结果
        result_img = YOLOv8Detector.draw_defects(self.cv_image, defects)  # 在图像上标记缺陷

        # 更新表格(回头看看能不能加)
        #self.ui.defectTable.setRowCount(len(defects))
        #for i, defect in enumerate(defects):
        #    self.ui.defectTable.setItem(i, 0, QTableWidgetItem(defect.type))
        #    self.ui.defectTable.setItem(i, 1, QTableWidgetItem(str(defect.x)))
            # ... 其他列

        # 更新状态
        #self.ui.lbStatus.setText(f"发现 {len(defects)} 处缺陷")

