import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QSizePolicy
from PyQt6.QtGui import QPixmap

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "images/d2logo.jpg")

class MachineLearning(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set window title
        self.setWindowTitle("Gazepoint Analysis")
        
        # Set background color to light gray
        self.setStyleSheet("background-color: lightgray; color: black;")

        self.layout = QGridLayout()


        # First directory selector
        self.hbox1 = QHBoxLayout()
        self.label1 = QLabel("Location of gaze file")
        self.label1.setStyleSheet("background-color: white; padding: 5px; qproperty-alignment: 'AlignCenter';")
        self.label1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed) 
        self.label1.show()
        self.button1 = QPushButton("Browse")
        self.button1.clicked.connect(self.select_directory1)
        self.button1.setFixedSize(100, self.label1.height())
        self.layout.addWidget(self.label1, 1, 0)  
        self.layout.addWidget(self.button1, 1, 1)  

        

        # Second directory selector
        self.hbox2 = QHBoxLayout()
        self.label2 = QLabel("Location of fixation file")
        self.label2.setStyleSheet("background-color: white; padding: 5px; qproperty-alignment: 'AlignCenter';")
        self.label2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.label2.show()
        self.button2 = QPushButton("Browse")
        self.button2.clicked.connect(self.select_directory2)
        self.button2.setFixedSize(100,self.label2.height())
        self.layout.addWidget(self.label2, 2, 0) 
        self.layout.addWidget(self.button2, 2, 1) 

        
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.setLayout(self.layout)

    def select_directory1(self):
        dir1 = QFileDialog.getExistingDirectory(self, 'Select gaze file')
        if dir1:
            self.label1.setText(dir1)

    def select_directory2(self):
        dir2 = QFileDialog.getExistingDirectory(self, 'Select fixation file')
        if dir2:  
            self.label2.setText(dir2)