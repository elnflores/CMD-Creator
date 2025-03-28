import requests
from bs4 import BeautifulSoup

VIZIER_TAG = 'https://vizier.cds.unistra.fr/viz-bin/'

def find_tag(url, name, class_):
    response = requests.get(url)
    if not response:
        print('Could not get request')
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    row = soup.find(name, class_)
    if row:
        tag = row.find('a', href=True)
        if tag:
            return tag  
    return None


def convert(id):
    id_split = id.split()
    split_string = '%20'.join(id_split)
    vizier_url = VIZIER_TAG + 'VizieR-S?' + split_string
    vizier_url = VIZIER_TAG + find_tag(vizier_url, 'tr', 'tuple-2')['href']
    simbad_url = find_tag(vizier_url, 'div', 'left simlink')['href']    
    simbad_tag = find_tag(simbad_url, 'tbody', 'datatable')
    return simbad_tag.text.strip()