
import sqlite3

def create_db():
    conn = sqlite3.connect('organization_chat.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        work_id TEXT NOT NULL UNIQUE,
        role TEXT NOT NULL,
        branch TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        manager_id INTEGER,
        FOREIGN KEY(manager_id) REFERENCES users(id)
    )
    ''')
    
    # Insert sample data for a branch (for example, 'Branch A')
    c.execute("INSERT INTO users (name, work_id, role, branch, email, phone, manager_id) VALUES ('Alice', 'A001', 'Manager', 'Branch A', 'alice@org.com', '1234567890', NULL)")
    c.execute("INSERT INTO users (name, work_id, role, branch, email, phone, manager_id) VALUES ('Bob', 'A002', 'Assistant', 'Branch A', 'bob@org.com', '1234567891', 1)")
    c.execute("INSERT INTO users (name, work_id, role, branch, email, phone, manager_id) VALUES ('Charlie', 'A003', 'HRM', 'Branch A', 'charlie@org.com', '1234567892', 1)")
    c.execute("INSERT INTO users (name, work_id, role, branch, email, phone, manager_id) VALUES ('David', 'A004', 'Accountant', 'Branch A', 'david@org.com', '1234567893', 1)")
    # Add more sample employees...

    # Commit and close
    conn.commit()
    conn.close()

# Uncomment to create and populate the database
# create_db()
  
import sys

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('organization_chat.db')
    return conn

# User login function
def user_login():
    print("Welcome to the organization chat system!")
    work_id = input("Please enter your work ID: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE work_id=?", (work_id,))
    user = cursor.fetchone()
    
    if user:
        print(f"Welcome {user[1]}! You are logged in as {user[3]} in {user[4]}")
        return user
    else:
        print("Invalid Work ID. Please try again.")
        conn.close()
        sys.exit()
        
# Function to display options after login
def show_options(user):
    print("\nChoose an option:")
    print("1. Communicate within your branch")
    print("2. Communicate with other branches")
    print("3. Create a group")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        send_message_within_branch(user)
    elif choice == '2':
        send_message_to_other_branches(user)
    elif choice == '3':
        create_group(user)
    elif choice == '4':
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid choice! Try again.")
        show_options(user)

# Function to send message within the branch
def send_message_within_branch(user):
    print("\nSending message within your branch.")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM users WHERE branch=?", (user[4],))
    members = cursor.fetchall()
    print("Members in your branch:")
    for i, member in enumerate(members, 1):
        print(f"{i}. {member[0]}")
    
    recipient_choice = int(input("Choose a member by number to send a message: "))
    recipient = members[recipient_choice - 1][0]
    message = input(f"Enter your message to {recipient}: ")
    
    print(f"Message sent to {recipient}!")
    show_options(user)

# Function to send message to a different branch
def send_message_to_other_branches(user):
    print("\nSending message to another branch.")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT DISTINCT branch FROM users WHERE branch != ?", (user[4],))
    branches = cursor.fetchall()
    print("Branches available:")
    for i, branch in enumerate(branches, 1):
        print(f"{i}. {branch[0]}")
    
    branch_choice = int(input("Choose a branch by number: "))
    selected_branch = branches[branch_choice - 1][0]
    
    cursor.execute("SELECT name FROM users WHERE branch=?", (selected_branch,))
    members = cursor.fetchall()
    print(f"\nMembers in {selected_branch}:")
    for i, member in enumerate(members, 1):
        print(f"{i}. {member[0]}")
    
    recipient_choice = int(input("Choose a member by number to send a message: "))
    recipient = members[recipient_choice - 1][0]
    message = input(f"messaging {recipient}: ")
    
    print(f"Message sent to {recipient} in {selected_branch}!")
    show_options(user)

# Function to create a group
def create_group(user):
    print("\nCreate a new group.")
    group_name = input("Enter the group name: ")
    group_members = input("Enter members by work ID (comma separated): ").split(',')
    
    print(f"Group '{group_name}' created with members: {', '.join(group_members)}")
    show_options(user)

# Main program flow
def main():
    user = user_login()
    show_options(user)

if __name__ == "__main__":
    main()









