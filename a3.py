'''
Created on Nov. 1, 2022

@author: dancrha
'''

import os

from PIL import Image

import cv2

import numpy as np 

''''
References:
www.geeksforgeeks.org
https://python.plainenglish.io/image-filtering-and-editing-in-python-with-code-e878d2a4415d

'''

# convert the image color in to black and white
img = Image.open("Images").convert("L")
image_array = np.array(img)

height, width = image_array.shape

# loop through the image array and change every pixel to black and white.
for i in range(0, height): 
# we need  a nested loop to address both height and width of the pixels. 
    for j in range(0, width): 
        '''
        #compare every index and see if they are black if not 
        change them to black or white accordingly 
        '''  
        if image_array[i][j] <= 127: 
            image_array[i][j] = 0  # this is to turn into black 
        elif (image_array[i][j] > 127): 
            image_array[i][j] = 255  # this is to turn into white 
result = Image.fromarray(image_array, "L")
result.save("result.png")

x_val = []
y_val = [] 
z_val = [] 
'''
a module named 'blackAndwhite.py' used to convert the imgaes in to black and 
white, you may refer to it as it is attached with A3. 
store the converted image in to 'palms'folder.
'''
dir1 = 'palms'  
for img in os.listdir(dir1):
    path = os.path.join(dir1, img)
    # we know the image is present
    if os.path.isfile(path):
        # open the image
        image = cv2.imread(path)
        # for half the image analysis, we split the image in two part.
        [original_y, original_x, _] = image.shape
        # the splits images are orginial_y and original_x.
        
        max_x, max_y, min_x, min_y = 0, 0, original_x, original_y
        
        for i in range(original_x):
            # loop via x values(could mean the row value)
            for j in range(original_y):
                # loop via y values(could mean the col value of the images pixels)
                colour = image[j][i]
                # store the image pixel index at i and j in to a variable called colour.
                if colour[0] <= 52 and colour[1] <= 52 and colour[2] <= 54:
                # if the stored pixels at the above index, it compute the min and max values in tore them in variable accordingly 
                    max_x = max(max_x, i)
                    max_y = max(max_y, j)
                    min_x = min(min_x, i)
                    min_y = min(min_y, j)
        # save all the x values --> aspect ratio width/height
        x_val.append(float(abs(max_x - min_x) / abs(max_y - min_y)))
        centre = int(0.5 * (max_x - min_x))
        centre += min_x
        # left image
        counter = 0
        for i in range(min_x, centre):
            for j in range(min_y, max_y):
                colour = image[j][i]
                # pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2] <= 54:
                    # increment the counter 
                    counter += 1        
                    
        y_val.append(float(counter / (abs(max_x - min_x) * abs(max_y - min_y))))
        
            # right image
        counter = 0
        for i in range(centre, max_x):
            for j in range(min_y, max_y):
                colour = image[j][i]
                # pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2] <= 54:
                    counter += 1
        z_val.append(float(counter / (abs(max_x - min_x) * abs(max_y - min_y))))

print(" x |  \t y  |  \t |  z")
print('------------------------')
for i in range(len(x_val) - 1):
    print("{:0.2f} |  {:0.2f} |  {:0.2f}".format(x_val[i], y_val[i], z_val[i]))
