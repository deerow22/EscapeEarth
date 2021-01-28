# Danielle
# Elise
# Anna-Claire
# Olivia
# Eliza

import pandas as pd
import lightkurve as lk


## The actual function
def dl_data(target_list, sector, savepath):
  """
  ~Purpose~
  REQUIREMENTS: pandas; lightkurve
  Args:
       target_list  -(list or array) list of TIC ID numbers
       sector       -(int) desired sector to download from
       savepath    -(str) path to save data to
  Returns:
       nothing, but saves files to savepath location
       """
  for count, id in enumerate(target_list):
    print('Starting {} out of {}'.format(count, len(target_list)))
    #format target name
    ticid = 'TIC {}'.format(id)
    #find file
    lc_search = lk.search_lightcurvefile(ticid, sector=sector)
    #download data
    print('downloading data...')
    lc_file = lc_search.download()

    #check for user input formatting
    if savepath[-1]=='/':
      savepath = savepath
    else:
      savepath = savepath + '/'
    # format unique file name for saving
    filename = 'FINAL_tic{}_sec{}'.format(id,sector)
    savefilepath = savepath + filename
    # convert class object from file to light curve
    lc = lc_file.PDCSAP_FLUX
    # save data
    print('saving data...')
    lc.to_fits(path='{}.fits'.format(savefilepath), overwrite=True)



## user input data

mytargets = [7582594, 7582633, 7582634, 7583285, 7584049]
mysavepath = 'Internship/'
sector = 14

dl_data(mytargets, sector, mysavepath)
