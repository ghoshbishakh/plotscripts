# plotscripts
Simple plotting scripts for a bit complicated matplotlib plots

## Grouped Boxplot
![grouped boxplot image](https://github.com/ghoshbishakh/plotscripts/raw/master/images/barplot.png)

Just change `boxplot.py` with our data and configs in the following lines:

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

