import shutil
import os
from Shipment_analysis import create_report

def job():

    # Check if any new files appeared in drop folder
    dropped_files = [file for file in os.listdir('/Users/jm/Desktop/5001Project/Drop') if file.endswith('.csv')]
    drop_path = os.path.join(os.getcwd(), '/Users/jm/Desktop/5001Project/Drop', ''.join(dropped_files))

    if dropped_files:
        create_report(drop_path)
        shutil.move(drop_path, os.path.join(os.getcwd(), '/Users/jm/Desktop/5001Project/Processed'))
        print('All Files Process. Completed')
    else:
        print('No New Files')


def main():
    job()
main()

