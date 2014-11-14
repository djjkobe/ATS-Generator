def unpackDatFile(outString, size16Ints):
   GAIN_TABLE2 = numpy.array([ 2.04600E-05 , 1.79025E-05 , 1.59133E-05 , 1.43220E-05 , 1.19350E-05 , 1.10169E-05 , 9.54800E-06,
                                8.95125E-06 , 7.95667E-06 , 6.82000E-06 , 6.22696E-06 , 5.50846E-06 , 4.93862E-06 , 4.34000E-06 , 3.87081E-06 , 3.49317E-06 , 
                                3.11348E-06 , 2.75423E-06 , 2.46931E-06 , 2.20338E-06 , 1.96192E-06 , 1.74659E-06 , 1.55674E-06 , 1.39049E-06 , 1.24539E-06 , 
                                1.10169E-06 , 9.87724E-07 , 8.78650E-07 , 7.82623E-07 , 6.98634E-07 , 6.22696E-07 , 5.52973E-07 , 4.93862E-07 , 4.40677E-07 , 
                                3.92384E-07 , 3.49317E-07 , 3.11348E-07 , 2.77558E-07 , 2.47358E-07 , 2.20678E-07 , 1.96461E-07 , 1.75086E-07 , 1.56183E-07 , 
                                1.39184E-07 , 1.24000E-07 , 1.10509E-07 , 9.85007E-08 , 8.78112E-08 , 7.82623E-08 , 6.97274E-08 , 6.21615E-08 , 5.54043E-08 , 
                                4.93692E-08 ]);

   ecgSS = numpy.int16(numpy.zeros( (size16Ints) ));
   ecgFB = numpy.int16(numpy.zeros( (size16Ints) ));
   timeVec = numpy.int16(numpy.zeros( (size16Ints) ));
   ind = 0;
   f=open(outString,'rb')
   for i in range(0,size16Ints):
      ss = unpack('>h',f.read(2))[0]
      fb = unpack('>h',f.read(2))[0]
      gain = unpack('>h',f.read(2))[0]
      #print calculateSSGain(ss)
      ssGain = GAIN_TABLE2[calculateSSGain((gain))+31-1];
      #ssGain = GAIN_TABLE2[numpy.int8(gain)+31-1]
      fbGain = GAIN_TABLE2[calculateFBGain((gain))+31-1];
      #fbGain = GAIN_TABLE2[numpy.int8(gain)+31-1]
      ecgSS[ind] = ss*ssGain*10*10000;
      ecgFB[ind] = fb*fbGain*10*10000;
      timeVec[ind] = ind;
      ind = ind + 1;
   print len(ecgSS)
   print len(ecgFB)
   print len(timeVec)
   print 'done'
   return [ecgSS,ecgFB,timeVec] 
