from .app import *
import json
from random import shuffle

#helper functions
def parseRegularRoundtoDict(roundItem, num):
   if '_id' in roundItem:
      roundItem.pop('_id', None)
   roundItem.update({'questionNumber' : num})
   return roundItem
   

def gropClassifier(gNum):
   group = {1 : "subjr", 2 : "jr", 3: "sr", 4 : "adult"}
   return group[gNum]

#State and Question Saver


#Routes
@app.route('/api/')
def method_name():
   return "ello"

@app.route('/api/levels')
def getLevels():
   levels = db.collection_names()
   return json.dumps(levels)

@app.route("/api/regularRound/<int:groupNumber>")
def regularRound(groupNumber):
   collections = list(db.regularRound.find({"group" : groupNumber}))
   shuffle(collections)
   data = []
   qCount = 1
   for doc in collections:
      data.append(parseRegularRoundtoDict(doc, qCount))
      qCount += 1
   return json.dumps(data)
   
@app.route("/api/pictureRound/<int:groupNumber>")
def pictureRound(groupNumber):
   collections = list(db.pictureRound.find({"group": groupNumber}))
   shuffle(collections)
   data = []
   qCount = 1
   for doc in collections:
      data.append(parseRegularRoundtoDict(doc, qCount))
      qCount += 1
   print(data)
   return json.dumps(data)
