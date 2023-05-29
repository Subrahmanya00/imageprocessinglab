#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import matplotlib.pyplot as plt
import numpy as np



img1 = cv2.imread('C:/Users/CCL/Downloads/po.jfif', 0)


[m, n] = img1.shape
print('Image Shape:', m, n)


print('Original Image:')
plt.imshow(img1, cmap="gray")



f = 4


img2 = np.zeros((m//f, n//f), dtype=np.int)


for i in range(0, m, f):
	for j in range(0, n, f):
		try:

			img2[i//f][j//f] = img1[i][j]
		except IndexError:
			pass



print('Down Sampled Image:')
plt.imshow(img2, cmap="gray")



img3 = np.zeros((m, n), dtype=np.int)
# new size
for i in range(0, m-1, f):
	for j in range(0, n-1, f):
		img3[i, j] = img2[i//f][j//f]

# Nearest neighbour interpolation-Replication
# Replicating rows

for i in range(1, m-(f-1), f):
	for j in range(0, n-(f-1)):
		img3[i:i+(f-1), j] = img3[i-1, j]

# Replicating columns
for i in range(0, m-1):
	for j in range(1, n-1, f):
		img3[i, j:j+(f-1)] = img3[i, j-1]

# Plot the up sampled image
print('Up Sampled Image:')
plt.imshow(img3, cmap="gray")


# In[ ]:




