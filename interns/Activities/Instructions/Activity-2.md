# Activity-2: Data Interpretation through visualization

__Instructions:__ There are some files, each containing a dataframe, inside our google drive "EscapeEarthData/Activity-2". 
1. I want you to open the data and plot it. See if you can interpret the images yet. Plot them individually and together on one plot. 
2. Then you should transform each dataframe's arrays using the code below. Plot the transformed data and try to interpret what you are seeing. 
Are there any trends? Are there sharp edges or a lot of scatter? Is there overlap? Let's discuss.



__Code:__

you should have already opened df1 - this code is only for one dataframe at a time, revise for other dfs as needed (ie change variable names "df1"-->"df2" everywhere below)


```
import astropy
from astropy.coordinates import SkyCoord

c_old = SkyCoord([df1['col1'].to_numpy()], [df1['col2'].to_numpy()], frame='icrs',unit='degree') #replace df1 if your variable names are different 
c_new = c_old.galactic
for count in range(len(c_new[0])):
        df1_new_col1 = c_new[0].l.degree
        df1_new_col2 = c_new[0].b.degree
new_data = {'col1':df1_new_col1,'col2':df1_new_col2}
df1_new = pd.DataFrame(new_data)
```


use the `df1_new` as your data now
