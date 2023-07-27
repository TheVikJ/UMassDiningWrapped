import matplotlib.pyplot as plt

shit = open("text.txt", "r")
Lines = shit.readlines()

print("Dining Commons: ")

swipes = {"Hamp": 0, "Berk": 0, "Worc": 0, "Frank": 0, "Roots": 0}
totalswipes = 0

# Parse text and count swipes
for line in Lines:
  if line.split(" ")[0] == "E":
    try:
      DC = line.split(" ")[5]
      DCname = ''.join(x for x in DC if x.isalpha())
      DCname = DCname.split("M")[1].split("D")[0]
      swipes[DCname] += 1
      totalswipes += 1
    except:
      pass

# Print swipes
for common in swipes:
  print("{0:6} {1:5} {2:3.5s}%".format(
    common, swipes[common], str((swipes[common] * 100) / totalswipes)))

print("\nCafes/Restaurants: ")

cafeNames = []
cafeDollars = []
totalDollars = 0

# Parse text and count dining dollars
for line in Lines:
  if line.split(" ")[0] == "UMass":
    cafe = line.split(" ")[5] + line.split(" ")[6]
    cafe = cafe.split("M")[1]
    cafeName = ''.join(x for x in cafe if x.isalpha())
    if cafeName not in cafeNames:
      cafeNames.append(cafeName)
      cafeDollars.append(0)
    cash = line.split(" ")
    dollars = float(cash[len(cash) - 1].split("	")[0].strip("$"))
    totalDollars += dollars
    cafeDollars[cafeNames.index(cafeName)] += dollars

# Print dining dollars
for i in range(0, len(cafeNames)):
  print("{0:16} {1:8} {2:3.5s}%".format(
    cafeNames[i], "$" + str(round(cafeDollars[i], 2)),
    str(round(((cafeDollars[i] * 100) / totalDollars), 3))))
  
# Plot swipes
dining = list(swipes.keys())
diningswipes=list(swipes.values())
fig1 = plt.figure()
bars = plt.bar(dining, diningswipes, width = 0.4)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.08, yval + 0.2, round(yval, 2))
plt.xlabel("Dining Commons")
plt.ylabel("Number of Meal Swipes")
plt.title("UMass Dining Commons Wrapped")
plt.savefig('DiningCommons.png')

# Plot dining dollars
fig2 = plt.figure()
plt.autoscale()
bars = plt.bar(cafeNames, cafeDollars, width = 0.4)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() - 0.1, yval + 0.2, round(yval, 2))
plt.xlabel("Cafe/Restaurant Names")
plt.ylabel("Dollars Spent ($)")
plt.xticks(rotation=30, ha='right')
plt.subplots_adjust(bottom=0.25)
plt.title("UMass Restaurants Wrapped")
plt.savefig('CafesRestaurants.png')