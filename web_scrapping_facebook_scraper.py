from facebook_scraper import get_posts
import csv
import os

os.chdir(r'C:\Users\gaura\OneDrive\Documents\Padhai\Gaurav\Python\Codes')

with open('facebook_posts.csv', 'w') as file:
        w = csv.writer(file)
        for post in get_posts('suncorpAUNZ', pages=2):
            w.writerow(post['text'])