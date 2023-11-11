#! /usr/bin/python3

from urllib.parse import unquote
import requests
import re
import sys

erreur = 'https://raw.githubusercontent.com/MassinDV/videos/main/offlintv.m3u8'

def snif(url):
    lien = s.get(url, timeout=15).text
    retour = re.findall(r'\"hlsManifestUrl\":\"(.*?)\"\}', lien)
    tri = unquote(''.join(retour))
    flux = requests.get(tri).text
    if '.m3u8' not in tri:
        print(erreur)
    else:
        print(flux)

s = requests.Session()
result = snif(str(sys.argv[1]))
print(result)
