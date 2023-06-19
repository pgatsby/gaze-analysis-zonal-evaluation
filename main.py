from PyQt6.QtWidgets import QApplication, QTabWidget, QVBoxLayout, QWidget
from frontend.gaze_analysis import GazeAnalysis
from frontend.machine_learning import MachineLearning


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set window title
        self.setWindowTitle("D2 Gaze Analytical Tool")

        # Set background color to light gray
        self.setStyleSheet("background-color: lightgray; color: black;")

        # Create a QTabWidget instance
        self.tab_widget = QTabWidget()

        self.gaze_analysis = GazeAnalysis()
        self.machine_learning = MachineLearning()

        self.tab_widget.addTab(self.gaze_analysis, 'Gaze Analysis')
        self.tab_widget.addTab(self.machine_learning, 'Machine Learning')

        # Create the main layout for the window and add the QTabWidget to it
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.tab_widget)

        # Set fixed size for the widget window
        self.resize(600, 500)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()