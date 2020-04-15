"""
Write a GUI program that converts seconds to years, weeks, days, hours, and minutes.
For this problem, assume 1 year is 365 days.
"""

# Hello Guys.

# Firstly, we need to import the modules from PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QIntValidator


# Our class MyGUI inherits QWidgets
# we can now add child widgets
class MyGUI(QWidget):

    # This is one of the magic method commonly used in OO Python
    # This method is the stage of instantiation of an instance
    # Part of the Object Lifecycle
    # Lifecycle of an object comprises of creation, manipulation, and destruction
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Here we override the __init__ method of QWidgets
        self.year = 29030400  # Equivalent to 60 seconds, 60 minutes, 24 hour, 7 day, 4 weeks, 12 months and unit in
        # seconds.
        self.week = 604800
        self.day = 86400
        self.hour = 3600
        self.form_layout = QFormLayout()
        self.edit_text = QLineEdit()
        self.submit_button = QPushButton()
        self.msg_box = QMessageBox()
        self.build_window()
        self.build_forms()
        self.applyEvents()

    def build_window(self): # So every method we define inside a class must have formal parameter of self.
        self.setWindowTitle("MyGUI")
        self.setGeometry(0, 0, 200, 150) # We define position-x, position-y, width, height
        self.setLayout(self.form_layout)
        self.show()

    def build_forms(self):
        self.edit_text.setValidator(QIntValidator()) # Here we strict to input only integers
        self.submit_button.setText("Submit")
        self.form_layout.addRow("Seconds: ", self.edit_text)
        self.form_layout.addRow(self.submit_button)

    def applyEvents(self):
        self.submit_button.clicked.connect(self.submit) # This is called signal or bind button with click listener
        # Then whenever the submit_button press it calls the method submit

    def submit(self):
        result = self.compute(self.edit_text.text())
        self.show_dialog(result)

    def compute(self, seconds):
        int_second = int(seconds)
        years = int_second // self.year # Here we use operation floor division for inputted second and a year in unit seconds
        int_second %= self.year # Then we calculate remainder from previous operation
        weeks = int_second // self.week # we calculate again the inputted seconds and a week in unit seconds
        int_second %= self.week
        days = int_second // self.day
        int_second %= self.day
        hours = int_second // self.hour
        int_second %= self.hour
        minutes = int_second // 60
        return "Years: {0}, Weeks: {1}, Days: {2}, Hours: {3}, Minutes: {4}".format(years, weeks, days, hours, minutes)

    def show_dialog(self, message):
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setWindowTitle("Output Dialog")
        self.msg_box.setText(message)
        self.msg_box.setStandardButtons(QMessageBox.Close)
        self.msg_box.exec_()


if __name__ == '__main__': # This is another magic method and commonly used.
    # You use this for either module to be imported or run as a script.
    app = QApplication(sys.argv) # Qt object that manages the flow of the gui program
    my_gui = MyGUI() # Here we call our class
    sys.exit(app.exec_()) # method to exit python and clean up actions
