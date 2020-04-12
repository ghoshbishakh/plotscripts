import matplotlib.pyplot as plt

# Configuration ----------------------------------------

# number of adjascent boxes = number of things to compare
# legends, one for each box
box_legends = ['BarType1', 'BarType2']


# number of such groups of boxes = number of test cases
# X labels = one for each group
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


# ==============================================================================================

# compute positions
number_of_groups =  len(group_labels)
number_of_boxes = len(box_legends)

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
medianprops = dict(linewidth=2, color='black')
bplots = []
k = 0
for data_group in data:
    bplot = plt.boxplot(data_group,
                        vert=True,  # vertical box alignment
                        patch_artist=True,  # fill with color
                        # labels=labels[k:k+4],
                        positions=positions[k],
                        boxprops=dict(facecolor=colors[k]),
                        medianprops=medianprops)
    bplots.append(bplot)
    k += 1

plt.legend([bp["boxes"][0] for bp in bplots], box_legends, loc='upper left')


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


