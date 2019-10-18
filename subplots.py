#subplots

import matplotlib.pyplot as plt

quartic = [elem * elem * elem * elem for elem in [1,2,3,4]]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16],'g-o')
plt.plot([1,2,3,4],quartic,'b-s')
plt.title("Squares Data")
plt.xlabel("Numbers")

plt.subplot(1,2,2)
plt.plot([1,2,3,4],[1,8,27,64],'r--^')
plt.title("Cubic Data")

plt.suptitle("All The Data")

plt.show()