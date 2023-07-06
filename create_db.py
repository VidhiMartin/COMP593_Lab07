"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime
from faker import Faker

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    open_connection = sqlite3.connect(db_path)
    cursor_ = open_connection.cursor()
    create_people_table_query = """
        CREATE TABLE IF NOT EXISTS people (
        
            ID          INTEGER PRIMARY KEY,
            Name        TEXT NOT NULL,
            Email       TEXT NOT NULL,
            Address     TEXT NOT NULL,
            City        TEXT NOT NULL,
            Province    TEXT NOT NULL,
            Bio         TEXT,
            Age         INTEGER,
            created_at  DATETIME NOT NULL,
            updated_at  DATETIME NOT NULL
        );
"""
    cursor_.execute(create_people_table_query)
    open_connection.commit()
    open_connection.close()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    fake = Faker()
    open_connection = sqlite3.connect(db_path)
    cursor_ = open_connection.cursor()
    insert_person_query = """
        INSERT INTO people
        (
            Name,
            Email,
            Address,
            City,
            Province,
            Bio,
            Age,
            created_at,
            updated_at
        )
        Values (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
    for _ in range(200):
        Name = fake.name()
        Email = fake.email()
        Address = fake.address().replace('\n', ', ')
        City = fake.city()
        Province = fake.state()
        Bio = fake.text()
        Age = fake.random_int(1, 100)
        created_at = datetime.now()
        updated_at = datetime.now()

        cursor_.execute(insert_person_query, (Name, Email, Address, City, Province, Bio, Age, created_at, updated_at ))

    open_connection.commit()
    open_connection.close()

    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    return

if __name__ == '__main__':
   main()