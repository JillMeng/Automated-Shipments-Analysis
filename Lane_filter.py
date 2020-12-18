import pandas as pd
from User_Input import source_mill
from Destination_list import destination_region

def origin_filter(df):
    '''
    Apply origin filter to the dataframe
    :param dataframe,origin
    :return: new dataframe
    '''
    origin_fil = input('Would you like to apply the origin filter? (y/n)\n').lower()
    while origin_fil != 'y' and origin_fil != 'n':
        origin_fil = input('Invalid choice! Please try again. (y/n)\n')
    if origin_fil.lower() == 'y':
        origin = source_mill()
        filter = df['Source City'] == origin
        new_df = df.loc[filter].reset_index()
    else:
        new_df = df
    return new_df

def desto_filter(df):
    '''
    Using booleans to apply destination filter functions in dataframe
    :param dataframe,booleans,destination list function
    :return: new dataframe
    '''
    destination_fil = input('Would you like to apply the destination filter? (y/n)\n').lower()
    while destination_fil != 'y' and destination_fil != 'n':
        destination_fil = input('Invalid choice! Please try again. (y/n)\n')
    if destination_fil.lower() == 'y':
        destination_lst = destination_region()
        booleans = []
        for desto in df['Destination Province Code']:
            if desto in destination_lst:
                booleans.append(True)
            else:
                booleans.append(False)
        desto_filter = pd.Series(booleans)
        new_df = df[desto_filter]
    else:
        new_df = df
    return new_df

def volume_filter(df_pivot):
    '''
    Apply volume filter to eliminate odd shipments
    :param pivot dataframe,minimum volume
    :return: new dataframe
    '''
    volume = int(input('Would you like to evaluate lanes with volume of more than?\n'))
    while volume < 0 and not isinstance(volume_filter, int):
        volume = int(input(print('Invalid choice! Please enter a positive integer.\n')))
    filter = df_pivot['Gross Volume'] >= volume
    new_df = df_pivot.loc[filter].reset_index()

    return new_df