import mysql.connector
from mysql.connector import Error

# This function is  to connect to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root@localhost',   # I have change this to my MySQL username
            password='Basildon@099',  #  I have change this to MySQL password
            database='movie_fan_club'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# this function i will use to fetch all members from the database
def fetch_all_members():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM members")
    result = cursor.fetchall()
    connection.close()
    return result

# this function is t to add a member to the database
def add_member(name, favorite_movie):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO members (name, favorite_movie) VALUES (%s, %s)", (name, favorite_movie))
    connection.commit()
    connection.close()

# function i will use to to remove a member by ID
def remove_member(member_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM members WHERE id = %s", (member_id,))
    connection.commit()
    connection.close()
