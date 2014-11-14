def Get_WCD_ID(MaskId):
    import pyodbc
    cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.8.0.15; DATABASE=WcdLive; UID=EventPrediction; PWD=ScaPredict1;')
    cursor = cnxn.cursor()
    a=MaskId
    b='EventPrediction.dbo.GetWcdPatientNumForMaskId @MaskId='+str(a)
    cursor.execute(b)
    rows = cursor.fetchall()
    for row in rows:
        c=(row[0])
    WcdPatientNum=c
    #print('done')
    return WcdPatientNum 
