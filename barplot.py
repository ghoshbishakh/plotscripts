import matplotlib.pyplot as plt
import statistics


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

if not data_means:
    data_means = [ [statistics.mean(datalist) for datalist in bartype] for bartype in data ]

if not data_stdev:
    data_stdev = [ [statistics.stdev(datalist) for datalist in bartype] for bartype in data ]

# print(data_means)
# print(data_stdev)

# compute positions
number_of_groups =  len(group_labels)
number_of_boxes = len(bar_legends)

positions = []
for i in range(number_of_boxes):
    positions.append(list(range(i+1, ((number_of_groups*number_of_boxes) + number_of_groups), number_of_boxes+1)))
# print(positions)

xtickpositions = [0]
for i in range(number_of_groups):
    ttt = (positions[0][i] + positions[-1][i])/2.0
    xtickpositions.append(ttt)
group_labels = [""] + group_labels

# print(xtickpositions)

# styles
plt.rcParams.update({'font.size': font_size})
plt.rcParams.update({'font.weight': font_weight})
plt.rcParams['axes.labelweight'] = label_font_weight
colors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]



fig, ax = plt.subplots()
fig.set_size_inches(fig_size[0], fig_size[1])


# rectangular box plot
k = 0
bplots = []
for data_group in data_means:
    print(data_group,data_stdev[k])
    print(positions[k])
    barplot = plt.bar(positions[k], data_group, 1, yerr=data_stdev[k], capsize=3)
    k += 1
    bplots.append(barplot)
plt.legend([bp[0] for bp in bplots], bar_legends, loc='upper left')




plt.ylabel(ylabel)
plt.xlabel(xlabel)

ax.yaxis.grid(True)
plt.xticks(rotation=xtickrotation)

plt.xticks(xtickpositions, group_labels)


plt.tight_layout()

if save:
    plt.savefig(file_name, format='eps')
else:
    plt.show()


