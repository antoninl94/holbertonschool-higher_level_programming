#!/usr/bin/python3
"""
This is the ``task_02_requests`` module
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function fetches all post from JSONplaceholder
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        data = response.json()
        for post in data:
            if 'title' in post:
                print(post['title'])


def fetch_and_save_posts():
    """
    This function fetches all post from JSONplaceholder
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        data = response.json()
        posts = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in data if 'title' in post]
        with open('posts.csv', 'w') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerows(posts)
