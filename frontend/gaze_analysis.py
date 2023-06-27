import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QSizePolicy, QLineEdit, QCheckBox, QComboBox
from PyQt6.QtGui import QPixmap

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "images/d2logo.jpg")


class GazeAnalysis(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QGridLayout()

        # Image display
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(
            600, 200, Qt.AspectRatioMode.KeepAspectRatio))

        image_layout = QHBoxLayout()
        image_layout.addStretch(1)
        image_layout.addWidget(self.image_label)
        image_layout.addStretch(1)

        # add the image layout to the grid layout
        self.layout.addLayout(image_layout, 0, 0, 1, 2)

        # First file selector
        self.label1 = QLabel("Path of gaze file")
        self.label1.setStyleSheet(
            "background-color: white; padding: 5px; qproperty-alignment: 'AlignLeft';")
        self.label1.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.button1 = QPushButton("Browse")
        self.button1.clicked.connect(self.select_file1)
        self.button1.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    
        file1_layout = QHBoxLayout()
        file1_layout.addWidget(self.label1)
        file1_layout.addWidget(self.button1)

        self.layout.addLayout(file1_layout, 1, 0, 1, 2)

        # Second file selector
        self.label2 = QLabel("Path of fixation file")
        self.label2.setStyleSheet(
            "background-color: white; padding: 5px; qproperty-alignment: 'AlignLeft';")
        self.label2.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.button2 = QPushButton("Browse")
        self.button2.clicked.connect(self.select_file2)
        self.button2.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)


        file2_layout = QHBoxLayout()
        file2_layout.addWidget(self.label2)
        file2_layout.addWidget(self.button2)

        self.layout.addLayout(file2_layout, 2, 0, 1, 2)

        # Output directory selector
        self.label3 = QLabel("Output path")
        self.label3.setStyleSheet(
            "background-color: white; padding: 5px; qproperty-alignment: 'AlignLeft';")
        self.label3.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.button3 = QPushButton("Browse")
        self.button3.clicked.connect(self.select_directory)
        self.button3.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.label3)
        output_layout.addWidget(self.button3)

        self.layout.addLayout(output_layout, 3, 0, 1, 2)



        # Add the checkbox, dropdown, and text field
        self.checkbox = QCheckBox("Add an event")
        self.checkbox.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.dropdown = QComboBox()
        self.dropdown.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.dropdown.addItems(
            ["Continuous Snapshot", "Cumulative Snapshot", "Overlapping Snapshot", "Event Analytics"])

        self.dropdown.setStyleSheet("""
        QComboBox{
            background-color: white;
            padding: 5px;
            margin: 0px;
        }
        """)
        self.textField = QLineEdit()
        self.textField.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.textField.setStyleSheet(
            "background-color: white; padding: 5px; qproperty-alignment: 'AlignLeft';")
        self.textFieldLabel = QLabel("Window Size (seconds)")
        self.textFieldLabel.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        # Initially disable the dropdown and text field
        self.dropdown.setEnabled(False)
        self.textField.setEnabled(False)

        # Connect the checkbox's stateChanged signal to enable/disable the other widgets
        self.checkbox.stateChanged.connect(self.toggle_event_options)

        self.dropdown.setVisible(False)
        self.textField.setVisible(False)
        self.textFieldLabel.setVisible(False)


        self.layout.addWidget(self.checkbox, 4, 0)
        self.layout.addWidget(self.dropdown, 5, 0)
        self.layout.addWidget(self.textFieldLabel, 4, 1)
        self.layout.addWidget(self.textField, 5, 1)

        # Additional dropdowns and input field for Event Analytics
        self.dropdown2 = QComboBox()
        self.dropdown2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.dropdown2.addItems(["Option 1", "Option 2", "Option 3"])  
        self.dropdown2.setStyleSheet("""
        QComboBox{
            background-color: white;
            padding: 5px;
            margin: 0px;
        }
        """)
        self.dropdown2.setEnabled(False)
        self.dropdown2.setVisible(False)

        self.dropdown3 = QComboBox()
        self.dropdown3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.dropdown3.addItems(["Option 1", "Option 2", "Option 3"]) 
        self.dropdown3.setStyleSheet("""
        QComboBox{
            background-color: white;
            padding: 5px;
            margin: 0px;
        }
        """)
        self.dropdown3.setEnabled(False)
        self.dropdown3.setVisible(False)

        self.layout.addWidget(self.dropdown2, 6, 0)
        self.layout.addWidget(self.dropdown3, 6, 1)


        self.dropdown.currentIndexChanged.connect(self.toggle_event_analytics_options)


        # Create a QVBoxLayout and add the existing QGridLayout to it
        self.outerLayout = QVBoxLayout()
        self.outerLayout.addLayout(self.layout)
        self.outerLayout.addStretch(1)

        # Run Analysis Button 
        self.hbox4 = QHBoxLayout()
        self.button4 = QPushButton("Run Analysis")
        # self.button4.clicked.connect()
        self.button4.setStyleSheet("background-color: #0287e6;")
        # Use the QHBoxLayout to center the button
        self.hbox4.addStretch(1)
        self.hbox4.addWidget(self.button4)
        self.hbox4.addStretch(1)

        # Add the QHBoxLayout to your outer QVBoxLayout
        self.outerLayout.addLayout(self.hbox4)

        self.setLayout(self.outerLayout) 

    def select_file1(self):
        file1, _ = QFileDialog.getOpenFileName(self, 'Select gaze file')
        if file1:
            self.label1.setText(file1)

    def select_file2(self):
        file2, _ = QFileDialog.getOpenFileName(self, 'Select fixation file')
        if file2:
            self.label2.setText(file2)

    def select_directory(self):
        dir1 = QFileDialog.getExistingDirectory(self, 'Select output path')
        if dir1:
            self.label3.setText(dir1)

    def toggle_event_options(self, state):
        # Enable the dropdown and text field if the checkbox is checked, otherwise disable them
        if state == 2:
            self.dropdown.setVisible(True)
            self.textField.setVisible(True)
            self.textFieldLabel.setVisible(True)
            self.dropdown.setEnabled(True)
            self.textField.setEnabled(True)
            self.dropdown.setEnabled(True)
            self.textField.setEnabled(True)
        else:
            self.dropdown.setCurrentIndex(0)  # Reset dropdown to default
            self.dropdown.setEnabled(False)
            self.textField.setEnabled(False)
            self.dropdown.setVisible(False)
            self.textField.setVisible(False)
            self.textFieldLabel.setVisible(False)
            self.dropdown.setEnabled(False)
            self.textField.setEnabled(False)
            self.dropdown2.setEnabled(False)
            self.dropdown3.setEnabled(False)
            self.dropdown2.setVisible(False)
            self.dropdown3.setVisible(False)


    def toggle_event_analytics_options(self):
        # If the selected item is 'Event Analytics', display additional dropdowns and input field
        if self.dropdown.currentText() == 'Event Analytics':
            self.dropdown2.setEnabled(True)
            self.dropdown3.setEnabled(True)
            self.dropdown2.setVisible(True)
            self.dropdown3.setVisible(True)
        else:
            self.dropdown2.setEnabled(False)
            self.dropdown3.setEnabled(False)
            self.dropdown2.setVisible(False)
            self.dropdown3.setVisible(False)

