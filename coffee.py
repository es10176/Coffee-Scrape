import requests
from bs4 import BeautifulSoup
from plyer import notification
import json
import csv
import pickle
import pandas as pd
import time
temp_data = []

def clean(ds):
    ds.dropna(inplace=True)
    ds.drop_duplicates(inplace=True)
    return ds


def extract_text(x):
    ed = requests.get(x)
    ed_soup = BeautifulSoup(ed.content, 'html.parser')
    extracted_text = []
    for line in ed_soup.find_all('p'):
        text = line.text.strip()
        if text:
            extracted_text.append(text)

    return extracted_text


def extract_links(y):
    ed = requests.get(y)
    ed_soup = BeautifulSoup(ed.content, 'html.parser')
    extracted_links = []
    for link in ed_soup.find_all('a'):
        href = link.get('href')
        if href:
            extracted_links.append(href)

    return extracted_links

def extract_all(z):
    output = requests.get(z)
    ed_soup = BeautifulSoup(output.content, 'html.parser')
    extracted_links = []
    for link in ed_soup.find_all('a'):
        href = link.get('href')
        if href:
            extracted_links.append(href)
            temp_data.append(extracted_links)
    
    ed = requests.get(z)
    ed_soup = BeautifulSoup(ed.content, 'html.parser')
    extracted_text = []
    for line in ed_soup.find_all('p'):
        text = line.text.strip()
        if text:
            extracted_text.append(text)
            temp_data.append(extracted_text)

    return temp_data



def export_csv(z):
    with open('coffee_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(z)


def export_json(x):
    file_name = "coffee_data"
            
    with open(f"{file_name}.json", 'w') as json_file:
        json.dump(x, json_file)
    
