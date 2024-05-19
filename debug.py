#!/usr/bin/env python3
import os
import sys

# Set environment variables
os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
os.environ['HBNB_TYPE_STORAGE'] = 'db'

# Print debug information
print(f"Python executable: {sys.executable}")
print(f"Environment variables set: {os.environ['HBNB_MYSQL_USER']}, {os.environ['HBNB_MYSQL_PWD']}, {os.environ['HBNB_MYSQL_HOST']}, {os.environ['HBNB_MYSQL_DB']}, {os.environ['HBNB_TYPE_STORAGE']}")

# Try importing storage and State
try:
        from models import storage
        from models.state import State
        print("Successfully imported storage and State from models.")
except ModuleNotFoundError as e:
        print(f"ModuleNotFoundError: {e}")

