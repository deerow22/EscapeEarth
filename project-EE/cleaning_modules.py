# standard imports
import glob
import pandas as pd
import os
import lightkurve as lk



# useful functions
def locate_files(tic,path=None):
    '''
    ~ Locates TESS lightcurve files with filenames formatted from a mast bulk download.~
    REQUIRES: glob
    Args:
        tic            -(int or str)TESS TIC ID
        path           -(str) path on computer to file(s) location
    Returns:
        list of path strings for all files found with specified tic
    '''
    if path == None: #if only need filename
        fullpath = glob.glob('*{}-*-s_lc.fits'.format(tic)) #to use wildcard*
    else: #user defined path to datafile on their computer
        pathstart = path
        pathstart = str(pathstart) #make a string in case user forgets to but think that gives an err anyway
        pathend = pathstart +'*{}-*-s_lc.fits'.format(tic) #s
        #titches path & filename
        fullpath= glob.glob(pathend) #to use wildcard*
    return fullpath


def open_rawdata(fullpath,sector):
    '''
    ~ Opens raw data light curve file objects downloaded to our shared google drive folder~
    REQUIRES: lightkurve as lk
    Args:
        fullpath   -(str) list of path strings for all files found with specified tic
        sector    -(int) sector number for desired data
    Returns:
        lcfs      -(list) list of lightkurve 'lightcurvefile' class objects
    '''
    lcfs = []
    for file in fullpath:
        if len(file)==0:
            print('no files')
        else:
            try:
                lcfile = lk.open(file)
                mystring = str(type(lcfile))
                if mystring[34:-2] == 'TessLightCurveFile':
                    hdr = lcfile.header()
                    mysector = hdr['SECTOR']
                    if sector == mysector:
                        lcfs.append(lcfile)
                    else:
                        pass
                else:
                    pass
            except FileNotFoundError:
                pass
    return lcfs

def Dataclean(TICIDlist,sectornumber,path):
	'''
	~PURPOSE~ cleans data: detrending, removing outliers, and removing NaN Flux
	REQUIRES: lightkurve as lk
		        TICIDlist    -(list) a list of TIC ids
        sectornumber -(int) the number of the sector we are working with
        path         -(str) the path to our raw data

	RETURNS: cleaned_data
	'''
	subsample_tics = TICIDlist
	sector = sectornumber
	raw_data_path = path
	list1 = []
	list2 = []
	for target in subsample_tics:
		#open data
		paths = locate_files(target,raw_data_path)
		original_data = open_rawdata(paths,sector)
		#saveguard against missing files
		if len(original_data)==0: #if no files exist go to next target in for loop
			pass
		else: #if files exist proceed
			#format data (class object type)
			new_data = original_data[0].PDCSAP_FLUX #detrends
			outliers = new_data.remove_outliers(sigma = 3) #removes outliers
			cleaned_data = outliers.remove_nans() #removes NaN Flux
			list1.append(cleaned_data)
			list2.append(target)
	return list1, list2












#one way
#variable = Dataclean(1,2,2)
#print(variable)
#([data1,data2,data3], [tic1,tic2,tic3])

#another anyway
#variable1, variable2 = Dataclean(1,2,3)
#print(variable1)
#[data1,data2,data3]
#print(variable2)
#[tic1,tic2,tic3]
