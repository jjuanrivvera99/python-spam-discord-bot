# Python spam bot for Discord

## Setup
Copy the .env.example into .env and fill the vars:

```javascript
EMAIL=YOUR_DISCORD_EMAIL
PASSWORD=YOUR_DISCORD_PASSWORD
SERVER=DISCORD_SERVER_ID
CHANNEL=DISCORD_CHANNEL_ID
FREQUENCY=60
```

Install dependencies (not needed with docker)
```bash
./setup.sh
```

## Execute
Run the program
```bash
python app.py
```

Running over docker
```bash
docker-compose up -d
```

## Limitations
Discord server must be visible at first view and channel must also be visible when server is opened