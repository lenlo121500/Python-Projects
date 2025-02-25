# BMI Tracker

## Overview

BMI Tracker is a simple desktop application built using Python and PyQt5. It allows users to input student data, including height and weight, to calculate Body Mass Index (BMI). The application stores the data in an SQLite database and provides features to add, edit, remove, and display student records in a table.

## Features

- Add Students: Input student name, height (cm), and weight (kg) to calculate BMI automatically.
- Edit Students: Modify student details and update their BMI information.
- Remove Students: Delete selected student records from the database.
- Display Student Data: View student records in a table format with BMI categories and recommendations.
- Data Persistence: Uses SQLite database to store student BMI records permanently.
- Interactive UI: Built with PyQt5 for a user-friendly graphical interface.

## Technologies Used

- Python 3
- PyQt5 (for GUI development)
- SQLite (for data storage)

## Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/lenlo121500/Python-Projects.git
   cd Python-Projects/bmi_tracker
   ```
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Application:
   ```bash
   python bmi_tracker.py
   ```

## Usage

1. Launch the application.
2. Enter a student's name, height (in cm), and weight (in kg).
3. Click "Add Student" to store the record.
4. Click on a student record to select and modify it using the "Edit Student" button.
5. Remove a student by selecting their row and clicking "Remove Student".
6. The BMI, category, and recommendation will be automatically calculated and stored.

## BMI Categories

The BMI Tracker calculates BMI using the formula:

```
BMI = weight (kg) / (height (m) * height (m))
```

| BMI Range   | Category    | Recommendation            |
| ----------- | ----------- | ------------------------- |
| < 18.5      | Underweight | Stay nourished and strong |
| 18.5 - 24.9 | Normal      | Keep up the good work     |
| 25 - 29.9   | Overweight  | Stay active and healthy   |
| > 30        | Obese       | Your health is a priority |

## File Structure

```
Python-Projects/
│── bmi_tracker/
│   │── bmi_tracker.py      # Main application script
│   │── student_bmi.db      # SQLite database (auto-created)
│   │── README.md           # Project documentation
│   │── requirements.txt    # Dependencies list
```

## Dependencies

The project requires the following Python libraries:

- PyQt5
- SQLite3 (built-in with Python)

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

## Author

Raul Castillo(lenlo121500)

## Contributing

Feel free to fork this repository and submit pull requests for improvements.
