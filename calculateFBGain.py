def calculateFBGain(gainValue):
    fbGain = gainValue & 0x3f;
    if fbGain >= 32 :
        #print "Negative Gain Found"
        fbGain = -64 + fbGain;
        #print fbGain
    if ((fbGain > 22) | (fbGain < -30)):
        fbGain = 22;
    return fbGain;
