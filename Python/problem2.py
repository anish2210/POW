# Create a program to demonstrate the use of try-catch-finally block with multiple exceptions

try:
    # Attempt to open a file and read its contents
    with open('non_existent_file.txt', 'r') as file:
        data = file.read()
    # Attempt to convert data to an integer
    number = int(data)
except FileNotFoundError:
    print("Error: The file was not found.")
except ValueError:
    print("Error: Could not convert data to an integer.")
finally:
    print("Execution of the try-catch block is complete.")