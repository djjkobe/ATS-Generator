def FindShockPeriod(ShockFilePath,ShockStartShift,freq,mode,ApplyFilter):
    import os
    [ss_ecg,fb_ecg,event_location,arrhythmia]=ExtractShockECG(ShockFilePath,ShockStartShift,freq,mode)
    letter='ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    N=len(event_location)
    #do not apply filter
    ecg_ss=ss_ecg
    ecg_fb=fb_ecg
    if N>1:
        if mode==1:
            shock=event_location[0]
            arr_start=[]
            p=shock-1
            while(p>=0):
                if(arrhythmia[p]==0):
                    break
                p=p-1
            if(p!=-1):
                arr_start=arrhythmia[p]+1
            startpoint=arr_start+ShockStartShift*freq
            stoppoint=shock-1
            ShockPeriod=ShockPeriod1()
            ShockPeriod.ecg=ecg1()
            ShockPeriod.ecg.ss=ecg_ss[startpoint-1:stoppoint]
            ShockPeriod.ecg.fb=ecg_fb[startpoint-1:stoppoint]
            ShockPeriod.MultipleShock=0
        else:
            for i in range(0,N):
                shock=event_location[i]
                arr_start=[]
                p=shock-1
                while(p>=0):
                    if(arrhythmia[p]==0):
                        break
                    p=p-1
                if(p!=-1):
                    arr_start=p+1+1
                startpoint=arr_start+ShockStartShift*freq
                stoppoint=shock-1
                tmp='ecg'+letter[i]
                ShockPeriod.tmp=ecg1()
                ShockPeriod.tmp.ss=ecg_ss[startpoint-1:stoppoint]
                ShockPeriod.tmp.fb=ecg_fb[startpoint-1:stoppoint]
                #clear shock arr_start startpoint stoppoint
            ShockPeriod.MultipleShock=N
    else:
        shock=event_location[0]
       
        arr_start=[]
        p=shock-1
        while(p>=0):
            if(arrhythmia[p]==0):
                break
            p=p-1
        if(p!=-1):
            arr_start=p+1+1
        startpoint=arr_start+ShockStartShift*freq
        print 'startpoint'
        print startpoint
        stoppoint=shock-1
        print 'stoppoint'
        print stoppoint
        ShockPeriod=ShockPeriod1()
        ShockPeriod.ecg=ecg1()
        ShockPeriod.ecg.ss=ecg_ss[startpoint-1:stoppoint]
        print 'length of ShockPeriod.ecg.ss'
        print stoppoint-startpoint
        ShockPeriod.ecg.fb=ecg_fb[startpoint-1:stoppoint]
        ShockPeriod.MultipleShock=0
        #fid=open('C:/Users/JDang/Desktop/check.txt','a')
        
    print ('Finish extract '+str(N)+' shock.\n')
    #fprintf('Finish extract %d shock.\n',N)    ???????????????????????????????
    return ShockPeriod            
