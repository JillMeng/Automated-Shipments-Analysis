from Write_to_excel import exlwriter
from Write_to_excel import addworksheet
import pandas as pd

def create_report(drop_path):
    try:
        df = pd.read_csv(drop_path)

        source_lst = ['PRINCE GEORGE', 'RADIUM HOT SPRINGS', 'ENGEN', 'ELKO']
        # iterate all source mills and create reports
        for SourceMill in source_lst:

            #formate date - split to get Ship Date
            df['Ship Date'] = df['Start Time'].str.split(' ').str[0]
            df['Ship Date'] = pd.to_datetime(df['Ship Date']).dt.date
            # sort values by ship date
            df = df.sort_values(by="Ship Date")

            #filter data that is late unshipped
            filter1 = (df['Source City'] == SourceMill) & (df['Load Status'] != 'SHIP CONFIRM') &\
                      (df['Secure Resources Status'] != 'SECURE RESOURCES_TENDER RESPONSE OPEN')
            #filer data that is late and unbooked
            filter2 = (df['Source City'] == SourceMill) & \
                      (df['Secure Resources Status'] == 'SECURE RESOURCES_TENDER RESPONSE OPEN')

            df_unshipped = df.loc[filter1,['Order','BM Shipment','Load Status','Ship Date','Service Provider Name',
                                           'Destination City','Destination Province Code']]
            df_unbooked = df.loc[filter2,['Order','BM Shipment#','Load Status','Ship Date','Service Provider Name',
                                          'Destination City','Destination Province Code']]

            # test the first dataframe
            number_unshipped = df_unshipped['Order'].count()
            if number_unshipped != 0:
                print('number of unshipped orders for {}:'.format(SourceMill), number_unshipped)
                df_unshipped = df_unshipped.sort_values(['Service Provider Name'])
                exlwriter(SourceMill,df_unshipped,'Unshipped_Lates')
            else:
                print('Congrats! You have no unshipped orders for {}!'.format(SourceMill))

            # test the second dataframe
            number_unbooked = df_unbooked['Order'].count()
            if number_unbooked != 0:
                print('number of unbooked orders for {}:'.format(SourceMill), number_unbooked)
                df_unbooked = df_unbooked.sort_values(['Destination City'])
                addworksheet(SourceMill, df_unbooked, 'Unbooked_Lates')
            else:
                print('Good job! You have no unbooked orders for {}!'.format(SourceMill) + "\n")

    except OSError:
        print('File cannot be found!')
    except PermissionError:
        print('You do not have permission to this file!')

    return ()