import numpy as np
import pandas as pd

def cleanse_nas(cert):
    
    # replace 'NO DATA!', 'not defined' and 'not recored' with null
    cert = cert.replace(['NO DATA!','NODATA!','not recorded','not defined','unknown',
                         'Unknown','Not defined','Not recorded','N/A','n/a','INVALID!'],np.nan)

    # replace any values starting sap as these are the column headers not real data
    cert = cert.replace([r'^SAP.*',r'^sap.*'],np.nan,regex=True)

    # replace '+ Chr(13) +' as it's meaningless
    cert = cert.replace([r"\+ Chr\(13\) \+",r"\+ chr\(13\) \+"],'+', regex=True)

    # replacing values in columns which are actually just the column header
    replacement_dict = {
        'hotwater_description':{r'^Hot-Water$':np.nan},
        'floor_description':{r'^Floor$':np.nan},
        'walls_description':{r'^Wall$':np.nan},
        'windows_description':{r'^Window$':np.nan},
        'roof_description':{r'^Roof$':np.nan},
        'main_heating_controls':{r'^Main-Heating-Controls$':np.nan},
        'secondheat_description':{r'^Secondary-Heating$':np.nan},
        'lighting_description':{r'^Lighting$':np.nan},
        'mainheatcont_description':{r'^Main-Heating-Controls$':np.nan}}

    cert = cert.replace(replacement_dict,regex=True)
    
    print('Finished cleansing NAs')
    
    return cert


