import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 90, 25, 14]

fig = plt.figure()

#fig.add_subplot(221)
#fig.add_subplot(222)
#fig.add_subplot(223)
#fig.add_subplot(224)

myFig, thePlots = plt.subplots(2, 2, facecolor='red', figsize=(10, 8))
"""
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
ax1.scatter(x, y)
ax2.bar(x, y)
#fig.add_subplot(ax1)
ax3.plot(x, y)
plt.show()
"""
count = 0
plot_layouts = [(2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4)]
for rownumber, colnumber, plotnumber in plot_layouts:
    the_plot = plt.subplot(rownumber, colnumber, plotnumber)
    ax = plt.gca()
    if count == 0:
        the_plot.plot(x, y)
    if count == 1:
        the_plot.bar(x, y)
    if count == 2:
        the_plot.scatter(x, y)
    if count == 3:
        the_plot.pie(y, x)
    count += 1

    plt.plot(x, y)

#thePlots[0].plot(x, y)
#thePlots[1].bar(x, y)
plt.suptitle("My Main Title for the Subplots")
plt.savefig('subplots.png')
