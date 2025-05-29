>> % Reading  an RGB image file in MATLAB environment 
>> img=imread('apple.jpg');

>> % The above function will be called here
>> I=colouredToGray(img);
>> figure, imshow(I);