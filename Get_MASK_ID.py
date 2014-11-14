def Get_MASK_ID(WcdPatientNum):
    
    import pyodbc

    cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.8.0.15; DATABASE=WcdLive; UID=EventPrediction; PWD=ScaPredict1;')
    cursor = cnxn.cursor()
    a=WcdPatientNum

                
    cmdstring="exec EventPrediction.dbo.GetMaskIdForWcdPatientNum'"+str(a)+"'"
    cursor.execute(cmdstring)
    MaskId=-1
    rows=cursor.fetchall()
    #print rows
    for row in rows:
        c=(row[0])
        MaskId=c
    return MaskId
