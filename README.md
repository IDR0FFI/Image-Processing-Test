# Image-Processing-Test

## User Guide

The program extracts the pixel color(RGB) value using the Pillow library in python and the passes the data to the C program which can performs operation on the array like *Box Blur*, *Guassian Blur*, and *Edge Detection*.


To perform either of the matrix operation(as given below), first of all update the values inside the `pixelUpdate.c` file and create the `.dll` for it.

For windows : 
```CMD
gcc -o pixelUpdate.dll -shared pixelUpdate.c
```
**Make sure that the gcc compiler output file and python program have the same architecture. The already compiled file is of x64.**

Provide input file for the image. 

High resolution image supported.
~Make sure that you do not provide images with very high resolution as it does work(maybe around 245,000 pixel).~

# <hr>

### Matrix
If the Matrix is of 3x3 type than change the range value to 1, otherwise for 5x5 type change it to 2.

#### Box Blur
```C
int matrix[3][3] = {
    {1, 1, 1},
    {1, 1, 1},
    {1, 1, 1}
};
```
While returning the sum divide it by 9 i.e. the sum of all the matrix value.

#### Guassian Blur 3x3
```C
int matrix[3][3] = {
    {1, 2, 1},
    {2, 4, 4},
    {1, 2, 1}
};
```
Divide the sum by 16.

#### Guassian Blur 5x5
```C
int matrix[5][5] = {
    {1,  4,  6,  4, 1},
    {4, 16, 24, 16, 4},
    {6, 24, 36, 24, 6},
    {4, 16, 24, 16, 4},
    {1,  4,  6,  4, 1}
};
```
Divide the sum by 256.

#### Edge Detection 
```C
int matrix[3][3] = {
    {-1, -1, -1},
    {-1,  8, -1},
    {-1, -1, -1}
};
```
If you want to identify significant edges divide the sum value by some value.

# <hr>

End.