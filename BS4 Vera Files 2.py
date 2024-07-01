# ITS FUCKING WORKING LETSGOOO **no database yet though
#kms ddos T^T
#data: title, autor, date, article
# LETSGOO NASA DATABASE NA, paano iaccess database...

import os
import requests
from bs4 import BeautifulSoup
import time
import logging
import sqlite3  
import shutil  # Import shutil for file operations

logging.basicConfig(level=logging.INFO)  # Set logging level

# Function to check if database file exists
def check_database_existence(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False
    
# Define the source path of the SQLite database file
source_path = 'mydatabase.db'

# Check if the database file exists
if not check_database_existence(source_path):
    logging.error(f"Database file '{source_path}' not found.")
    exit(1)  # Exit the script if the database file is not found

conn = sqlite3.connect('mydatabase.db')

# Function to create table in SQLite database
def create_table():
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT,
                           author TEXT,
                           date TEXT,
                           article TEXT)''')
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error creating SQLite table: {e}")

# Function to insert data into SQLite database
def insert_data_into_db(title, author, date, article):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, author, date, article) VALUES (?, ?, ?, ?)",
                       (title, author, date, article))
        conn.commit()
        logging.info(f"Inserted data into database: {title}")
    except sqlite3.Error as e:
        logging.error(f"Error inserting data into SQLite table: {e}")

# Function to fetch specific links from a given URL
def get_specific_links(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize an empty set to store unique specific links
        specific_links = set()

        # Find all 'a' tags (links) in the parsed HTML
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # Check if the link contains '/articles/' and is not already in the set
                if '/articles/' in href and href not in specific_links:
                    specific_links.add(href)

        return specific_links

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching page: {e}")
        return set()  # Return an empty set on error

# Function to get data from specific links
def get_data_from_specific_links(links):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        for link in links:
            try:
                # Send a GET request to the specific link with headers
                response = requests.get(link, headers=headers, timeout=10)
                response.raise_for_status()  # Raise an exception for bad responses

                # Parse HTML content of the specific link
                soup = BeautifulSoup(response.content, 'html.parser')

                # Example: Extract data from <p> tags or specific elements
                title = soup.find('h1', class_='article_title heading-size-1')
                if title:
                    title_text = title.text.strip()

                author = soup.find('span', id='article_author')
                if author:
                    author_text = author.text.strip()

                date = soup.find('span', id='article_date')
                if date:
                    date_text = date.text.strip()

                article_text = ""
                for paragraph in soup.find_all('p'):
                    article_text += paragraph.text.strip() + "\n"

                # Insert data into SQLite database
                insert_data_into_db(title_text, author_text, date_text, article_text)

                # Implementing rate limiting to avoid being blocked
                time.sleep(1)  # Sleep for 1 second between requests

            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching data from {link}: {e}")

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create the 'articles' table in SQLite database
        create_table()

        # URL to scrape for specific links
        url_to_scrape = 'https://verafiles.org/section/fact-check-filipino'
        specific_links = get_specific_links(url_to_scrape)

        # Print all specific links found
        logging.info("Specific links found:")
        for link in specific_links:
            logging.info(link)
        
        # Fetch data from specific links and insert into database
        get_data_from_specific_links(specific_links)

    finally:
        # Close connection to SQLite database
        conn.close()
        
        # Download the database file
        source_path = 'mydatabase.db'
        destination_path = '/path/to/download/folder/mydatabase.db'
        
        try:
            shutil.copy(source_path, destination_path)
            print(f"Database downloaded successfully to: {destination_path}")
        except FileNotFoundError:
            print("Source database file not found.")
        except PermissionError:
            print("Permission denied to copy database file.")
        except Exception as e:
            print(f"Error downloading database: {e}")
