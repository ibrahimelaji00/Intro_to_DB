#!/usr/bin/python3
"""
Script to create a MySQL database 'alx_book_store'.
If the database already exists, it will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (change user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # ⚠️ adapte avec ton user MySQL
            password="yourpassword"  # ⚠️ adapte avec ton mot de passe
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect or create database. Details: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed")  # optionnel

if __name__ == "__main__":
    create_database()
