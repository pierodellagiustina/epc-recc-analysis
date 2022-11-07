## Notes

#### Vars to include *baseline*
'property_type', 
'built_form', 
'total_floor_area', 
'energy_tariff', 
'mains_gas_flag',
'floor_level_numeric',
'floor_level_classes',
'flat_top_storey',
'flat_storey_count',
'multi_glaze_proportion', #doubt we will be able to get this from user!
'glazed_type',
'glazed_area', #doubt we will be able to get this from user!
'extension_count',
'number_habitable_rooms', #A! check this and the following - likely to be highly correlated
'number_heated_rooms',
'low_energy_lighting', #A! check this and the following - likely to be highly correlated
'low_energy_lighting_perc', #this is a derived var
'number_open_fireplaces', #doubt we will be able to get this from user!
'hotwater_mains', #derived from the hotwater description - domain driven 
'hotwater_immersion',
'hotwater_commmunity',
'hotwater_solar',
'hotwater_gas',
'hotwater_recovery',
'hot_water_energy_eff', #doubt we will be able to get this from user!
'hot_water_env_eff', #consider dropping - highly correlated
'windows_description',
'pitched_roof',
'flat_roof',
'mainheat_description',
'mainheatcont_description', #doubt they will be able to provide this!
'main_fuel', #doubt they will know 
'wind_turbine_flag',
'heat_loss_corridor', # need to see if they know 
'floor_height',
'solar_water_heating_flag',
'mechanical_ventilation', # ?
'construction_age_band',
'tenure'


#### Left out - to reconsider
- All costs variables (lighting, heting, hot water etc.). Try to understand how they are calculated and if they can be derived from bills - if so they can be input by user
- 'main_heating_controls'
- 'floor_desctiption','floor_energy_eff','floor_env_eff'
- 'windows_energy_eff', 'windows_env_eff'
- 'walls_description', 'walls_energy_eff', 'walls_env_eff'
- 'sheating_energy_eff', 'sheating_env_eff'
- roof_description','roof_energy_eff', 'roof_env_eff'
For all the above maybe possible to ask IF user knows
- 'mainheat_energy_eff', 'mainheat_env_eff'
- 'mainheatc_energy_eff', 'mainheatc_env_eff'
- 'lighting_energy_eff','lighting_env_eff'
- 'unheated_corridor_length'
- 'fixed_lighting_outlets_count', 'low_energy_fixed_light_count'
- 'floors_average_thermal_transmittance'
- 'secondheat_description' #this could actually be known
- 'lighting_description' #too detailed
- 'roof_average_thermal_transmittance'
- 'walls_average_thermal_transmittance'
- 'main_heating_controls' #leaving it out for now because do not know how to treat the many levels

- ANY INFORMATION TO DO WITH GEOGRAPHY HAS BEEN LEFT OUT FOR NOW!!!!



#### Analysis plan
- set up AOC per class
- add other vars *likely to have*
- deal with geography - need to add other regions in training set
- delete vars *unlikely to have*
- reduce classes (some can be grouped?)

#### Vars notes
What is not included below should be fine to keep (ppl should know)
- `multi_glaze_proportion`, unlikely to have but should have enough other variables to learn from?
- `low_energy_lighting_perc`, maybe just yes/no flag? Maybe 0-0.5-1?
- `hotwater` categories, very important
- `wind_turbine_flag`, to consider depending on geographies
- `energy_tariff`
- `floor_level_classes`, see how we want to deal with floor level
- `glazed_area`, just remove
- `hot_water_energy_eff` and `hot_water_env_eff`, highly predictive - be careful w removing
- `window_description`, low importance atm, but see later
- `mainheat_description`, some of these classes are important, maybe see how they can be passed?
- `mainheatcont_description`, same as above
- `main_fuel`, maybe can be simplified and retain only the stuff that matters? eg, gas/electricity, community/private?
- `heat_loss_corridor`, seems to be quite important for some classes
