# importing cv2  
import cv2  
   
# path  
path = '/home/developer/workspace/tf_trt_models/image_raw.jpg'
   
# Reading an image in default mode 
image = cv2.imread(path) 
   
# Window name in which image is displayed 
window_name = 'Image'
  
# Using cv2.copyMakeBorder() method 
image = cv2.copyMakeBorder(image, 3, 3, 3, 3, cv2.BORDER_CONSTANT,(119,119,119)) 
  
# Displaying the image  
cv2.imshow(window_name, image) 
cv2.imwrite('Border_image.jpg', image) 



