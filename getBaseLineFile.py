import scipy
import numpy
from numpy import *
from scipy import signal
import os
import struct

from struct import unpack
import subprocess
import glob
import shutil
from datetime import datetime
import pyodbc
def getBaseLineFile(wcdID):
   #writeDir = '/var/www/wcdFiles/'
   writeDir='C:/Users/JDang/Desktop/'
   cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.8.0.15; DATABASE=WcdLive; UID=EventPrediction; PWD=ScaPredict1;')
   cursor = cnxn.cursor()
   print 'successfully connect to the database'
   cursorString = "SELECT CONVERT(varchar(max),CONVERT(varbinary(max),flagattachment),0) FROM WcdEcgEvent WHERE PatientNum = %d AND EcgEventTypeNum = 1" % wcdID
   a=cursor.execute(cursorString)
   out = cursor.fetchone()
   
   cursorString = "SELECT CONVERT(varbinary(max),processedimage) FROM WcdEcgEvent WHERE PatientNum= %d AND EcgEventTypeNum = 1" % wcdID
   cursor.execute(cursorString)
   outECG = cursor.fetchone()
   #print outECG
   if  outECG is not None:
      outString = writeDir + str(wcdID) +'monitorImage.dat'
      f=open(outString,"w")
      outE = outECG[0];
      size=len(outE)
      f.write(outE);
      f.close();
      fileEnd = '%d.ffi' % wcdID;
      flagFile = writeDir + fileEnd
      f=open(flagFile,'w')
      out = out[0]
      f.write(out.encode('ascii', errors='blackslashreplace'));
      f.close()
      print 'start ot unpack'
      return unpackDatFile(outString, size/6)
