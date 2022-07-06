"""
Creating a masked array using the
numpy.ma subpackage
In most situations, real-life data is noisy and messy. It contains lots of gaps or missing
characters in the data. Masked arrays are helpful in such cases and handle the issue.
Masked arrays may contain invalid and missing values. The numpy.ma subpackage offers
all the masked array-required functionality. In this section of the chapter, we will use the
face image as the original image source and perform log mask operations.
Have a look at the following code block:
"""

# Import required library
import numpy as np
from scipy.misc import face
import matplotlib.pyplot as plt

face_image = face()
mask_random_array = np.random.randint(0, 3, size=face_image.shape)

fig, ax = plt.subplots(nrows=2, ncols=2)

# Display the Original Image
plt.subplot(2, 2, 1)
plt.imshow(face_image)
plt.title("Original Image")
plt.axis('off')

# Display masked array
masked_array = np.ma.array(face_image, mask=mask_random_array)
plt.subplot(2, 2, 2)
plt.title("Masked Array")
plt.imshow(masked_array)
plt.axis('off')

# Log operation on original image
plt.subplot(2, 2, 3)
plt.title("Log Operation on Original")
plt.imshow(np.ma.log(face_image).astype('uint8'))
plt.axis('off')

# Log operation on masked array
plt.subplot(2, 2, 4)
plt.title("Log Operation on Masked")
plt.imshow(np.ma.log(masked_array).astype('uint8'))
plt.axis('off')

# Display the subplots
plt.show()

"""
In the preceding code block, we first loaded the face image from the scipy.misc
subpackage and created a random mask using the randint() function. Then, we applied
the random mask on the face image. After this, we applied the log operation on the original
face image and masked face image. Finally, we displayed all the images in 2*2 subplots.
You can also try a range of mask operations on the image from the numpy.ma subpackage.
Here, we are only focusing on the log operation of the masked array. That is all about basic
linear algebra concepts.
"""
