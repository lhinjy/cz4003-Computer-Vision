% 2.1 Contrast Stretching

% A
Pc = imread('mrt-train.jpg');
whos Pc
P = rgb2gray(Pc);

% B
figure
imshow(P);

% C
min(P(:)),max(P(:))

% D
P1 = imsubtract(P,13);
P2 = (255/(204-13))*P1;
figure
imshow(P2)
min(P2(:)), max(P2(:))

% E
figure
imshow(P2);
figure
imshow(P2, []);
	
    
    
    
% 2.2 Histogram Equalization

% A
figure
imhist(P,10)
figure
imhist(P, 256)

% B
P3 = histeq(P,255);
figure
imhist(P3, 10)
figure
imhist(P3,256)
    
% C
P4 = histeq(P,255);
figure
imhist(P4, 10)
figure
imhist(P4,256)

    
    
    

% 2.3 Linear Spatial Filtering

% A
h1 = fspecial('gaussian', 5, 1);
h2 = fspecial('gaussian', 5, 2);
sum(h1,'all')
sum(h2,'all')
figure
mesh(h1)
figure
mesh(h2)

% B
LSF = imread('ntu-gn.jpg');
figure
imshow(LSF);
    
% C
LSF1 = uint8(conv2(LSF,h1));
figure
imshow(LSF1);
LSF2 = uint8(conv2(LSF,h2));
figure
imshow(LSF2);

% D
LSF3 = imread('ntu-sp.jpg');
figure
imshow(LSF3);

% E
LSF4 = uint8(conv2(LSF3,h1));
figure
imshow(LSF4);
LSF5 = uint8(conv2(LSF3,h2));
figure
imshow(LSF5);
	
    
    

% 2.4 Median Filtering
LMF3= medfilt2(LSF3, [3 3]);
LMF5 = medfilt2(LSF3, [5 5]);
figure
imshow(LMF3)
figure
imshow(LMF5)


    
    
% 2.5 Suppressing Noise Interference Patterns

% A
NIP = imread('pck-int.jpg');
figure
imshow(NIP)

% B
F = fft2(NIP);
S = abs(F).^2;
figure
imagesc(fftshift(S.^0.1));
colormap('default')
figure
imagesc(S.^0.1);
     
% C
[x, y] = ginput(2)

% D
x1 = 9;
y1 = 241;
F(x1-2:x1+2, y1-2:y1+2)=0;
S = abs(F).^2;
figure
imagesc(fftshift(S.^0.1));
colormap('default');
    
   % Correcting the X, Y axis
x1 = 241;
y1 = 9;
x2 = 17;
y2 = 249;
F(x1-2:x1+2, y1-2:y1+2)=0;
F(x2-2:x2+2, y2-2:y2+2)=0;
S = abs(F).^2;
figure
imagesc(fftshift(S.^0.1));
colormap('default');

% E
FI = ifft2(F);
figure
imshow(FI);
FI = uint8(ifft2(F));
figure
imshow(FI);
    
F(x1-8:x1+8, y1-8:y1+8)=0;
F(x2-8:x2+8, y2-8:y2+8)=0;
FI2 = uint8(ifft2(F));
figure
imshow(FI2);
	
% F
PC = imread('primate-caged.jpg');
PCF = fft2(PC);
S = abs(PCF).^2;
figure
imagesc(fftshift(S.^0.1));
    
  % Convert image because the previous one didnt work
whos PC
PCI = rgb2gray(PC);
figure
imshow(PCI)
PCF = fft2(PCI);
S = abs(PCF).^2;
figure
imagesc(fftshift(S.^0.1));
	
[x,y] = ginput
   
 % 3x3 Neighbour elements 
PCF(252-1:252+1, 11-1:11+1) = 0;
PCF(248-1:248+1, 22-1:22+1) = 0;
PCF(243-1:243+1, 33-1:33+1) = 0;
PCF(6-1: 6+1, 247-1:247+1) = 0;
PCF(10-1:10+1, 237-1:237+1) = 0;
PCF(16-1:16+1, 247-1:247+1) = 0;
PCFI = uint8(ifft2(PCF));
figure
imshow(PCFI);
    
   % 5x5 Neighbour elements 
PCF(252-2:252+2, 11-2:11+2) = 0;
PCF(248-2:248+2, 22-2:22+2) = 0;
PCF(243-2:243+2, 33-2:33+2) = 0;
PCF(6-2: 6+2, 247-2:247+2) = 0;
PCF(10-2:10+2, 237-2:237+2) = 0;
PCF(16-2:16+2, 247-2:247+2) = 0;
PCFI = uint8(ifft2(PCF));
figure
imshow(PCFI);
        
  % 7x7 Neighbour elements 
PCF(252-3:252+3, 11-3:11+3) = 0;
PCF(248-3:248+3, 22-3:22+3) = 0;
PCF(243-3:243+3, 33-3:33+3) = 0;
PCF(6-3: 6+3, 247-3:247+3) = 0;
PCF(10-3:10+3, 237-3:237+3) = 0;
PCF(16-3:16+3, 247-3:247+3) = 0;
PCFI = uint8(ifft2(PCF));
figure
imshow(PCFI);
    
  % 9x9 Neighbour elements 
PCF(252-4:252+4, 11-4:11+4) = 0;
PCF(248-4:248+4, 22-4:22+4) = 0;
PCF(243-4:243+4, 33-4:33+4) = 0;
PCF(6-4: 6+4, 247-4:247+4) = 0;
PCF(10-4:10+4, 237-4:237+4) = 0;
PCF(16-4:16+4, 247-4:247+4) = 0;
PCFI = uint8(ifft2(PCF));
figure
imshow(PCFI);

   % 11x11 Neighbour elements 
PCF(252-5:252+5, 11-5:11+5) = 0;
PCF(248-5:248+5, 22-5:22+5) = 0;
PCF(243-5:243+5, 33-5:33+5) = 0;
PCF(6-5: 6+5, 247-5:247+5) = 0;
PCF(10-5:10+5, 237-5:237+5) = 0;
PCF(16-5:16+5, 247-5:247+5) = 0;
PCFI = uint8(ifft2(PCF));
figure
imshow(PCFI);
    
    
    

% 2.6 Undoing Perspective Distortion of Planar Surface

% A
Bk = imread('book.jpg');
figure
imshow(Bk);

% B
[X,Y] = ginput(4);

imageX = [0 210 210 0];
imageY = [0 0 297 297];

% C
A = [
  [X(1),Y(1),1,0,0,0, -imageX(1)*X(1),-imageX(1)*Y(1)];
  [0,0,0,X(1),Y(1),1, -imageY(1)*X(1),-imageY(1)*Y(1)];
  [X(2),Y(2),1,0,0,0, -imageX(2)*X(2),-imageX(2)*Y(2)];
  [0,0,0,X(2),Y(2),1, -imageY(2)*X(2),-imageY(2)*Y(2)];
  [X(3),Y(3),1,0,0,0, -imageX(3)*X(3),-imageX(3)*Y(3)];
  [0,0,0,X(3),Y(3),1, -imageY(3)*X(3),-imageY(3)*Y(3)];
  [X(4),Y(4),1,0,0,0, -imageX(4)*X(4),-imageX(4)*Y(4)];
  [0,0,0,X(4),Y(4),1, -imageY(4)*X(4),-imageY(4)*Y(4)];
];

v = [imageX(1); imageY(1); imageX(2); imageY(2); imageX(3); imageY(3); imageX(4); imageY(4)];
u = A \ v;
U = reshape([u;1], 3, 3)'; 
w = U*[X'; Y'; ones(1,4)];
w = w ./ (ones(3,1) * w(3,:));

% D
T = maketform('projective', U');
P2 = imtransform(Bk, T, 'XData', [0 210], 'YData', [0 297]);

% E
figure
imshow(P2);