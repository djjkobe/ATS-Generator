def Connect(ecgSS,ecgFB,ShockPeriod):        #function ECG=Connect(BaselinePeriod,ShockPeriod)  
# This function can connect blaseline period with shock period to form a pre-rhythem -- arhythmia -- post-rhythem ecg
# If only one shock, output will be ECG.samples
# If more than one shock, output will be ECG.samplesA, ECG.samplesB...
    
    
    letter='ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    #baselinelength=len(BaselinePeriod.ecg.ss)
    baselinelength=len(ecgSS)
    print 'length of baseline'
    print len(ecgSS)
    print 'MultipleShock'
    print ShockPeriod.MultipleShock
    if(ShockPeriod.MultipleShock==0):
        currentstart=1
        currentend=baselinelength
        shockperiodlength=len(ShockPeriod.ecg.ss)
        ECG=ECG11()
        ECG.samples=ecg1()
        ECG.samples.ss=[]
        ECG.samples.fb=[]
        ECG.samples.ss[currentstart-1:currentend]=ecgSS
        ECG.samples.fb[currentstart-1:currentend]=ecgFB
        currentstart=currentend+1
        currentend=currentend+shockperiodlength
        print 'start'
        print currentstart-1
        print 'currentend'
        print currentend
        fid=open('C:/Users/JDang/Desktop/wenjian.txt','a');
        fid.write("????????????????????????????\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        ECG.samples.ss[currentstart-1:currentend]=ShockPeriod.ecg.ss
        i=currentstart-1
        while(i<currentend):
            fid.write(str(ECG.samples.ss[i]))
            fid.write('-')
            i=i+1
        fid.close()
        ECG.samples.fb[currentstart-1:currentend]=ShockPeriod.ecg.fb
        currentstart=currentend+1
        currentend=currentend+baselinelength
        ECG.samples.ss[currentstart-1:currentend]=ecgSS
        ECG.samples.fb[currentstart-1:currentend]=ecgFB
        t1=ECG.samples.ss
        t2=ECG.samples.fb
        print 'length of ECG.samples.ss'
        print len(t1)
        print 'length of ECG.samples.fb'
        print len(t2)
        ECG.length=ecg1()
        ECG.length.baseline=len(ecgSS)
        ECG.length.arrhythmia=len(ShockPeriod.ecg.ss)
        print 'ECG.length.arrhythmia'
        print ECG.length.arrhythmia
        ECG.length.arrhythmiaend=ECG.length.baseline+ECG.length.arrhythmia
        ECG.length.total=len(ECG.samples.ss)
    else:
        for i in range(0,ShockPeriod.MultipleShock):
            currentstart=1
            currentend=baselinelength
            tmp1='ecg'+letter[i]
            ecg.ss=ShockPeriod.tmp1.ss
            ecg.fb=ShockPeriod.tmp1.fb
            shockperiodlength=len(ecg.ss)
            tmp='samples'+letter[i]
            ECG.tmp.ss[currentstart-1:currentend]=BaselinePeriod.ecg.ss
            #ECG.(genvarname(['samples' letter(i)])).ss(currentstart:currentend)=BaselinePeriod.ecg.ss
            ECG.tmp.fb[currentstart-1:currentend]=BaselinePeriod.ecg.fb
            #ECG.(genvarname(['samples' letter(i)])).fb(currentstart:currentend)=BaselinePeriod.ecg.fb
            currentstart=currentend+1
            currentend=currentend+shockperiodlength
            ECG.tmp.ss[currentstart-1:currentend]=ecg.ss
            #ECG.(genvarname(['samples' letter(i)])).ss(currentstart:currentend)=ecg.ss
            ECG.tmp.fb[currentstart-1:currentend]=ecg.fb
            #ECG.(genvarname(['samples' letter(i)])).fb(currentstart:currentend)=ecg.fb
            currentstart=currentend+1
            currentend=currentend+baselinelength
            ECG.tmp.ss[currentstart-1:currentend]=BaselinePeriod.ecg.ss
            #ECG.(genvarname(['samples' letter(i)])).ss(currentstart:currentend)=BaselinePeriod.ecg.ss
            ECG.tmp.fb[currentstart-1:currentend]=BaselinePeriod.ecg.fb
            #ECG.(genvarname(['samples' letter(i)])).fb(currentstart:currentend)=BaselinePeriod.ecg.fb
            ECG.tmp.baseline=len(BaselinePeriod.ecg.ss)
            #ECG.(genvarname(['length' letter(i)])).baseline=len(BaselinePeriod.ecg.ss)
            ECG.tmp.arrhythmia=len(ecg.ss)
            #ECG.(genvarname(['length' letter(i)])).arrhythmia=len(ecg.ss)
            ECG.tmp.arrhythmiaend=len(BaselinePeriod.ecg.ss)+len(ecg.ss)
            #ECG.(genvarname(['length' letter(i)])).arrhythmiaend=len(BaselinePeriod.ecg.ss)+len(ecg.ss)
            ECG.tmp.total=len(ECG.tmp.ss)
            #ECG.(genvarname(['length' letter(i)])).total=len(ECG.(genvarname(['samples' letter(i)])).ss)
    return ECG
    print('Finish connect pre-rhythem arrhythmia post-rhythem.')
