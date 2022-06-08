def main(path, filename):
    # path to where your .csv lives, and the name of the csv.
    import numpy as np
    import geopy
    from geopy.geocoders import ArcGIS
    import pandas as pd

    Target_Addresses = pd.read_csv(path+'\\'+filename)
    Target_Addresses['Lat'] = np.nan
    Target_Addresses['Long'] = np.nan
    Indexed_Targets = Target_Addresses.set_index('UniqueID')

    geolocator = ArcGIS() #some parameters here
    Fails = []
    for index, row in Indexed_Targets.iterrows():
        Address = row['Address']
        Result = geolocator.geocode(Address)
        if Result == None:
            Result = geolocator.geocode(Address[:-7])
            if Result == None:
                Fails.append[Address]
            else:
                Indexed_Targets.set_value(index, 'Lat', Result.latitude)
                Indexed_Targets.set_value(index, 'Long', Result.longitude)
        else:
            Indexed_Targets.set_value(index, 'Lat', Result.latitude)
            Indexed_Targets.set_value(index, 'Long', Result.longitude)
    for address in Fails:
        print (address)
    Indexed_Targets.to_csv(filename[:-4]+"_RESULTS.csv")

if __name__ == '__main__':
    
    # whatever these are for you...
    main("C:\\Users\\mnaim\\OneDrive\\Desktop\\Coding VSCO\\ADA\\ada project", "starbucks.csv")
