# ez-pz 

[![CodeFactor](https://www.codefactor.io/repository/github/timmypidashev/ez_pz/badge)](https://www.codefactor.io/repository/github/timmypidashev/ez_pz)
[![Discord](https://discord.com/api/guilds/791160100567384094/embed.png)](https://discord.gg/EDRjZdkGBG)
[![Python](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py)
[![wakatime](https://wakatime.com/badge/github/timothypidashev/ez-db.svg)](https://wakatime.com/badge/github/timothypidashev/ez-db)

A simple to use database handler using sqlite3

# Features
* Building from .sql files
* General query commands
* Very simple and easy to use!
* Sync and Async support!

# Installation
ez-pz is hosted on **[PyPI](https://pypi.org/project/ez-pz/)**, so the installation process is as simple as:
```bash
pip install ez-pz
```
Also don't forget to install **[asqlite](https://github.com/timothypidashev/asqlite)**. It is not currently hosted on PyPI
so run this command to install:
```bash
pip install git+https://github.com/Rapptz/asqlite
```

# Sync Usage
As simple as can get:
```python
import ez_pz as db 

db = db.DB(db_path="./database/database.db")

db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
db.commit()
```
A little more complex with .sql files:
```python
import ez_pz as db 

db = db.DB(db_path="./database/database.db", build_path="./database/build.sql")

db.build()
```

# Async Usage
```python
import ez_pz as db
import asyncio

db = db.AsyncDB(db_path="./database/database.db", build_path="./database/build.sql")

async def run():
    await db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    await db.commit()
    
    """
    Queries requiring tuples[] or multiple variables, should be encapsulated by another set of `()`
    """
    level, exp = (await db.record(f"SELECT level, exp FROM users WHERE UserID = {user.id}")[0])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
```

# Planning and Future
This package is now shifitng gears from a database manager to an all purpose collection of modules that work and work well. 
Here are the current plans:
* A log module that gets rid of all the debug/clutter that the standard log module has.
* Currently that's the only idea I have in my head. Feel free to suggest any.

# Thats It!
Join the Discord server for more info and help on this package and many other projects:

[![Consider joining my Discord server!](https://invidget.switchblade.xyz/EDRjZdkGBG)](https://discord.gg/EDRjZdkGBG)
