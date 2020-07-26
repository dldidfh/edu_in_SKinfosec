import numpy as np


# x = np.array([2,4,6,8])

# print("np.max(x) : {}".format(np.max(x)))
# print("np.min(x) : {}".format(np.min(x)))
# print("np.argmax(x) : {}".format(np.argmax(x)))
# print("np.argmin(x) : {}".format(np.argmin(x)))

a = np.ones([3,3])
print("a.shape : {}  \na : {}".format(a.shape,a))
b = np.zeros([3,2])
print("b.shape : {}  \nb : {}".format(b.shape,b))

# y = np.array([[2,4,6],[1,2,4],[0,5,8]])
# #열기준 최대 최소
# print("np.max(x) : {}".format(np.max(y, axis=0)))
# print("np.min(x) : {}".format(np.min(y, axis=0)))
# print("np.argmax(x) : {}".format(np.argmax(y, axis=0)))
# print("np.argmin(x) : {}".format(np.argmin(y, axis=0)))

# #행기준 최대 최소
# print("np.max(x) : {}".format(np.max(y, axis=1)))
# print("np.min(x) : {}".format(np.min(y, axis=1)))
# print("np.argmax(x) : {}".format(np.argmax(y, axis=1)))
# print("np.argmin(x) : {}".format(np.argmin(y, axis=1)))
