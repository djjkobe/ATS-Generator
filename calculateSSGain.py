def calculateSSGain(gainValue):
    ssGain = gainValue & 0xfc0;
    ssGain >>= 6;
    ssGain = ssGain & 0x3f;
    if ssGain >= 32 :
       ssGain = -64 + ssGain;
    if ((ssGain > 22) | (ssGain< -30)):
        ssGain = 22;
    return ssGain;
