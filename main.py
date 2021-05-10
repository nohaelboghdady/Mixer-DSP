# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow,QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsPixmapItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import exp
import logging
# Remove all handlers associated with the root logger object.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='test.log', level=logging.DEBUG,format='%(asctime)s:%(message)s' )

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1266, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.Image1Button = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Image1Button.setIcon(icon)
        self.Image1Button.setObjectName("Image1Button")
        self.horizontalLayout_5.addWidget(self.Image1Button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.Image1_components = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Image1_components.setFont(font)
        self.Image1_components.setObjectName("Image1_components")
        self.Image1_components.addItem("")
        self.Image1_components.addItem("")
        self.Image1_components.addItem("")
        self.Image1_components.addItem("")
        self.horizontalLayout_5.addWidget(self.Image1_components)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.image1_Display = QtWidgets.QGraphicsView(self.centralwidget)
        self.image1_Display.setObjectName("image1_Display")
        self.horizontalLayout_6.addWidget(self.image1_Display)
        self.image1_Display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.image1_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.image1_CompDisplay = QtWidgets.QGraphicsView(self.centralwidget)
        self.image1_CompDisplay.setObjectName("image1_CompDisplay")
        self.horizontalLayout_6.addWidget(self.image1_CompDisplay)
        self.image1_CompDisplay.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.image1_CompDisplay.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.Image2Button = QtWidgets.QPushButton(self.centralwidget)
        self.Image2Button.setIcon(icon)
        self.Image2Button.setObjectName("Image2Button")
        self.horizontalLayout_2.addWidget(self.Image2Button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.Image2_components = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Image2_components.setFont(font)
        self.Image2_components.setObjectName("image2_components")
        self.Image2_components.addItem("")
        self.Image2_components.addItem("")
        self.Image2_components.addItem("")
        self.Image2_components.addItem("")
        self.horizontalLayout_2.addWidget(self.Image2_components)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.image2_Display = QtWidgets.QGraphicsView(self.centralwidget)
        self.image2_Display.setObjectName("image2_Display")
        self.horizontalLayout_4.addWidget(self.image2_Display)
        self.image2_Display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.image2_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.image2_CompDisplay = QtWidgets.QGraphicsView(self.centralwidget)
        self.image2_CompDisplay .setObjectName("image2_CompDisplay ")
        self.horizontalLayout_4.addWidget(self.image2_CompDisplay )
        self.image2_CompDisplay.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.image2_CompDisplay.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 5, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.Component1 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Component1.setFont(font)
        self.Component1.setObjectName("Component1")
        self.Component1.addItem("")
        self.Component1.addItem("")
        self.horizontalLayout_10.addWidget(self.Component1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.comp1_Slider = QtWidgets.QSlider(self.centralwidget)
        self.comp1_Slider.setMinimumSize(QtCore.QSize(200, 0))
        self.comp1_Slider.setMaximum(100)
        self.comp1_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.comp1_Slider.setObjectName("comp1_Slider")
        self.horizontalLayout_10.addWidget(self.comp1_Slider)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.component2_components = QtWidgets.QComboBox(self.centralwidget)
        self.component2_components.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.component2_components.setFont(font)
        self.component2_components.setObjectName("component2_components")
        self.component2_components.addItem("")
        self.component2_components.addItem("")
        self.component2_components.addItem("")
        self.component2_components.addItem("")
        self.component2_components.addItem("")
        self.component2_components.addItem("")
        self.horizontalLayout_13.addWidget(self.component2_components)
        self.gridLayout_4.addLayout(self.horizontalLayout_13, 7, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.Component2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Component2.setFont(font)
        self.Component2.setObjectName("c")
        self.Component2.addItem("")
        self.Component2.addItem("")
        self.horizontalLayout_12.addWidget(self.Component2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.comp2_Slider = QtWidgets.QSlider(self.centralwidget)
        self.comp2_Slider.setMinimumSize(QtCore.QSize(200, 0))
        self.comp2_Slider.setMaximum(100)
        self.comp2_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.comp2_Slider.setObjectName("comp2_Slider")
        self.horizontalLayout_12.addWidget(self.comp2_Slider)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 6, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.component1_components = QtWidgets.QComboBox(self.centralwidget)
        self.component1_components.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.component1_components.setFont(font)
        self.component1_components.setObjectName("component1_components")
        self.component1_components.addItem("")
        self.component1_components.addItem("")
        self.component1_components.addItem("")
        self.component1_components.addItem("")
        self.component1_components.addItem("")
        self.component1_components.addItem("")
        self.horizontalLayout_11.addWidget(self.component1_components)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.MixerOutput = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.MixerOutput.setFont(font)
        self.MixerOutput.setObjectName("MixerOutput")
        self.MixerOutput.addItem("")
        self.MixerOutput.addItem("")
        self.horizontalLayout_9.addWidget(self.MixerOutput)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.output1_Display = QtWidgets.QGraphicsView(self.centralwidget)
        self.output1_Display.setObjectName("output1_Display")
        self.horizontalLayout_7.addWidget(self.output1_Display)
        self.output1_Display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.output1_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.output2_Display = QtWidgets.QGraphicsView(self.centralwidget)
        self.output2_Display.setObjectName("output2_Display")
        self.horizontalLayout_7.addWidget(self.output2_Display)
        self.output2_Display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.output2_Display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1266, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        #create graphics scenes
        self.inputScene1 = QGraphicsScene()
        self.inputScene2 = QGraphicsScene()
        
        self.compScene1 = QGraphicsScene()
        self.compScene2 = QGraphicsScene()
        
        self.outputScene1 = QGraphicsScene()
        self.outputScene2 = QGraphicsScene()
        
        #arrays
        self.inputDisplays = [self.image1_Display,self.image2_Display]
        self.compDisplays = [self.image1_CompDisplay,self.image2_CompDisplay]
        self.outputDisplays = [self.output1_Display, self.output2_Display]
        
        self.inputScenes = [self.inputScene1,self.inputScene2]
        self.compScenes = [self.compScene1,self.compScene2]
        self.outputScenes = [self.outputScene1,self.outputScene2]
        
        #dropdowns
        self.InputDropdown = [self.Image1_components,self.Image2_components]
        
        self.outputComponents = [None,None]
        
        self.inputImages = [None,None]
        self.outputImages = [None,None]
        
        self.firstInputImage = 0;
        self.secondInputImage = 1;
        
        self.comp1_img1 = None
        self.comp1_img2 = None
        self.comp2_img1 = None
        self.comp2_img2= None

        self.Image1Button.clicked.connect(lambda: self.createInstance(self.firstInputImage))
        self.Image2Button.clicked.connect(lambda: self.createInstance(self.secondInputImage))
    
        self.Image1_components.activated.connect(lambda: self.changeComponent(self.firstInputImage, self.Image1_components.currentIndex()))
        self.Image2_components.activated.connect(lambda: self.changeComponent(self.secondInputImage, self.Image2_components.currentIndex()))
    
        self.MixerOutput.activated.connect(lambda: self.chooseOuput(self.MixerOutput.currentIndex()))
        self.Component1.activated.connect(lambda: self.chooseOuput(self.MixerOutput.currentIndex()))
        self.Component2.activated.connect(lambda: self.chooseOuput(self.MixerOutput.currentIndex()))
        self.component1_components.activated.connect(lambda: self.chooseOuput(self.MixerOutput.currentIndex()))
        self.component2_components.activated.connect(lambda: self.chooseOuput(self.MixerOutput.currentIndex()))
        
        self.comp1_Slider.valueChanged.connect(self.updateSliderValue)
        self.comp2_Slider.valueChanged.connect(self.updateSliderValue)
    
    def createInstance(self,index):
        
        fixedDisplay = self.inputDisplays[index]
        fixedScene = self.inputScenes[index]
        
        ComponentsDisplay = self.compDisplays[index]
        ComponentsScene = self.compScenes[index]
        
        
        currentImage = Image()
        isLoaded = currentImage.loadImage(index,self.output2_Display.size(),fixedScene,fixedDisplay,ComponentsScene,ComponentsDisplay)

        print(isLoaded)
        if isLoaded:
            self.inputImages[index] = currentImage
            logging.info('User opened a new Image: image%s' %index )



    def changeComponent(self,imageIndex,choice):
        currentImage = self.inputImages[imageIndex]
        currentImage.changeComponent(choice)
        logging.info('User changed the display component ')
    
    
    def chooseOuput(self,displayIndex): 
        
        #initialize slider value to zero
        
        
        #get targeted output display & scene
        currentDisplay = self.outputDisplays[displayIndex]
        currentScene = self.outputScenes[displayIndex]

        logging.debug('User chose output Display %s' %displayIndex)

    
        #assign 1st image to chosen output display 
        self.outputImages[0] = self.inputImages[self.Component1.currentIndex()]
        
        #assign 2nd image to chosen output display 
        self.outputImages[1] = self.inputImages[self.Component2.currentIndex()]
        
 
        # get chosen images' instances for output manipulation
        image1 = self.outputImages[0]
        image2 = self.outputImages[1]
        
        logging.info('User selected image%s for component1' %(self.Component1.currentIndex()+1))
        logging.info('User selected image%s for component2' %(self.Component2.currentIndex()+1))
        
        
        #which component for each image
        firstImageChoice = self.component1_components.currentIndex()
        secondImageChoice = self.component2_components.currentIndex()
        
        
        
        
        #transfer to class for image manipulation
        self.comp1_img1 = image1.updateOutputScene(currentDisplay,currentScene,self.component1_components.currentIndex())
        self.comp1_img2 = image2.updateOutputScene(currentDisplay,currentScene,self.component1_components.currentIndex())
        
        #for 2nd combobox
        self.comp2_img1 = image1.updateOutputScene(currentDisplay,currentScene,self.component2_components.currentIndex())
        self.comp2_img2 = image2.updateOutputScene(currentDisplay,currentScene,self.component2_components.currentIndex())
        
        self.updateSliderValue()
        
        


    def updateSliderValue(self):
        image = Image()
        
        if self.component1_components.currentIndex() == 0 or self.component1_components.currentIndex() == 2 or self.component1_components.currentIndex() == 4:
            realTerm = image.sliderEffect(self.comp1_img1, self.comp1_img2,self.comp1_Slider.value())
            ImagTerm = image.sliderEffect(self.comp2_img2,self.comp2_img1,self.comp2_Slider.value())
        elif self.component1_components.currentIndex() == 1 or self.component1_components.currentIndex() == 3 or self.component1_components.currentIndex() == 5:
            ImagTerm = image.sliderEffect(self.comp1_img1, self.comp1_img2,self.comp1_Slider.value())
            realTerm = image.sliderEffect(self.comp2_img2,self.comp2_img1,self.comp2_Slider.value())
            
        
        if (self.component1_components.currentIndex() == 2 or self.component1_components.currentIndex() == 3 ) and (self.component2_components.currentIndex() == 2 or self.component2_components.currentIndex() == 3):
            isReal_Imag = True
        else:
            isReal_Imag = False
            
        logging.info('User updated slider value')
        # newComponent = newComp1 + newComp2
        self.outputImages[self.firstInputImage].redraw(realTerm,ImagTerm,isReal_Imag)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        self.Image1Button.setText(_translate("MainWindow", "Open"))
        self.Image1_components.setCurrentText(_translate("MainWindow", "Magnitude Spectrum"))
        self.Image1_components.setItemText(0, _translate("MainWindow", "Magnitude Spectrum"))
        self.Image1_components.setItemText(1, _translate("MainWindow", "Phase Spectrum"))
        self.Image1_components.setItemText(2, _translate("MainWindow", "Real Component"))
        self.Image1_components.setItemText(3, _translate("MainWindow", "Imaginary Component"))
        self.label_2.setText(_translate("MainWindow", "Image 2"))
        self.Image2Button.setText(_translate("MainWindow", "Open"))
        self.Image2_components.setCurrentText(_translate("MainWindow", "Magnitude Spectrum"))
        self.Image2_components.setItemText(0, _translate("MainWindow", "Magnitude Spectrum"))
        self.Image2_components.setItemText(1, _translate("MainWindow", "Phase Spectrum"))
        self.Image2_components.setItemText(2, _translate("MainWindow", "Real Component"))
        self.Image2_components.setItemText(3, _translate("MainWindow", "Imaginary Component"))
        self.label_6.setText(_translate("MainWindow", "Component 1:   "))
        self.Component1.setCurrentText(_translate("MainWindow", "Image 1"))
        self.Component1.setItemText(0, _translate("MainWindow", "Image 1"))
        self.Component1.setItemText(1, _translate("MainWindow", "Image 2"))
        self.component2_components.setCurrentText(_translate("MainWindow", "Magnitude Component"))
        self.component2_components.setItemText(0, _translate("MainWindow", "Magnitude Component"))
        self.component2_components.setItemText(1, _translate("MainWindow", "Phase Component"))
        self.component2_components.setItemText(2, _translate("MainWindow", "Real Component"))
        self.component2_components.setItemText(3, _translate("MainWindow", "Imaginary Component"))
        self.component2_components.setItemText(4, _translate("MainWindow", "Uniform Magnitude"))
        self.component2_components.setItemText(5, _translate("MainWindow", "Uniform Phase"))
        self.label_7.setText(_translate("MainWindow", "Component 2:   "))
        self.Component2.setCurrentText(_translate("MainWindow", "Image 1"))
        self.Component2.setItemText(0, _translate("MainWindow", "Image 1"))
        self.Component2.setItemText(1, _translate("MainWindow", "Image 2"))
        self.component1_components.setCurrentText(_translate("MainWindow", "Magnitude Component"))
        self.component1_components.setItemText(0, _translate("MainWindow", "Magnitude Component"))
        self.component1_components.setItemText(1, _translate("MainWindow", "Phase Component"))
        self.component1_components.setItemText(2, _translate("MainWindow", "Real Component"))
        self.component1_components.setItemText(3, _translate("MainWindow", "Imaginary Component"))
        self.component1_components.setItemText(4, _translate("MainWindow", "Uniform Magnitude"))
        self.component1_components.setItemText(5, _translate("MainWindow", "Uniform Phase"))
        self.label_5.setText(_translate("MainWindow", "Mixer Output to:   "))
        self.MixerOutput.setCurrentText(_translate("MainWindow", "Output 1"))
        self.MixerOutput.setItemText(0, _translate("MainWindow", "Output 1"))
        self.MixerOutput.setItemText(1, _translate("MainWindow", "Output 2"))
        self.label_3.setText(_translate("MainWindow", "Output 1"))
        self.label_4.setText(_translate("MainWindow", "Output 2"))

class Image(Ui_MainWindow):
    
    imageSizes = [None,None]
    previousImage = None
    
    def __init__(self):
        self.image_dimensions = None
        self.pixmap = None
        self.pixmapItem = None
        self.fixedDisplay = None
        self.fixedScene = None
        self.ComponentsScene = None
        self.ComponentsDisplay = None
        self.inputImageArray = None
        self.magnitude_spectrum = None
        self.magnitudeItem = None
        self.phase_spectrum = None
        self.phaseItem = None
        self.real_component = None
        self.realItem = None
        self.imag_component = None
        self.imagItem = None
        self.outputDisplay = None
        self.outputScene = None
        self.uniform_phase = None
        self.uniform_magnitude = None
        self.matrixComponents = [None,None,None,None,None,None]
        self.components = [None,None,None,None,None,None]

        
        

    def loadImage(self,index,size,fixedScene,fixedDisplay,ComponentsScene,ComponentsDisplay):
        """ This function will load the user selected image""" 
        #change extension based on photos for test (.jpg,.jpeg,.png)
        image_path = QFileDialog.getOpenFileName(filter="Image (*.png*)")[0]
        
        image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # frame = image
        
        #for the fft & slider manipulation
        self.inputImageArray = image
        
        self.image_dimensions = size
        print('file:',image_path)


        #change to pixmap
        self.image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)

        self.pixmap = QPixmap.fromImage(self.image)
        
        #keep previos pixmap
        self.previousImage = self.imageSizes[index]
        # append to images array
        self.imageSizes[index] = self.pixmap.size()

        #Compare Image size for validation
        isEqual = self.validateSize(index)
        
        if (isEqual):

            ### calculate all required components
            self.getComponents()
            
            #get scene,view
            self.fixedDisplay = fixedDisplay
            self.fixedScene = fixedScene
            self.ComponentsScene = ComponentsScene
            self.ComponentsDisplay = ComponentsDisplay
            
            #add to scene to be drawn
            self.addToScene(index)
            
            
            
            return True
            
        else: 
            return False
                                                
      
    
        
    def addToScene(self,index):

        
        ###### how to view the image ######
        # scroll & keep its size
        # self.pixmap = self.pixmap.scaled(self.graphicsView.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        #fit 
        # self.pixmap = self.pixmap.scaled(self.graphicsView.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        #fill
        self.pixmap = self.pixmap.scaled(self.image_dimensions, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # QGraphicsPixmapItem class provides a pixmap item that you can add to a QGraphicsScene.
        self.pixmapItem = QGraphicsPixmapItem(self.pixmap)
        
        #magnitude
        self.magnitude_spectrum = self.magnitude_spectrum.scaled(self.image_dimensions, Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        self.magnitudeItem = QGraphicsPixmapItem(self.magnitude_spectrum)
        self.components[0] = self.magnitudeItem
        
        #phase
        self.phase_spectrum = self.phase_spectrum.scaled(self.image_dimensions, Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        self.phaseItem = QGraphicsPixmapItem(self.phase_spectrum)
        self.components[1] = self.phaseItem
        
        #real
        self.real_component = self.real_component.scaled(self.image_dimensions, Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        self.realItem = QGraphicsPixmapItem(self.real_component)
        self.components[2] = self.realItem
        
        #imaginary
        self.imag_component = self.imag_component.scaled(self.image_dimensions, Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        self.imagItem = QGraphicsPixmapItem(self.imag_component)
        self.components[3] = self.imagItem
        
        #add the item to the graphics set
        self.fixedScene.addItem(self.pixmapItem)
        
        #show which component?
        self.ComponentsScene.addItem(self.imagItem)
        self.ComponentsScene.addItem(self.realItem)
        self.ComponentsScene.addItem(self.phaseItem)
        self.ComponentsScene.addItem(self.magnitudeItem)
        
        
        
        
        #set the graphics scene to our graphics view
        self.fixedDisplay.setScene(self.fixedScene)
        self.ComponentsDisplay.setScene(self.ComponentsScene)
        
    
        
    def validateSize(self,index):
        
        if (self.imageSizes[0] == self.imageSizes[1]) or (self.imageSizes[0]!= None and self.imageSizes[1] == None) or (self.imageSizes[0]== None and self.imageSizes[1] != None):
            # self.showMessage('Alert', 'Please upload another image for comparison ')
            return True
            logging.info('User opened an accepted image size')
        else:
            self.imageSizes[index] = self.previousImage
            self.showMessage('Warning', 'Size mismatch, please load another image.  ')
            logging.warning('User loaded different size images')
            return False
      
        
    def getComponents(self):
        
        dft = np.fft.fft2(self.inputImageArray)
        fshift = np.fft.fftshift(dft)
        
        #getMagnitude
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        shape = np.shape(magnitude_spectrum)
        self.matrixComponents[0] = np.abs(dft)
        magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
        magnitudeFrame = cv2.cvtColor(magnitude_spectrum, cv2.COLOR_BGR2RGB)
        magnitude_image = QImage(magnitudeFrame, magnitudeFrame.shape[1],magnitudeFrame.shape[0],magnitudeFrame.strides[0],QImage.Format_RGB888) 
        self.magnitude_spectrum = QPixmap.fromImage(magnitude_image)
        
        #getPhase
        phase_spectrum = np.angle(fshift)
        self.matrixComponents[1] = np.angle(dft)
        phase_spectrum = np.asarray(phase_spectrum, dtype=np.uint8)
        phaseFrame = cv2.cvtColor(phase_spectrum, cv2.COLOR_BGR2RGB)
        phase_image = QImage(phaseFrame, phaseFrame.shape[1],phaseFrame.shape[0],phaseFrame.strides[0],QImage.Format_RGB888)
        self.phase_spectrum = QPixmap.fromImage(phase_image)
        
        #getReal
        real_component = np.real(fshift)
        self.matrixComponents[2] = np.real(dft)
        real_component = np.asarray(real_component, dtype=np.uint8)
        realFrame = cv2.cvtColor(real_component, cv2.COLOR_BGR2RGB)
        real_image = QImage(realFrame, realFrame.shape[1],realFrame.shape[0],realFrame.strides[0],QImage.Format_RGB888)
        self.real_component = QPixmap.fromImage(real_image) 
        
        #getImaginary
        imaginary_component = np.imag(fshift)
        self.matrixComponents[3] = np.imag(dft)
        imaginary_component = np.asarray(imaginary_component, dtype=np.uint8)
        imagFrame = cv2.cvtColor(imaginary_component, cv2.COLOR_BGR2RGB)
        imaginary_image = QImage(imagFrame, imagFrame.shape[1],imagFrame.shape[0],imagFrame.strides[0],QImage.Format_RGB888)
        self.imag_component = QPixmap.fromImage(imaginary_image)
        
        
        #get uniform magnitude(all magnitude values are set to 1)
        self.matrixComponents[4] = np.full(shape, 0)
        # self.matrixComponents[4] = np.abs(dft)/np.abs(dft)
         
        # get uniform phase (all phase values are set to 0)
        self.matrixComponents[5] = np.full(shape,1)
    
    def changeComponent(self,choice):

        currentComponent = self.components[choice]
        # currentComponent = self.ComponentsScene.items()[choice]
        logging.info('User chosen new component updated on screen')
        self.ComponentsScene.removeItem(currentComponent)
        self.ComponentsScene.addItem(currentComponent)

        #set the graphics scene to our graphics view
        self.ComponentsDisplay.setScene(self.ComponentsScene)
        
   
        
    def updateOutputScene(self,display,scene,choice):
        self.outputDisplay = display
        self.outputScene = scene
        
        # self.Comp2Manipulate = self.components[choice]
        Comp2Manipulate = self.matrixComponents[choice]
        
        
        # self.redraw()
        
        return Comp2Manipulate
    
    
    #manipulate the image based on its slider values then redraw it
    def sliderEffect(self,comp1,comp2,value):
        
        newComp = (comp1 * value/100) + (comp2 * (100-value)/100)

        return newComp


    def redraw(self,realTerm,ImagTerm,isReal_Imag):
        
        #Fourier Inverse
        if isReal_Imag:
            imageMatrix = realTerm + 1j*ImagTerm
            image = np.fft.ifft2(imageMatrix) 
        else:
            imageMatrix= realTerm*np.cos(ImagTerm)+1j*realTerm*np.sin(ImagTerm)
            image = np.fft.ifft2(imageMatrix)
            
        
        image = np.asarray(image, dtype=np.uint8)
        imageFrame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        newImage = QImage(imageFrame, imageFrame.shape[1],imageFrame.shape[0],imageFrame.strides[0],QImage.Format_RGB888) 
        
        
        #display 
        image2Darw = QPixmap.fromImage(newImage)
        image2Darw = image2Darw.scaled(self.image_dimensions, Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        item = QGraphicsPixmapItem(image2Darw)
        self.outputScene.addItem(item) 
        self.outputDisplay.setScene(self.outputScene)
        

    def showMessage(self, header, message):
        """
        Responsible for showing message boxes
        ============= ===================================================================================
        **Arguments**
        header:       Box header title.
        message       the informative message to be shown.
        button:       button type.
        icon:         icon type.
        ============= ===================================================================================
        """
        msg = QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

