import matplotlib.pyplot as plt
import statistics


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



# styles
plt.rcParams.update({'font.size': font_size})
plt.rcParams.update({'font.weight': font_weight})
plt.rcParams['axes.labelweight'] = label_font_weight
colors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]



fig, ax = plt.subplots()
fig.set_size_inches(fig_size[0], fig_size[1])

for idx, line in enumerate(data):
    if len(line) < 3:
        plt.plot(line[0], line[1], label=line_legends[idx], linewidth=linewidth)
    else:
        plt.errorbar(line[0], line[1], yerr=line[2], label=line_legends[idx], capsize=capsize, elinewidth=elinewidth)


plt.ylabel(ylabel)
plt.xlabel(xlabel)

if len(line_legends) > 1:
    ax.legend()

ax.yaxis.grid(True)
plt.xticks(rotation=xtickrotation)


if log_scale:
    plt.yscale('log')


plt.tight_layout()

if save:
    plt.savefig(file_name, format='eps')
else:
    plt.show()
