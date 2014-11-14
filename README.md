ATS-Generator
Developer: Jiajie Dang
Email: djjkobe@gmail.com
=============
This is a Python program that convert .ATS file to .ATS file for testing. The outline of the project is as followed:
1.choose shock file
manually choose the shock file(Implement the GUI using TkInter)

2.get shock type
(1)get Maskid from shockfile name

(2)get RealID from MaskID for further use
function: Get_WCD_ID

(3)use MaskID to get the Category of the shock 
function:ShockTypeSelection 
function: get_Shock_Reason
function: get_mask_id

(4)get the shock type by the category

3. choose baseline file and set the start shift time
manually choose the baseline file(Implement by Tkinter)

4.choose destination 
manually choose the destination (Implement by Tkinter)

5.find shock period
(1)First extract the shock ecg from the shockfile we chose earlier 
function: ExtractShockECG

(2)convert the shock ecg to mat format and get four arguments(ss_ecg, fb_ecg, event_location, arrhythmia)
function: ECG2MAT

(3)check how many shocks in the shockfile were found and handle them sepreately 

6.find baseline period


7.connect baseline period and shockperiod together
function: Connect

8. saveATS and update the processed list
function:saveATS
function:UpdateProcessedList





