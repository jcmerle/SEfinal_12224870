#!/usr/bin/env python3

import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")

def deleteBook(bookId, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{bookId}", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            }
    )
    if r.status_code == 200:
        print(f"Book {bookId} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delete book {bookId}.")

# Get the Auth Token Key
apiKey = getAuthToken()

# Using the faker module, generate random "fake" books
fake = Faker()
for i in range(0, 4):
    deleteBook(i, apiKey)
for i in range(126, 130):
    deleteBook(i, apiKey)