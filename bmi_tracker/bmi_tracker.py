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
                                weight REAL,
                                bmi REAL,
                                category TEXT,
                                message TEXT)''')
            conn.commit()

    # Calculates BMI and returns the category and message
    def calculate_bmi(self, height, weight):
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

    # Loads student data into the table
    def load_data(self):
        self.table.setRowCount(0)
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, height, weight, bmi, category, message FROM students")
            students = cursor.fetchall()

        for row_idx, student in enumerate(students):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(student[1:]):
                #Skip id column
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row_idx, col_idx, item)

            # Store the ID in a hidden column
            self.table.setItem(row_idx, 6, QTableWidgetItem(str(student[0])))

    # Removes selected student from the database
    def remove_student(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Warning", "Please select a student to remove.")
            return
        
        student_name = self.table.item(selected_row, 0).text()
        student_id = self.table.item(selected_row, 6).text()

        confirm = QMessageBox.question(self, "Confirm", f"Are you sure you want to remove {student_name}?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.No:
            return
        
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id))
            conn.commit()

        self.load_data()
        self.clear_inputs()
        QMessageBox.information(self, "Success", f"{student_name} removed successfully!")

    # Updates the selected student's data in the database.
    def edit_student(self):
        if self.selected_student_id is None:
            QMessageBox.warning(self, "Warning", "Please select a student to edit.")
            return
        
        name = self.name_entry.text().strip()
        try:
            # Divide by 100 to convert cm to meters
            height = float(self.height_entry.text()) / 100
            weight = float(self.weight_entry.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalud input! Please enter numeric values only.")
            return
        
        bmi, category, message = self.calculate_bmi(height, weight)

        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET name = ?, height = ?, weight = ?, bmi = ?, category = ?, message = ? WHERE id = ?",
                           (name, height, weight, bmi, category, message, self.selected_student_id))
            conn.commit()
        
        self.load_data()
        self.clear_inputs()
        QMessageBox.information(self, "Success", f"{name} updated successfully!\nNew BMI: {bmi} ){category}")
        # Reset selection
        self.selected_student_id = None

    # Fills input fields with selected student data for editing
    def select_student(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return
        
        #Get ID from the hidden column
        self.selected_student_id = self.table.item(selected_row, 6).text()
        self.name_entry.setText(self.table.item(selected_row, 0).text())
        self.height_entry.setText(str(float(self.table.item(selected_row, 1).text()) * 100))
        self.weight_entry.setText(self.table.item(selected_row, 2).text())

    # Clear input fields
    def clear_inputs(self):
        self.name_entry.clear()
        self.height_entry.clear()
        self.weight_entry.clear()

    # Creates GUI elements
    def create_widgets(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(QLabel("Name:"))
        self.name_entry = QLineEdit()
        h_layout.addWidget(self.name_entry)

        h_layout.addWidget(QLabel("Height (cm):"))
        self.height_entry = QLineEdit()
        h_layout.addWidget(self.height_entry)

        h_layout.addWidget(QLabel("Weight (kg):"))
        self.weight_entry = QLineEdit()
        h_layout.addWidget(self.weight_entry)

        self.add_button = QPushButton("Add Student")
        self.add_button.clicked.connect(self.add_student)
        h_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Edit Student")
        self.edit_button.clicked.connect(self.edit_student)
        h_layout.addWidget(self.edit_button)

        v_layout.addLayout(h_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Name", "Height (m)", "Weight(kg)", "BMI", "Category", "Message", "ID"])
        self.table.setColumnHidden(6, True) # hide id column
        self.table.setColumnWidth(5, 260)
        self.table.cellClicked.connect(self.select_student)
        v_layout.addWidget(self.table)

        self.remove_button = QPushButton("Remove Student")
        self.remove_button.clicked.connect(self.remove_student)
        v_layout.addWidget(self.remove_button)

        self.setLayout(v_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMIApp()
    window.show()
    sys.exit(app.exec())