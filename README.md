# transmission-watcher
This thing will enable multiple watch folders for transmission, configurable with json.

## config.json
```
{
  "Downloads": {
    "Ubuntu": {
      "Directory": "/watchdir/ubuntu",
      "Download": "/downloads/ubuntu"
    },
    "Debian": {
      "Directory": "/watchdir/debian",
      "Download": "/downloads/debian"
    }
  },
  "Settings": {
      "Host": "192.168.0.123",
      "Port": "9091",
      "User": "username",
      "Pass": "password",
      "Sleeptime": 10
  }
}
```

The downloads section contains one dictionary per item, with both watch dir and download dir configured.
The settings section contains information on where to find the transmission server, as well as credentials and how often to scan your watch directories. Default is every 10 seconds.

## Run standalone
1. `pip install transmission_rpc`
2. Edit your config.json.
3. `python3 watcher.py`

## Run with docker-compose
1. `docker build -t transmission-watcher .`
2. Run the container with `docker-compose up`.


