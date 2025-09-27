# ASSIGNMENT 5

# 1. Creates a dictionary where Student names are keys and their marks are values.
student_marks = {
    "Rahul": 90,
    "Shiva": 85,
    "Eva": 78,
    "Mia": 92,
    "Khusi": 81
}

print("Student records initialized.")
print("-" * 30)

# 2. Ask the user to input a student's name
# The strip() method removes any leading/trailing whitespace
name_to_find = input("Enter the student's name to look up their marks: ").strip()

# 3. Retrieves and displays the corresponding marks
# 4. If the student name is not found, display an appropriate message.
# A try-except block is the standard Python way to handle this expected error (KeyError).
try:
    # Attempt to retrieve the mark using the student name as the key
    marks = student_marks[name_to_find]
    
    # Point 3: Display the corresponding marks
    print(f"\n✅ SUCCESS: The marks for {name_to_find} are: {marks}")

except KeyError:
    # Point 4: If the student name is not found, display an appropriate message.
    print(f"\n❌ ERROR: The student name '{name_to_find}' was not found in the records.")
    print("Please check the spelling and try again.")