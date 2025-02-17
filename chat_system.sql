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


