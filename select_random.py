#!/usr/bin/python
#
# Select random People and allocate them to Lunches

__author__ = 'mario@betaworks.com (Mario Menti)'

import getopt
import sys
import string
import MySQLdb
import datetime
import random

db = MySQLdb.connect("localhost","lunchy","lunchroulette","lunch_roulette" )
cursor = db.cursor()

today = datetime.date.today()
cursor.execute("select * from People where avail_1 = 1 and last_updated >= '%s'" % (today))
all_slot1 = list(cursor.fetchall())
cursor.execute("select * from People where avail_2 = 1 and last_updated >= '%s'" % (today))
all_slot2 = list(cursor.fetchall())
cursor.execute("select * from People where avail_3 = 1 and last_updated >= '%s'" % (today))
all_slot3 = list(cursor.fetchall())
cursor.execute("select * from People where avail_4 = 1 and last_updated >= '%s'" % (today))
all_slot4 = list(cursor.fetchall())

use_slot1 = all_slot1
use_slot2 = all_slot2
use_slot3 = all_slot3
use_slot4 = all_slot4

# determine the lunch_id to start from 
cursor.execute("select max(lunch_id) from Lunches")
row = cursor.fetchone()
lunch_id = row[0]
if lunch_id is None: lunch_id = 0
lunch_id += 1

def create_lunches(slot_id, slot1, slot2, slot3, slot4): 
  global lunch_id

  # need at least 3 people in a timeslot
  # TODO: be more clever and create groups of 3 or 4 (not a fixed 3), depending on the numbers in slot
  mymod = 0
  if len(slot1) >= 3:
    mymod = len(slot1) % 3
  # remove some people so we have groups of 3
  # TODO: this should be clever and not remove people if this is the only timeslot they can do
  for x in range(0,mymod):
    slot1.pop()
  cnt = 0
  while slot1: 
    if cnt == 3:
      cnt = 0
      lunch_id += 1
    # pick random row and remove from all lists
    row = random.choice(slot1)
    slot1.remove(row)
    # also remove from all the other lists, so we don't select the same one again
    if slot2.count(row) > 0: slot2.remove(row)
    if slot3.count(row) > 0: slot3.remove(row)
    if slot4.count(row) > 0: slot4.remove(row)
    print "slot %s, lunch id %s: %s" % (slot_id, lunch_id, row[1])
    cnt += 1
    
create_lunches(1, use_slot1, use_slot2, use_slot3, use_slot4)
create_lunches(2, use_slot2, use_slot1, use_slot3, use_slot4)
create_lunches(3, use_slot3, use_slot1, use_slot2, use_slot4)
create_lunches(4, use_slot4, use_slot1, use_slot2, use_slot3)

db.close()

