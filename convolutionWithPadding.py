import numpy as np

img_size = (300,300)

kernel_size = (4,4)

img = np.random.randint(0,255,img_size,dtype = int)
kernel = np.ones(kernel_size)

output = np.zeros(img_size)

padding_h = kernel_size[0]//2
padding_w = kernel_size[1]//2

padded_img = np.pad(img, (padding_h,padding_w), mode='constant', constant_values = 0)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        
        window = padded_img[i:i+kernel_size[0],j:j+kernel_size[1]]
        output[i,j] = np.sum(window*kernel)
