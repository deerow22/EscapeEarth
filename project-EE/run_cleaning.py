#imports
import cleaning_modules as cm
import os


#BE SURE TO CHOOSE OR AMEND THE 'rawdatapath' & 'filename_danielle' paths for your computer!! 

# our inputs
tic_list = [7582594, 7582633, 7620704, 7618785, 7584049]
sectornumber = 14
rawdatapath = '/Users/helenfellow/Desktop/sec14_rawdata_subsample/'
rawdatapath_danielle = '/Users/helenfellow/Desktop/sec14_rawdata_subsample/'

cleandata, cleanticids = cm.Dataclean(tic_list,sectornumber,rawdatapath)

#data = cleaned data as a lightkurve class object

for count, i in enumerate(cleanticids):
    tic = i
    data = cleandata[count]
    filename_danielle = '/Users/helenfellow/Desktop/Internship/{}/lc.fits'.format(tic)
    filename_maria= '/Users/helenfellow/Desktop/Internship/EscapeEarth/{}/lc.fits'.format(tic)
    filename_elise = '~/Desktop/Internship/EscapeEarth/{}/lc.fits'.format(tic)
    filename_olivia = '~/Desktop/Brown Scholars/Internship/EscapeEarth/{}/lc.fits'.format(tic)
    filename_sarah = '~/Desktop/AMNH/BridgeUp Internship/Internship/EscapeEarth/{}/lc.fits'.format(tic)
    filename_anna_claire = '~/Desktop/Internship/EscapeEarth/{}/lc.fits'.format(tic)
    filename_eliza = '~/Desktop/Internship/EscapeEarth/{}/lc.fits'.format(tic)
#commentout
    os.makedirs(os.path.dirname(filename_danielle), exist_ok=True) #verify/make folder with tic_id as the name
    data.to_fits(filename_danielle,flux_column_name = 'flux',overwrite=True);
