% Matlab Code to convert an RGB 
% Image to Binary image reading image 
I = imread('GFG.jpeg');

% Creating figure window for input image
% Displaying the input image
imshow(I);

% Converting the image from rgb to
% binary using thresholding 
J = rgb2ntsc(I);

% Creating figure window for the output image
% Displaying the output image
imshow(J);