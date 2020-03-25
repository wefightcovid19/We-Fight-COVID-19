import pandas as pd
from datetime import datetime

data = pd.read_csv('../assets/data/CA-COVID19-Data.csv', index_col='Date')
difference = data.diff(axis=0)

def date_converter(date):
    datetime_object = datetime.strptime(date, '%m/%d/%y')
    return datetime_object.strftime("%m-%d-%Y")

result = []
for column in data.columns:
    day = 1
    for date, count in data[column].iteritems():
        if count > 0:
            result.append([day, "United States", column, count, 0, 0, 0, date_converter(date)])
            day+=1

final = pd.DataFrame.from_records(result, columns=['','Country_Region','Province_State','Confirmed','Recovered',"Active",'Deaths','Date'])
final.to_csv("../assets/data/county-data.csv", index=False)