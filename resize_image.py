import cv2
import csv


print("Enter file name:")
image_name = input()
image_path = '/home/developer/workspace/image_validation/'
image_format = '.jpg'

final_path =  image_path + image_name + image_format
print("Confirm: {}".format(final_path))


with open('image_list.csv', 'w' ,newline='') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow([image_name,999])


img = cv2.imread(final_path, cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img)
 
width = 500
height = 500
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
cv2.imwrite('./input_image/Resized_image_01.jpg', resized) 
 
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

