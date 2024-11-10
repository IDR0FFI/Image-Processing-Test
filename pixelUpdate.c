#include <stdio.h>
#include <stdlib.h>

int Avg(int* pixel, int row, int column, int width, int height){
	int sum=0, range=1;
	//Range value should be equal to 2 for 5x5 matrix and 1 for 3x3 matrix.
	/*int matrix[5][5] = {
		{-2, -2, -2, -2, -2},
		{-2, -1, -1, -1, -2},
		{-2, -1, 40, -1, -2},
		{-2, -1, -1, -1, -2},
		{-2, -2, -2, -2, -2}
	};*/

	int matrix[3][3] = {
		{1, 1, 1},
		{1, 1, 1},
		{1, 1, 1}
	};
	
	for (int i=-range; i<=range; i++){
		for (int j=-range; j<=range; j++){
			//Out of bounds condition : start
			if ((row+i)<0 || (column+j)<0){
	  			sum += 0;
	  		}
	  		else if((row+i)>=height || (column+j)>=width){
	  			sum += 0;
	  		}
			// end

	  		else {
	  			sum += (*(pixel + i*width + j))*matrix[range+i][range+j];
	  		}
		}
	}
	return sum;
}

int* Update(int* pixel, int width, int height){
	// Allocating memory for the updated array of pixel
	int size = width*height;
	int* new_pixel = (int*)malloc(size*sizeof(int));
	
	//Iterating over each pixel value
	for (int i=0; i<width*height; i++){
		new_pixel[i] = Avg(pixel, i/width, i%width, width, height);
		pixel++;
	}

	return new_pixel;
}

void Free(int* arr){
	free(arr);
}