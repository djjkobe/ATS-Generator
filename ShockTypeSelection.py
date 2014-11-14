def ShockTypeSelection(MaskID):
    import numpy as np
    from numpy import *
    print("Which catergory the file is?")
    print("catergory 1: true shock")
    print("catergory 2: false shock")
    choice=input("Please select type\n")
    if(choice==1):                                              # true shock
        ShockType=Category()
        ShockType.type='trueshock'
        # get shock record from database
        record=Record()
        record=Get_Shock_Reason(ShockType.type)
        #print record
        a=record.RealID
        for i in range(0,len(a)):
            if(a[i]==Get_WCD_ID(MaskID)):
                break
        subtype=record.ShockReason[i]
        #subtype=record.ShockReason(find(record.RealID==Get_WCD_ID(MaskID),1))
      
        if not subtype:
            shockID = np.zeros((1,len(record.realID)))
            for i in range(0,len(record.RealID)):
                shockID[i]=Get_MASK_ID(record.RealID[i])

            a=shockID
            for i in range(0,len(a)):
                if(a[i]==MaskID):
                    break
            subtype=record.ShockReason[i]
            #subtype=record.ShockReason(find(shockID==MaskID,1))
        
        if not subtype:
            ShockType.subtype='unclassified'
            ShockType.preShockRhythem='unclassified'
        elif (subtype=='VT->VF') | (subtype=='VT -> VF') | (subtype=='VT-> VF')| (subtype=='VT-VF') | (subtype=='VT->VFVT->VF'):
            ShockType.subtype='VTtoVF'
            ShockType.preShockRhythem=subtype
        elif (subtype=='PMVT->VF') | (subtype=='Polymorphic VT->VF')| (subtype=='PolymorphicVT->VF') | (subtype=='PolyVT->VF'):
            ShockType.subtype='VTtoVF'
            ShockType.preShockRhythem=subtype
        elif (subtype=='VT,NSVT->fine VF') | (subtype=='VT(Torsades)->VF') | (subtype=='VT w/torsades->VF')| (subtype=='VT->torsades->VF'):
            ShockType.subtype='VTtoVF'
            ShockType.preShockRhythem=subtype
        elif (subtype[len(subtype)-2:len(subtype)]=='VT') | (subtype[len(subtype)-2:len(subtype)]=='vt'):
            ShockType.subtype='VT'      
            ShockType.preShockRhythem=subtype
        elif (subtype[len(subtype[0])-2:len(subtype[0])]=='VF') | (subtype[0][len(subtype[0])-2:len(subtype[0])]=='vf'):
            ShockType.subtype='VF'
            ShockType.preShockRhythem=subtype
        else:
            ShockType.subtype='else'
            ShockType.preShockRhythem=subtype
    
    if(choice==2):                                              # false shock
        ShockType=Category()
        ShockType.type='falseshock'
        record=Get_Shock_Reason(ShockType.type)
        a=record.RealID
        b=Get_WCD_ID(MaskID)
        for i in range(0,len(a)):
            if(a[i]==b):
                break
        subtype=record.ShockReason[i]
        #print subtype
        if  not subtype:
            shockID = np.zeros((1,len(record.realID)))
            #print record.RealID[0]
            for i in range(0,len(record.RealID)):
                q=Get_MASK_ID(record.RealID[i])
                shockID[i]=q
            a=shockID
            for i in range(0,len(shockID)):
                if(a[i]==MaskID):
                    break
            subtype=record.ShockReason[i]
            #subtype=record.ShockReason(find(shockID==MaskID,1))
        if  not subtype:
            ShockType.subtype='unclassified'
            ShockType.PrimaryReason='unclassified'
        elif (subtype==1) | (subtype==2) | (subtype==3) | (subtype==4) | (subtype==12):
            ShockType.subtype='noise'
            ShockType.PrimaryReason=subtype
        elif (subtype==5) | (subtype==7):
            ShockType.subtype='multiple counting'
            ShockType.PrimaryReason=subtype
        elif (subtype==8) | (subtype==9):
            ShockType.subtype='NSVT'
            ShockType.PrimaryReason=subtype
        elif (subtype==6):
            ShockType.subtype='SVT'
            ShockType.PrimaryReason=subtype
        elif (subtype==10) | (subtype==11):
            ShockType.subtype='oversensing'
            ShockType.PrimaryReason=subtype
        else:
            ShockType.subtype='else'
            ShockType.PrimaryReason=subtype

    return ShockType
