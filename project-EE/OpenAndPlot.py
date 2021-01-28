#Danielle is here AGAIN
#Elise is here
#Olivia is here a G a I n
#Sarah is here again
#Eliza is here
#Eliza is here again
#Anna-Claire is here a g a i n
#Maria is here !:) Hello people :)



import lightkurve as lk
import numpy as np
import pandas as pd
import glob



class OpenAndPlot:
    def __init__(self,data):
        self.telescope = 'TESS'

        if type(data)==list:
            if len(data)==2:
                self.targetid = data[0]
                self.sector = data[1]
            else:
                print('List should have 2 values: [ticid, sector]')
        else:
            print('Please format data as follows: [ticid,sector]')
# 		return

    def __repr__(self):
#         str_name = str(self.targetid)
        return "TIC: {}".format(self.targetid)


##functions we'll be adding
#plot_cleaned_lc: ticid, sector
    def plot_cleaned_lc(self):
        '''
        DESCRIPTION
        Scatter plot one cleaned ticid from sectors 14 or 15
        INPUTS
        ticid    -(int)TESS TIC ID
        sector   -(int)the region of oberservation
        OUTPUT
        Plots lightcurve of specified TIC ID
        '''
        lc = self.open_lc(stage='clean')
        try:
            plot = lc.scatter()
        except AttributeError:
            plot = "No data or check sector value"
            pass
        return plot
#open_lc: ticid,sector,stage
    def open_lc(self,stage):
        if stage == 'raw':
            return self.open_raw_lc()
        elif stage == 'clean':
            return self.open_clean_lc()
        else:
            return print('stage parameter not understood; valid entries include: "raw" or "clean"')

#open_raw_lc: ticid,sector
    def open_raw_lc(self):
        try:
            filename = glob.glob('/content/gdrive/My Drive/EscapeEarthData/Sector_{}_rawdata/*{}-*-s_lc.fits'.format(self.sector,self.targetid))
            lc_file = lk.open(filename[0])
            lc = lc_file.PDCSAP_FLUX
        except IndexError:
            lc = "None"
            pass
        return lc

#open_cleaned_lc: ticid,sector
    def open_clean_lc(self):
        try:
            lc_file = lk.open('/content/gdrive/My Drive/EscapeEarthData/Sec{}_cleaned/{}/lc.fits'.format(self.sector, self.targetid))
            lc = lc_file.FLUX
            return lc
        except FileNotFoundError:
            lc = "None"
            return lc



#plot_raw_data: ticid,sector
    def plot_raw_data(self):
        try:
            filename = glob.glob('/content/gdrive/My Drive/EscapeEarthData/Sector_{}_rawdata/*{}-*-s_lc.fits'.format(self.sector, self.targetid))
            lc_file = lk.open(filename[0])
            lc = lc_file.PDCSAP_FLUX
        except IndexError:
            lc = "None"
            pass
        return lc.plot()

