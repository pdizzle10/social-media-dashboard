import pandas as pd
import datetime

#import & clean dataframe and set up for the for loop
df = pd.read_csv("./files/post_dates_raw.csv")
df.drop(df.index[100:],inplace=True)
df["post_date"] = pd.to_datetime(df["post_date"], format="%d/%m/%Y")
df["post_id"] = pd.to_numeric(df["post_id"])
today = pd.to_datetime("2023-08-25")
i = -1
clean = pd.DataFrame(columns=["Date", "ID"])

#loop through each date, find how many days between today and date, create a new list of all those dates, turn into a dataframe with the right ID and concatenate
for date in df["post_date"]:
    i = i + 1
    date = date.to_pydatetime() 
    # print(date)
    diff = today - date
    days = diff.days
    # print(days)
    numlist = list(range(1,days+1))
    # print(numlist)
    
    datelist = [date]

    for num in numlist:
        newdate = date + datetime.timedelta(days=num)
        datelist.append(newdate)
    
    dct = {"Date":datelist,"ID":df["post_id"][i]}
    new = pd.DataFrame(dct)


    clean = pd.concat([clean, new],ignore_index=True)

# uncomment to save file to csv
clean.to_csv(r"./files/clean_dates.csv", index=False)