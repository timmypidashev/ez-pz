# A simple, lightweight, multi-function utility library.
[![CodeFactor](https://www.codefactor.io/repository/github/timmypidashev/ez_pz/badge)](https://www.codefactor.io/repository/github/timmypidashev/ez_pz)
[![Discord](https://discord.com/api/guilds/791160100567384094/embed.png)](https://discord.gg/EDRjZdkGBG)
[![Python](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py)
[![wakatime](https://wakatime.com/badge/user/b920b284-3cde-4cd4-b72e-f7f22d050b16/project/794a858c-e826-496e-8982-5da77e0dbb09.svg)](https://wakatime.com/badge/user/b920b284-3cde-4cd4-b72e-f7f22d050b16/project/794a858c-e826-496e-8982-5da77e0dbb09)

# Features
* Fast sqlite database handler with `async` support
* Simple logging module [work in progress]
* Very simple and easy to use!

# Installation
ez-pz is hosted on **[PyPI](https://pypi.org/project/ez-pz/)**, so the installation process is as simple as:
```bash
pip install ez-pz
```

# Database
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
