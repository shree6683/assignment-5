

📘 Assignment 5: Python Basics – Dictionary & List Operations
📝 Overview
This assignment includes two beginner-friendly Python tasks that demonstrate the use of dictionaries, lists, slicing, and error handling. These tasks are designed to strengthen your understanding of core Python concepts through practical examples.

🧩 Task 1: Student Marks Lookup System
🎯 Objective
Create a Python program that allows users to look up student marks from a predefined dictionary.
🛠 Features
- Initializes a dictionary with student names and their marks
- Accepts user input to search for a student
- Displays the student's marks if found
- Handles missing entries using a try-except block
📌 How It Works
- A dictionary named student_marks is created with five student records.
- The user is prompted to enter a student's name.
- The program searches the dictionary for the name.
- If found, it displays the marks.
- If not found, it shows an error message suggesting the user check the spelling.
💡 Sample Output
Student records initialized.
------------------------------
Enter the student's name to look up their marks: Mia

✅ SUCCESS: The marks for Mia are: 92


Enter the student's name to look up their marks: John

❌ ERROR: The student name 'John' was not found in the records.
Please check the spelling and try again.



🧩 Task 2: List Slicing and Reversal
🎯 Objective
Create a Python program that demonstrates list slicing and reversal using built-in Python techniques.
🛠 Features
- Creates a list of numbers from 1 to 10
- Extracts the first 5 elements using slicing
- Reverses the extracted list using Pythonic slicing
- Displays both the extracted and reversed lists
📌 How It Works
- A list named original_list is created using range(1, 11).
- The first five elements are extracted using slicing: original_list[0:5].
- The extracted list is reversed using [::-1].
- Both lists are printed for clarity.
💡 Sample Output
1. Original List (1-10): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2. Extracted first 5 elements: [1, 2, 3, 4, 5]
3. Reversed extracted list: [5, 4, 3, 2, 1]

4. Final Output:
   - Extracted List: [1, 2, 3, 4, 5]
   - Reversed List:  [5, 4, 3, 2, 1]



🚀 How to Run
Make sure Python is installed on your system. Then run each task using the terminal or command prompt:
python task1_student_marks.py
python task2_list_slicing.py



📂 File Structure
assignment5/
│
├── task1_student_marks.py     # Task 1: Student marks lookup
├── task2_list_slicing.py      # Task 2: List slicing and reversal
└── README.md                  # Project documentation



📚 Concepts Covered
- Python dictionaries and key-value access
- Exception handling with try-except
- List creation and slicing
- Reversing lists using slicing
- User input and string manipulation

🧠 Future Enhancements
- Add case-insensitive search for student names
- Allow multiple lookups in a loop
- Extend list operations to include sorting or filtering
- Convert both tasks into GUI or web-based applications


