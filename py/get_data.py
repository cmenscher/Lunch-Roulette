#!/usr/bin/python
#
# Get data from daily Google lunch roulette spreadsheet and update corresponding MySQL People table

__author__ = 'mario@betaworks.com (Mario Menti)'


try: 
  from xml.etree import ElementTree
except ImportError:  
  from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
import getopt
import sys
import string
import MySQLdb
import datetime

class SimpleCRUD:

  def __init__(self, email, password):
    self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
    self.gd_client.email = email
    self.gd_client.password = password
    self.gd_client.source = 'betaworks lunch roulette'
    self.gd_client.ProgrammaticLogin()
    self.curr_key = ''
    self.curr_wksht_id = ''
    self.list_feed = None

  def _PrintFeed(self, feed):
    for i, entry in enumerate(feed.entry):
      if isinstance(feed, gdata.spreadsheet.SpreadsheetsCellsFeed):
        print '%s %s\n' % (entry.title.text, entry.content.text)
      elif isinstance(feed, gdata.spreadsheet.SpreadsheetsListFeed):
        print '%s %s %s' % (i, entry.title.text, entry.content.text)
        # Print this row's value for each column (the custom dictionary is
        # built from the gsx: elements in the entry.) See the description of
        # gsx elements in the protocol guide.
        print 'Contents:'
        for key in entry.custom:
          print '  %s: %s' % (key, entry.custom[key].text)
        print '\n',
      else:
        print '%s %s\n' % (i, entry.title.text)

  def _ProcessData(self, feed):
    db = MySQLdb.connect("localhost","lunchy","lunchroulette","lunch_roulette" )
    cursor = db.cursor()
    for i, entry in enumerate(feed.entry):
      rowdata =  map(lambda e: (e[1].text), entry.custom.items())
      l_updated = datetime.datetime.strptime(rowdata[0],"%d/%m/%Y %H:%M:%S")
      use_av_1 = 0
      use_av_2 = 0
      use_av_3 = 0
      use_av_4 = 0
      if rowdata[1].find('12:00') != -1:  use_av_1 = 1
      if rowdata[1].find('12:30') != -1:  use_av_2 = 1
      if rowdata[1].find('1:00') != -1:  use_av_3 = 1
      if rowdata[1].find('1:30') != -1:  use_av_4 = 1
      mysql_update_qry = "update People set last_updated = '%s', avail_1 = %s, avail_2 = %s, avail_3 = %s, avail_4 = %s where email = '%s'" % (l_updated, use_av_1, use_av_2, use_av_3, use_av_4, rowdata[2])
      cursor.execute(mysql_update_qry)

    db.close()

  def Run(self):

    # Get the list of spreadsheets
    feed = self.gd_client.GetSpreadsheetsFeed()
    # self._PrintFeed(feed)
    # assume doc index=0
    id_parts = feed.entry[0].id.text.split('/')
    doc_key = id_parts[len(id_parts) - 1]
  
    # Get the list of worksheets
    feed = self.gd_client.GetWorksheetsFeed(doc_key)
    # self._PrintFeed(feed)
    # assume worksheet index=0
    id_parts = feed.entry[0].id.text.split('/')
    ws_key = id_parts[len(id_parts) - 1]
    
    # Get the list feed
    feed = self.gd_client.GetListFeed(doc_key, ws_key)
    self._ProcessData(feed)
  

def main():
  # parse command line options
  try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["user=", "pw="])
  except getopt.error, msg:
    print 'python spreadsheetExample.py --user [username] --pw [password] '
    sys.exit(2)
 
  user = ''
  pw = ''
  key = ''
  # Process options
  for o, a in opts:
    if o == "--user":
      user = a
    elif o == "--pw":
      pw = a

  if user == '' or pw == '':
    print 'python get_data.py --user [username] --pw [password] '
    sys.exit(2)
  
  sample = SimpleCRUD(user, pw)
  sample.Run()


if __name__ == '__main__':
  main()
