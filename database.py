import sqlite3

# Connect to the SQLite database (make sure the path is correct)
conn = sqlite3.connect('C:/Users/setti/Downloads/HiFieats/instance/HiFieats.db')
cursor = conn.cursor()

# List of customer data to be inserted
customers = [
    ('amit_shukla', 'amit.shukla@google.com', 'password123', 'customer', 'Bellandur, Bangalore', '9876543210'),
    ('neha_kapoor', 'neha.kapoor@mail.com', 'secure234', 'customer', 'HSR Layout, Bangalore', '8765432109'),
    ('rohan_malhotra', 'rohan.malhotra@google.com', 'password345', 'customer', 'Sarjapur, Bangalore', '7654321098'),
    ('tanya_mehta', 'tanya.mehta@mail.com', 'secure456', 'customer', 'Jayanagar, Bangalore', '6543210987'),
    ('saurabh_pandey', 'saurabh.pandey@google.com', 'password567', 'customer', 'Electronic City, Bangalore', '5432109876'),
    ('simran_kaur', 'simran.kaur@mail.com', 'secure678', 'customer', 'Whitefield, Bangalore', '4321098765'),
    ('harshit_bajaj', 'harshit.bajaj@google.com', 'password789', 'customer', 'Indiranagar, Bangalore', '3210987654'),
    ('isha_arora', 'isha.arora@mail.com', 'secure890', 'customer', 'BTM Layout, Bangalore', '2109876543'),
    ('aditya_nayar', 'aditya.nayar@google.com', 'password901', 'customer', 'Koramangala, Bangalore', '1098765432'),
    ('pragya_sharma', 'pragya.sharma@mail.com', 'secure012', 'customer', 'Banashankari, Bangalore', '9988776655')
]


# Loop through the list and insert each customer into the users table
for customer in customers:
    cursor.execute('''
        INSERT INTO users (username, email, password, role, location, contact)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', customer)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Customers added successfully!")
