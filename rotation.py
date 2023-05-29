#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import the Python Image
# processing Library
from PIL import Image

# Giving The Original image Directory
# Specified
Original_Image = Image.open("C:/Users/CCL/Downloads/CannyFish.jpg")

# Rotate Image By 180 Degree
rotated_image1 = Original_Image.rotate(180)

# This is Alternative Syntax To Rotate
# The Image
rotated_image2 = Original_Image.transpose(Image.ROTATE_90)

# This Will Rotate Image By 60 Degree
rotated_image3 = Original_Image.rotate(-45)
rotated_image4= Original_Image.rotate(-270)


rotated_image1.show()
rotated_image2.show()
rotated_image3.show()
rotated_image4.show()



# In[ ]:




