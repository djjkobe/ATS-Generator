def getflagbits(x):
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
    bit0=int2str(x)[len(int2str(x))-1]
    bit1=int2str(x)[len(int2str(x))-2]
    bit2=int2str(x)[len(int2str(x))-3]
    bit3=int2str(x)[len(int2str(x))-4]
    bit4=int2str(x)[len(int2str(x))-5]
    bit5=int2str(x)[len(int2str(x))-6]
    bit6=int2str(x)[len(int2str(x))-7]
    bit7=int2str(x)[len(int2str(x))-8]
    bit8=int2str(x)[len(int2str(x))-9]
    bit9=int2str(x)[len(int2str(x))-10]
    bit10=int2str(x)[len(int2str(x))-11]
    bit11=int2str(x)[len(int2str(x))-12]
    bit12=int2str(x)[len(int2str(x))-13]
    bit13=int2str(x)[len(int2str(x))-14]
    bit14=int2str(x)[len(int2str(x))-15]
    bit15=int2str(x)[len(int2str(x))-16]
    bit16=int2str(x)[len(int2str(x))-17]
    bit17=int2str(x)[len(int2str(x))-18]
    bit18=int2str(x)[len(int2str(x))-19]
    bit19=int2str(x)[len(int2str(x))-20]
    bit20=int2str(x)[len(int2str(x))-21]
    bit21=int2str(x)[len(int2str(x))-22]
    bit22=int2str(x)[len(int2str(x))-23]
    bit23=int2str(x)[len(int2str(x))-24]
    bits=[bit0,bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8,bit9,bit10,bit11,bit12,bit13,bit14,bit15,bit16,bit17,bit18,bit19,bit20,bit21,bit22,bit23]
    return bits
