# axes

import matplotlib.pyplot as plt

fig, ax = plt.subplots(ncols=2,nrows=2,figsize=(6,6))
ax[0,0].plot([1,2,3,4],[1,4,98,16],"g-o")
ax[0,0].set_xlabel("Numbers")
ax[0,0].set_ylabel("Squares")
ax[0,0].set_ylim(0,100)
yticks = []
for x in range(0,105,5):
    if x%10==0:
        yticks.append(str(x))
    else:
        yticks.append('')

#print(yticks)
ax[0,0].set_yticks(range(0,105,5), yticks)

ax[0,1].set_xlabel("Important label")

ax[1,1].plot([1,2,3,4],[1,8,27,64])
ax[1,1].set_ylim(0,100)
ax[1,1].set_title("In the way")

plt.subplots_adjust(hspace=0.5)
plt.show()