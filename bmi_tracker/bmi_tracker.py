# Beginner-friendly BMI Tracker Application
import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt5.QtCore import Qt

class BMIApp(QWidget):
    
    DB_NAME = "student_bmi.db"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Tracker")
        self.setGeometry(100, 100, 800, 500)

        #Store selected student's ID
        self.selected_student_id = None

        self.init_db()
        self.create_widgets()
        self.load_data()

    # Creates the database and table if they don't exist
    def init_db(self):
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS
            students (          
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                height REAL,
                                weigth REAL,
                                bmi REAL,
                                category TEXT,
                                message TEXT)''')
            conn.commit()

    # Calculates BMI and returns the category and message
    def calculate_bmi(self, weight, height):
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return round(bmi, 2), "Underweight", "Stay nourished and strong"
        elif 18.5 <= bmi < 24.9:
            return round(bmi, 2), "Normal", "Keep up the good work"
        elif 25 <= bmi <29.9:
            return round(bmi, 2), "Overweight", "Stay active and healthy"
        else:
            return round(bmi, 2), "Obese", "Your health is a priority"

    # Adds student info to the database and refreshes the table
    def add_student(self):
        name = self.name_entry.text().strip()
        try:
            # Divide by 100 to convert cm to meters
            height = float(self.height_entry.text()) / 100
            weight = float(self.weight_entry.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input! Please enter numeric values only.")
            return
        
        bmi, category, message = self.calculate_bmi(height, weight)

        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (name, height, weight, bmi, category, message) VALUES (?, ?, ?, ?, ?, ?)",
                           (name, height, weight, bmi, category, message))
            conn.commit()
        
        self.load_data()
        self.clear_inputs()
        
        QMessageBox.information(self, "Success", f"{name} added successfully!\nBMI: {bmi} ({category})")

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