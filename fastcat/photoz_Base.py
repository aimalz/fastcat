#
# Basic (None) photo-z object
#
import numpy as np

class PhotoZBase(object):
    """
    Basic object for describing PhotoZ error distribution.
    
    Eventually we'll probably need at least two methods to 
    work out best universal interface (one via full P(z), other via
    some sort "PZ bin")

    Base object corresponds to perfectly known PZ.

    """
    def __init__(self):
        self.type="base"

    def writeH5 (self,dataset):
        dataset.attrs['type']=self.type

    @staticmethod
    def readH5 (dataset):
        """ Tries to read from H5.
            If not matched, return None
        """
        if dataset.attrs['type']=="base":
            return PhotoZBase()
        else:
            return None

    def applyPhotoZ (self,arr):
        """ nothing to do for base class"""
        pass
        return arr

    def getMeanRMS (self,arr):
        """ Returns mean and sqrt variance for 
            the photoz pDF, given array
            Note that for assymetric PZ, you are at your
            own risk.
        """
        # in base class we return redshift and zero varinace.
        N=len(arr)
        return arr["z"],np.zeros(N)

    def getMinMax(self,arr):
        """ Returns range of redshifts where p(z) is considerable, i.e.
        no real probability at z<zmin or z>zmax.
        Note that in case of catastrophic outliers, one can have considerable
        amounts of zeros in this range
        """
        return arr["z"], arr["z"]

    def PofZ(self,arr,z,dz):
        """ Returns probability of PZ be at z +-dz/2"""
        N=len(arr)
        P=zeros(N)
        dzo2=dz/2
        P[np.where(abs(arr["z"]-z)<dzo2)]=1.0
        return P
    
    def cPofZ(self,arr,zx):
        """ Returns cumulative probability of PZ be at z<zx"""
        N=len(arr)
        cP=zeros(N)
        cP[np.where(arr["z"]<zx)]=1.0
        return cP
    
    def NameString(self):
        return "TrueZ"
    