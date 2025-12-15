import numpy as np

img_size = (200,400)

kernel_size = (3,3)

kernel = np.ones(kernel_size)

img = np.random.randint(0,255,img_size,dtype =int)

out_h = img_size[0]-kernel_size[0]+1
out_w = img_size[1]-kernel_size[1]+1

output = np.zeros((out_h,out_w))

for i in range(out_h):
    for j in range(out_w):
        
        window = img[i:i+kernel_size[0], j:j+kernel_size[1]]
        
        output[i,j] =np.sum(window*kernel)
