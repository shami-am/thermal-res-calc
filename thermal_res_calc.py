import os, sys, numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QColor, QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QSplashScreen
import pyqtgraph as pg
import vars as vr
import neurolab.trans as nl
from scipy.interpolate import PchipInterpolator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 640))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(20, 23, 38);")
        self.pixmap = QPixmap("resources/splash_img.png")
        self.splash = QSplashScreen(self.pixmap, QtCore.Qt.WindowStaysOnTopHint)
        self.splash.setMask(self.pixmap.mask())
        self.splash.show()
        QTimer.singleShot(1000, self.splash.close)
        app.processEvents()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 711, 81))
        self.widget.setStyleSheet("background-color: rgb(26, 31, 50);\n""border-radius: 15px;")
        self.widget.setObjectName("widget")

        font1 = QtGui.QFont("Segoe UI Semibold")
        font1.setPixelSize(16)
        font2 = QtGui.QFont("Segoe UI Semibold")
        font2.setPixelSize(17)
        font3 = QtGui.QFont("Segoe UI Semibold")
        font3.setPixelSize(12)
        font4 = QtGui.QFont("Segoe UI Semibold")
        font4.setPixelSize(11)

        dv = QDoubleValidator(0.0, 1000.0, 4)

        iv = QIntValidator(0, 90)

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(16, 12, 91, 31))
        self.label_5.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(132, 12, 91, 31))
        self.label_6.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(248, 12, 91, 31))
        self.label_7.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(364, 12, 91, 31))
        self.label_8.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(480, 12, 91, 31))
        self.label_9.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(596, 12, 91, 31))
        self.label_10.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font1)
        self.angle_le = QtWidgets.QLineEdit(self.widget)
        self.angle_le.setGeometry(QtCore.QRect(11, 45, 109, 25))
        self.angle_le.setFont(font1)
        self.angle_le.setWhatsThis("")
        self.angle_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                    "border-color: rgb(119, 129, 153);")
        self.angle_le.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_le.setObjectName("angle_le")
        self.angle_le.setValidator(iv)
        self.height_le = QtWidgets.QLineEdit(self.widget)
        self.height_le.setGeometry(QtCore.QRect(127, 45, 109, 25))
        self.height_le.setFont(font1)
        self.height_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                     "border-color: rgb(119, 129, 153);")
        self.height_le.setAlignment(QtCore.Qt.AlignCenter)
        self.height_le.setObjectName("height_le")
        self.height_le.setValidator(dv)
        self.thickness_le = QtWidgets.QLineEdit(self.widget)
        self.thickness_le.setGeometry(QtCore.QRect(243, 45, 109, 25))
        self.thickness_le.setFont(font1)
        self.thickness_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                        "border-color: rgb(119, 129, 153);")
        self.thickness_le.setAlignment(QtCore.Qt.AlignCenter)
        self.thickness_le.setObjectName("thickness_le")
        self.thickness_le.setValidator(dv)
        self.intemp_le = QtWidgets.QLineEdit(self.widget)
        self.intemp_le.setGeometry(QtCore.QRect(359, 45, 109, 25))
        self.intemp_le.setFont(font1)
        self.intemp_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                     "border-color: rgb(119, 129, 153);")
        self.intemp_le.setAlignment(QtCore.Qt.AlignCenter)
        self.intemp_le.setObjectName("intemp_le")
        self.intemp_le.setValidator(dv)
        self.outtemp_le = QtWidgets.QLineEdit(self.widget)
        self.outtemp_le.setGeometry(QtCore.QRect(475, 45, 109, 25))
        self.outtemp_le.setFont(font1)
        self.outtemp_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                      "border-color: rgb(119, 129, 153);")
        self.outtemp_le.setAlignment(QtCore.Qt.AlignCenter)
        self.outtemp_le.setObjectName("outtemp_le")
        self.outtemp_le.setValidator(dv)
        self.em_le = QtWidgets.QLineEdit(self.widget)
        self.em_le.setGeometry(QtCore.QRect(591, 45, 109, 25))
        self.em_le.setFont(font1)
        self.em_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                 "border-color: rgb(119, 129, 153);")
        self.em_le.setAlignment(QtCore.Qt.AlignCenter)
        self.em_le.setObjectName("em_le")
        self.em_le.setValidator(dv)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(750, 30, 231, 81))
        self.widget_2.setStyleSheet("background-color: rgb(26, 31, 50);\n""border-radius: 15px;")
        self.widget_2.setObjectName("widget_2")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(15, 12, 91, 31))
        self.label_11.setStyleSheet("color: rgb(211, 211, 211);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(font1)
        self.output_le = QtWidgets.QLineEdit(self.widget_2)
        self.output_le.setGeometry(QtCore.QRect(10, 45, 109, 25))
        self.output_le.setFont(font1)
        self.output_le.setStyleSheet("border: 1px solid red;\n""border-radius: 5px;\n""color: rgb(211, 211, 211);\n"
                                     "border-color: rgb(119, 129, 153);")
        self.output_le.setAlignment(QtCore.Qt.AlignCenter)
        self.output_le.setObjectName("output_le")
        self.compute_button = QtWidgets.QPushButton(self.widget_2)
        self.compute_button.setGeometry(QtCore.QRect(126, 10, 95, 25))
        self.compute_button.setStyleSheet("background-color: rgb(87, 230, 163);\n""border-radius: 5px;\n")
        self.compute_button.setIconSize(QtCore.QSize(40, 40))
        self.compute_button.setObjectName("compute_button")
        self.compute_button.setFont(font2)
        self.reset_button = QtWidgets.QPushButton(self.widget_2)
        self.reset_button.setGeometry(QtCore.QRect(126, 45, 95, 25))
        self.reset_button.setStyleSheet("background-color: rgb(49, 61, 101);\n""color: rgb(211, 211, 211);\n"
                                        "border-radius: 5px;\n")
        self.reset_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/white_reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon1)
        self.reset_button.setIconSize(QtCore.QSize(40, 40))
        self.reset_button.setObjectName("reset_button")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(20, 150, 471, 471))
        self.widget_3.setStyleSheet("background-color: rgb(26, 31, 50);\n""border-radius: 15px;")
        self.widget_3.setObjectName("widget_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget_3)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 451, 451))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(510, 150, 471, 471))
        self.widget_4.setStyleSheet("background-color: rgb(26, 31, 50);\n""border-radius: 15px;")
        self.widget_4.setObjectName("widget_4")
        pg.setConfigOption('background', QColor(26, 31, 50))
        pg.setConfigOption('foreground', 'w')
        self.curve_graph_widget = pg.PlotWidget(self.widget_4)
        styles = {"color": "#d3d3d3", "font-size": "14px"}
        self.curve_graph_widget.setLabel("left", "", **styles)
        self.curve_graph_widget.setLabel("bottom", "", **styles)
        self.curve_graph_widget.setGeometry(QtCore.QRect(10, 10, 451, 421))
        self.curve_graph_widget.setStyleSheet("")
        self.curve_graph_widget.setObjectName("curve_graph_widget")
        self.r_angle_button = QtWidgets.QPushButton(self.widget_4)
        self.r_angle_button.setGeometry(QtCore.QRect(378, 435, 85, 25))
        self.r_angle_button.setStyleSheet("background-color: rgb(49, 61, 101);\n""color: rgb(211, 211, 211);\n"
                                          "border-radius: 5px;\n")
        self.r_angle_button.setObjectName("r_angle_button")
        self.r_angle_button.setFont(font3)
        self.output_th_button = QtWidgets.QPushButton(self.widget_4)
        self.output_th_button.setGeometry(QtCore.QRect(286, 435, 85, 25))
        self.output_th_button.setStyleSheet("background-color: rgb(49, 61, 101);\n""color: rgb(211, 211, 211);\n"
                                            "border-radius: 5px;\n")
        self.output_th_button.setObjectName("output_th_button")
        self.output_th_button.setFont(font3)
        self.output_he_button = QtWidgets.QPushButton(self.widget_4)
        self.output_he_button.setGeometry(QtCore.QRect(194, 435, 85, 25))
        self.output_he_button.setStyleSheet("background-color: rgb(49, 61, 101);\n""color: rgb(211, 211, 211);\n"
                                            "border-radius: 5px;\n")
        self.output_he_button.setObjectName("output_he_button")
        self.output_he_button.setFont(font3)
        self.output_em_button = QtWidgets.QPushButton(self.widget_4)
        self.output_em_button.setGeometry(QtCore.QRect(102, 435, 85, 25))
        font = QtGui.QFont()
        font.setFamily("\"Segoe UI Semibold\"")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.output_em_button.setFont(font)
        self.output_em_button.setStyleSheet("background-color: rgb(49, 61, 101);\n""color: rgb(211, 211, 211);\n"
                                            "border-radius: 5px;\n")
        self.output_em_button.setObjectName("output_em_button")
        self.output_em_button.setFont(font3)
        self.checkBox = QtWidgets.QCheckBox(self.widget_4)
        self.checkBox.setGeometry(QtCore.QRect(9, 437, 91, 20))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setFont(font4)
        self.curve_graph_widget.raise_()
        self.r_angle_button.raise_()
        self.output_th_button.raise_()
        self.output_he_button.raise_()
        self.checkBox.raise_()
        self.output_em_button.raise_()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 121, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setFont(font2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(760, 0, 121, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 151, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 120, 121, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)

        color_w = QColor(211, 211, 211)
        color_r = QColor(190, 51, 70)
        color_b = QColor(69, 63, 188)
        color_g = QColor(63, 188, 133)

        pen_w = QtGui.QPen(color_w, 5)
        pen_r = QtGui.QPen(color_r, 5)
        pen_b = QtGui.QPen(color_b, 5)
        pen_g = QtGui.QPen(color_g, 5)
        scene.setBackgroundBrush(QtGui.QBrush(QColor(26, 31, 50)))

        def draw_rect(in_temp, out_temp, angle):
            scene.clear()
            transform = QtGui.QTransform()
            transform.rotate(-angle)
            if in_temp > out_temp:
                s = scene.addLine(300, 65, 0, 65, pen_r)
                s.setTransform(transform)

                s = scene.addLine(0, 65, 0, 0, pen_w)
                s.setTransform(transform)

                s = scene.addLine(0, 0, 300, 0, pen_b)
                s.setTransform(transform)

                s = scene.addLine(300, 0, 300, 65, pen_w)
                s.setTransform(transform)

                text = scene.addSimpleText(self.label_9.text() + '\t' + self.outtemp_le.text() + "°", font2)
                text.setBrush(QColor(69, 63, 188))
                text.setPos(-20, -270)

                text = scene.addSimpleText(self.label_8.text() + '\t' + self.intemp_le.text() + "°", font2)
                text.setBrush(QColor(190, 51, 70))
                text.setPos(-20, -300)

            elif in_temp < out_temp:
                s = scene.addLine(300, 65, 0, 65, pen_b)
                s.setTransform(transform)

                s = scene.addLine(0, 65, 0, 0, pen_w)
                s.setTransform(transform)

                s = scene.addLine(0, 0, 300, 0, pen_r)
                s.setTransform(transform)

                s = scene.addLine(300, 0, 300, 65, pen_w)
                s.setTransform(transform)

                text = scene.addSimpleText(self.label_9.text() + '\t' + self.outtemp_le.text() + "°", font2)
                text.setBrush(color_r)
                text.setPos(-20, -270)

                text = scene.addSimpleText(self.label_8.text() + '\t' + self.intemp_le.text() + "°", font2)
                text.setBrush(color_b)
                text.setPos(-20, -300)

            else:
                s = scene.addLine(300, 65, 0, 65, pen_g)
                s.setTransform(transform)

                s = scene.addLine(0, 65, 0, 0, pen_w)
                s.setTransform(transform)

                s = scene.addLine(0, 0, 300, 0, pen_g)
                s.setTransform(transform)

                s = scene.addLine(300, 0, 300, 65, pen_w)
                s.setTransform(transform)

                text = scene.addSimpleText(self.label_9.text() + '\t' + self.outtemp_le.text() + "°", font2)
                text.setBrush(color_g)
                text.setPos(-20, -270)

                text = scene.addSimpleText(self.label_8.text() + '\t' + self.intemp_le.text() + "°", font2)
                text.setBrush(color_g)
                text.setPos(-20, -300)

        def get_r_t(v, angle, thick, direction):
            ts = nl.TanSig()
            v = np.transpose(v)
            angles = np.array([0, 5, 10, 15, 30, 45, 60, 75, 90])
            x0 = (2 * (v[0][0] - vr.ps_min[0][0]) / (vr.ps_max[0][0] - vr.ps_min[0][0]) - 1)
            x1 = (2 * (v[1][0] - vr.ps_min[0][1]) / (vr.ps_max[0][1] - vr.ps_min[0][1]) - 1)
            x2 = (2 * (v[2][0] - vr.ps_min[0][2]) / (vr.ps_max[0][2] - vr.ps_min[0][2]) - 1)
            x3 = (2 * (v[3][0] - vr.ps_min[0][3]) / (vr.ps_max[0][3] - vr.ps_min[0][3]) - 1)
            x = np.transpose([[x0, x1, x2, x3]])
            thicknesses = np.array([13, 20, 40, 90, 114, 143])

            if direction == 1:
                z = vr.down_0_13T_LW.dot(ts(vr.down_0_13T_IW.dot(x) + vr.down_0_13T_b1)) + vr.down_0_13T_b2
                r_down_0_13 = (vr.down_0_13T_ts_max - vr.down_0_13T_ts_min) * (z[0][0] + 1) / 2 + vr.down_0_13T_ts_min
                z = vr.down_0_20T_LW.dot(ts(vr.down_0_20T_IW.dot(x) + vr.down_0_20T_b1)) + vr.down_0_20T_b2
                r_down_0_20 = (vr.down_0_20T_ts_max - vr.down_0_20T_ts_min) * (z[0][0] + 1) / 2 + vr.down_0_20T_ts_min
                z = vr.down_0_40T_LW.dot(ts(vr.down_0_40T_IW.dot(x) + vr.down_0_40T_b1)) + vr.down_0_40T_b2
                r_down_0_40 = (vr.down_0_40T_ts_max - vr.down_0_40T_ts_min) * (z[0][0] + 1) / 2 + vr.down_0_40T_ts_min
                z = vr.down_0_90T_LW.dot(ts(vr.down_0_90T_IW.dot(x) + vr.down_0_90T_b1)) + vr.down_0_90T_b2
                r_down_0_90 = (vr.down_0_90T_ts_max - vr.down_0_90T_ts_min) * (z[0][0] + 1) / 2 + vr.down_0_90T_ts_min
                z = vr.down_0_114T_LW.dot(ts(vr.down_0_114T_IW.dot(x) + vr.down_0_114T_b1)) + vr.down_0_114T_b2
                r_down_0_114 = (vr.down_0_114T_ts_max - vr.down_0_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_0_114T_ts_min
                z = vr.down_0_143T_LW.dot(ts(vr.down_0_143T_IW.dot(x) + vr.down_0_143T_b1)) + vr.down_0_143T_b2
                r_down_0_143 = (vr.down_0_143T_ts_max - vr.down_0_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_0_143T_ts_min
                r_value = np.array([r_down_0_13, r_down_0_20, r_down_0_40, r_down_0_90, r_down_0_114, r_down_0_143])
                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc0 = pchip_interp(thick)

                z = vr.down_5_13T_LW.dot(ts(vr.down_5_13T_IW.dot(x) + vr.down_5_13T_b1)) + vr.down_5_13T_b2
                r_down_5_13 = (vr.down_5_13T_ts_max - vr.down_5_13T_ts_min) * (z[0][0] + 1) / 2 + vr.down_5_13T_ts_min
                z = vr.down_5_20T_LW.dot(ts(vr.down_5_20T_IW.dot(x) + vr.down_5_20T_b1)) + vr.down_5_20T_b2
                r_down_5_20 = (vr.down_5_20T_ts_max - vr.down_5_20T_ts_min) * (z[0][0] + 1) / 2 + vr.down_5_20T_ts_min
                z = vr.down_5_40T_LW.dot(ts(vr.down_5_40T_IW.dot(x) + vr.down_5_40T_b1)) + vr.down_5_40T_b2
                r_down_5_40 = (vr.down_5_40T_ts_max - vr.down_5_40T_ts_min) * (z[0][0] + 1) / 2 + vr.down_5_40T_ts_min
                z = vr.down_5_90T_LW.dot(ts(vr.down_5_90T_IW.dot(x) + vr.down_5_90T_b1)) + vr.down_5_90T_b2
                r_down_5_90 = (vr.down_5_90T_ts_max - vr.down_5_90T_ts_min) * (z[0][0] + 1) / 2 + vr.down_5_90T_ts_min
                z = vr.down_5_114T_LW.dot(ts(vr.down_5_114T_IW.dot(x) + vr.down_5_114T_b1)) + vr.down_5_114T_b2
                r_down_5_114 = (vr.down_5_114T_ts_max - vr.down_5_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_5_114T_ts_min
                z = vr.down_5_143T_LW.dot(ts(vr.down_5_143T_IW.dot(x) + vr.down_5_143T_b1)) + vr.down_5_143T_b2
                r_down_5_143 = (vr.down_5_143T_ts_max - vr.down_5_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_5_143T_ts_min
                r_value = np.array([r_down_5_13, r_down_5_20, r_down_5_40, r_down_5_90, r_down_5_114, r_down_5_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc5 = pchip_interp(thick)

                z = vr.down_10_13T_LW.dot(ts(vr.down_10_13T_IW.dot(x) + vr.down_10_13T_b1)) + vr.down_10_13T_b2
                r_down_10_13 = (vr.down_10_13T_ts_max - vr.down_10_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_10_13T_ts_min
                z = vr.down_10_20T_LW.dot(ts(vr.down_10_20T_IW.dot(x) + vr.down_10_20T_b1)) + vr.down_10_20T_b2
                r_down_10_20 = (vr.down_10_20T_ts_max - vr.down_10_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_10_20T_ts_min
                z = vr.down_10_40T_LW.dot(ts(vr.down_10_40T_IW.dot(x) + vr.down_10_40T_b1)) + vr.down_10_40T_b2
                r_down_10_40 = (vr.down_10_40T_ts_max - vr.down_10_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_10_40T_ts_min
                z = vr.down_10_90T_LW.dot(ts(vr.down_10_90T_IW.dot(x) + vr.down_10_90T_b1)) + vr.down_10_90T_b2
                r_down_10_90 = (vr.down_10_90T_ts_max - vr.down_10_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_10_90T_ts_min
                z = vr.down_10_114T_LW.dot(ts(vr.down_10_114T_IW.dot(x) + vr.down_10_114T_b1)) + vr.down_10_114T_b2
                r_down_10_114 = (vr.down_10_114T_ts_max - vr.down_10_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_10_114T_ts_min
                z = vr.down_10_143T_LW.dot(ts(vr.down_10_143T_IW.dot(x) + vr.down_10_143T_b1)) + vr.down_10_143T_b2
                r_down_10_143 = (vr.down_10_143T_ts_max - vr.down_10_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_10_143T_ts_min
                r_value = np.array(
                    [r_down_10_13, r_down_10_20, r_down_10_40, r_down_10_90, r_down_10_114, r_down_10_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc10 = pchip_interp(thick)

                z = vr.down_15_13T_LW.dot(ts(vr.down_15_13T_IW.dot(x) + vr.down_15_13T_b1)) + vr.down_15_13T_b2
                r_down_15_13 = (vr.down_15_13T_ts_max - vr.down_15_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_15_13T_ts_min
                z = vr.down_15_20T_LW.dot(ts(vr.down_15_20T_IW.dot(x) + vr.down_15_20T_b1)) + vr.down_15_20T_b2
                r_down_15_20 = (vr.down_15_20T_ts_max - vr.down_15_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_15_20T_ts_min
                z = vr.down_15_40T_LW.dot(ts(vr.down_15_40T_IW.dot(x) + vr.down_15_40T_b1)) + vr.down_15_40T_b2
                r_down_15_40 = (vr.down_15_40T_ts_max - vr.down_15_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_15_40T_ts_min
                z = vr.down_15_90T_LW.dot(ts(vr.down_15_90T_IW.dot(x) + vr.down_15_90T_b1)) + vr.down_15_90T_b2
                r_down_15_90 = (vr.down_15_90T_ts_max - vr.down_15_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_15_90T_ts_min
                z = vr.down_15_114T_LW.dot(ts(vr.down_15_114T_IW.dot(x) + vr.down_15_114T_b1)) + vr.down_15_114T_b2
                r_down_15_114 = (vr.down_15_114T_ts_max - vr.down_15_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_15_114T_ts_min
                z = vr.down_15_143T_LW.dot(ts(vr.down_15_143T_IW.dot(x) + vr.down_15_143T_b1)) + vr.down_15_143T_b2
                r_down_15_143 = (vr.down_15_143T_ts_max - vr.down_15_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_15_143T_ts_min
                r_value = np.array(
                    [r_down_15_13, r_down_15_20, r_down_15_40, r_down_15_90, r_down_15_114, r_down_15_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc15 = pchip_interp(thick)

                z = vr.down_30_13T_LW.dot(ts(vr.down_30_13T_IW.dot(x) + vr.down_30_13T_b1)) + vr.down_30_13T_b2
                r_down_30_13 = (vr.down_30_13T_ts_max - vr.down_30_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_30_13T_ts_min
                z = vr.down_30_20T_LW.dot(ts(vr.down_30_20T_IW.dot(x) + vr.down_30_20T_b1)) + vr.down_30_20T_b2
                r_down_30_20 = (vr.down_30_20T_ts_max - vr.down_30_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_30_20T_ts_min
                z = vr.down_30_40T_LW.dot(ts(vr.down_30_40T_IW.dot(x) + vr.down_30_40T_b1)) + vr.down_30_40T_b2
                r_down_30_40 = (vr.down_30_40T_ts_max - vr.down_30_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_30_40T_ts_min
                z = vr.down_30_90T_LW.dot(ts(vr.down_30_90T_IW.dot(x) + vr.down_30_90T_b1)) + vr.down_30_90T_b2
                r_down_30_90 = (vr.down_30_90T_ts_max - vr.down_30_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_30_90T_ts_min
                z = vr.down_30_114T_LW.dot(ts(vr.down_30_114T_IW.dot(x) + vr.down_30_114T_b1)) + vr.down_30_114T_b2
                r_down_30_114 = (vr.down_30_114T_ts_max - vr.down_30_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_30_114T_ts_min
                z = vr.down_30_143T_LW.dot(ts(vr.down_30_143T_IW.dot(x) + vr.down_30_143T_b1)) + vr.down_30_143T_b2
                r_down_30_143 = (vr.down_30_143T_ts_max - vr.down_30_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_30_143T_ts_min
                r_value = np.array(
                    [r_down_30_13, r_down_30_20, r_down_30_40, r_down_30_90, r_down_30_114, r_down_30_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc30 = pchip_interp(thick)

                z = vr.down_45_13T_LW.dot(ts(vr.down_45_13T_IW.dot(x) + vr.down_45_13T_b1)) + vr.down_45_13T_b2
                r_down_45_13 = (vr.down_45_13T_ts_max - vr.down_45_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_45_13T_ts_min
                z = vr.down_45_20T_LW.dot(ts(vr.down_45_20T_IW.dot(x) + vr.down_45_20T_b1)) + vr.down_45_20T_b2
                r_down_45_20 = (vr.down_45_20T_ts_max - vr.down_45_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_45_20T_ts_min
                z = vr.down_45_40T_LW.dot(ts(vr.down_45_40T_IW.dot(x) + vr.down_45_40T_b1)) + vr.down_45_40T_b2
                r_down_45_40 = (vr.down_45_40T_ts_max - vr.down_45_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_45_40T_ts_min
                z = vr.down_45_90T_LW.dot(ts(vr.down_45_90T_IW.dot(x) + vr.down_45_90T_b1)) + vr.down_45_90T_b2
                r_down_45_90 = (vr.down_45_90T_ts_max - vr.down_45_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_45_90T_ts_min
                z = vr.down_45_114T_LW.dot(ts(vr.down_45_114T_IW.dot(x) + vr.down_45_114T_b1)) + vr.down_45_114T_b2
                r_down_45_114 = (vr.down_45_114T_ts_max - vr.down_45_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_45_114T_ts_min
                z = vr.down_45_143T_LW.dot(ts(vr.down_45_143T_IW.dot(x) + vr.down_45_143T_b1)) + vr.down_45_143T_b2
                r_down_45_143 = (vr.down_45_143T_ts_max - vr.down_45_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_45_143T_ts_min
                r_value = np.array(
                    [r_down_45_13, r_down_45_20, r_down_45_40, r_down_45_90, r_down_45_114, r_down_45_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc45 = pchip_interp(thick)

                z = vr.down_60_13T_LW.dot(ts(vr.down_60_13T_IW.dot(x) + vr.down_60_13T_b1)) + vr.down_60_13T_b2
                r_down_60_13 = (vr.down_60_13T_ts_max - vr.down_60_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_60_13T_ts_min
                z = vr.down_60_20T_LW.dot(ts(vr.down_60_20T_IW.dot(x) + vr.down_60_20T_b1)) + vr.down_60_20T_b2
                r_down_60_20 = (vr.down_60_20T_ts_max - vr.down_60_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_60_20T_ts_min
                z = vr.down_60_40T_LW.dot(ts(vr.down_60_40T_IW.dot(x) + vr.down_60_40T_b1)) + vr.down_60_40T_b2
                r_down_60_40 = (vr.down_60_40T_ts_max - vr.down_60_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_60_40T_ts_min
                z = vr.down_60_90T_LW.dot(ts(vr.down_60_90T_IW.dot(x) + vr.down_60_90T_b1)) + vr.down_60_90T_b2
                r_down_60_90 = (vr.down_60_90T_ts_max - vr.down_60_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_60_90T_ts_min
                z = vr.down_60_114T_LW.dot(ts(vr.down_60_114T_IW.dot(x) + vr.down_60_114T_b1)) + vr.down_60_114T_b2
                r_down_60_114 = (vr.down_60_114T_ts_max - vr.down_60_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_60_114T_ts_min
                z = vr.down_60_143T_LW.dot(ts(vr.down_60_143T_IW.dot(x) + vr.down_60_143T_b1)) + vr.down_60_143T_b2
                r_down_60_143 = (vr.down_60_143T_ts_max - vr.down_60_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_60_143T_ts_min
                r_value = np.array(
                    [r_down_60_13, r_down_60_20, r_down_60_40, r_down_60_90, r_down_60_114, r_down_60_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc60 = pchip_interp(thick)

                z = vr.down_75_13T_LW.dot(ts(vr.down_75_13T_IW.dot(x) + vr.down_75_13T_b1)) + vr.down_75_13T_b2
                r_down_75_13 = (vr.down_75_13T_ts_max - vr.down_75_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_75_13T_ts_min
                z = vr.down_75_20T_LW.dot(ts(vr.down_75_20T_IW.dot(x) + vr.down_75_20T_b1)) + vr.down_75_20T_b2
                r_down_75_20 = (vr.down_75_20T_ts_max - vr.down_75_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_75_20T_ts_min
                z = vr.down_75_40T_LW.dot(ts(vr.down_75_40T_IW.dot(x) + vr.down_75_40T_b1)) + vr.down_75_40T_b2
                r_down_75_40 = (vr.down_75_40T_ts_max - vr.down_75_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_75_40T_ts_min
                z = vr.down_75_90T_LW.dot(ts(vr.down_75_90T_IW.dot(x) + vr.down_75_90T_b1)) + vr.down_75_90T_b2
                r_down_75_90 = (vr.down_75_90T_ts_max - vr.down_75_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_75_90T_ts_min
                z = vr.down_75_114T_LW.dot(ts(vr.down_75_114T_IW.dot(x) + vr.down_75_114T_b1)) + vr.down_75_114T_b2
                r_down_75_114 = (vr.down_75_114T_ts_max - vr.down_75_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_75_114T_ts_min
                z = vr.down_75_143T_LW.dot(ts(vr.down_75_143T_IW.dot(x) + vr.down_75_143T_b1)) + vr.down_75_143T_b2
                r_down_75_143 = (vr.down_75_143T_ts_max - vr.down_75_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_75_143T_ts_min
                r_value = np.array(
                    [r_down_75_13, r_down_75_20, r_down_75_40, r_down_75_90, r_down_75_114, r_down_75_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc75 = pchip_interp(thick)

                z = vr.down_90_13T_LW.dot(ts(vr.down_90_13T_IW.dot(x) + vr.down_90_13T_b1)) + vr.down_90_13T_b2
                r_down_90_13 = (vr.down_90_13T_ts_max - vr.down_90_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_13T_ts_min
                z = vr.down_90_20T_LW.dot(ts(vr.down_90_20T_IW.dot(x) + vr.down_90_20T_b1)) + vr.down_90_20T_b2
                r_down_90_20 = (vr.down_90_20T_ts_max - vr.down_90_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_20T_ts_min
                z = vr.down_90_40T_LW.dot(ts(vr.down_90_40T_IW.dot(x) + vr.down_90_40T_b1)) + vr.down_90_40T_b2
                r_down_90_40 = (vr.down_90_40T_ts_max - vr.down_90_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_40T_ts_min
                z = vr.down_90_90T_LW.dot(ts(vr.down_90_90T_IW.dot(x) + vr.down_90_90T_b1)) + vr.down_90_90T_b2
                r_down_90_90 = (vr.down_90_90T_ts_max - vr.down_90_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_90T_ts_min
                z = vr.down_90_114T_LW.dot(ts(vr.down_90_114T_IW.dot(x) + vr.down_90_114T_b1)) + vr.down_90_114T_b2
                r_down_90_114 = (vr.down_90_114T_ts_max - vr.down_90_114T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_114T_ts_min
                z = vr.down_90_143T_LW.dot(ts(vr.down_90_143T_IW.dot(x) + vr.down_90_143T_b1)) + vr.down_90_143T_b2
                r_down_90_143 = (vr.down_90_143T_ts_max - vr.down_90_143T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_143T_ts_min
                r_value = np.array(
                    [r_down_90_13, r_down_90_20, r_down_90_40, r_down_90_90, r_down_90_114, r_down_90_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc90 = pchip_interp(thick)

                pchip_interp = PchipInterpolator(angles, np.array([rc0, rc5, rc10, rc15, rc30, rc45, rc60, rc75, rc90]))
                rc = pchip_interp(angle)
                return rc

            else:
                z = vr.up_0_13T_LW.dot(ts(vr.up_0_13T_IW.dot(x) + vr.up_0_13T_b1)) + vr.up_0_13T_b2
                r_up_0_13 = (vr.up_0_13T_ts_max - vr.up_0_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_0_13T_ts_min
                z = vr.up_0_20T_LW.dot(ts(vr.up_0_20T_IW.dot(x) + vr.up_0_20T_b1)) + vr.up_0_20T_b2
                r_up_0_20 = (vr.up_0_20T_ts_max - vr.up_0_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_0_20T_ts_min
                z = vr.up_0_40T_LW.dot(ts(vr.up_0_40T_IW.dot(x) + vr.up_0_40T_b1)) + vr.up_0_40T_b2
                r_up_0_40 = (vr.up_0_40T_ts_max - vr.up_0_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_0_40T_ts_min
                z = vr.up_0_90T_LW.dot(ts(vr.up_0_90T_IW.dot(x) + vr.up_0_90T_b1)) + vr.up_0_90T_b2
                r_up_0_90 = (vr.up_0_90T_ts_max - vr.up_0_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_0_90T_ts_min
                z = vr.up_0_114T_LW.dot(ts(vr.up_0_114T_IW.dot(x) + vr.up_0_114T_b1)) + vr.up_0_114T_b2
                r_up_0_114 = (vr.up_0_114T_ts_max - vr.up_0_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_0_114T_ts_min
                z = vr.up_0_143T_LW.dot(ts(vr.up_0_143T_IW.dot(x) + vr.up_0_143T_b1)) + vr.up_0_143T_b2
                r_up_0_143 = (vr.up_0_143T_ts_max - vr.up_0_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_0_143T_ts_min
                r_value = np.array([r_up_0_13, r_up_0_20, r_up_0_40, r_up_0_90, r_up_0_114, r_up_0_143])
                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc0 = pchip_interp(thick)

                z = vr.up_5_13T_LW.dot(ts(vr.up_5_13T_IW.dot(x) + vr.up_5_13T_b1)) + vr.up_5_13T_b2
                r_up_5_13 = (vr.up_5_13T_ts_max - vr.up_5_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_5_13T_ts_min
                z = vr.up_5_20T_LW.dot(ts(vr.up_5_20T_IW.dot(x) + vr.up_5_20T_b1)) + vr.up_5_20T_b2
                r_up_5_20 = (vr.up_5_20T_ts_max - vr.up_5_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_5_20T_ts_min
                z = vr.up_5_40T_LW.dot(ts(vr.up_5_40T_IW.dot(x) + vr.up_5_40T_b1)) + vr.up_5_40T_b2
                r_up_5_40 = (vr.up_5_40T_ts_max - vr.up_5_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_5_40T_ts_min
                z = vr.up_5_90T_LW.dot(ts(vr.up_5_90T_IW.dot(x) + vr.up_5_90T_b1)) + vr.up_5_90T_b2
                r_up_5_90 = (vr.up_5_90T_ts_max - vr.up_5_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_5_90T_ts_min
                z = vr.up_5_114T_LW.dot(ts(vr.up_5_114T_IW.dot(x) + vr.up_5_114T_b1)) + vr.up_5_114T_b2
                r_up_5_114 = (vr.up_5_114T_ts_max - vr.up_5_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_5_114T_ts_min
                z = vr.up_5_143T_LW.dot(ts(vr.up_5_143T_IW.dot(x) + vr.up_5_143T_b1)) + vr.up_5_143T_b2
                r_up_5_143 = (vr.up_5_143T_ts_max - vr.up_5_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_5_143T_ts_min
                r_value = np.array([r_up_5_13, r_up_5_20, r_up_5_40, r_up_5_90, r_up_5_114, r_up_5_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc5 = pchip_interp(thick)

                z = vr.up_10_13T_LW.dot(ts(vr.up_10_13T_IW.dot(x) + vr.up_10_13T_b1)) + vr.up_10_13T_b2
                r_up_10_13 = (vr.up_10_13T_ts_max - vr.up_10_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_10_13T_ts_min
                z = vr.up_10_20T_LW.dot(ts(vr.up_10_20T_IW.dot(x) + vr.up_10_20T_b1)) + vr.up_10_20T_b2
                r_up_10_20 = (vr.up_10_20T_ts_max - vr.up_10_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_10_20T_ts_min
                z = vr.up_10_40T_LW.dot(ts(vr.up_10_40T_IW.dot(x) + vr.up_10_40T_b1)) + vr.up_10_40T_b2
                r_up_10_40 = (vr.up_10_40T_ts_max - vr.up_10_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_10_40T_ts_min
                z = vr.up_10_90T_LW.dot(ts(vr.up_10_90T_IW.dot(x) + vr.up_10_90T_b1)) + vr.up_10_90T_b2
                r_up_10_90 = (vr.up_10_90T_ts_max - vr.up_10_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_10_90T_ts_min
                z = vr.up_10_114T_LW.dot(ts(vr.up_10_114T_IW.dot(x) + vr.up_10_114T_b1)) + vr.up_10_114T_b2
                r_up_10_114 = (vr.up_10_114T_ts_max - vr.up_10_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_10_114T_ts_min
                z = vr.up_10_143T_LW.dot(ts(vr.up_10_143T_IW.dot(x) + vr.up_10_143T_b1)) + vr.up_10_143T_b2
                r_up_10_143 = (vr.up_10_143T_ts_max - vr.up_10_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_10_143T_ts_min
                r_value = np.array([r_up_10_13, r_up_10_20, r_up_10_40, r_up_10_90, r_up_10_114, r_up_10_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc10 = pchip_interp(thick)

                z = vr.up_15_13T_LW.dot(ts(vr.up_15_13T_IW.dot(x) + vr.up_15_13T_b1)) + vr.up_15_13T_b2
                r_up_15_13 = (vr.up_15_13T_ts_max - vr.up_15_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_15_13T_ts_min
                z = vr.up_15_20T_LW.dot(ts(vr.up_15_20T_IW.dot(x) + vr.up_15_20T_b1)) + vr.up_15_20T_b2
                r_up_15_20 = (vr.up_15_20T_ts_max - vr.up_15_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_15_20T_ts_min
                z = vr.up_15_40T_LW.dot(ts(vr.up_15_40T_IW.dot(x) + vr.up_15_40T_b1)) + vr.up_15_40T_b2
                r_up_15_40 = (vr.up_15_40T_ts_max - vr.up_15_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_15_40T_ts_min
                z = vr.up_15_90T_LW.dot(ts(vr.up_15_90T_IW.dot(x) + vr.up_15_90T_b1)) + vr.up_15_90T_b2
                r_up_15_90 = (vr.up_15_90T_ts_max - vr.up_15_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_15_90T_ts_min
                z = vr.up_15_114T_LW.dot(ts(vr.up_15_114T_IW.dot(x) + vr.up_15_114T_b1)) + vr.up_15_114T_b2
                r_up_15_114 = (vr.up_15_114T_ts_max - vr.up_15_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_15_114T_ts_min
                z = vr.up_15_143T_LW.dot(ts(vr.up_15_143T_IW.dot(x) + vr.up_15_143T_b1)) + vr.up_15_143T_b2
                r_up_15_143 = (vr.up_15_143T_ts_max - vr.up_15_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_15_143T_ts_min
                r_value = np.array([r_up_15_13, r_up_15_20, r_up_15_40, r_up_15_90, r_up_15_114, r_up_15_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc15 = pchip_interp(thick)

                z = vr.up_30_13T_LW.dot(ts(vr.up_30_13T_IW.dot(x) + vr.up_30_13T_b1)) + vr.up_30_13T_b2
                r_up_30_13 = (vr.up_30_13T_ts_max - vr.up_30_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_30_13T_ts_min
                z = vr.up_30_20T_LW.dot(ts(vr.up_30_20T_IW.dot(x) + vr.up_30_20T_b1)) + vr.up_30_20T_b2
                r_up_30_20 = (vr.up_30_20T_ts_max - vr.up_30_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_30_20T_ts_min
                z = vr.up_30_40T_LW.dot(ts(vr.up_30_40T_IW.dot(x) + vr.up_30_40T_b1)) + vr.up_30_40T_b2
                r_up_30_40 = (vr.up_30_40T_ts_max - vr.up_30_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_30_40T_ts_min
                z = vr.up_30_90T_LW.dot(ts(vr.up_30_90T_IW.dot(x) + vr.up_30_90T_b1)) + vr.up_30_90T_b2
                r_up_30_90 = (vr.up_30_90T_ts_max - vr.up_30_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_30_90T_ts_min
                z = vr.up_30_114T_LW.dot(ts(vr.up_30_114T_IW.dot(x) + vr.up_30_114T_b1)) + vr.up_30_114T_b2
                r_up_30_114 = (vr.up_30_114T_ts_max - vr.up_30_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_30_114T_ts_min
                z = vr.up_30_143T_LW.dot(ts(vr.up_30_143T_IW.dot(x) + vr.up_30_143T_b1)) + vr.up_30_143T_b2
                r_up_30_143 = (vr.up_30_143T_ts_max - vr.up_30_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_30_143T_ts_min
                r_value = np.array([r_up_30_13, r_up_30_20, r_up_30_40, r_up_30_90, r_up_30_114, r_up_30_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc30 = pchip_interp(thick)

                z = vr.up_45_13T_LW.dot(ts(vr.up_45_13T_IW.dot(x) + vr.up_45_13T_b1)) + vr.up_45_13T_b2
                r_up_45_13 = (vr.up_45_13T_ts_max - vr.up_45_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_45_13T_ts_min
                z = vr.up_45_20T_LW.dot(ts(vr.up_45_20T_IW.dot(x) + vr.up_45_20T_b1)) + vr.up_45_20T_b2
                r_up_45_20 = (vr.up_45_20T_ts_max - vr.up_45_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_45_20T_ts_min
                z = vr.up_45_40T_LW.dot(ts(vr.up_45_40T_IW.dot(x) + vr.up_45_40T_b1)) + vr.up_45_40T_b2
                r_up_45_40 = (vr.up_45_40T_ts_max - vr.up_45_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_45_40T_ts_min
                z = vr.up_45_90T_LW.dot(ts(vr.up_45_90T_IW.dot(x) + vr.up_45_90T_b1)) + vr.up_45_90T_b2
                r_up_45_90 = (vr.up_45_90T_ts_max - vr.up_45_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_45_90T_ts_min
                z = vr.up_45_114T_LW.dot(ts(vr.up_45_114T_IW.dot(x) + vr.up_45_114T_b1)) + vr.up_45_114T_b2
                r_up_45_114 = (vr.up_45_114T_ts_max - vr.up_45_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_45_114T_ts_min
                z = vr.up_45_143T_LW.dot(ts(vr.up_45_143T_IW.dot(x) + vr.up_45_143T_b1)) + vr.up_45_143T_b2
                r_up_45_143 = (vr.up_45_143T_ts_max - vr.up_45_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_45_143T_ts_min
                r_value = np.array([r_up_45_13, r_up_45_20, r_up_45_40, r_up_45_90, r_up_45_114, r_up_45_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc45 = pchip_interp(thick)

                z = vr.up_60_13T_LW.dot(ts(vr.up_60_13T_IW.dot(x) + vr.up_60_13T_b1)) + vr.up_60_13T_b2
                r_up_60_13 = (vr.up_60_13T_ts_max - vr.up_60_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_60_13T_ts_min
                z = vr.up_60_20T_LW.dot(ts(vr.up_60_20T_IW.dot(x) + vr.up_60_20T_b1)) + vr.up_60_20T_b2
                r_up_60_20 = (vr.up_60_20T_ts_max - vr.up_60_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_60_20T_ts_min
                z = vr.up_60_40T_LW.dot(ts(vr.up_60_40T_IW.dot(x) + vr.up_60_40T_b1)) + vr.up_60_40T_b2
                r_up_60_40 = (vr.up_60_40T_ts_max - vr.up_60_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_60_40T_ts_min
                z = vr.up_60_90T_LW.dot(ts(vr.up_60_90T_IW.dot(x) + vr.up_60_90T_b1)) + vr.up_60_90T_b2
                r_up_60_90 = (vr.up_60_90T_ts_max - vr.up_60_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_60_90T_ts_min
                z = vr.up_60_114T_LW.dot(ts(vr.up_60_114T_IW.dot(x) + vr.up_60_114T_b1)) + vr.up_60_114T_b2
                r_up_60_114 = (vr.up_60_114T_ts_max - vr.up_60_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_60_114T_ts_min
                z = vr.up_60_143T_LW.dot(ts(vr.up_60_143T_IW.dot(x) + vr.up_60_143T_b1)) + vr.up_60_143T_b2
                r_up_60_143 = (vr.up_60_143T_ts_max - vr.up_60_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_60_143T_ts_min
                r_value = np.array([r_up_60_13, r_up_60_20, r_up_60_40, r_up_60_90, r_up_60_114, r_up_60_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc60 = pchip_interp(thick)

                z = vr.up_75_13T_LW.dot(ts(vr.up_75_13T_IW.dot(x) + vr.up_75_13T_b1)) + vr.up_75_13T_b2
                r_up_75_13 = (vr.up_75_13T_ts_max - vr.up_75_13T_ts_min) * (z[0][0] + 1) / 2 + vr.up_75_13T_ts_min
                z = vr.up_75_20T_LW.dot(ts(vr.up_75_20T_IW.dot(x) + vr.up_75_20T_b1)) + vr.up_75_20T_b2
                r_up_75_20 = (vr.up_75_20T_ts_max - vr.up_75_20T_ts_min) * (z[0][0] + 1) / 2 + vr.up_75_20T_ts_min
                z = vr.up_75_40T_LW.dot(ts(vr.up_75_40T_IW.dot(x) + vr.up_75_40T_b1)) + vr.up_75_40T_b2
                r_up_75_40 = (vr.up_75_40T_ts_max - vr.up_75_40T_ts_min) * (z[0][0] + 1) / 2 + vr.up_75_40T_ts_min
                z = vr.up_75_90T_LW.dot(ts(vr.up_75_90T_IW.dot(x) + vr.up_75_90T_b1)) + vr.up_75_90T_b2
                r_up_75_90 = (vr.up_75_90T_ts_max - vr.up_75_90T_ts_min) * (z[0][0] + 1) / 2 + vr.up_75_90T_ts_min
                z = vr.up_75_114T_LW.dot(ts(vr.up_75_114T_IW.dot(x) + vr.up_75_114T_b1)) + vr.up_75_114T_b2
                r_up_75_114 = (vr.up_75_114T_ts_max - vr.up_75_114T_ts_min) * (z[0][0] + 1) / 2 + vr.up_75_114T_ts_min
                z = vr.up_75_143T_LW.dot(ts(vr.up_75_143T_IW.dot(x) + vr.up_75_143T_b1)) + vr.up_75_143T_b2
                r_up_75_143 = (vr.up_75_143T_ts_max - vr.up_75_143T_ts_min) * (z[0][0] + 1) / 2 + vr.up_75_143T_ts_min
                r_value = np.array([r_up_75_13, r_up_75_20, r_up_75_40, r_up_75_90, r_up_75_114, r_up_75_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc75 = pchip_interp(thick)

                z = vr.down_90_13T_LW.dot(ts(vr.down_90_13T_IW.dot(x) + vr.down_90_13T_b1)) + vr.down_90_13T_b2
                r_down_90_13 = (vr.down_90_13T_ts_max - vr.down_90_13T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_13T_ts_min
                z = vr.down_90_20T_LW.dot(ts(vr.down_90_20T_IW.dot(x) + vr.down_90_20T_b1)) + vr.down_90_20T_b2
                r_down_90_20 = (vr.down_90_20T_ts_max - vr.down_90_20T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_20T_ts_min
                z = vr.down_90_40T_LW.dot(ts(vr.down_90_40T_IW.dot(x) + vr.down_90_40T_b1)) + vr.down_90_40T_b2
                r_down_90_40 = (vr.down_90_40T_ts_max - vr.down_90_40T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_40T_ts_min
                z = vr.down_90_90T_LW.dot(ts(vr.down_90_90T_IW.dot(x) + vr.down_90_90T_b1)) + vr.down_90_90T_b2
                r_down_90_90 = (vr.down_90_90T_ts_max - vr.down_90_90T_ts_min) * (
                        z[0][0] + 1) / 2 + vr.down_90_90T_ts_min
                z = vr.down_90_114T_LW.dot(ts(vr.down_90_114T_IW.dot(x) + vr.down_90_114T_b1)) + vr.down_90_114T_b2
                r_down_90_114 = (vr.down_90_114T_ts_max - vr.down_90_114T_ts_min) * (z + 1) / 2 + vr.down_90_114T_ts_min
                z = vr.down_90_143T_LW.dot(ts(vr.down_90_143T_IW.dot(x) + vr.down_90_143T_b1)) + vr.down_90_143T_b2
                r_down_90_143 = (vr.down_90_143T_ts_max - vr.down_90_143T_ts_min) * (z + 1) / 2 + vr.down_90_143T_ts_min
                r_value = np.array(
                    [r_down_90_13, r_down_90_20, r_down_90_40, r_down_90_90, r_down_90_114, r_down_90_143])

                pchip_interp = PchipInterpolator(thicknesses, r_value)
                rc90 = pchip_interp(thick)

                pchip_interp = PchipInterpolator(angles, np.array([rc0, rc5, rc10, rc15, rc30, rc45, rc60, rc75, rc90]))
                rc = pchip_interp(angle)
                return rc

        def both_fit(angle, t_cold, t_hot, thick, emm, direction):
            height_a = np.array([4, 5, 6, 7, 8, 12, 16, 20, 24, 30, 36, 42, 48, 60, 72, 84, 96])
            r_value_a = np.array([])
            for i in range(0, len(height_a)):
                v = np.array([[t_cold, t_hot, height_a[i], emm]])
                r_value_a = np.append(r_value_a, get_r_t(v, angle, thick, direction))

            pchip_interp = PchipInterpolator(height_a, r_value_a)

            height1 = min(height_a)
            height2 = max(height_a)
            height = np.linspace(height1, height2, num=601)

            rf_a = np.array([])
            for j in range(0, len(height)):
                rf_a = np.append(rf_a, pchip_interp(height[j]))

            rf = np.array(rf_a)
            return rf

        def both_fit1h(height, angle, t_cold, t_hot, thick, emm, direction):
            height_b = np.array([4, 5, 6, 7, 8, 12, 16, 20, 24, 30, 36, 42, 48, 60, 72, 84, 96])
            r_value_b = np.array([])
            for i in range(0, len(height_b)):
                v = np.array([[t_cold, t_hot, height_b[i], emm]])
                r_value_b = np.append(r_value_b, get_r_t(v, angle, thick, direction))

            pchip_interp = PchipInterpolator(height_b, r_value_b)
            return pchip_interp(height)

        def input_values():
            # checking for correct values
            # typecasting user values into corresponding variables

            try:
                angle = int(self.angle_le.text())

            except ValueError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect value')
                err_msg.setInformativeText('Incorrect value in Angle field')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            try:
                height = float(self.height_le.text())

            except ValueError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect value')
                err_msg.setInformativeText('Incorrect value in Height field')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            try:
                thick = float(self.thickness_le.text())

            except ValueError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect value')
                err_msg.setInformativeText('Incorrect value in Thickness field')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            try:
                intemp = float(self.intemp_le.text())

            except ValueError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect value')
                err_msg.setInformativeText('Incorrect value in Inner temperature field')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            try:
                outtemp = float(self.outtemp_le.text())

            except ValueError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect value')
                err_msg.setInformativeText('Incorrect value in Outer temperature field')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            try:
                em = float(self.em_le.text())

            except ValueError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect value')
                err_msg.setInformativeText('Incorrect value in Effective emittance field')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            if intemp >= outtemp:
                t_cold = outtemp
                t_hot = intemp
                direction = -1

            else:
                t_cold = intemp
                t_hot = outtemp
                direction = 1

            return t_cold, t_hot, intemp, outtemp, height, thick, angle, em, direction

        def compute():
            # Error messages for missing values
            if self.angle_le.text() == '':
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Missing Value')
                err_msg.setInformativeText('Angle cannot be empty')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()

            elif self.height_le.text() == '':
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Missing Value')
                err_msg.setInformativeText('Height cannot be empty')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()

            elif self.thickness_le.text() == '':
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Missing Value')
                err_msg.setInformativeText('Thickness cannot be empty')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()

            elif self.intemp_le.text() == '':
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Missing Value')
                err_msg.setInformativeText('Inner temperature cannot be empty')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()

            elif self.outtemp_le.text() == '':
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Missing Value')
                err_msg.setInformativeText('Outer temperature cannot be empty')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()

            elif self.em_le.text() == '':
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Missing Value')
                err_msg.setInformativeText('Effective emittance cannot be empty')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()

            else:
                vals = input_values()
                try:
                    draw_rect(vals[2], vals[3], vals[6])
                    rc = both_fit1h(vals[4], vals[6], vals[0], vals[1], vals[5], vals[7], vals[8])
                    if rc < 0:
                        # Error message for invalid r value
                        err_msg = QtWidgets.QMessageBox()
                        err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                        err_msg.setText('Error')
                        err_msg.setInformativeText('R value is not valid')
                        err_msg.setWindowTitle('Error')
                        err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                        err_msg.exec_()
                    else:
                        r_val = round(float(rc), 4)
                        self.output_le.setText(str(r_val))

                except (TypeError, ValueError):
                    pass

        self.r_vs_em = True
        self.r_vs_he = True
        self.r_vs_th = True
        self.r_vs_ang = True

        emm1 = 0.0001
        emm2 = 0.82
        self.emm = np.linspace(emm1, emm2, num=51)

        def graph_r_vs_em():
            vals = input_values()

            rc = np.array([])
            for i in range(0, len(self.emm)):
                try:
                    rc = np.append(rc, both_fit1h(vals[4], vals[6], vals[0], vals[1], vals[5], self.emm[i], vals[8]))

                except (TypeError):
                    err_msg = QtWidgets.QMessageBox()
                    err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                    err_msg.setText('Incorrect values')
                    err_msg.setInformativeText('Incorrect values for graphing')
                    err_msg.setWindowTitle('Error')
                    err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                    err_msg.exec_()
                    return

            output_em_graph = pg.PlotCurveItem(clear=True, pen=pg.mkPen(color_r, width=2),
                                               name='R Value vs Effective emittance')

            self.curve_graph_widget.setLabel("left", "R Value", **styles)
            self.curve_graph_widget.setLabel("bottom", "Effective Emittance", **styles)
            self.r_vs_em = False
            if self.checkBox.isChecked():
                if self.r_vs_he & self.r_vs_th & self.r_vs_ang:
                    output_em_graph.setData(self.emm, rc)
                    self.curve_graph_widget.addItem(output_em_graph)
                else:
                    self.r_vs_he = True
                    self.r_vs_th = True
                    self.r_vs_ang = True
                    self.curve_graph_widget.clear()
                    output_em_graph.setData(self.emm, rc)
                    self.curve_graph_widget.addItem(output_em_graph)

            else:
                self.curve_graph_widget.clear()
                output_em_graph.setData(self.emm, rc)
                self.curve_graph_widget.addItem(output_em_graph)

        height1 = 4
        height2 = 96
        self.height = np.linspace(height1, height2, num=601)

        def graph_r_vs_height():
            vals = input_values()

            try:
                rc_fit = both_fit(vals[6], vals[0], vals[1], vals[5], vals[7], vals[8])

            except TypeError:
                err_msg = QtWidgets.QMessageBox()
                err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                err_msg.setText('Incorrect values')
                err_msg.setInformativeText('Incorrect values for graphing')
                err_msg.setWindowTitle('Error')
                err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                err_msg.exec_()
                return

            output_he_graph = pg.PlotCurveItem(clear=True, pen=pg.mkPen(color_r, width=2), name='R Value vs Height')

            self.curve_graph_widget.setLabel("left", "R Value", **styles)
            self.curve_graph_widget.setLabel("bottom", "Height", **styles)
            self.r_vs_he = False
            if self.checkBox.isChecked():
                if self.r_vs_em & self.r_vs_th & self.r_vs_ang:
                    output_he_graph.setData(self.height, rc_fit)
                    self.curve_graph_widget.addItem(output_he_graph)

                else:
                    self.r_vs_em = True
                    self.r_vs_th = True
                    self.r_vs_ang = True
                    self.curve_graph_widget.clear()
                    output_he_graph.setData(self.height, rc_fit)
                    self.curve_graph_widget.addItem(output_he_graph)

            else:
                self.curve_graph_widget.clear()
                output_he_graph.setData(self.height, rc_fit)
                self.curve_graph_widget.addItem(output_he_graph)

        self.height_a = np.array([4, 5, 6, 7, 8, 12, 16, 20, 24, 30, 36, 42, 48, 60, 72, 84, 96])
        self.thickness = np.array([13, 20, 40, 90, 114, 143])

        def graph_r_vs_thickness():
            vals = input_values()

            rc_fit_h = np.array([])
            rd = np.zeros(shape=(len(self.height_a), len(self.thickness)))
            for j in range(0, len(self.height_a)):
                r_value = np.array([])
                try:
                    v = np.array([[vals[0], vals[1], self.height_a[j], vals[7]]])

                except TypeError:
                    err_msg = QtWidgets.QMessageBox()
                    err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                    err_msg.setText('Incorrect values')
                    err_msg.setInformativeText('Incorrect values for graphing')
                    err_msg.setWindowTitle('Error')
                    err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                    err_msg.exec_()
                    return

                for i in range(0, len(self.thickness)):
                    r_value = np.append(r_value, get_r_t(v, vals[6], self.thickness[i], vals[8]))
                rd[j] = r_value

            rd = np.transpose(rd)
            for i in range(0, len(self.thickness)):
                rd_a = np.ndarray.flatten(rd[:][i])
                pchip_interp = PchipInterpolator(self.height_a, rd_a)
                rc_fit_h = np.append(rc_fit_h, pchip_interp(vals[4]))

            rc_fit_t = np.array([])
            thick1 = 13
            thick2 = 143
            thick = np.linspace(thick1, thick2, num=301)
            pchip_interp = PchipInterpolator(self.thickness, rc_fit_h)
            for i in range(0, len(thick)):
                rc_fit_t = np.append(rc_fit_t, pchip_interp(thick[i]))

            output_th_graph = pg.PlotCurveItem(clear=True, pen=pg.mkPen(color_r, width=2), name='R Value vs Thickness')

            self.curve_graph_widget.setLabel("left", "R Value", **styles)
            self.curve_graph_widget.setLabel("bottom", "Thickness", **styles)
            self.r_vs_th = False
            if self.checkBox.isChecked():
                if self.r_vs_em & self.r_vs_he & self.r_vs_ang:
                    output_th_graph.setData(thick, rc_fit_t)
                    self.curve_graph_widget.addItem(output_th_graph)
                else:
                    self.r_vs_em = True
                    self.r_vs_he = True
                    self.r_vs_ang = True
                    self.curve_graph_widget.clear()
                    output_th_graph.setData(thick, rc_fit_t)
                    self.curve_graph_widget.addItem(output_th_graph)

            else:
                self.curve_graph_widget.clear()
                output_th_graph.setData(thick, rc_fit_t)
                self.curve_graph_widget.addItem(output_th_graph)

        angle1 = 0
        angle2 = 90
        self.angle = np.linspace(angle1, angle2, num=601)
        self.angle_a = np.array([0, 5, 10, 15, 30, 45, 60, 75, 90])

        def graph_r_vs_angle():
            vals = input_values()

            rc_fit_a = np.array([])
            for i in range(0, len(self.angle_a)):
                try:
                    rc_fit_a = np.append(rc_fit_a,
                                         both_fit1h(vals[4], self.angle_a[i], vals[0], vals[1], vals[5], vals[7],
                                                    vals[8]))

                except TypeError:
                    err_msg = QtWidgets.QMessageBox()
                    err_msg.setIcon(QtWidgets.QMessageBox.Critical)
                    err_msg.setText('Incorrect values')
                    err_msg.setInformativeText('Incorrect values for graphing')
                    err_msg.setWindowTitle('Error')
                    err_msg.setGeometry(QtCore.QRect(800, 800, 500, 100))
                    err_msg.exec_()
                    return

            pchip_interp = PchipInterpolator(self.angle_a, rc_fit_a)
            rc = np.array([])
            for j in range(0, len(self.angle)):
                rc = np.append(rc, pchip_interp(self.angle[j]))

            r_angle_graph = pg.PlotCurveItem(clear=True, pen=pg.mkPen(color_r, width=2), name='R Value vs Angle')
            self.curve_graph_widget.setLabel("left", "R Value", **styles)
            self.curve_graph_widget.setLabel("bottom", "Angle", **styles)
            self.r_vs_ang = False
            if self.checkBox.isChecked():
                if self.r_vs_em & self.r_vs_he & self.r_vs_th:
                    r_angle_graph.setData(self.angle, rc)
                    self.curve_graph_widget.addItem(r_angle_graph)
                else:
                    self.r_vs_em = True
                    self.r_vs_he = True
                    self.r_vs_th = True
                    self.curve_graph_widget.clear()
                    r_angle_graph.setData(self.angle, rc)
                    self.curve_graph_widget.addItem(r_angle_graph)

            else:
                self.curve_graph_widget.clear()
                r_angle_graph.setData(self.angle, rc)
                self.curve_graph_widget.addItem(r_angle_graph)

        def reset():
            scene.clear()
            self.curve_graph_widget.clear()
            self.angle_le.setText('')
            self.height_le.setText('')
            self.thickness_le.setText('')
            self.intemp_le.setText('')
            self.outtemp_le.setText('')
            self.em_le.setText('')
            self.output_le.setText('')
            self.curve_graph_widget.setLabel("left", "", **styles)
            self.curve_graph_widget.setLabel("bottom", "", **styles)
            self.r_vs_em = True
            self.r_vs_he = True
            self.r_vs_th = True
            self.r_vs_ang = True

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.compute_button.clicked.connect(compute)
        self.reset_button.clicked.connect(reset)
        self.output_em_button.clicked.connect(graph_r_vs_em)
        self.output_he_button.clicked.connect(graph_r_vs_height)
        self.output_th_button.clicked.connect(graph_r_vs_thickness)
        self.r_angle_button.clicked.connect(graph_r_vs_angle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermal Resistance Calculator"))
        self.label_5.setText(_translate("MainWindow", "Angle"))
        self.label_6.setText(_translate("MainWindow", "Height"))
        self.label_7.setText(_translate("MainWindow", "Thickness"))
        self.label_8.setToolTip(_translate("MainWindow", "Inner temperature"))
        self.label_8.setText(_translate("MainWindow", "Inner Temp."))
        self.label_9.setToolTip(_translate("MainWindow", "Outer temperature"))
        self.label_9.setText(_translate("MainWindow", "Outer Temp."))
        self.label_10.setToolTip(_translate("MainWindow", "Effective emittance"))
        self.label_10.setText(_translate("MainWindow", "EM"))
        self.angle_le.setToolTip(_translate("MainWindow", "Values should start from 0"))
        self.intemp_le.setToolTip(_translate("MainWindow", "Takes up to 4 decimals places"))
        self.outtemp_le.setToolTip(_translate("MainWindow", "Takes up to 4 decimals places"))
        self.em_le.setToolTip(_translate("MainWindow", "Takes up to 4 decimals places"))
        self.label_11.setToolTip(_translate("MainWindow", "Thermal resistance"))
        self.label_11.setText(_translate("MainWindow", "R-Value"))
        self.compute_button.setText(_translate("MainWindow", "Compute"))
        self.reset_button.setToolTip(_translate("MainWindow", "Reset values and graphs"))
        self.r_angle_button.setToolTip(_translate("MainWindow", "Plots graph using R value versus angle"))
        self.r_angle_button.setText(_translate("MainWindow", "R vs Angle"))
        self.output_th_button.setToolTip(_translate("MainWindow", "Plots graph using R value versus thickness"))
        self.output_th_button.setText(_translate("MainWindow", "R vs Thickness"))
        self.output_he_button.setToolTip(_translate("MainWindow", "Plots graph using R value versus height"))
        self.output_he_button.setText(_translate("MainWindow", "R vs Height"))
        self.output_em_button.setToolTip(
            _translate("MainWindow", "Plots graph using R value versus effective emittance"))
        self.output_em_button.setText(_translate("MainWindow", "R vs EM"))
        self.checkBox.setText(_translate("MainWindow", "Overlay Plots"))
        self.label.setText(_translate("MainWindow", "Input"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.label_3.setText(_translate("MainWindow", "Rectangle Graph"))
        self.label_4.setText(_translate("MainWindow", "Curve Graph"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
