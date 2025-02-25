# Beginner-friendly BMI Tracker Application
import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt5.QtCore import Qt

class BMIApp(QWidget):
    pass

    def __init__(self):
        super().__init__()

    def init_db(self):
        pass

    def calculate_bmi():
        pass

    def add_student():
        pass

    def load_data(self):
        pass

    def remove_student(self):
        pass

    def edit_student(self):
        pass

    def select_student(self):
        pass

    def clear_inputs(self):
        pass

    def create_widgets(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMIApp()
    window.show()
    sys.exit(app.exec())