from datetime import datetime

print("coryou8501's Spreadsheet Automation Menu")

menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}

print("Choose a number from the following options")

for number, description in menu_options.items():
    print(number, description)

choice = input("")

if choice in menu_options:
    print("You selected", choice, "at", datetime.now())
else:
    print("Error: Invalid choice selected.")
    
