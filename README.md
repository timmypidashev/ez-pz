# ez-db

[![CodeFactor](https://www.codefactor.io/repository/github/timothypidashev/ez-db/badge)](https://www.codefactor.io/repository/github/timothypidashev/ez-db)
[![Discord](https://discord.com/api/guilds/791160100567384094/embed.png)](https://discord.gg/EDRjZdkGBG)
[![Python](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py)
[![wakatime](https://wakatime.com/badge/github/timothypidashev/ez-db.svg)](https://wakatime.com/badge/github/timothypidashev/ez-db)

A simple to use database handler using sqlite3

# Features
* Building from .sql files
* General query commands
* Very simple and easy to use!

# Installation
ez-db is hosted on **[PyPI](https://pypi.org/project/ez-db/)**, so the installation process is as simple as:
```bash
pip install ez-db
```

# Usage
As simple as can get:
```python
import ez_db as db 

db = db.DB(db_path="./database/database.db")

db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
db.commit()
```
A little more complex with .sql files:
```python
import ez_db as db 

db = db.DB(db_path="./database/database.db", build_path="./database/build.sql")

db.build()
```
# Thats It!
Join the Discord server for more info and help on this package and many other projects:
[![Conside joining my Discord server!](https://invidget.switchblade.xyz/EDRjZdkGBG)](https://discord.gg/EDRjZdkGBG)
