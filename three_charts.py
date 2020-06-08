# three_charts.py
import matplotlib.pyplot as plt
import numpy as np

#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
labels = []
sizes = []
for values in pie_data:
    hi = values["company"]
    labels.append(hi)
    he = values["market_share"]
    sizes.append(he)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show() # need to explicitly "show" the chart window
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
x = []
y = []
for values in line_data:
    hie = values["date"]
    hii = values["stock_price_usd"]
    x.append(hie)
    y.append(hii)

plt.plot(x, y)
plt.show()
#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")

genre = []
viewers = []
for value in bar_data:
    so = value["genre"]
    soo = value["viewers"]
    genre.append(so)
    viewers.append(soo)


fig = plt.figure(figsize =(7,5))

positions = [1, 2, 3, 4 ,5 ,6 ,7 ]
plt.bar(positions,viewers, width = 0.5,)
plt.xticks(positions, genre)
plt.show()