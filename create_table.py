import sqlite3

# Connect to the database
conn = sqlite3.connect('restaurant.db')









import sqlite3

# Connect to the database
conn = sqlite3.connect('restaurant.db')
print("Connected to database successfully")

# Create Authentication table
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
print("Authentication table created successfully!")

# Create Orders table
conn.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    order_details TEXT NOT NULL,
    total_price REAL NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
print("Orders table created successfully!")










cursor = conn.cursor()


cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")


# Commit the transaction
conn.commit()
print("Admin user added successfully!")

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Should include the admin user

conn.close()