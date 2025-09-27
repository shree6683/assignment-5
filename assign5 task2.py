#task 2: Write a Python program that:

# 1. Creates a list of numbers from 1 to 10.
original_list = list(range(1, 11))
print(f"1. Original List (1-10): {original_list}")

# 2. Extract the first 5 elements from the list.
# List slicing [start:end] extracts elements. [0:5] extracts elements at index 0 up to (but not including) index 5.
extracted_list = original_list[0:5]
print(f"2. Extracted first 5 elements: {extracted_list}")

# 3. Reverse these extracted elements.
# Slicing with a step of -1 ([::-1]) is the most idiomatic way to reverse a list in Python.
reversed_list = extracted_list[::-1]
print(f"3. Reversed extracted list: {reversed_list}")

# 4. Prints both the extracted list and the reversed list.
print("\n4. Final Output:")
print(f"   - Extracted List: {extracted_list}")
print(f"   - Reversed List:  {reversed_list}")