#test of final version of analysis fcns put into OpenAndPlot

#Task List
#Group: Import, Class Analysis Tool

class LCAnalysis:
    #imports needed for class
    import lightkurve as lk
    import numpy as np
    import pandas as pd

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

     #Start of Class Analysis Functions

    def BLS(self,pN=1000,dN=10):
       # from astropy import units as u
       from astropy.timeseries import BoxLeastSquares
       import numpy as np
       '''
       Purppose
       ------------------
       A Box Least Squares function to print out the compute stats of the periodogram.
       Parameters
       -------------------
       period grid            - describes how often the transit is happening (arrays different value)
       duration grid          - describes the width of the transit (array of different values)
       lightcurve             - lightkurve class object
       Return
       list of stats in the following the order: period, duration, transit-time, power, depth
       ------------------
       Calculate several statistics of a candidate transit.
       '''
       #assigning parameters to variables
       period =  self.periods(pN)
       duration = self.duration_grid(dN)
       flat_lc, flat_time = self.flatten()
       #t = timestamps
       #y = observations
       t = flat_time #lc.time #time
       y = flat_lc.flux #flux
       #dy is the uncertianty
       model = BoxLeastSquares(t, y, dy= flat_lc.flux_err)
       periodogram = model.power(period,duration)
       max_power = np.argmax(periodogram.power)
       #calculates the max stats w/in the transit
       stats = [periodogram.period[max_power],
                            periodogram.duration[max_power],
                            periodogram.transit_time[max_power],
                            max_power,periodogram.depth[max_power]]
       #stats is the one peak, periodogram is the areay
       return stats

    def periods(self, pN=1000):
        import numpy as np
        period=np.logspace(-0.523, 1.43, pN, endpoint=True)
        return period

    def duration_grid(self, dN=10):
        import numpy as np
        duration=np.linspace(.01, 0.298, dN)
        return duration

    def folded(self,period):
        flat_lc, flat_time = self.flatten()
        folded = flat_lc.fold(period=period)
        return folded.scatter()

    def flatten(self):
       lk_lc = self.open_clean_lc()
       lc_flat = lk_lc.flatten()
       flat_time = lc_flat.time - lc_flat.time[0]
       return lc_flat, flat_time

    #open_cleaned_lc: ticid,sector
    def open_clean_lc(self):
        import lightkurve as lk
        try:
            lc_file = lk.open('/content/gdrive/My Drive/EscapeEarthData/Sec{}_cleaned/{}/lc.fits'.format(self.sector, self.targetid))
            lc = lc_file.FLUX
            return lc
        except FileNotFoundError:
            lc = "None"
            return lc
