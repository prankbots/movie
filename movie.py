import lineX
from lineX import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift.protocol import TCompactProtocol
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
_session = requests.session()
botStart = time.time()
movieOp = codecs.open("movie.json","r","utf-8")
mengirim = json.load(movieOp)
me = LINE() # INI LOGIN LANGSUNG
#me = LINE("gmail.com", "passwd") #ini kalo mau pake gmail
#me = LINE("TOKEN")
oepoll = OEPoll(me)
meProfile = me.getProfile()
meSettings = me.getSettings()
# BATAS MID
meM = me.getProfile().mid
set = {
  "Key": False,
  "text": "acil:"
}
def Comt(text):
  pesan = text.lower()
  if set["Key"] == True:
    if pesan.startswith(set["text"]):
      Pbot = pesan.replace(set["text"],"")
    else:
      Pbot = "Undefined command"
  else:
    Pbot = text.lower()
  return Pbot
def template(op):
  global threading
  global groupParam
  global rsa
  try:
    if op.type == 0:
      return
    if op.type == 25 or op.type == 26: # INI PUBLIK SAMA SELF JALAN KABEH
      self = op.message
      to = self.to
      Id = self.id
      text = self.text
      if self.toType == 0 or self.toType == 1 or self.toType == 2:
        if self.toType == 0:
          if self._from != me.profile.mid:
            to = self._from
          else:
            to = self.to
        elif msg.toType == 1:
          to = self.to
        elif self.toType == 2:
          to = self.to
        elif self.contentType == 16: # INI AUTO LIKE BRO
            url = self.contentMetadata["postEndUrl"]
            me.likeTL(url[25:58], url[66:], likeType=1005)
            me.commantTL(url[25:58], url[66:],"ᴀᴜᴛᴏ ʟɪᴋᴇ ʙʏ ᴘʀᴀɴᴋʙᴏᴛ\nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ sᴜʙsᴄʀᴀʙᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀᴍɪ ᴅɪsɪɴɪ\nhttps://bit.ly/2xbVxlh")
        if self.contentType == 0:
          if text is None:
            return
          else:
            Pbot == Comt(text)
            if Pbot = "movie":
              me.sendFlex(to, mengirim["movie"])
  except Exception as e:
    print(e)
    if op.type == 59:
      print(op)
while True:
  try:
    ops=oepoll.singleTrace(count=50)
    if ops != None:
      for op in ops: 
        template(op)
        oepoll.setRevision(op.revision)       
  except Exception as e:
    me.log("ERROR\n IN [ " + " ] == " + str(e) + "INI HARUS DI PERBAIKI")
