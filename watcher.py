#!/usr/bin/python

import os
import json
import time
import datetime
from transmission_rpc import Client


def log(text):
    timestamp = '[{:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now())
    print(f'{timestamp} {text}')

def add(watch_dir, download_dir, item):
    files = os.listdir(watch_dir)
    for file in files:
        if file.lower().endswith('.torrent') and not file.startswith('.'):
            log(f'Adding {item} torrent: {file}')
            try:
                f = open(watch_dir + '/' + file, 'rb')
                new = c.add_torrent(f, download_dir=download_dir)
                new.start()
                f.close()
                os.remove(watch_dir + '/' + file)
            except Exception as e:
                log(f'Error encountered: {e}')

def main():
    global c

    # Open our config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Set up connection to transmission
    c = Client(
            host=config["Settings"]["Host"],
            port=config["Settings"]["Port"],
            username=config["Settings"]["User"],
            password=config["Settings"]["Pass"])

    # Some pretty logging
    log('Started watcher.')
    log('Configured watch directories:')
    for i in config["Downloads"]:
        log(f'- {i}: {config["Downloads"][i]["Directory"]} → {config["Downloads"][i]["Download"]}')

    while True:
        for i in config["Downloads"]:
            add(config["Downloads"][i]["Directory"], config["Downloads"][i]["Download"], i)
        time.sleep(config["Settings"]["Sleeptime"])

if __name__ == '__main__':
    main()
