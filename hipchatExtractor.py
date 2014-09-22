from hypchat import HypChat
import os, os.path
import datetime
import ConfigParser
from types import NoneType
from math import log

outFile = open('hipchat.out','w')

# The list of names we will turn into nodes.
# Everyone else will be a client
allowedNames = [
  'kevin',
  'jonathan',
  'cedric',
  'gary',
  'andrea',
  'allie',
  'nemanja',
  'roberto',
  'bob',
  'jeronimo',
  'sebastian'
]

config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/.hypchat'), '/etc/hypchat'])
AUTH_TOKEN = config.get('HipChat', 'token')
roomId = config.get('HipChat', 'roomId')


def writeLine(time, name, messageLength, timeDiff, timeSinceStart):
  outFile.write(str(time))
  outFile.write(',')
  outFile.write(name)
  outFile.write(',')
  outFile.write(str(messageLength))
  outFile.write(',')
  outFile.write(str(timeDiff))
  outFile.write(',')
  outFile.write(str(timeSinceStart))
  outFile.write('\n')

if __name__ == '__main__':
  hc = HypChat(AUTH_TOKEN)

  startIndex = 0
  indexInterval = 150
  previousDate = 0
  totalTime = 0
  now = datetime.datetime.utcnow()

  totalContents = []

  # Get 8 * 150 results from the given room.
  for i in range(8):
    response = hc.get_room(roomId).history(now, maxResults=150, startIndex=startIndex)
    contents = list(response.contents())
    totalContents[:0] = contents
    startIndex += indexInterval
  for l in totalContents:
    date = l['date']
    name = l['from']

    # Plugins, such as Inc or Linky, do not produce actual names
    # So we remove them from the data
    if type(name) == unicode or type(name) == NoneType:
      continue
    
    name = name['name']
    name = name.split()[0].lower()
    if name not in allowedNames:
      name = "client"
    messageLength = len(l['message'])
    timeDiff = 0
    if previousDate != 0:
      # We get a logarithmic difference to avodi long dead periods
      timeDiff = int(log(int((date - previousDate).total_seconds()*1000)))
      totalTime = totalTime + timeDiff
    previousDate = date
    writeLine(date, name, messageLength, timeDiff, totalTime)

