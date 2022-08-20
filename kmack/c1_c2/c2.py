from re import A
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./gpdata.csv")

# Target Android Version 7.1 and up for NEW forensics capabilities because new ones would come from the NEWEST version of Android and within the data the newest version is 7.1 and up

def get_count(cat, inst) -> int:
    count = 0
    
    for _ in list(df[cat]):
        if inst == _:
            count += 1

    return count

# BEST OVERALL RATING
# SCATTER PLOT
cats = list(df["Category"])
ratings = list(df["Rating"])


cat_set = list(set(cats))
cat_hash = {}

rep = 1
for i in range(len(cat_set)):
    cat_hash.update({cat_set[i]: rep})
    rep += 1

for _ in cat_hash:
    print(_, cat_hash[_])

for i in range(len(cats)):
    cats[i] = cat_hash[cats[i]]

'''
plt.scatter(cats, ratings)
plt.show()
'''

# FIND AVERAGES
cat_rt_hash = {}
for _ in cats:
    cat_rt_hash.update({_: 0})

for i in range(len(cats)):
    if not(pd.isna(ratings[i])):
        cat_rt_hash[cats[i]] += ratings[i]

print()
for c in cat_set:
    ct = get_count("Category", c)

    print(c, cat_rt_hash[cat_hash[c]]/ct)

# PHOTOGRAPHY HAS THE BEST OVERALL RATING

# PRICING TRENDS BY CATEGORY'
'''
print()
print(cat_set[0])
print(df['Category'] == cat_set[0], 'Price')
a = df.loc[df['Category'] == cat_set[0], 'Price']
print(a)
'''

cats = df["Category"]
prices = df["Price"]

print(prices[0])

cat_price_hash = {}

for _ in cat_set:
	cat_price_hash.update({_: []})

print(cat_price_hash)

for i in range(len(cats)):
	cat_price_hash[cats[i]].append(prices[i])


for key in cat_price_hash:
	y = cat_price_hash[key]
	try:
		y = [ float(_) for _ in y ]
		x = [i for i in range(len(y))]

		plt.scatter(x, y)
		plt.title(key)
		plt.xlabel("num")
		plt.ylabel("Prices")
		plt.show()
	except:
		pass
		"""
		print(key)
		print(y)
		print(df.value_counts(subset=["Category"]))
		break
		"""
# House and Home
# - all apps are free
# Communication
# - some apps are paid and typically fall in the range of 0 to 5$ with an outlier at 20$
# Personalization
# - Many apps are paid and typically fall in the range of 0 to 5 dollars with a couple outliers at 7 and 10 dollars
# Family
# - Most apps are free and most of the paid apps fall within the range of 0 to 50$ with 3 outliers all close to 400$
# Medical
# - Many apps are paid and typically fall within the range of 0 to just under 50$ with 3 outliers at around 75$ and one major outlier at 200$
# Comics
# - all apps are free
# Video Players
# - Most apps are free and paid ones range from 0 to 6$
# Social
# - Most apps are free and paid ones range from 0 to 14$
# Books and Reference
# - Some apps are paid and range from 0 to 7$
# News and Magazines
# - Most apps are free with two apps one at 1$ and the other at 3$
# Sports 
# - Most apps are free and paid apps typically fall in the range from 0 to 10$ with an outlier at 30$
# Art and Design
# - Most apps are free and the 3 paid apps are 2$
# Tools
# - Many apps are paid and typically fall withing the range of 0 to 15$ with an outlier at just above 25$
# Food and Drink 
# - Most apps are free and there are 2 paid apps one at around 3.50 and the other at 5$
# Health and Fitness
# - Some apps are paid and typically fall within the range of 0 and 10$
# Health and Fitness
# - 2 apps are paid with one being 2.50$ and the other 3.00$
# Parenting
# - 2 apps are paid with one being 4.50$ and the other 5.00$
# Events 
# - 1 app is paid and is above 100$
# Finance 
# - Some apps are paid and have 2 clusters one from 0 to 50$ and around 400$
# Beauty
# - All apps are free
# Auto and Vehicles 
# - Only 3 paid apps, one just under 2$, the other 2$, and the last one 10$
# Maps and Navigation
# - Some paid apps, typicall from 0 to 12$
# Productivity 
# - Many paid apps, typicall from 0 to 10$ with one app at just under 160$
# Dating 
# - Many paid apps, typicall from 0 to 8$
# Lifestyle 
# - Some paid apps, with 2 apps one at 50$ and the other at 300$ and another cluster of apps around 400$
# Libraries and Demo
# - Only 1 paid app at 1$
# Education
# - 3 apps at 4$ 1 app at 6$
# Weather
# - some paid apps that typically fall in the range of 0 to 7$
# Business 
# - some paid apps that typically fall in the range of 0 to 20$ with one outlier at close to 90$
# Photography 
# - Many paid apps that typically fall in the range of 0 to 10$ with one outlier at 20$ and the other at 30$
# Travel and Local 
# - Many paid apps that typically fall in the range of 0 to 9$ 
# Game 
# - Many paid apps that typically fall in the range of 0 to just above 17.50$ 
# Entertainment 
# - Only 2 paid apps, one just under 3$, the other 5$

# SUSPICIOUS APPLICATIONS
# App Name - Life Made WI-Fi Touchscreen Photo Frame - all the data is shifted by 1 column left