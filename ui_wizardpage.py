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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QPushButton,
    QSizePolicy, QWidget, QWizardPage)

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        if not WizardPage.objectName():
            WizardPage.setObjectName(u"WizardPage")
        WizardPage.resize(547, 338)
        self.graphicsView = QGraphicsView(WizardPage)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(40, 70, 256, 192))
        self.label = QLabel(WizardPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 35, 81, 21))
        self.check_start_button = QPushButton(WizardPage)
        self.check_start_button.setObjectName(u"check_start_button")
        self.check_start_button.setGeometry(QRect(330, 180, 121, 81))
        self.image_input_button = QPushButton(WizardPage)
        self.image_input_button.setObjectName(u"image_input_button")
        self.image_input_button.setGeometry(QRect(330, 70, 121, 81))

        self.retranslateUi(WizardPage)

        QMetaObject.connectSlotsByName(WizardPage)
    # setupUi

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QCoreApplication.translate("WizardPage", u"WizardPage", None))
        self.label.setText(QCoreApplication.translate("WizardPage", u"\u56fe\u7247:", None))
        self.check_start_button.setText(QCoreApplication.translate("WizardPage", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.image_input_button.setText(QCoreApplication.translate("WizardPage", u"\u5bfc\u5165\u6587\u4ef6", None))
    # retranslateUi

