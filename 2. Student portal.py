students = {}
logged = None
def register():
    print("Registration")

username = input("Enter username: ")
password= input("Enter password: ")
full_name = input("Enter your full name: ")
date_of_birth = input("Enter your date of birth i DD/MM/YYYY format: ")
gender = input("Enter gender: ")
contact_number = input("Enter your personal contact number: ")
email = input("Enter your email: ")
address = input("Enter your permanent address: ")
roll_no = input("Enter Roll Number: ")
department = input("Enter your department: ")
students[username] = {
"name": username,
"password": password,
"date of birth": date_of_birth,
"gender": gender,
"contact number": contact_number,
"email": email,
"address": address,
"roll_no": roll_no,
"department": department,
}

print(f"{username} registered successfully")

def login():
    global logged
    if logged:
        print("You are already logged in.")
        return

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in students and students[username]["password"] == password:
        logged = username
        print(f"Welcome {students[username]['name']}! Login successful.\n")
    else:
        print("Invalid credentials.\n")

