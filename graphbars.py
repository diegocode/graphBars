# This program draws a vertical bar chart
# from data given in a dictionary
#
# You can configure:
#
# width, height, char used to draw every bar
# and if labels, values, percentages are shown or not
#
# diegoCode / CC-BY-SA 4.0 / ARG

import csv

max_width = 36
max_height = 10

show_label = True
show_value = True
show_percent = True
default_char = '#'

# data for graphic => label: value
# data = {'apple': 50, 'banana': 75, 'peach': 30, 'orange': 40, 'lemon': 60}

class DataPoint:
    def __init__(self, lbl, val, char = default_char):
        self.label = lbl
        self.value = val
        self.character = char

class DataSeries:
    def __init__(self):
        self.points = []
        self.qty = 0

    def addPoint(self, p):
        self.points.append(p)
        self.qty += 1

    def getMaxValue(self):
        m = self.points[0].value
        for p in self.points[1:]:
            if p.value > m:
                m = p.value
                
        return m

# load data from file
data = {}
with open("data.csv") as f:
	s = csv.reader(f, delimiter=";")
	for i in s:
		data[i[0]] = float(i[1])

print(data)

# sort items 
tData = sorted(data.items(), key=lambda x: -x[1])

# char used to draw bars
# if quantity of chars  < than quantity of bars
# then default_char is used
charsGraph = ['X', '0', '&', "%"]

ds = DataSeries()

# populates DataSeries object
for n, t in enumerate(tData):
    if n > len(charsGraph) - 1:
        p = DataPoint(t[0], t[1])
    else:
        p = DataPoint(t[0], t[1], charsGraph[n])
    ds.addPoint(p)

# width is the width of every bar
width = max_width // ds.qty

# if enabled, show labels
if show_label:
    for p in ds.points:
        print(p.label.center(width), end='')
    print()

# if enabled show values
if show_value:
    for p in ds.points:
        print(str(p.value).center(width), end='')
    print()

# if enabled show percentage
if show_percent:
    for p in ds.points:
        auxs = '%5.1f%%' % (p.value / ds.getMaxValue() * 100)
        print(auxs.center(width), end='')
    print()
print()

# calculates the value of every row 
valdiv = ds.getMaxValue() / max_height

# draws bars
aux = 0
while aux < max_height:
    for p in ds.points:
        if p.value >= valdiv * (max_height - aux):
            print( ' ' + (p.character * (width - 2)) + ' ', end='')
        else:
            print( ' ' * width, end='')
    aux += 1

    print()

print()
