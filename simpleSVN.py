#!/usr/bin/env python

from urllib2 import urlopen
from bs4 import BeautifulSoup
from sys import argv
from os import system, mkdir

def info():
 print "Simple SVN alternative"
 print "Author: Fabien DROMAS"
 print "Mail: fabien.dromas@synetis.com"
 
def createFolder(name):
 mkdir(name)
 
def getHTML(url):
  req=urlopen(url)
  html=req.read()
  parse=BeautifulSoup(html)
  return parse
  
def downloadItems(parse, url, folder):
 for i in parse.findAll('a'):
  system("/usr/bin/wget "+url+i.get('href')+" -O "+folder+"/"+i.get('href'))
 
 
if len(argv)<2:
 info()
 print "\n"
 print "Usage: %s svn_link folder_name" %argv[0]
else:
 createFolder(argv[2])
 downloadItems(getHTML(argv[1]), argv[1], argv[2])
