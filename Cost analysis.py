import pandas as pd
from Lane_filter import origin_filter
from Lane_filter import volume_filter
from Lane_filter import desto_filter
from Cost_visualiation import graphs


def main():
    try:

        df = pd.read_csv('/Users/jm/Desktop/5001Project/Weekly shipment data.csv')

        #Apply filter - filter rows by origin
        df = origin_filter(df)

        #Apply fileter - filter rows by destination
        df = desto_filter(df)

        df_pivot = pd.pivot_table(df,values=['Gross Volume','Cost'],index = ['Source City','Destination Province Code',
                                                                                 'Destination City'],
                                  aggfunc={'Gross Volume':'sum','Cost':'mean'})

        # export dataframe to Excel sheet
        writer = pd.ExcelWriter('Cost_analysis.xlsx', engine='xlsxwriter')
        df_pivot.to_excel(writer, sheet_name='Cost_analysis')
        writer.save()

        # filter rows by the volume of shipment
        new_df = volume_filter(df_pivot)


        # create visualization of the cost
        new_df['OD_pare'] = new_df['Source City'].astype(str) + '-' + new_df['Destination City'].astype(str)
        number_of_rows = new_df.shape[0]
        print(number_of_rows)
        while number_of_rows >= 50:
            print('You have chosen too many lanes. Please apply filter!')
            new_df = origin_filter(new_df)
            new_df = desto_filter(new_df)
            new_df = volume_filter(new_df)
            number_of_rows = new_df.shape[0]

        # create visualization
        graphs(new_df)


    except OSError:
        print('File cannot be found!')
    except PermissionError:
        print('You do not have permission to this file!')

main()