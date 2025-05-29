%Example 1

% MATLAB code for convert images in YIQ format 
% Reading the Original image and 
% converting to YIQ format. 
% This YIQ format image will be
% effectively used as input. 
% Make sure the image file path is in
% the same directory as code. 
I = imread('GFG.jpeg'); 
J = rgb2ntsc(I);

% Creating figure window for the input image
% Displaying the input image
figure;
imshow(J);

% Converting YIQ to RGB 
K = ntsc2rgb(J);

% Displaying the RGB Image 
figure;
imshow(K);

%Example 2

% MATLAB code 
% Reading the Original image and converting 
% to YIQ format. This YIQ format image will 
% be effectively used as input. 
I = imread('lighthouse.png'); 
J = rgb2ntsc(I);

% Creating figure window for the input image
% Displaying the input image
figure;
imshow(J);

% Converting YIQ to RGB 
K = ntsc2rgb(J);

% Displaying the RGB Image 
figure;
imshow(K);

