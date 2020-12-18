import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

def exlwriter(filename, df, sheetname):
    '''
    Export dataframe to excel and format it as a table
    :param filename,dataframe,sheetname
    :return: nothing
    '''
    # export to Excel sheet
    writer = pd.ExcelWriter('/Users/jm/Desktop/5001Project/Late_Orders_{}.xlsx'.format(filename), engine='xlsxwriter')
    df.to_excel(writer, sheet_name= sheetname, startrow=1, header=False, index=False)
    worksheet = writer.sheets[sheetname]
    # Get the dimensions of the dataframe.
    (max_row, max_col) = df.shape
    # Create a list of column headers, to use in add_table().
    column_settings = [{'header': column} for column in df.columns]
    # Add the Excel table structure.
    worksheet.add_table(0, 0, max_row, max_col-1, {'columns': column_settings})
    # Make the columns wider for clarity.
    worksheet.set_column(0, max_col-1, 26)

    writer.save()
    return ()

def addworksheet(filename, df2, sheetname):
    '''
    :param filename:
    :param df2:
    :param sheetname:
    :return:
    '''
    writer = pd.ExcelWriter('/Users/jm/Desktop/5001Project/Late_Orders_{}.xlsx'.format(filename), engine='openpyxl')
    writer.book = load_workbook('/Users/jm/Desktop/5001Project/Late_Orders_{}.xlsx'.format(filename))
    df2.to_excel(writer, sheet_name=sheetname, index=False)
    '''
    worksheet = writer.sheets[sheetname]
    (max_row, max_col) = df2.shape
    # Create a dictionary of column headers, to use in add_table().
    column_settings2 = [{'header': column} for column in df2.columns]
    print(column_settings2)
    # Add the Excel table structure.
    worksheet.add_table(0, 0, max_row, max_col-1, {'columns': column_settings2})
    # Make the columns wider for clarity.
    worksheet.set_column(0, max_col - 1, 12)
    '''
    writer.save()
    return ()
