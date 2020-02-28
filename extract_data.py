from urllib.request import urlopen
from sys import argv

import json
import pandas as pd


# Global variables
DATES = []
HIGHS = []
LOWS = []
OPENS = []
CLOSES = []
FILENAMES = []



def get_jsonparsed_data(_url):
    # takes url as input, returns dict
    response = urlopen(_url)
    data = response.read().decode("utf-8")
    return json.loads(data)


def write_data_to_csv(_filename):
    global DATES
    global HIGHS
    global LOWS
    global OPENS
    global CLOSES

    print ('writing data to csv ' + _filename)

    output_data = pd.DataFrame(
        {
            'Date': DATES,
            'Price High': HIGHS,
            'Price Low': LOWS,
            'Price Open': OPENS,
            'Price Close': CLOSES,
        }
    )

    output_data.to_csv(_filename)


def set_filenames(_argv):
    global FILENAMES

    for i in range(1, len(_argv)):
        FILENAMES.append('CSVs/' + _argv[i] + '_data.csv')

def clear_data():
    global DATES
    global HIGHS
    global LOWS
    global OPENS
    global CLOSES

    DATES.clear()
    HIGHS.clear()
    LOWS.clear()
    OPENS.clear()
    CLOSES.clear()



def extract_data(_argv):
    global DATES
    global HIGHS
    global LOWS
    global OPENS
    global CLOSES
    global FILENAMES

    url = ''

    set_filenames(_argv)

    for i in range (1, len(_argv)):
        url = 'https://financialmodelingprep.com/api/v3/historical-price-full/' + _argv[i]
        if url == '':
            print ('URL ISSUE...')
            exit()
        else:
            data = get_jsonparsed_data(url)

        for data_point in data['historical']:
            DATES.append(data_point['date'])
            HIGHS.append(data_point['high'])
            LOWS.append(data_point['low'])
            OPENS.append(data_point['open'])
            CLOSES.append(data_point['close'])

        file = FILENAMES[i - 1]
        write_data_to_csv(file)
        clear_data()


if __name__ == '__main__':
    extract_data(argv)
