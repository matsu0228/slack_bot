from slackbot.bot import Bot
# import configparser
import os, sys
app_lib =  os.path.abspath(__file__) + "/myvenv/"
sys.path.append( app_lib )

import logging from getLogger
logger = getLogger(__name__)
logger.debug('main:',  sys.path)

def main():
  bot = Bot()
  bot.run()

if __name__ == "__main__":
  logger.debug('main:',  sys.path)
  main()
  # ini = configparser.ConfigParser( app_lib + 'config.ini')