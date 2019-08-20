#!/usr/bin/python3

import pprint
import requests

def main():
    r = requests.get('https://www.anapioficeandfire.com/api')
    pprint.pprint(r.json())

main()
