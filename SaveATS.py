def SaveATS(ECG,AfterInterpRate,freq,ShockType,Destination,patientid,DeviceModel,mode,MultipleShock,EnlageSignal,RealID):
    import numpy as np
    import scipy.io
    import scipy.io as sio
    InterpRate=AfterInterpRate/freq
    if((mode==1)or MultipleShock==0):
        print 'goes there'
        #ECG=ECG11()
        #ECG.samples=ecg1()
        print 'ECG.samples.ss'
        #print len(ECG.samples.ss)
        tmp=ECG.samples.ss
        tmp1=ECG.samples.fb
        cc=np.double(tmp)
        cc1=np.double(tmp1)
        ecg_ss=cc*EnlageSignal
        ecg_fb=cc1*EnlageSignal
        #ecg_ss=np.int16(interp1(cc,InterpRate)*EnlageSignal)
        #ecg_fb=np.int16(interp1(cc1,InterpRate)*EnlageSignal)
        ATS=np.zeros(len(ecg_ss)*2)
        for i in range(0,len(ecg_ss)):
            ATS[i*2]=ecg_ss[i]
            i=i+1
        for i in range(0,len(ecg_ss)):
            ATS[i*2+1]=ecg_fb[i]
            i=i+1
        MaskId=float(patientid)
        RealIdNum=Get_WCD_ID(MaskId)
        RealId=str(RealIdNum)
        outfilename=Destination+RealId+DeviceModel+'.'+ShockType+'.ats'
        fid=open(outfilename,'w')
        fid.write(np.int16(ATS))
        fid.close()
        txtfilename=Destination+RealId+DeviceModel+'.'+ShockType+'.txt'
        fileID_txt=open(txtfilename, 'w')
        #write information into a txt file. need to find a way to skip this step
       
        #fprintf(fileID_txt,'Patient wcd ID:\r\n%s\r\n', RealId)
        fileID_txt.write('Patient wcd ID:\r\n'+RealId+'\r\n')
        #fprintf(fileID_txt,'Patient mask ID:\r\n%s\r\n', patientid)
        fileID_txt.write('Patient mask ID:\r\n'+patientid+'\r\n')
        #fprintf(fileID_txt,'Device model:\r\n%s\r\n', DeviceModel)
        fileID_txt.write('Device model:\r\n'+DeviceModel+'\r\n')
        #fprintf(fileID_txt,'Shock type:\r\n%s\r\n', ShockType)
        fileID_txt.write('Shock type:\r\n'+ShockType+'\r\n')
        #fprintf(fileID_txt,'Sampling rate:\r\n%d\r\n\r\n', AfterInterpRate)
        fileID_txt.write('Sampling rate:\r\n'+str(AfterInterpRate)+'\r\n\r\n')
        #fprintf(fileID_txt,'Total length for one channel(s):\r\n%4.3f\r\n',ECG.length.total/freq)
        fileID_txt.write('Total length for one channel(s):\r\n'+str(ECG.length.total/freq)+'\r\n')
        #fprintf(fileID_txt,'Total length for both channels(s):\r\n%4.3f\r\n',ECG.length.total/freq*2)
        fileID_txt.write('Total length for both channels(s):\r\n'+str(ECG.length.total/freq*2)+'\r\n')
        #fprintf(fileID_txt,'Baseline length(s):\r\n%3.3f\r\n',ECG.length.baseline/freq)
        fileID_txt.write('Baseline length(s):\r\n'+str(ECG.length.baseline/freq)+'\r\n')
        #fprintf(fileID_txt,'Arrhythmia length(s):\r\n%3.3f\r\n',ECG.length.arrhythmia/freq)
        fileID_txt.write('Arrhythmia length(s):\r\n'+str(ECG.length.arrhythmia/freq)+'\r\n')
        #fprintf(fileID_txt,'Arrhythmia start at(s):\r\n%3.3f\r\n',(ECG.length.baseline+1)/freq)
        fileID_txt.write('Arrhythmia start at(s):\r\n'+str((ECG.length.baseline+1)/freq)+'\r\n')
        #fprintf(fileID_txt,'Arrhythmia end at(s):\r\n%3.3f\r\n\r\n',ECG.length.arrhythmiaend/freq)
        fileID_txt.write('Arrhythmia end at(s):\r\n'+str(ECG.length.arrhythmiaend/freq)+'\r\n\r\n')                
      #fprintf(fileID_txt,'Total length for one channel(samples):\r\n%d\r\n',ECG.length.total*InterpRate)
        fileID_txt.write('Total length for one channel(samples):\r\n'+str(ECG.length.total*InterpRate)+'\r\n')
        #fprintf(fileID_txt,'Total length for both channels(samples):\r\n%d\r\n',ECG.length.total*InterpRate*2)
        fileID_txt.write('Total length for both channels(samples):\r\n'+str(ECG.length.total*InterpRate*2)+'\r\n')
        #fprintf(fileID_txt,'Baseline length(samples):\r\n%d\r\n', ECG.length.baseline*InterpRate)
        fileID_txt.write('Baseline length(samples):\r\n'+str(ECG.length.baseline*InterpRate)+'\r\n')
        #fprintf(fileID_txt,'Arrhythmia length(samples):\r\n%d\r\n', ECG.length.arrhythmia*InterpRate)
        fileID_txt.write('Arrhythmia length(samples):\r\n'+str(ECG.length.arrhythmia*InterpRate)+'\r\n')
        #fprintf(fileID_txt,'Arrhythmia start at(samples):\r\n%d\r\n', ECG.length.baseline*InterpRate+1)
        fileID_txt.write('Arrhythmia start at(samples):\r\n'+str((ECG.length.baseline*InterpRate+1))+'\r\n')
        #fprintf(fileID_txt,'Arrhythmia end at(samples):\r\n%d\r\n', ECG.length.arrhythmiaend*InterpRate)
        fileID_txt.write('Arrhythmia end at(samples):\r\n'+str(ECG.length.arrhythmiaend*InterpRate)+'\r\n')
        fileID_txt.close()
    else:
        letter='ABCDEFGHIGKLMNOPQRSTUVWXYZ'
        MaskId=float(patientid)
        RealIdNum=Get_WCD_ID(MaskId)
        RealId=str(RealIdNum)
        for i in range(0,MultipleShock):
            tmp='samples'+i
            ecg_ss=np.int16(interp1(np.double(ECG.tmp.ss),InterpRate)*EnlageSignal)
            ecg_fb=np.int16(interp1(np.double(ECG.tmp.fb),InterpRate)*EnlageSignal)
            ATS=np.zeros(len(ecg_ss)*2)
            for k in range(0,len(ecg_ss)):
                ATS[k*2]=ecg_ss[k]
                k=k+1
            for k in range(0,len(ecg_ss)):
                ATS[k*2+1]=ecg_fb[k]
                k=k+1
            outfilename=Destination+RealId+DeviceModel+'.'+ShockType+'.ats'
            fid=open(outfilename,'w')
            fid.write(np.int16(ATS))
            fid.close()
            txtfilename=Destination+RealId+DeviceModel+'.'+ShockType+'.txt'
            fileID_txt=open(txtfilename, 'w')
            #fprintf(fileID_txt,'Patient wcd ID:\r\n%s\r\n', RealId)
            fileID_txt.write('Patient wcd ID:\n'+RealId+'\n')
            #fprintf(fileID_txt,'Patient mask ID:\r\n%s\r\n', patientid)
            fileID_txt.write('Patient mask ID:\n'+patientid+'\n')
            #fprintf(fileID_txt,'Device model:\r\n%s\r\n', DeviceModel)
            fileID_txt.write('Device model:\n'+DeviceModel+'\n')
            #fprintf(fileID_txt,'Shock type:\r\n%s\r\n', ShockType)
            fileID_txt.write('Shock type:\n'+ShockType+'\n')
            #fprintf(fileID_txt,'Sampling rate:\r\n%d\r\n\r\n', AfterInterpRate)
            fileID_txt.write('Sampling rate:\n'+str(AfterInterpRate)+'\n')
            #fprintf(fileID_txt,'Total length for one channel(s):\r\n%4.3f\r\n',ECG.length.total/freq)
            tmp1='length'+i
            fileID_txt.write('Total length for one channel(s):\n'+str(ECG.tmp1.total/freq)+'\n')
            #fprintf(fileID_txt,'Total length for both channels(s):\r\n%4.3f\r\n',ECG.length.total/freq*2)
            fileID_txt.write('Total length for both channels(s):\n'+str(ECG.tmp1.total/freq*2)+'\n')
            #fprintf(fileID_txt,'Baseline length(s):\r\n%3.3f\r\n',ECG.length.baseline/freq)
            fileID_txt.write('Baseline length(s):\n'+str(ECG.tmp1.baseline/freq)+'\n')
            #fprintf(fileID_txt,'Arrhythmia length(s):\r\n%3.3f\r\n',ECG.length.arrhythmia/freq)
            fileID_txt.write('Arrhythmia length(s):\n'+str(ECG.tmp1.arrhythmia/freq)+'\n')
            #fprintf(fileID_txt,'Arrhythmia start at(s):\r\n%3.3f\r\n',(ECG.length.baseline+1)/freq)
            fileID_txt.write('Arrhythmia start at(s):\n'+str((ECG.tmp1.baseline+1)/freq)+'\n')
            #fprintf(fileID_txt,'Arrhythmia end at(s):\r\n%3.3f\r\n\r\n',ECG.length.arrhythmiaend/freq)
            fileID_txt.write('Arrhythmia end at(s):\r\n'+str(ECG.length.arrhythmiaend/freq)+'\n')                 
            #fprintf(fileID_txt,'Total length for one channel(samples):\r\n%d\r\n',ECG.length.total*InterpRate)
            fileID_txt.write('Total length for one channel(samples):\n'+str(ECG.tmp1.total*InterpRate)+'\n')
            #fprintf(fileID_txt,'Total length for both channels(samples):\r\n%d\r\n',ECG.length.total*InterpRate*2)
            fileID_txt.write('Total length for both channels(samples):\n'+str(ECG.tmp1.total*InterpRate*2)+'\n')
            #fprintf(fileID_txt,'Baseline length(samples):\r\n%d\r\n', ECG.length.baseline*InterpRate)
            fileID_txt.write('Baseline length(samples):\n'+str(ECG.tmp1.baseline*InterpRate)+'\n')
            #fprintf(fileID_txt,'Arrhythmia length(samples):\r\n%d\r\n', ECG.length.arrhythmia*InterpRate)
            fileID_txt.write('Arrhythmia length(samples):\n'+str(ECG.tmp1.arrhythmia*InterpRate)+'\n')
            #fprintf(fileID_txt,'Arrhythmia start at(samples):\r\n%d\r\n', ECG.length.baseline*InterpRate+1)
            fileID_txt.write('Arrhythmia start at(samples):\n'+str((ECG.tmp1.baseline*InterpRate+1))+'\n')
            #fprintf(fileID_txt,'Arrhythmia end at(samples):\r\n%d\r\n', ECG.length.arrhythmiaend*InterpRate)
            fileID_txt.write('Arrhythmia end at(samples):\n'+str(ECG.tmp1.arrhythmiaend*InterpRate)+'\n')
            fileID_txt.close()
