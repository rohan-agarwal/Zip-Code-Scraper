# Package imports
import urllib2 as ur
from bs4 import BeautifulSoup
import re
import pandas as pd

__author__ = 'Rohan Agarwal'


# Pull raw html page data
def connect(site):
    req = ur.Request(site)
    response = ur.urlopen(req)
    page = response.read()
    return page


# Use BeautifulSoup to retrieve text
def bs_parse(page):
    soup = BeautifulSoup(page, "html.parser")

    # Processing
    text = soup.get_text()
    text = text.replace('\r', '')
    text = text.replace('\t', '')
    text = text.replace('\n', '')
    text = text.replace('\\n', '')
    return text


# Use regex to parse and format
def regex_parse(text):
    # Get the meat of the text
    regex_meat = re.search(r"""(?:{return .)(.*[0-9])(?:.;}function)""", text)
    meat = regex_meat.groups()[0]

    # Parse attribute names and values
    regex_values = re.search(r"""(?:[a-zA-Z])([0-9].*)""", meat)
    values = regex_values.groups()[0]
    values = [str(s) for s in values.split(',')]
    regex_names = re.search(r"""(.*[A-Za-z])(?:[0-9])""", meat)
    names = regex_names.groups()[0]
    names = [str(s) for s in names.split(',')]

    row = dict(zip(names, values))
    return row


# Pull demographic information for all zip codes in the US
def main():
    codes = pd.read_csv('zipcodes.csv')
    codes = codes['zipcode']
    rows = []
    for code in codes:
        print code
        try:
            site = 'http://zipwho.com/?zip=' + str(code) + '&city=&filters=--_--_--_--&state=&mode=zip'
            page = connect(site)
            text = bs_parse(page)
            row = regex_parse(text)
            rows.append(row)
        except:
            print 'no information available for ' + str(code)

    df = pd.DataFrame(rows)
    df.to_csv('results.csv')
    return df


main()
