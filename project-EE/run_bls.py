#https://docs.google.com/presentation/d/1nJR1YiOolG41xITh9mAs61WhhRY_JuTn8uIx49LPm5k/edit#slide=id.p

import matplotlib.pyplot as plt
import numpy as np
import lightkurve as lk
import pandas as pd
import OpenAndPlot as op

def periods(N=1000):
    period=np.logspace(-0.523, 1.43, N, endpoint=True)
    return period

def duration_grid(N=10):
    duration=np.linspace(.01, 0.298, N)
    return duration

def flatten (lc):
    '''
    inputs: cleaned lightkurve data
    output: flattened time and flux data
    function: takes in lightkurve data and flattens the time and flux
    '''
    lc_flat = lc.flatten()
    flat_time = lc_flat.time - lc_flat.time[0]
    return lc_flat, flat_time

def BLS(periodgrid,lightcurve,flat_time,durationgrid):
    from astropy.timeseries import BoxLeastSquares

    '''
    Purppose
    ------------------
    A Box Least Squares function to print out the compute stats of the periodogram.

    Parameters
    -------------------
    period grid            - describes how often the transit is happening (arrays different value)
    duration grid          - describes the width of the transit (array of different values)
    lightcurve             - lightkurve class object

    Returns
    list of stats in the following order: period, duration, transit-time, power, depth
    ------------------
    Calculate several statistics of a candidate transit.
    '''
    #assigning parameters to variables
    period = periodgrid
    duration = durationgrid
    lc = lightcurve

    t = flat_time #time
    y = lc.flux #flux

    #dy is the uncertianty
    model = BoxLeastSquares(t, y, dy= lc.flux_err)
    periodogram = model.power(period,duration)
    max_power = np.argmax(periodogram.power)

    #calculates the max stats w/in the transit
    stats = [periodogram.period[max_power],
            periodogram.duration[max_power],
            periodogram.transit_time[max_power],
            max_power,
            periodogram.depth[max_power]]

    #stats is the one peak, periodogram is the array
    return stats
    
    
    
#########################################################################################

if __name__=="__main__":



    ##############################
    ##############################
    #change sector here
    sector = 15
    main_path = '/Volumes/Seagate-stars/SECTORS'
    ##############################
    ##############################


    #opening target lists
    #different paths have to be added in
    target_path = '{}/Sector_{}/all_targets_S0{}_v1.csv'.format(main_path,sector,sector)


    save_power = '{}/INTERN_RESULTS/bls_powers_sec{}.npy'.format(main_path, sector)
    save_period = '{}/INTERN_RESULTS/bls_periods_sec{}.npy'.format(main_path, sector)
    save_duration = '{}/INTERN_RESULTS/bls_durations_sec{}.npy'.format(main_path, sector)
    save_depth = '{}/INTERN_RESULTS/bls_depths_sec{}.npy'.format(main_path, sector)
    save_transit_time = '{}/INTERN_RESULTS/bls_transit_times_sec{}.npy'.format(main_path, sector)
    save_path = [save_depth,save_duration,save_transit_time,save_period,save_power]

    final_save = '{}/INTERN_RESULTS/bls_statsdf_sec{}.csv'.format(main_path, sector)

    target_list = pd.read_csv(target_path,skiprows=5)
    # target_list15 = pd.read_csv(path15,skiprows=5) #from sector 15
    testing_targets = [ 7582633, 7620704, 7618785, 123 ] #7582594, 7584049 – don't exist

    #period grid
    pg = periods()
    #duration grid
    dg = duration_grid()
    #create a empty list for each stat (period,depth,duration,power,transit_time)
    period = []; depth = []; duration = []; power =[]; transit_time = []; tics = []

    #change targets here
    ##############################
    ##############################
    targets = target_list['TICID'].to_numpy()
    ##############################
    ##############################

    for count,star_id in enumerate(targets):
        print('Starting {} out of {}'.format(count,len(targets)))
        data = [star_id,sector]
        #intialize class
        lc = op.OpenAndPlot(data)
        #open data
        data_path = '/Volumes/Seagate-stars/SECTORS/Sector_{}/Sec{}_cleaned/{}/lc.fits'.format(sector,sector,star_id)
        open_data = lc.open_lc('clean',data_path)
        if open_data != "None": #safeguard against no file found
            #flatten the data
            flat_lc,flat_time = flatten(open_data)
            #run the bls on flattened data
            bls_output = BLS(pg,flat_lc,flat_time,dg)
            #append each of the stats to a separate list
            period.append(bls_output[0]); duration.append(bls_output[1])
            transit_time.append(bls_output[2]); power.append(bls_output[3])
            depth.append(bls_output[4]); tics.append(star_id)
            #save that list
            #np.save()
            my_arr = [depth,duration,transit_time, period, power]
            for i in range(len(save_path)):
                np.save(save_path[i],my_arr[i])
        else:
            pass

    # print(len(period),len(duration),len(depth),len(power),len(transit_time))
    # print(period,duration,depth,depth,power,transit_time)
    #create a dictionary of all the stats
    stats_dict = {'TIC':tics,'Period':period,'Duration':duration,'Transit Time':transit_time, "Power": power,'Depth':depth}
    #use that dictionary to create a pandas dataframe
    stats_df = pd.DataFrame(stats_dict)
    #write that dataframe to a file
    stats_df.to_csv(final_save)

