# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Shop(object):
    def setupUi(self, Shop):
        Shop.setObjectName("Shop")
        Shop.resize(1360, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Shop.sizePolicy().hasHeightForWidth())
        Shop.setSizePolicy(sizePolicy)
        Shop.setMaximumSize(QtCore.QSize(1366, 768))
        Shop.setStyleSheet("QMainWindow {\n"
"    background-color: #F0F0F0;\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget#catalogWidget {\n"
"    border: 2px solid #654321;\n"
"    border-radius: 0px;\n"
"    background-color: #F5F5DC;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    font-weight: normal;\n"
"    padding: 6px;\n"
"    border: 1px solid #654321;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: #e0d5c3;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QTreeWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: 1px solid #654321;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Shop)
        self.centralwidget.setStyleSheet("QMainWindow {\n"
"    background-color:#F5F5DC;\n"
"    border: 1px solid #D2B48C;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(11, 11, 1344, 746))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageSignIn = QtWidgets.QWidget()
        self.pageSignIn.setObjectName("pageSignIn")
        self.label_signin = QtWidgets.QLabel(self.pageSignIn)
        self.label_signin.setGeometry(QtCore.QRect(530, 60, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_signin.setFont(font)
        self.label_signin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signin.setObjectName("label_signin")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.pageSignIn)
        self.lineEdit_phone.setGeometry(QtCore.QRect(490, 230, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.btn_signin = QtWidgets.QPushButton(self.pageSignIn)
        self.btn_signin.setGeometry(QtCore.QRect(490, 370, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_signin.setFont(font)
        self.btn_signin.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_signin.setObjectName("btn_signin")
        self.lineEdit_psw = QtWidgets.QLineEdit(self.pageSignIn)
        self.lineEdit_psw.setGeometry(QtCore.QRect(490, 300, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_psw.setFont(font)
        self.lineEdit_psw.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_psw.setObjectName("lineEdit_psw")
        self.btn_signup_2 = QtWidgets.QPushButton(self.pageSignIn)
        self.btn_signup_2.setGeometry(QtCore.QRect(560, 480, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_signup_2.setFont(font)
        self.btn_signup_2.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_signup_2.setObjectName("btn_signup_2")
        self.stackedWidget.addWidget(self.pageSignIn)
        self.pageSignUp = QtWidgets.QWidget()
        self.pageSignUp.setObjectName("pageSignUp")
        self.lineEdit_psw_2 = QtWidgets.QLineEdit(self.pageSignUp)
        self.lineEdit_psw_2.setEnabled(True)
        self.lineEdit_psw_2.setGeometry(QtCore.QRect(490, 270, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_psw_2.setFont(font)
        self.lineEdit_psw_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_psw_2.setObjectName("lineEdit_psw_2")
        self.lineEdit_phone_2 = QtWidgets.QLineEdit(self.pageSignUp)
        self.lineEdit_phone_2.setEnabled(True)
        self.lineEdit_phone_2.setGeometry(QtCore.QRect(490, 410, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_phone_2.setFont(font)
        self.lineEdit_phone_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_phone_2.setObjectName("lineEdit_phone_2")
        self.lineEdit_email = QtWidgets.QLineEdit(self.pageSignUp)
        self.lineEdit_email.setEnabled(True)
        self.lineEdit_email.setGeometry(QtCore.QRect(490, 340, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_signup = QtWidgets.QLabel(self.pageSignUp)
        self.label_signup.setGeometry(QtCore.QRect(530, 30, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_signup.setFont(font)
        self.label_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signup.setObjectName("label_signup")
        self.lineEdit_name = QtWidgets.QLineEdit(self.pageSignUp)
        self.lineEdit_name.setEnabled(True)
        self.lineEdit_name.setGeometry(QtCore.QRect(490, 200, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.checkBox = QtWidgets.QCheckBox(self.pageSignUp)
        self.checkBox.setGeometry(QtCore.QRect(510, 480, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox.setFont(font)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.btn_signup = QtWidgets.QPushButton(self.pageSignUp)
        self.btn_signup.setGeometry(QtCore.QRect(490, 510, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_signup.setObjectName("btn_signup")
        self.btn_signin_2 = QtWidgets.QPushButton(self.pageSignUp)
        self.btn_signin_2.setGeometry(QtCore.QRect(560, 590, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_signin_2.setFont(font)
        self.btn_signin_2.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_signin_2.setObjectName("btn_signin_2")
        self.stackedWidget.addWidget(self.pageSignUp)
        self.page_MainShop = QtWidgets.QWidget()
        self.page_MainShop.setObjectName("page_MainShop")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_MainShop)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1341, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_technolite = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_technolite.setFont(font)
        self.label_technolite.setAlignment(QtCore.Qt.AlignCenter)
        self.label_technolite.setObjectName("label_technolite")
        self.horizontalLayout.addWidget(self.label_technolite)
        self.btn_cart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cart.sizePolicy().hasHeightForWidth())
        self.btn_cart.setSizePolicy(sizePolicy)
        self.btn_cart.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_cart.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_cart.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_cart.setObjectName("btn_cart")
        self.horizontalLayout.addWidget(self.btn_cart)
        self.btn_pers_acc = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_pers_acc.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_pers_acc.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_pers_acc.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_pers_acc.setObjectName("btn_pers_acc")
        self.horizontalLayout.addWidget(self.btn_pers_acc)
        self.widget = QtWidgets.QWidget(self.page_MainShop)
        self.widget.setGeometry(QtCore.QRect(10, 80, 341, 651))
        self.widget.setStyleSheet("QWidget {\n"
"    border: 2px solid #654321;\n"
"    border-radius: 8px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_catalog = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_catalog.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_catalog.setObjectName("verticalLayout_catalog")
        self.treeWidget_category = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget_category.setStyleSheet("\n"
"QTreeWidget::item:hover {\n"
"    background-color: #e0d5c3;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #d2b48c;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeWidget::item:selected:active {\n"
"    border: none;\n"
"}\n"
"\n"
"QTreeWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: 1px solid #654321;\n"
"}")
        self.treeWidget_category.setHeaderHidden(False)
        self.treeWidget_category.setObjectName("treeWidget_category")
        self.treeWidget_category.headerItem().setText(0, "Каталог")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget_category.headerItem().setFont(0, font)
        self.verticalLayout_catalog.addWidget(self.treeWidget_category)
        self.widget_2 = QtWidgets.QWidget(self.page_MainShop)
        self.widget_2.setGeometry(QtCore.QRect(370, 80, 971, 651))
        self.widget_2.setObjectName("widget_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 971, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_pr1 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_pr1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pr1.sizePolicy().hasHeightForWidth())
        self.btn_pr1.setSizePolicy(sizePolicy)
        self.btn_pr1.setStyleSheet("QToolButton {\n"
"   background-color: white;\n"
"   border: 2px solid #654321;\n"
"   border-radius: 8px;\n"
"   color: black;\n"
"   padding: 10px;\n"
"   text-align: center;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e6e6e6;\n"
"}")
        self.btn_pr1.setText("")
        self.btn_pr1.setIconSize(QtCore.QSize(30, 30))
        self.btn_pr1.setCheckable(False)
        self.btn_pr1.setAutoRepeatInterval(100)
        self.btn_pr1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_pr1.setObjectName("btn_pr1")
        self.gridLayout.addWidget(self.btn_pr1, 0, 0, 1, 1)
        self.btn_pr2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pr2.sizePolicy().hasHeightForWidth())
        self.btn_pr2.setSizePolicy(sizePolicy)
        self.btn_pr2.setStyleSheet("QToolButton {\n"
"   background-color: white;\n"
"   border: 2px solid #654321;\n"
"   border-radius: 8px;\n"
"   color: black;\n"
"   padding: 10px;\n"
"   text-align: center;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e6e6e6;\n"
"}")
        self.btn_pr2.setText("")
        self.btn_pr2.setIconSize(QtCore.QSize(30, 30))
        self.btn_pr2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_pr2.setObjectName("btn_pr2")
        self.gridLayout.addWidget(self.btn_pr2, 0, 3, 1, 1)
        self.btn_pr3 = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pr3.sizePolicy().hasHeightForWidth())
        self.btn_pr3.setSizePolicy(sizePolicy)
        self.btn_pr3.setStyleSheet("QToolButton {\n"
"   background-color: white;\n"
"   border: 2px solid #654321;\n"
"   border-radius: 8px;\n"
"   color: black;\n"
"   padding: 10px;\n"
"   text-align: center;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e6e6e6;\n"
"}")
        self.btn_pr3.setText("")
        self.btn_pr3.setIconSize(QtCore.QSize(30, 30))
        self.btn_pr3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_pr3.setObjectName("btn_pr3")
        self.gridLayout.addWidget(self.btn_pr3, 0, 2, 1, 1)
        self.btn_pr4 = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pr4.sizePolicy().hasHeightForWidth())
        self.btn_pr4.setSizePolicy(sizePolicy)
        self.btn_pr4.setStyleSheet("QToolButton {\n"
"   background-color: white;\n"
"   border: 2px solid #654321;\n"
"   border-radius: 8px;\n"
"   color: black;\n"
"   padding: 10px;\n"
"   text-align: center;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e6e6e6;\n"
"}")
        self.btn_pr4.setText("")
        self.btn_pr4.setIconSize(QtCore.QSize(30, 30))
        self.btn_pr4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_pr4.setObjectName("btn_pr4")
        self.gridLayout.addWidget(self.btn_pr4, 6, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_MainShop)
        self.page_orders = QtWidgets.QWidget()
        self.page_orders.setObjectName("page_orders")
        self.stackedWidget.addWidget(self.page_orders)
        self.page_cart = QtWidgets.QWidget()
        self.page_cart.setObjectName("page_cart")
        self.label_cart = QtWidgets.QLabel(self.page_cart)
        self.label_cart.setGeometry(QtCore.QRect(530, 20, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_cart.setFont(font)
        self.label_cart.setStyleSheet("color: #654321;\n"
"")
        self.label_cart.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cart.setObjectName("label_cart")
        self.btn_cart_go_shop = QtWidgets.QPushButton(self.page_cart)
        self.btn_cart_go_shop.setGeometry(QtCore.QRect(310, 570, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cart_go_shop.setFont(font)
        self.btn_cart_go_shop.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_cart_go_shop.setObjectName("btn_cart_go_shop")
        self.btn_clear_cart = QtWidgets.QPushButton(self.page_cart)
        self.btn_clear_cart.setGeometry(QtCore.QRect(590, 570, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_clear_cart.setFont(font)
        self.btn_clear_cart.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_clear_cart.setObjectName("btn_clear_cart")
        self.tableWidget_cart = QtWidgets.QTableWidget(self.page_cart)
        self.tableWidget_cart.setGeometry(QtCore.QRect(30, 110, 1289, 369))
        self.tableWidget_cart.setAutoScroll(True)
        self.tableWidget_cart.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget_cart.setTabKeyNavigation(True)
        self.tableWidget_cart.setProperty("showDropIndicator", True)
        self.tableWidget_cart.setObjectName("tableWidget_cart")
        self.tableWidget_cart.setColumnCount(5)
        self.tableWidget_cart.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cart.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cart.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cart.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cart.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cart.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_cart.setHorizontalHeaderItem(4, item)
        self.tableWidget_cart.horizontalHeader().setVisible(True)
        self.tableWidget_cart.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_cart.horizontalHeader().setDefaultSectionSize(255)
        self.tableWidget_cart.horizontalHeader().setHighlightSections(True)
        self.tableWidget_cart.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_cart.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_cart.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_cart.verticalHeader().setVisible(False)
        self.tableWidget_cart.verticalHeader().setDefaultSectionSize(37)
        self.btn_export_cart = QtWidgets.QPushButton(self.page_cart)
        self.btn_export_cart.setGeometry(QtCore.QRect(870, 570, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_export_cart.setFont(font)
        self.btn_export_cart.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_export_cart.setObjectName("btn_export_cart")
        self.stackedWidget.addWidget(self.page_cart)
        self.page_pers_acc = QtWidgets.QWidget()
        self.page_pers_acc.setObjectName("page_pers_acc")
        self.label_pers_acc = QtWidgets.QLabel(self.page_pers_acc)
        self.label_pers_acc.setGeometry(QtCore.QRect(510, 20, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_pers_acc.setFont(font)
        self.label_pers_acc.setStyleSheet("color: #654321;\n"
"")
        self.label_pers_acc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pers_acc.setObjectName("label_pers_acc")
        self.label_name = QtWidgets.QLabel(self.page_pers_acc)
        self.label_name.setGeometry(QtCore.QRect(390, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: #654321;\n"
"")
        self.label_name.setObjectName("label_name")
        self.label_email = QtWidgets.QLabel(self.page_pers_acc)
        self.label_email.setGeometry(QtCore.QRect(390, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet("color: #654321;\n"
"")
        self.label_email.setObjectName("label_email")
        self.label_phone = QtWidgets.QLabel(self.page_pers_acc)
        self.label_phone.setGeometry(QtCore.QRect(390, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_phone.setFont(font)
        self.label_phone.setStyleSheet("color: #654321;\n"
"")
        self.label_phone.setObjectName("label_phone")
        self.lineEdit_name_2 = QtWidgets.QLineEdit(self.page_pers_acc)
        self.lineEdit_name_2.setGeometry(QtCore.QRect(490, 190, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_name_2.setFont(font)
        self.lineEdit_name_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_name_2.setReadOnly(True)
        self.lineEdit_name_2.setPlaceholderText("")
        self.lineEdit_name_2.setObjectName("lineEdit_name_2")
        self.lineEdit_email_2 = QtWidgets.QLineEdit(self.page_pers_acc)
        self.lineEdit_email_2.setGeometry(QtCore.QRect(490, 270, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_email_2.setFont(font)
        self.lineEdit_email_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_email_2.setReadOnly(True)
        self.lineEdit_email_2.setPlaceholderText("")
        self.lineEdit_email_2.setObjectName("lineEdit_email_2")
        self.lineEdit_phone_3 = QtWidgets.QLineEdit(self.page_pers_acc)
        self.lineEdit_phone_3.setGeometry(QtCore.QRect(490, 350, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_phone_3.setFont(font)
        self.lineEdit_phone_3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8B4513;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #F5F5F5;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgba(51, 51, 51, 0.5);\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #A0522D;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_phone_3.setReadOnly(True)
        self.lineEdit_phone_3.setPlaceholderText("")
        self.lineEdit_phone_3.setObjectName("lineEdit_phone_3")
        self.btn_pers_acc_shop = QtWidgets.QPushButton(self.page_pers_acc)
        self.btn_pers_acc_shop.setGeometry(QtCore.QRect(570, 590, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_pers_acc_shop.setFont(font)
        self.btn_pers_acc_shop.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_pers_acc_shop.setObjectName("btn_pers_acc_shop")
        self.stackedWidget.addWidget(self.page_pers_acc)
        self.page_product = QtWidgets.QWidget()
        self.page_product.setObjectName("page_product")
        self.label_image = QtWidgets.QLabel(self.page_product)
        self.label_image.setGeometry(QtCore.QRect(20, 40, 411, 361))
        self.label_image.setStyleSheet("border: 2px solid #654321;\n"
"border-radius: 5px;  /* Закругление углов */\n"
"padding: 5px;  /* Отступы внутри QLabel */")
        self.label_image.setScaledContents(True)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.label_name_product = QtWidgets.QLabel(self.page_product)
        self.label_name_product.setGeometry(QtCore.QRect(570, 40, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_name_product.setFont(font)
        self.label_name_product.setStyleSheet("")
        self.label_name_product.setText("")
        self.label_name_product.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_product.setObjectName("label_name_product")
        self.label_price = QtWidgets.QLabel(self.page_product)
        self.label_price.setGeometry(QtCore.QRect(600, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_price.setFont(font)
        self.label_price.setStyleSheet("")
        self.label_price.setObjectName("label_price")
        self.label_input_price = QtWidgets.QLabel(self.page_product)
        self.label_input_price.setGeometry(QtCore.QRect(670, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_input_price.setFont(font)
        self.label_input_price.setStyleSheet("")
        self.label_input_price.setText("")
        self.label_input_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_price.setObjectName("label_input_price")
        self.label_about = QtWidgets.QLabel(self.page_product)
        self.label_about.setGeometry(QtCore.QRect(10, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_about.setFont(font)
        self.label_about.setStyleSheet("")
        self.label_about.setObjectName("label_about")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_product)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(600, 210, 651, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_characteristic = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        self.tableWidget_characteristic.setObjectName("tableWidget_characteristic")
        self.tableWidget_characteristic.setColumnCount(2)
        self.tableWidget_characteristic.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_characteristic.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_characteristic.setHorizontalHeaderItem(1, item)
        self.tableWidget_characteristic.horizontalHeader().setDefaultSectionSize(320)
        self.tableWidget_characteristic.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_characteristic.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_characteristic)
        self.btn_shop = QtWidgets.QPushButton(self.page_product)
        self.btn_shop.setGeometry(QtCore.QRect(960, 660, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_shop.setFont(font)
        self.btn_shop.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_shop.setObjectName("btn_shop")
        self.btn_cart_2 = QtWidgets.QPushButton(self.page_product)
        self.btn_cart_2.setGeometry(QtCore.QRect(690, 660, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cart_2.setFont(font)
        self.btn_cart_2.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #654321;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(160, 82, 45, 0.5);\n"
"    color: rgba(255, 255, 255, 0.5);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_cart_2.setObjectName("btn_cart_2")
        self.label_input_about = QtWidgets.QLabel(self.page_product)
        self.label_input_about.setGeometry(QtCore.QRect(20, 500, 451, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_input_about.setFont(font)
        self.label_input_about.setStyleSheet("border: 2px solid #654321;\n"
"border-radius: 5px;  /* Закругление углов */\n"
"padding: 5px;  /* Отступы внутри QLabel */\n"
"\n"
"")
        self.label_input_about.setText("")
        self.label_input_about.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_input_about.setWordWrap(True)
        self.label_input_about.setObjectName("label_input_about")
        self.stackedWidget.addWidget(self.page_product)
        Shop.setCentralWidget(self.centralwidget)

        self.retranslateUi(Shop)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Shop)

    def retranslateUi(self, Shop):
        _translate = QtCore.QCoreApplication.translate
        Shop.setWindowTitle(_translate("Shop", "Shop"))
        self.label_signin.setText(_translate("Shop", "Вход"))
        self.lineEdit_phone.setPlaceholderText(_translate("Shop", "Введите номер телефона"))
        self.btn_signin.setText(_translate("Shop", "Войти"))
        self.lineEdit_psw.setPlaceholderText(_translate("Shop", "Введите пароль"))
        self.btn_signup_2.setText(_translate("Shop", "Регистрация"))
        self.lineEdit_psw_2.setPlaceholderText(_translate("Shop", "Придумайте пароль"))
        self.lineEdit_phone_2.setPlaceholderText(_translate("Shop", "Введите номер телефона"))
        self.lineEdit_email.setPlaceholderText(_translate("Shop", "Введите email"))
        self.label_signup.setText(_translate("Shop", "Регистрация"))
        self.lineEdit_name.setPlaceholderText(_translate("Shop", "Введите имя"))
        self.checkBox.setText(_translate("Shop", "Даю согласие на обработку персональных данных"))
        self.btn_signup.setText(_translate("Shop", "Зарегистрироваться"))
        self.btn_signin_2.setText(_translate("Shop", "Войти"))
        self.label_technolite.setText(_translate("Shop", "TechnoLite"))
        self.btn_cart.setText(_translate("Shop", "Корзина"))
        self.btn_pers_acc.setText(_translate("Shop", "Личный кабинет"))
        self.label_cart.setText(_translate("Shop", "Корзина"))
        self.btn_cart_go_shop.setText(_translate("Shop", "В магазин"))
        self.btn_clear_cart.setText(_translate("Shop", "Очистить корзину"))
        item = self.tableWidget_cart.verticalHeaderItem(0)
        item.setText(_translate("Shop", "1"))
        item = self.tableWidget_cart.horizontalHeaderItem(0)
        item.setText(_translate("Shop", "ID"))
        item = self.tableWidget_cart.horizontalHeaderItem(1)
        item.setText(_translate("Shop", "Название"))
        item = self.tableWidget_cart.horizontalHeaderItem(2)
        item.setText(_translate("Shop", "Цена"))
        item = self.tableWidget_cart.horizontalHeaderItem(3)
        item.setText(_translate("Shop", "Количество"))
        item = self.tableWidget_cart.horizontalHeaderItem(4)
        item.setText(_translate("Shop", "Итоговая стоимость"))
        self.btn_export_cart.setText(_translate("Shop", "Экспорт"))
        self.label_pers_acc.setText(_translate("Shop", "Личный кабинет"))
        self.label_name.setText(_translate("Shop", "Имя"))
        self.label_email.setText(_translate("Shop", "Email"))
        self.label_phone.setText(_translate("Shop", "Телефон"))
        self.btn_pers_acc_shop.setText(_translate("Shop", "В магазин"))
        self.label_image.setText(_translate("Shop", "Фото"))
        self.label_price.setText(_translate("Shop", "Цена:"))
        self.label_about.setText(_translate("Shop", "Описание:"))
        item = self.tableWidget_characteristic.horizontalHeaderItem(0)
        item.setText(_translate("Shop", "Характеристики"))
        item = self.tableWidget_characteristic.horizontalHeaderItem(1)
        item.setText(_translate("Shop", "Значение"))
        self.btn_shop.setText(_translate("Shop", "В магазин"))
        self.btn_cart_2.setText(_translate("Shop", "Добавить в корзину"))
