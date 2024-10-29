import ctypes
from PIL import Image
import os

# C program dll file
sourceDirectory = os.getcwd()
pixelUpdate = ctypes.CDLL(os.path.join(sourceDirectory, "pixelUpdate.dll"))

# Image pixel value extraction
image = Image.open("Sample Image/Sample3.jpg", 'r')
pixel_data = list(image.getdata())

# Width and height
width = image.size[0]
height = image.size[1]
size = len(pixel_data)

# Setting up the function
Update = pixelUpdate.Update
Update.restype = ctypes.POINTER(ctypes.c_int)
Update.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]

# Directly passing the python list does not work
# Need to make a C array to pass the values
pixelR_p = (ctypes.c_int * size)(*([x[0] for x in pixel_data]))
pixelG_p = (ctypes.c_int * size)(*([x[1] for x in pixel_data]))
pixelB_p = (ctypes.c_int * size)(*([x[2] for x in pixel_data]))


# Calling the function
new_pixelR_p = Update(pixelR_p, width, height)
new_pixelR = new_pixelR_p[:size]
pixelUpdate.Free(new_pixelR_p)

new_pixelG_p = Update(pixelG_p, width, height)
new_pixelG = new_pixelG_p[:size]
pixelUpdate.Free(new_pixelG_p)

new_pixelB_p = Update(pixelB_p, width, height)
new_pixelB = new_pixelB_p[:size]
pixelUpdate.Free(new_pixelB_p)


# Tuple of RGB pixel value
new_pixel_data = list(zip(list(new_pixelR), list(new_pixelG), list(new_pixelB)))

# Saving the Image 
new_image = Image.new("RGB", (width, height))
new_image.putdata(new_pixel_data)
new_image.save("output.jpg")