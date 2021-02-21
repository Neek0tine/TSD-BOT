# TSDBot; Discord.py [rewrite] 1.6.0
import os
from configparser import ConfigParser
from threading import Thread

import psutil
from discord.ext import commands
from flask import Flask

app = Flask('')


@app.route('/')
def main():
    stats = f"TSDBot; Discord.py [rewrite] 1.6.0 -- Status : Up -- Ram Usage: {psutil.virtual_memory().percent} % -- Available Memory: {round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} %"
    return stats


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()


keep_alive()

config = ConfigParser()
config.read('config.ini')
data = config['BOT_CFG']
BOT_TOKEN = data['TOKEN']
BOT_INVITE = data['INVITE']


def get_prefix(bot, message):
    prefixes = ['tsd ']
    if not message.guild:
        return 'tsd '
    return commands.when_mentioned_or(*prefixes)(bot, message)


client = commands.Bot(command_prefix=get_prefix)

if __name__ == '__main__':
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            client.load_extension(f'cogs.{file[:-3]}')
            print(f'Cog loaded : {file}')

client.run(BOT_TOKEN, bot=True, reconnect=True)
