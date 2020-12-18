import matplotlib.pyplot as plt
import pandas as pd


def graphs(df):
    # create visualization of the cost
    x = df['OD_pare']
    y = df['Gross Volume']
    plt.barh(x, y)
    plt.xlabel('Volume Shipped')
    plt.title('Volume Analysis')
    plt.tight_layout()
    plt.savefig('Volume_analysis')

    # create visualization of the cost
    z = df['Cost']
    plt.barh(x, z)
    plt.xlabel('Average Cost')
    plt.title('Cost Analysis')
    plt.tight_layout()
    plt.savefig('Cost_analysis')
    return ()

'''
def insert_graph(df):

    writer = pd.ExcelWriter('/Users/jm/Desktop/5001Project/Cost_analysis.xlsx', engine='xlsxwriter')
    sheet = writer.book.add_worksheet('Cost_analysis')
    sheet.insert_image(0, 0, 'Cost_analysis,png')
    imgdata = BytesIO(img)
    fig = plt.figure()
    img.figure.savefig(imgdata)
    print(imgdata.getvalue())

    return ()
'''


