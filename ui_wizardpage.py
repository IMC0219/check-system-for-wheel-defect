# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizardpage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGraphicsView, QLabel,
    QPushButton, QSizePolicy, QWidget, QWizardPage)

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        if not WizardPage.objectName():
            WizardPage.setObjectName(u"WizardPage")
        WizardPage.resize(670, 419)
        self.graphicsView = QGraphicsView(WizardPage)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(40, 70, 256, 192))
        self.label = QLabel(WizardPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 35, 81, 21))
        self.check_start_button = QPushButton(WizardPage)
        self.check_start_button.setObjectName(u"check_start_button")
        self.check_start_button.setGeometry(QRect(410, 180, 121, 81))
        self.image_input_button = QPushButton(WizardPage)
        self.image_input_button.setObjectName(u"image_input_button")
        self.image_input_button.setGeometry(QRect(330, 70, 121, 81))
        self.SpinBox_conf = QDoubleSpinBox(WizardPage)
        self.SpinBox_conf.setObjectName(u"SpinBox_conf")
        self.SpinBox_conf.setGeometry(QRect(330, 240, 62, 22))
        self.SpinBox_conf.setMaximum(1.000000000000000)
        self.SpinBox_conf.setSingleStep(0.100000000000000)
        self.SpinBox_conf.setValue(0.500000000000000)
        self.SpinBox_iou = QDoubleSpinBox(WizardPage)
        self.SpinBox_iou.setObjectName(u"SpinBox_iou")
        self.SpinBox_iou.setGeometry(QRect(330, 190, 62, 22))
        self.SpinBox_iou.setMaximum(1.000000000000000)
        self.SpinBox_iou.setSingleStep(0.100000000000000)
        self.SpinBox_iou.setValue(0.500000000000000)
        self.label_2 = QLabel(WizardPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 170, 91, 20))
        self.label_3 = QLabel(WizardPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 220, 91, 16))

        self.retranslateUi(WizardPage)

        QMetaObject.connectSlotsByName(WizardPage)
    # setupUi

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QCoreApplication.translate("WizardPage", u"WizardPage", None))
        self.label.setText(QCoreApplication.translate("WizardPage", u"\u56fe\u7247:", None))
        self.check_start_button.setText(QCoreApplication.translate("WizardPage", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.image_input_button.setText(QCoreApplication.translate("WizardPage", u"\u5bfc\u5165\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("WizardPage", u"conf\u7f6e\u4fe1\u5ea6\u533a\u95f4(0-1):", None))
        self.label_3.setText(QCoreApplication.translate("WizardPage", u"iou\u7f6e\u4fe1\u5ea6\u533a\u95f4(0-1):", None))
    # retranslateUi

