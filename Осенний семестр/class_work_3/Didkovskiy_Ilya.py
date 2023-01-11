import numpy as np

a = np.array([1, 1, 5, 5, 1, 5, 7, 7, 5, 0, 9, 8, 7, 6, 5, 4, 3, 2, 10], int)

top1 = np.argmax(np.bincount(a))
kolvotop1 = sum(a == top1)
a = a[a != top1]

top2 = np.argmax(np.bincount(a))
kolvotop2 = sum(a == top2)
a = a[a != top2]

top3 = np.argmax(np.bincount(a))
kolvotop3 = sum(a == top3)
a = a[a != top3]
print("1: " + str(top1) + "; повторений: " + str(kolvotop1) + "\n" +
      "2: " + str(top2) + "; повторений: " + str(kolvotop2) + "\n" +
      "3: " + str(top3) + "; повторений: " + str(kolvotop3) + "\n")

