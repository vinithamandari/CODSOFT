import sqlite3

# Connect to the database
db = sqlite3.connect('contacts.db')
cursor = db.cursor()

# Create a table to store contacts if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
               (name text, phone_number text, email text, address text)''')
db.commit()

# Function to add a new contact
def add_contact():
    name = input('Enter the contact name: ')
    phone_number = input('Enter the contact phone number: ')
    email = input('Enter the contact email: ')
    address = input('Enter the contact address: ')

    cursor.execute('''INSERT INTO contacts VALUES (?, ?, ?, ?)''', (name, phone_number, email, address))
    db.commit()
    print('Contact added successfully!')

# Function to view all contacts
def view_contacts():
    cursor.execute('SELECT name, phone_number FROM contacts')
    contacts = cursor.fetchall()

    if not contacts:
        print('No contacts found.')
    else:
        print('--- Contact List ---')
        for contact in contacts:
            print(f'Name: {contact[0]}, Phone number: {contact[1]}')
        print('-------------------')

# Function to search for a contact
def search_contact():
    search_term = input('Enter the contact name or phone number to search: ')

    cursor.execute('''SELECT * FROM contacts WHERE name LIKE ? OR phone_number LIKE ?''', (f'%{search_term}%', f'%{search_term}%'))
    contacts = cursor.fetchall()

    if not contacts:
        print('Contact not found.')
    else:
        print('--- Search Results ---')
        for contact in contacts:
            print(f'Name: {contact[0]}, Phone number: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}')
        print('---------------------')

# Function to update a contact
def update_contact():
    name = input('Enter the contact name to update: ')

    cursor.execute('SELECT * FROM contacts WHERE name = ?', (name,))
    contact = cursor.fetchone()

    if contact:
        print('Current details:')
        print(f'Name: {contact[0]}, Phone number: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}')

        new_name = input('Enter the new contact name (press Enter to keep unchanged): ')
        new_phone_number = input('Enter the new contact phone number (press Enter to keep unchanged): ')
        new_email = input('Enter the new contact email (press Enter to keep unchanged): ')
        new_address = input('Enter the new contact address (press Enter to keep unchanged): ')

        # Update only non-empty fields
        if new_name:
            contact[0] = new_name
        if new_phone_number:
            contact[1] = new_phone_number
        if new_email:
            contact[2] = new_email
        if new_address:
            contact[3] = new_address

        cursor.execute('''UPDATE contacts SET name = ?, phone_number = ?, email = ?, address = ? WHERE name = ?''',
                       (contact[0], contact[1], contact[2], contact[3], name))
        db.commit()
        print('Contact updated successfully!')
    else:
        print('Contact not found.')

# Function to delete a contact
def delete_contact():
    name = input('Enter the contact name to delete: ')

    cursor.execute('SELECT * FROM contacts WHERE name = ?', (name,))
    contact = cursor.fetchone()

    if contact:
        cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
        db.commit()
        print('Contact deleted successfully!')
    else:
        print('Contact not found.')

# User interface
while True:
    print('--- Contact Book Menu ---')
    print('1. Add a contact')
    print('2. View contact list')
    print('3. Search for a contact')
    print('4. Update a contact')
    print('5. Delete a contact')
    print('6. Quit')

    choice = input('Enter your choice (1-6): ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print('Exiting Contact Book. Goodbye!')
        break
    else:
        print('Invalid choice. Please select again.')

# Close the database connection
db.close()