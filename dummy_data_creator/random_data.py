import pandas as pd
import numpy as np

'''
This first section loads and cleans the dataset. First by assigning each post ID
to the correct platform (using data from posts_raw.csv). Then by setting empty columns.

The function then basically works in chronological order. It finds when a post was first published
and then assigns that date a maximum number. It then decreases the max number by one for every subsequent
day up to a max of 50 days (all following days are 0).

It then multplies that max number by a multiplier, which is different for the various metrics. e.g. impressions
are usually much higher than comments so the multiplier is much higher.

It also multiplies the different platforms with a different multiplier as they usually perform differently.

It then saves the data to a CSV.
'''

performance = pd.read_csv("./files/clean_dates.csv")
posts = pd.read_csv("./files/posts_raw.csv")

fb = list(posts[posts["platform"] == "facebook"]["post_id"])
ig = list(posts[posts["platform"] == "instagram"]["post_id"])
tt = list(posts[posts["platform"] == "tiktok"]["post_id"])

performance.loc[performance["ID"].isin(fb), "Platform"] = "FB"
performance.loc[performance["ID"].isin(ig), "Platform"] = "IG"
performance.loc[performance["ID"].isin(tt), "Platform"] = "TT"

performance[["impressions", "likes", "comments", "shares", "clicks"]] = 0

def randomiser (column,multiplier, df):
    #find day difference between first post date and current row date
    temp_date = []
    for id in df["ID"]:
        oldest = df[df["ID"]==id]["Date"].min()
        temp_date.append(oldest)

    df["Oldest"] = temp_date
    df["Diff"] =  pd.to_datetime(df["Date"]) - pd.to_datetime(df["Oldest"])
    df["Diff"] = df["Diff"].dt.days

    #find the highest days since posting & set max cap
    temp_max = []
    for id in df["ID"]:
        highest = df[df["ID"]==id]["Diff"].max()
        temp_max.append(highest)

    df["Max"] = temp_max
    df.loc[df["Max"] > 50, "Max"] = 50

    #set a calculation for the final random numbers make sure can't be below 0
    df["Final"] = df["Max"] - df["Diff"] + np.random.randint(-5,+3)
    df.loc[df["Final"] < 0, "Final"] = 0

    #multiply the different platforms
    df.loc[df["Platform"] == "FB",column] = df["Final"] * multiplier * 1
    df.loc[df["Platform"] == "IG",column] = df["Final"] * multiplier * 3
    df.loc[df["Platform"] == "TT",column] = df["Final"] * multiplier * 5

    df.drop(["Oldest", "Diff", "Max", "Final"], axis = 1, inplace = True)

randomiser("Impressions",99, performance)
randomiser("Likes", 18, performance) 
randomiser("Comments", 2, performance)
randomiser("Shares", 2, performance)
randomiser("Clicks", 4, performance)



'''
This next section is just to apply a random integer to the paid posts for 
how much was spent that day. The chronology doesn't matter here so it's a simpler calculation

'''

paid = list(posts[posts["promoted_boolean"] == "y"]["post_id"])
performance.loc[df["ID"].isin(paid), "promoted"] = "paid"
performance["cost"] = 0

for row in performance.index:
    if performance.iloc[row,2] == "paid":
        performance.iloc[row,3] = np.random.randint(100,500)


#commented out this part, uncomment to save as CSV
# performance.to_csv(r"./files/final_randomised_numbers.csv", index=False)



'''
This next section lets you fill the country list with random countries.
You input to the function your country list, the columns they should fill, and your dataframe.
You can put less columns than countries but you can't put more columns than countries.
'''

interactions = pd.read_csv("./files/interactions_raw.csv")
# interactions.head()

top4_9 = ["canada", "australia", "nigeria", "france", "pakistan", "germany"]
top10_20 = ["turkey",
"spain",
"egypt",
"poland",
"south africa",
"russia",
"ghana",
"italy",
"indonesia",
"brazil",
"mexico",
"portugal",
"belgium",
"ukraine",
"morocco",
"tanzania",]

def random_countries(countries,columns,df):
    for row in df.index:
        numlist = list(range(len(countries)))
        for column in columns:
            randomnum = numlist[np.random.randint(len(numlist))]
            randomcountry = countries[randomnum]
            df.iloc[row,column] = randomcountry
            numlist.remove(randomnum)

random_countries(top4_9,[5,6,7,8,9,10],interactions)
random_countries(top10_20,[11,12,13,14,15,16,17,18,19,20,21],interactions)
interactions

#commented out this part, uncomment to save as CSV
# interactions.to_csv(r"./files/final_randomised_countries.csv", index=False)