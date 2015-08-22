'''
  Convert input.csv to output.csv
  The row format of input.csv is 2013-07-10 02:52:49,-44.490947,171.220966
  The output.csv is appended for every row readed in the input.csv

  For run this script you need install Python 3, package pytz and package requests.
'''
import csv
import time
import datetime
import requests
import pytz
import argparse
from pytz import timezone
from time import mktime
from datetime import datetime

_date_fmt = "%Y-%m-%d %H:%M:%S"

def timezoneID_from_latlong(latitude, longitude):
    timestamp = time.time()
    api_response = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location={0},{1}&timestamp={2}'.format(latitude,longitude,timestamp))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        timezone_id = api_response_dict['timeZoneId']
        timezone_name = api_response_dict['timeZoneName']
        return timezone_id

def load_csv_file_and_add_timezone(file):
    csv_rows = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            strt = time.strptime(row[0], _date_fmt)
            utc_time = datetime.fromtimestamp(mktime(strt))
            tz = timezone(timezoneID_from_latlong(row[1], row[2]))
            tz_time = utc_time.replace(tzinfo=pytz.utc).astimezone(tz).strftime(_date_fmt)
            csv_rows.append((row[0], row[1], row[2], tz, tz_time))
    return csv_rows


def save_csv(file, rows):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def main():
    parser = argparse.ArgumentParser(
    description='Convert CSV file adding timezone information.'
    )
    parser.add_argument('-i', '--input', help='CSV input file name.', default='input.csv')
    parser.add_argument('-o', '--output', help='CSV output file name.', default='output.csv')
    args = parser.parse_args()
    #inputfile = 'input.csv'
    #outputfile = 'output.csv'

    rows = load_csv_file_and_add_timezone(args.input)
    save_csv(args.output, rows)

if __name__ == '__main__':
    main()
