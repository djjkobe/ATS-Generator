# This function will called by FindShockPeriod function
# It can extact certain length before treatable arrhythmia (by ShockStartShift) and 1 ecg after shock from original .ecg
# If ShockStartShift is negtive, means get time before treatable arrhythmia. Otherwise, itwill get time after treatable arrhythmia. Unit is second.
# Input: ShockFilePath should be the whole of the shock file
# Input: freq should be 400 for 4000 Model
# Output: ShockPeriodECG: ECG signal
def ExtractShockECG(ShockFilePath,ShockStartShift,freq,mode):
    import os
    import numpy as np
    def int2str(i):     #get 32-bits binary representation of a number
        str = ""
        flag = -1
        while i>0 or flag==-1:
            if(i%2 == 1):
                flag = -1
                str="1"+str
            else:
                str="0"+str
                flag = 0
            i = i/2
        if(flag==-1):
            str = "1"+str
        return str.zfill(32)
    ShockPeriodECG=[]
    visit=0
    extractlimit=-1*freq*ShockStartShift
    #file_info=os.listdir(ShockFilePath)
    fID=open(ShockFilePath,'rb')
    #initial variables
    offset=0
    ending=45000000    #new .ecg will less than 1 hour
    fileevent=0
    ecgNum=0
    currentecgNum=0
    previousflag=0
    nextflag=0
    shocklocation=[]
    #print shocklocation[1]
    
    size=os.path.getsize(ShockFilePath)
  
    #loop 
    while(offset<=size):
        print offset
        visit=0
        if((size-offset)<45000000):
            ending=size-offset   #number of bytes left
            if ending==0:       #left if no more bytes left
                break
            
        data=fID.read(ending)
        a=[]
        for i in range(0,len(data)):
            a.append(ord(data[i]))
        data=np.uint8(a)
     
        #if it's the first time in loop
        if(offset==0):              
            previous_data=data
        if(ending==45000000):       
            predataID=[]
            i=0
            while(i<ending):
                predataID.append(previous_data[i])
                i=i+5
        #offset==0      
        elif ending<45000000 and offset==0:
            predateID=[]
        #offset!=0
        else:
            predataID=[]
            i=0
            while(i<45000000):
                predataID.append(previous_data[i])
                i=i+5
        
        dataID=[]
        k=0
        while(k<ending):
            dataID.append(data[k])
            k=k+5
        ecgNum=ecgNum+currentecgNum
       
        #currentecgNum=sum(dataID(:)==0)
        count=0
        for i in range(0,len(dataID)):
            if(data[i]==0):
                count=count+1
        currentecgNum=count
    
   
        # if the end time is in next packet, save it at the begining of the next packet
        if(nextflag==1):
            # ecglocation=find(dataID==0)*5-4
            ecglocation=[]
            for i in range(0,len(dataID)):
                if(dataID[i]==0):
                    ecglocation.append((i+1)*5-4)
                    
            if((ending<45000000)and(stopecg>len(ecglocation))):
                stoppacket=ecglocation[len(ecglocation)-1]+4
            else:
                stoppacket=ecglocation[stopecg-1]+4
                
            N=len(ShockPeriodECG)
            #ShockPeriodECG=[]
            ShockPeriodECG[N:N+len(data[0:stoppacket])]=data[0:stoppacket]
            #clear N
            nextflag=0

        #find shock event
        flaglocation=[]
        for i in range(0,len(dataID)):
            if(dataID[i]==2):
                flaglocation.append((i+1)*5-4)
        if (flaglocation):
            print 'flaglocation'
            print len(flaglocation)
            for k in range(0,len(flaglocation)):
                if(data[flaglocation[k]+3-1]==17 and data[flaglocation[k+1]+3-1]==17):
                    fileevent=fileevent+1
                    print 'length of flaglocation'
                    print len(flaglocation)
                    print 'k+1'
                    print k+1
                    print 'fileevent'
                    print fileevent
                    print 'flaglocation[k+1]'
                    print flaglocation[k+1]
                    #print shocklocation[fileevent-1]
                    shocklocation.append(flaglocation[k+1])
                    visit=1
        #if there is a shock event in this offset, save it 
        if visit==1:
            firstshock=shocklocation[0]
            if (mode==1):
                lastshock=firstshock
            else:
                lastshock=shocklocation[len(shocklocation)-1]
            ecglocation=[]
            # ecglocation=find(dataID==0)*5-4            
            for i in range(0,len(dataID)):
                if(dataID[i]==0):
                    ecglocation.append((i+1)*5-4)
            print 'length of ecglocation'
            print len(ecglocation)
            # preecglocation=(find(predataID==0)*5)-4
            preecglocation=[]
            for k in range(0,len(predataID)):
                if(predataID[k]==0):
                    preecglocation.append((k+1)*5-4)
            print 'length of preecglocation'
            print len(preecglocation)
            # gainlocation=find(dataID==1)*5-4
            gainlocation=[]
            for m in range(0,len(dataID)):
                if(dataID[m]==1):
                    gainlocation.append((m+1)*5-4)
            print 'length of gainlocation'
            print len(gainlocation)
            # pregainlocation=(find(predataID==1)*5)-4
            
            pregainlocation=[]
            for n in range(0,len(predataID)):
                if(predataID[n]==1):
                    pregainlocation.append((n+1)*5-4)
            print 'length of pregainlocation'
            print len(pregainlocation)
            # find end time: 1 ecg after shock
            # stopecg=find(ecglocation>lastshock,1,'first')
            stopecg=-1
            for p in range(0,len(ecglocation)):
                if(ecglocation[p]>lastshock):
                    stopecg=p+1
                    break
            print 'stopecg'
            print stopecg
            if(stopecg<=len(ecglocation)and stopecg>=0):
                stoppacket=ecglocation[stopecg-1]+4
            else:
                if(ending<45000000):
                    stoppacket=len(data)
                else:
                    stopecg=stopecg-currentecgNum
                    nextflag=1
                    
            # find start time: Shock Start Shift before arrhythmia
            # find arrhythmia start time first
            
            # noisedet=(find(dataID==3)*5)-4
            noisedet=[]
            for i in range(0,len(dataID)):
                if(dataID[i]==3):
                    noisedet.append((i+1)*5-4)
            print 'nosedet'
            print len(noisedet)
            # prenoisedet=(find(predataID==3)*5)-4
            prenoisedet=[]
            for j in range(0,len(predataID)):
                if(predataID[j]==3):
                    prenoisedet.append((j+1)*5-4)
            print 'prenoisedet'
            print len(prenoisedet)
            # det=noisedet(bitget(data(noisedet+3),8)==0)
            a1=np.array(noisedet)
            c=[]
            for m in range(0,len(a1)):
                c.append(a1[m]+2)
            target=list(data[c])
            dup=[]
            for k in range(0,len(target)):
                dup.append(int(int2str(target[k])[32-8]))
            
            b=[]
            for i in range(0,len(dup)):
                if(dup[i]==0):
                    b.append(i)
            det=list(a1[b])
            print 'det'
            print len(det)
            # predet=prenoisedet(bitget(previous_data(prenoisedet+3),8)==0)
            a2=np.array(prenoisedet)
            c2=[]
            for m in range(0,len(a2)):
                c2.append(a2[m]+2)
            target2=list(previous_data[c2])
            dup2=[]
            for k in range(0,len(target2)):
                dup2.append(int(int2str(target2[k])[32-8]))
            
            b2=[]
            for i in range(0,len(dup2)):
                if(dup2[i]==0):
                    b2.append(i)
            predet=list(a2[b2])
            print 'predet'
            print len(predet)
            if not det:
                ecglocation=preecglocation
                # arr0=predet(bitget(previous_data(predet+3),7)==0)
                a3=np.array(predet)
                c3=[]
                for m in range(0,len(a3)):
                    c3.append(a3[m]+2)
                target3=list(previous_data[c3])
                dup3=[]
                for k in range(0,len(target3)):
                    dup3.append(int(int2str(target3[k])[32-7]))
            
                b3=[]
                for i in range(0,len(dup3)):
                    if(dup3[i]==0):
                        b3.append(i)
                arr0=list(a3[b3])
                # arr=predet(bitget(previous_data(predet+3),7)==1)
                a4=np.array(predet)
                c4=[]
                for m in range(0,len(a4)):
                    c4.append(a4[m]+2)
                target4=list(previous_data[c4])
                dup4=[]
                for k in range(0,len(target4)):
                    dup4.append(int(int2str(target4[k])[32-7]))
            
                b4=[]
                for i in range(0,len(dup4)):
                    if(dup4[i]==1):
                        b4.append(i)
                arr=list(a4[b4])

                previousflag=1
            else:
                # arr0=det(bitget(data(det+3),7)==0)
                a5=np.array(det)
                c5=[]
                for m in range(0,len(a5)):
                    c5.append(a5[m]+2)
                target5=list(data[c5])
                dup5=[]
                for k in range(0,len(target5)):
                    dup5.append(int(int2str(target5[k])[32-7]))
            
                b5=[]
                for i in range(0,len(dup5)):
                    if(dup5[i]==0):
                        b5.append(i)
                arr0=list(a5[b5])
                print 'arr0'
                print len(arr0)
                # arr=det(bitget(data(det+3),7)==1)
                a6=np.array(det)
                c6=[]
                for m in range(0,len(a6)):
                    c6.append(a6[m]+2)
                target6=list(data[c6])
                dup6=[]
                for k in range(0,len(target6)):
                    dup6.append(int(int2str(target6[k])[32-7]))
            
                b6=[]
                for i in range(0,len(dup6)):
                    if(dup6[i]==1):
                        b6.append(i)
                arr=list(a6[b6])
                print 'arr'
                print len(arr)
            # find(arr0<firstshock,1,'last')
            p=len(arr0)-1
            while(p>=0):
                if(arr0[p]<firstshock):
                    break
                p=p-1
            if (not arr0)or (p==-1):
                # arr0=predet(bitget(previous_data(predet+3),7)==0)
                a7=np.array(predet)
                c7=[]
                for m in range(0,len(a7)):
                    c7.append(a7[m]+2)
                target7=list(previous_data[c7])
                dup7=[]
                for k in range(0,len(target7)):
                    dup7.append(int(int2str(target7[k])[32-7]))
                
                b7=[]
                for i in range(0,len(dup7)):
                    if(dup7[i]==0):
                        b7.append(i)
                arr0=list(a7[b7])
                # arr=predet(bitget(previous_data(predet+3),7)==1)
                a8=np.array(predet)
                c8=[]
                for m in range(0,len(a8)):
                    c8.append(a8[m]+2)
                target8=list(previous_data[c8])
                dup8=[]
                for k in range(0,len(target8)):
                    dup8.append(int(int2str(target8[k])[32-7]))
            
                b8=[]
                for i in range(0,len(dup8)):
                    if(dup8[i]==1):
                        b8.append(i)
                arr=list(a8[b8])
            
                lastarr0=arr0[len(arr0)-1]
                # lastarr=arr(find(arr>lastarr0,1,'first'))
                lastarr=[]
                for p in range(0,len(arr)):
                    if(arr[p]>lastarr0):
                        break
                    p=p+1
                print 'p'
                print p
                print 'length of arr'
                print len(arr)
                if(p!=len(arr)):
                    lastarr=arr[p-1]
                ecglocation1=preecglocation
                previousflag=1
                if lastarr==[]:
                    #arr=det(bitget(data(det+3),7)==1)
                    a9=np.array(det)
                    c9=[]
                    for m in range(0,len(a9)):
                        c9.append(a9[m]+2)
                    target9=list(data[c9])
                    dup9=[]
                    for k in range(0,len(target9)):
                        dup.append(int(int2str(target9[k])[32-7]))
            
                    b9=[]
                    for i in range(0,len(dup9)):
                        if(dup9[i]==1):
                            b9.append(i)
                    arr=list(a9[b9])
                    
                    lastarr=arr[0]
                    previousflag=0
                    ecglocation1=ecglocation
                ecglocation=ecglocation1
            else:
                # lastarr0=arr0(find(arr0<firstshock,1,'last'))
                # lastarr=arr(find(arr>lastarr0,1,'first'))
                p=len(arr0)-1
                q=0
                lastarr0=[]
                lastarr=[]
                while(p>=0):
                    if(arr0[p]<firstshock):
                        break
                    p=p-1
                if(p!=0):
                    lastarr0=arr0[p]
                print 'lastarr0'
                print lastarr0
                while(q<len(arr)):
                    if(arr[q]>lastarr0):
                        break
                    q=q+1
                if(q!=len(arr)):
                    lastarr=arr[q]
                print 'lastarr'
                print lastarr
            # beforeecg=find(ecglocation<lastarr,1,'last')
            p=len(ecglocation)-1
            beforeecg=[]
            while(p>=0):
                if(ecglocation[p]<lastarr):
                    break
                p=p-1
            if(p!=0):
                beforeecg=p+1
            if not beforeecg:
                beforeecg=len(preecglocation)
                previousflag=1
            print 'beforeecg'
            print beforeecg
            # find start ecg which is Shock Start Shift before arrhythmia and
            # find the last gain before that ecg
            if previousflag==0:
                startecg=beforeecg-extractlimit
                if startecg<=0:
                    startecg=len(preecglocation)-(extractlimit-beforeecg)
                    if startecg<0:
                        startecg=0
                    if(startecg!=0):
                        startpacket=preecglocation[startecg-1]
                        # lastgain=pregainlocation(find(pregainlocation<startpacket,1,'last'))
                        lastgain=[]
                        p=len(pregainlocation)-1
                        while(p>=0):
                            if(pregainlocation[p]<startpacket):
                                break
                            p=p-1
                        if(p!=-1):
                            lastgain=pregainlocation[p]
                            
                        gain=previous_data[lastgain-1:lastgain+4]
                        previousflag=1
                    else:
                        startpacket=ecglocation[0]
                        # lastgain=gainlocation(find(gainlocation<startpacket,1,'last'))
                        lastgain=[]
                        p=len(gainlocation)-1
                        while(p>=0):
                            if(gainlocation(p)<startpacket):
                                break
                            p=p-1
                        lastgain=gainlocation[p]
                        gain=data[lastgain-1:lastgain+4]
                else:
                    print 'startecg'
                    print startecg
                    print 'length of ecglocation'
                    print len(ecglocation)
                    startpacket=ecglocation[startecg-1]
                    # lastgain=gainlocation(find(gainlocation<startpacket,1,'last')) 
                    lastgain=[]
                    p=len(gainlocation)-1
                    while(p>=0):
                        if(gainlocation[p]<startpacket):
                            break
                        p=p-1
                    if(p!=-1):
                        lastgain=gainlocation[p]
                    gain=data[lastgain-1:lastgain+4]
                    if gain==[]:
                        lastgain=pregainlocation[len(pregainlocation)-1]
                        gain=previous_data[lastgain-1:lastgain+4]
            else:
                
                startecg=beforeecg-extractlimit
                startpacket=preecglocation[startecg-1]
                # lastgain=find(pregainlocation<startpacket,1,'last')
                p=len(pregainlocation)-1
                lastgain=[]
                while(p>=0):
                    if(pregainlocation[p]<startpacket):
                        break
                    p=p-1
                if(p!=-1):
                    lastgain=p
                gain=previous_data[lastgain-1:lastgain+4]
            # save ECG
            ShockPeriodECG=gain
            N=len(ShockPeriodECG)
            if(previousflag==1):
                mm=previous_data[startpacket-1:end]
                ShockPeriodECG=np.append(ShockPeriodECG,mm)
                #ShockPeriodECG[N-1:N+len(previous_data[startpacket-1:end])]=previous_data[startpacket-1:end]
                startpacket=ecglocation[0]
            #clear N
            N=len(ShockPeriodECG)
            #if(nextflag==0):
            mm=data[startpacket-1:stoppacket]
            ShockPeriodECG=np.append(ShockPeriodECG,mm)
            #ShockPeriodECG[N:N+len(data[startpacket-1:stoppacket])]=data[startpacket-1:stoppacket]
            #else:
            #ShockPeriodECG[N:N+len(data[startpacket-1:stoppacket])]=data[startpacket-1:stoppacket]
            #clear N
        if(offset!=0):
            previous_data=data
        shocklocation=[]
        previousflag=0
        fileevent=0
        offset=offset+45000000
    print len(ShockPeriodECG)
   
    #ECG2MAT(ShockPeriodECG)
    #fid=open('C:/Users/JDang/Desktop/ATS/code/ECGtoATS/version4.0/temp.ecg','w')
    #fid.write(ShockPeriodECG)
    #fid.close()
   
    def int2str(i):
            str = ""
            flag = -1
            while i>0 or flag==-1:
                if(i%2 == 1):
                    flag = -1
                    str="1"+str
                else:
                    str="0"+str
                    flag = 0
                i = i/2
            if(flag==-1):
                str = "1"+str
            return str.zfill(32)
    #fid=open('C:/Users/JDang/Desktop/ATS/code/ECGtoATS/version4.0/temp.ecg','rb')
    #ShockPeriodECG=bytearray(fid.read())
    #print len(ShockPeriodECG)
    offset=0
    repeat=200000
    ending=1000000
    
    # gain lookup table
    GAIN_TABLE=[7,8,9,10,12,13,15,16,18,21,23,26,29,33,37,41,46,52,58,65,73,82,92,103,115,130,145,163,183,205,230,259,290,325,365,410,460,516,579,649,729,818,917,1029,1155,1296,1454,1631,1830,2054,2304,2585,2901]
    # Initilaize
    
    
    file_size=len(ShockPeriodECG)
    KK=file_size/5
    ecgNum=0
    # ecg
    ss_gain=1
    fb_gain=1
    ss_ecg=np.zeros((KK))
    ss_ecg=np.int16(ss_ecg)
    fb_ecg=np.zeros((KK))
    fb_ecg=np.int16(fb_ecg)
    # flags
    previousflag=0
    event=0
    eventlocation=[]
    # detection/arrhythmia
    detectionflag=0
    treatablearr=0
    arrhythmia=np.zeros((KK))
    arrhythmia=np.uint8(arrhythmia)
    i=0
    fid=open('C:/Users/JDang/Desktop/wenjian.txt','a')
    while(i<=file_size-5):
        id=(ShockPeriodECG[i])
        if id==0:   # ecg sample
            ecgNum=ecgNum+1
            # arrhythmia
            arrhythmia[ecgNum-1]=detectionflag and treatablearr
            #print "arrhythmia added"
            # ecg
            tmp1=np.int16(round((np.int8(ShockPeriodECG[i+2])*256+ShockPeriodECG[i+1])*ss_gain))
            #print 'ShockPeriodECG[i+1]'
            #print ShockPeriodECG[i+1]
            #print 'ShockPeriodECG[i+2]'
            #print ShockPeriodECG[i+2]
            #print 'tmp1'
            #print tmp1
            ss_ecg[ecgNum-1]=tmp1
            #print "ss_ecg added"
            fid.write(str(tmp1))
            fid.write('-')
            tmp2=np.int16(round((np.int8(ShockPeriodECG[i+4])*256+ShockPeriodECG[i+3])*fb_gain))
            fb_ecg[ecgNum-1]=tmp2
            #print "fb_ecg added"
        if id==1:   # gain setting
            ss_gain=(143.27/(GAIN_TABLE[np.int8(ShockPeriodECG[i+1])-1+31]))
            print 'ss_gain'
            print ss_gain
            fb_gain=(143.27/(GAIN_TABLE[np.int8(ShockPeriodECG[i+2])-1+31]))
        if id==2:
            # shock
            if np.uint8(ShockPeriodECG[i+3])==17:
                if(np.uint8(ShockPeriodECG[i+3-5])==17 or
                   np.uint8(ShockPeriodECG[i+3-10])==17):
                    event+=1
                    eventlocation.append(ecgNum)
                    #print "eventlocation added"
        if id==3:
            # if bitget(noisedata(k).payload(1,3),8)==0
            a1=np.uint8(ShockPeriodECG[i+3])
            a2=int(int2str(a1)[32-8])
            if a2==0:
                
                detectionflag=1
                if int(int2str(a1)[32-7])==1:
                    
                    treatablearr=1
                else:
                    
                    treatablearr=0
   
        i+=5
    print 'ss_ecg'
    print len(ss_ecg)
    print 'fb_ecg'
    print len(fb_ecg)
    print 'eventlocation'
    print eventlocation
    print 'arrhythmia'
    print len(arrhythmia)
    fid.close()
    return [ss_ecg,fb_ecg,eventlocation,arrhythmia]
