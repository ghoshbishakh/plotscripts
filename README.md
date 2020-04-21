# plotscripts
Simple plotting scripts for a bit complicated matplotlib plots

## Grouped Boxplot
![grouped boxplot image](https://github.com/ghoshbishakh/plotscripts/raw/master/images/boxplot.png)

Just change `boxplot.py` with your data and configs in the following lines:

```python
# Configuration ----------------------------------------

# number of adjascent boxes = number of things to compare
# = legends, one for each box
box_legends = ['BarType1', 'BarType2']


# number of such groups of boxes = number of test cases
# = X labels = one for each group
group_labels = ["G1", "G2", "G3"]


xlabel = "Groups"
ylabel = "Values"

save=False
file_name = "boxplot.eps"


# Styles ------------------------------------------------

xtickrotation = 0
font_size = 12
font_weight = 'bold'
label_font_weight = 'bold'

fig_size = (6, 4)

#  Data-------------------------------------------------------
#  Format = [
#              [ [box1group1data],  [box1group2data],..],
#              [ [box2group1data],  [box2group2data],..],
#           ]


data = [

[
[3,4,5,6,7,4,4,5,6,6,7],
[4,5,6,7,4,4,5,6,6,7,8,8,8,8,9,9,10],
[5,6,7,4,4,5,6,6,7,8,8,9,9,9,9,9,10,12]
],

[
[1,2,3,4,5,6,7,4,4,5,6,6,7],
[1,2,3,4,5,6,7,4,4,5,6,6,7],
[1,2,3,4,5,6,7,4,4,5,6,6,7]
]

]
```

---

## Grouped Barplot

![grouped barplot](https://github.com/ghoshbishakh/plotscripts/raw/master/images/barplot.png)

Just change `barplot.py` with your data and configs in the following lines:


```python
# Configuration ----------------------------------------

# number of adjascent bars = number of things to compare
# = legends, one for each box
bar_legends = ['BarType1', 'BarType2', 'BarType3']


# number of such groups of bars = number of test cases
# = X labels = one for each group
group_labels = ["G1", "G2", "G3"]


xlabel = "Groups"
ylabel = "Values"

save=False
file_name = "barplot.eps"


# Styles ------------------------------------------------

xtickrotation = 0
font_size = 12
font_weight = 'bold'
label_font_weight = 'bold'

fig_size = (6, 4)

#  Data-------------------------------------------------------
#  Format = [
#              [ [bar1group1data],  [bar1group2data],..],
#              [ [bar2group1data],  [bar2group2data],..],
#           ]

#  OR YOU CAN ALSO PROVIDE MEAN AND STDEVS DIRECTLY

data = [

[
[3,4,5,6,7,4,4,5,6,6,7],
[4,5,6,7,4,4,5,6,6,7,8,8,8,8,9,9,10],
[5,6,7,4,4,5,6,6,7,8,8,9,9,9,9,9,10,12]
],

[
[1,2,3,4,5,6,7,4,4,5,6,6,7],
[1,2,3,4,5,6,7,4,4,5,6,6,7],
[1,2,3,4,5,6,7,4,4,5,6,6,7]
],

[
[3,4,5,6,7,4],
[4,5,6,7,4,4,5,6,],
[5,6,7,4,4,5,6,6,7,8,8]
]

]

data_means  = None
data_stdev = None
# ==============================================================================================
```

---

## Line Plots with error bars

![line plot](https://github.com/ghoshbishakh/plotscripts/raw/master/images/lineplot.png)

Just change `lineplot.py` with your data and configs in the following lines:


```python
# Configuration ----------------------------------------

# number of lines = number of things to compare
# = legends, one for each box
line_legends = ['Line1', 'Line2']



xlabel = "X axis"
ylabel = "Y axis"

log_scale = False

save=False
file_name = "lineplot.eps"


# Styles ------------------------------------------------

linewidth=2

# error bar styles:
capsize=2
elinewidth=2


xtickrotation = 0
font_size = 12
font_weight = 'bold'
label_font_weight = 'bold'



fig_size = (6, 4)

#  Data-------------------------------------------------------
#  Format = [
             # ( [line1 x points],  [line 1 y points], [line 1 y error : Not required]),
             # ( [line 2 x points],  [line 2 y points], [line 1 y error : Not required]),
#           ]


data = [

( [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], ),
( [1,2,3,4,5,6,7,8,9,10,11,12], [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]),

]

# ==============================================================================================

```