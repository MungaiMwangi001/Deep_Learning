% read the rgb image.
I = imread('leena.png');  

% convert it to gray image using rgb2gray() function.  
Ig = rgb2gray(I);    

% apply inbuilt otsu thresholding and
% convert the image to binary image.       
T = graythresh(Ig);         
Tg = T*255;  

% detect foreground and background
% pixels of the binary image.               
m = Ig > Tg                   
figure, imshow(m)  
       
I1 = I(:, :, 1);              
I2 = I(:, :, 2);
I3 = I(:, :, 3);
I1(~m) = 0;
I2(~m) = 0;

% in background pixels, take the third 
% channel and color it blue.
I3(~m) = 255;                 
In=cat(3, I1, I2, I3);
figure, imshow(In);