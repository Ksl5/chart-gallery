# three_charts.py
import matplotlib.pyplot as plt

#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

labels = ["Company X", "Company Y", "Company Z"]
sizes = [0.55, 0.30, 0.15]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

#
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

line_value = [dat["stock_price_usd"] for dat in line_data]

line_labels = [dat["date"] for dat in line_data]

plt.plot(line_labels, line_value, color='g',marker='o',linestyle='dashed',markersize=12, linewidth=2)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Daily Stock Price\nJan. 1, 2019 - Jan. 8, 2019')
plt.show()


print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

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

#bar_value = [gen["viewers"] for gen in bar_data]
#bar_labels = [gen["genre"] for gen in bar_data]
#width = 0.25
#plt.bar(bar_value, bar_labels, width)
#plt.show()

plt.style.use('ggplot')

x = [dat["genre"]for dat in bar_data]
Viewers = [dat["viewers"]for dat in bar_data]

bar_value = [gen["viewers"] for gen in bar_data]
bar_labels = [gen["genre"] for gen in bar_data]
plt.barh(bar_labels, bar_value, align='center')
plt.show()

#x_pos = [i for i, _ in enumerate(x)]
#
#plt.barh(x_pos, Viewers, color='green')
#plt.xlabel("Genere")
#plt.ylabel("Viewers")
#plt.title("Movies")
#
#plt.xticks(x_pos, x)
#
#plt.show()


print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data
