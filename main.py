import pyodbc
import os.path
import Tkinter
import tkFileDialog
import re

class ECG11:
    def __init__(self):
        self.samples=[]
        self.samplesA=[]
        self.samplesB=[]
        self.samplesC=[]
        self.samplesD=[]
        self.samplesE=[]
        self.samplesF=[]
        self.samplesG=[]
        self.samplesH=[]
        self.samplesI=[]
        self.samplesJ=[]
        self.samplesK=[]
        self.samplesL=[]
        self.samplesM=[]
        self.samplesN=[]
        self.samplesO=[]
        self.samplesP=[]
        self.samplesQ=[]
        self.samplesR=[]
        self.samplesS=[]
        self.samplesT=[]
        self.samplesU=[]
        self.samplesV=[]
        self.samplesW=[]
        self.samplesX=[]
        self.samplesY=[]
        self.samplesZ=[]
        self.length=[]

class Category:
    def __init__(self, type, subtype,PrimaryReason,preShockRhythem):
        self.type = type
        self.subtype =subtype
        self.PrimaryReason=PrimaryReason
        self.preShockRhythem=preShockRhythem
    def __init__(self):
        self.type = []
        self.subtype =[]
        self.PrimaryReason=[]
        self.preShockRhythem=[]
class Record:
    def __init__(self, ifexist, shocktype,RealID,ShockReason):
        self.ifexist = ifexist
        self.shocktype =shocktype
        self.RealID=RealID
        self.ShockReason=ShockReason
    def __init__(self):
        self.ifexist = []
        self.shocktype =[]
        self.RealID=[]
        self.ShockReason=[]
class ShockPeriod1:
        def __init__(self):
            self.ecg =[]
            self.ecgA=[]
            self.ecgB=[]
            self.ecgC=[]
            self.ecgD=[]
            self.ecgE=[]
            self.ecgF=[]
            self.ecgG=[]
            self.ecgH=[]
            self.ecgI=[]
            self.ecgJ=[]
            self.ecgK=[]
            self.ecgL=[]
            self.ecgM=[]
            self.ecgN=[]
            self.ecgO=[]
            self.ecgP=[]
            self.ecgQ=[]
            self.ecgR=[]
            self.ecgS=[]
            self.ecgT=[]
            self.ecgU=[]
            self.ecgV=[]
            self.ecgW=[]
            self.ecgX=[]
            self.ecgY=[]
            self.ecgZ=[]
            self.MutipleShock=0
class ecg1:
    def __init__(self):

        
        self.ss =[]
        self.fb=[]
        self.baseline=[]
        self.arrhythmia=[]
        self.arrhythmiaend=[]
        self.total=0
#you need choose shock file first
#you have option to choose baseline and destination
#close all
#clear
#clc% list options
#freq=400
#import pdb
#pdb.set_trace()

freq=400
AfterInterpRate=400
mode=1                 # mode=1 means only get first shock, mode=0 means get every shock of the patientand pending with 'ABCD..' to ATS file
ShockStartShift=-13    # get whole length of arrhythmia
ApplyFilter=0          # ApplyFilter=1 means use filter to pre-process signal, ApplyFilter=0 means do not use filter.
LengthofBaseline=60*2  # pre-rhythem/post rhythem length is 1 min
DeviceModel="g4000"    # device model should be 4000 for current test
EnlageSignal=4

# make signal bigger (ATS signal=original signal*EnlagelSignal)
# choose shock file
baselineEcgFile=""
count=1
"""
while(not os.path.exists(baselineEcgFile)):
    if(count==1):
        prompt='Plese input the name of the file(end with .ecg)\n'
        count=count+1
    else:
        prompt='The file you wanted is not exist,plese input the name of the file again(end with .ecg)\n'
    baselinefile=input(prompt)
    baselinepath="C:/Users/JDang/Desktop/ATS/code/ECGtoATS/version4.0/"
    baselineEcgFile=baselinepath+baselinefile
patientid=baselinefile[0:6]
MaskID=str2double(patientid)
"""
Tkinter.Tk().withdraw() # Close the root window
in_path = tkFileDialog.askopenfilename()
p=re.split('/',in_path)
shockfile=p[len(p)-1]
shockEcgFile=in_path
print shockEcgFile
patientid=shockfile[0:6]
MaskID=float(patientid)


# get shock type
RealID=Get_WCD_ID(MaskID)
Category=ShockTypeSelection(MaskID)
#print Category
type=Category.type
ShockType=Category.subtype
print ShockType
"""
# choose baseline file
prompt='Do you need maually choose baseline file? 1.y or 2.n (default:n)\n'
choosebaselinefile=input(prompt)

if choosebaselinefile==1:
    #[baselinefile,baselinepath]=uigetfile('\\10.19.0.9\holterdatasets\ecg\*.ecg')
    #BaselineEcgFile=strcat(baselinepath,baselinefile)
    Tkinter.Tk().withdraw() # Close the root window
    in_path = tkFileDialog.askopenfilename()
    p=re.split('/',in_path)
    baselinefile=p[len(p)-1]
    baselineEcgFile=in_path
    print baselineEcgFile
    prompt='How long is baseline start shift time(min): (default:30min)\n'
    BaselineStartShift=input(prompt)
    #if isempty(BaselineStartShift):
        #BaselineStartShift=30*60
    #else:
    BaselineStartShift=BaselineStartShift*60
   
else:
    [BaselineEcgFile,FileAfterShock]=FindCleanFile(MaskID,type)
    if FileAfterShock==0:
        BaselineStartShift=30*60 # If the baseline file is before shock, need 30 min shift from beginning
    else:
        BaselineStartShift=60*60 # If the baseline file is after shock, need 60 min shift from beginning
"""

# choose destination 
#fprint('')        #????????????
prompt='Do you need maually choose destination folder? 1.y or 2.n \n default:n (will use ATS drive as destination)\n'
choosedestination=input(prompt)
if choosedestination==1:
    Tkinter.Tk().withdraw() # Close the root window
    in_path = tkFileDialog.askdirectory()
    Destination=in_path+'/'
    print Destination
else:
    Destination=ATSdrive+type+'/'+ShockType+'/'     # You have to define the ATSdrive before running the program

# find shock period
ShockPeriod=FindShockPeriod(shockEcgFile,ShockStartShift,freq,mode,ApplyFilter)

#[ecgSS,ecgFB,timeVec]=getBaseLineFile(RealID)
#ECG=Connect(ecgSS,ecgFB,ShockPeriod)
[ecgSS,ecgFB,timeVec]=getBaseLineFile(RealID)
print 'length of ecgSS is '
print len(ecgSS)
print ecgSS
print 'need to upsample the baseline'
ecgSS1=interp1(ecgSS,4)
ecgFB1=interp1(ecgFB,4)
#BaselinePeriod=FindBaseline(BaselineEcgFile,LengthofBaseline,BaselineStartShift,freq,ApplyFilter)
#[ecgSS,ecgFB,timeVec]=getBaseLineFile(RealID)
#if BaselinePeriod:
print 'length of ecgSS1'
print len(ecgSS1)
print 'length of ecgFB1'
print len(ecgFB1)
if(len(ecgSS1)!=0):
    ECG=Connect(ecgSS1,ecgFB1,ShockPeriod)
    print 'ECG successfully created'
    print 'length of ECG is '
    #print len(ECG)
    SaveATS(ECG,AfterInterpRate,freq,ShockType,Destination,patientid,DeviceModel,mode,ShockPeriod.MultipleShock,EnlageSignal,RealID)
    #UpdateProcessedList(MaskID,type)
else:
    print "Some error happened can not find baseline period"
    
print('finish generate ATS file!')
