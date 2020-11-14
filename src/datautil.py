#datautil.py
import os
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    
    
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def download_data(url, n=50, sleep=1):
    cpus = [dict() for x in range(n+1)]
    soup = get_soup(url)
    table = soup.find('div', class_='chart')
    rows = table.find_all('li')
    attributes = ['Class:', 'Socket', 'Clocks', 'Turbo ', 'Cores:', 'Typica']

    i = 0
    for row in rows:
        link = row.find('a').get('href')
        link = 'https://www.cpubenchmark.net/' + link

        soup = get_soup(link)
        price = row.find('span', class_='price-neww').get_text()
        name = row.find('span', class_='prdname').get_text()
        

        cpus[i]["name"] = name
        cpus[i]["price"] = price

        table = soup.find('div', class_= 'left-desc-cpu')
        body = table.find_all('p')
        for col in body:
            text = col.get_text()
            title = col.find('strong').get_text()

            #Verifying attribute is one that we want
            if title[:6] in attributes:
                data = text.split(':')

                #Edge case for cores/threads being in the same exact <p> tag
                if title == "Cores:":

                    #Another edge case for amd cpu's
                    if (text.find("(") != -1):
                        data[1] = data[1][1]
                        data.append("Threads")
                        data.append(data[1])

                    else:
                        temp2 = data[2]
                        data[1] = data[1][1]
                        data[2] = "Threads"
                        data.append(temp2[1:])

                    cpus[i][data[2]] = data[3]

                ##Formatting strings
                if title != "Socket:":
                    data[1] = data[1].replace(" ", "")
                else:
                    data[1] = data[1][1:]

                if (title=='Clockspeed:') or (title=='Turbo Speed:'):
                    data[1] = data[1][:-3]

                #Assign to dict
                cpus[i][data[0]] = data[1]

        if i >= n-1:
            break
        i = i+1
        time.sleep(sleep)
    
    return pd.DataFrame.from_dict(cpus)

def save_df(df, filename):
    basedir = os.path.dirname(os.getcwd())
    filepath = 'data/' + filename
    full_path = os.path.join(basedir, filepath)
    df.to_csv(full_path, index=False)

def load_data(url, file):
    file = os.path.dirname(os.getcwd()) + '/data/' + file
    print(file)
    if not os.path.exists(file):
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        df = download_data(url)
        save_df(df, file)
    return pd.read_csv(file)
