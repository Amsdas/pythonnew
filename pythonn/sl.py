import csv
import hashlib

# ETL Process: Extract data from CSV, Transform data, Load into dictionary
def load_users(filename):
    users = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            username, password_hash = row
            users[username] = password_hash
    return users

# Login function
def login(users):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users:
            stored_password_hash = users[username]
            # Hash the entered password to match with stored password hash
            entered_password_hash = hashlib.sha256(password.encode()).hexdigest()
            if entered_password_hash == stored_password_hash:
                print("Login successful!")
                return username
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again.")

def main():
    # Load user data from CSV
    users = load_users('users.csv')

    # Login
    logged_in_user = login(users)
    print("Welcome,", logged_in_user)

if __name__ == "__main__":
    main()
