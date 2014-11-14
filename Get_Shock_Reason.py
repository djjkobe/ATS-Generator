"""
 This function is used for get sub-shock type from our SCARP database
 Currently, the 'GetAppropriateShockDataFromClinicalDB' and 'GetInappropriateShockDataFromClinicalDB' procedure are both static and they maybe support dynamic query next year (2014)
 Input: ShockType: either 'trueshock', 'falseshock'. Otherinput will cause record.ifexist=-1
 Output: record.ifexist: if exist record, it is 0 Otherwise it is -1
 Output: record. shocktype: same as input
 Output: record. RealID: patient WCD ID
 Output: record. ShockReason: sub shock type (if it is true shock, it is sub shock type string, elseif it is false shock, it is index of sub shock type)
 False shock reason index:
 0   Empty 
 1	Dual-lead signal artifact
 2	SS artifact
 3	FB artifact
 4	Artifact-Not specified
 5	Multiple counting
 6	SVT
 7	Morphology change
 8	NSVT
 9	Self-terminating VT
 10	Asystole
 11	Oversensing
 12	Noise
"""
def  Get_Shock_Reason(ShockType):
    
    record= Record()
    record.ifexist=-1            # if no record exist, record.ifexist=-1 else record.ifexist=0
    record.shocktype=ShockType
    cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.8.0.15; DATABASE=WcdLive; UID=EventPrediction; PWD=ScaPredict1;')
    cursor = cnxn.cursor()

    if (ShockType=='trueshock'):   # For trueshock patients, we need Pre_shock_rhythm
        # execute store procedure
        cmdstring='EventPrediction.dbo.GetAppropriateShockDataFromClinicalDB'
        cursor.execute(cmdstring)
        # find records
        rows=cursor.fetchall()
        #rec_cnt=0
        if(rows):
            record.ifexist=0
        for row in rows:
            #rec_cnt=rec_cnt+1
            record.RealID.append(row[0])
            record.ShockReason.append(row[1])
        
    elif(ShockType=='falseshock'):   # For falseshock patients, we need Reason_ID(Primary)
        cmdstring='EventPrediction.dbo.GetInappropriateShockDataFromClinicalDB'
        cursor.execute(cmdstring)
        # find records
        rows=cursor.fetchall()
        #rec_cnt=0
        if (rows):
            # records found
            record.ifexist=0
        for row in rows:
            #rec_cnt=rec_cnt+1
            record.RealID.append(row[0])
            if(not row[1]):
                record.ShockReason.append(0)
            record.ShockReason.append(row[1])
    return record
