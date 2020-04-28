"""visualization.py

The BBoxVisualization class implements drawing of nice looking
bounding boxes based on object detection results.
"""


import numpy as np
import cv2


# Constants
ALPHA = 0.5
FONT = cv2.FONT_HERSHEY_PLAIN
TEXT_SCALE = 1.0
TEXT_THICKNESS = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def gen_colors(num_colors):
    """Generate different colors.

    # Arguments
      num_colors: total number of colors/classes.

    # Output
      bgrs: a list of (B, G, R) tuples which correspond to each of
            the colors/classes.
    """
    import random
    import colorsys

    hsvs = [[float(x) / num_colors, 1., 0.7] for x in range(num_colors)]
    random.seed(1234)
    random.shuffle(hsvs)
    rgbs = list(map(lambda x: list(colorsys.hsv_to_rgb(*x)), hsvs))
    bgrs = [(int(rgb[2] * 255), int(rgb[1] * 255),  int(rgb[0] * 255))
            for rgb in rgbs]
    return bgrs


def draw_boxed_text(img, text, topleft, color):
    """Draw a transluent boxed text in white, overlayed on top of a
    colored patch surrounded by a black border. FONT, TEXT_SCALE,
    TEXT_THICKNESS and ALPHA values are constants (fixed) as defined
    on top.

    # Arguments
      img: the input image as a numpy array.
      text: the text to be drawn.
      topleft: XY coordinate of the topleft corner of the boxed text.
      color: color of the patch, i.e. background of the text.

    # Output
      img: note the original image is modified inplace.
    """
    assert img.dtype == np.uint8
    img_h, img_w, _ = img.shape
    if topleft[0] >= img_w or topleft[1] >= img_h:
        return img
    margin = 3
    size = cv2.getTextSize(text, FONT, TEXT_SCALE, TEXT_THICKNESS)
    w = size[0][0] + margin * 2
    h = size[0][1] + margin * 2
    # the patch is used to draw boxed text
    patch = np.zeros((h, w, 3), dtype=np.uint8)
    patch[...] = color
    cv2.putText(patch, text, (margin+1, h-margin+2), FONT, TEXT_SCALE,
                WHITE, thickness=TEXT_THICKNESS, lineType=cv2.LINE_8)
    cv2.rectangle(patch, (0, 0), (w-1, h-1), BLACK, thickness=1)
    w = min(w, img_w - topleft[0])  # clip overlay at image boundary
    h = min(h, img_h - topleft[1])
    # Overlay the boxed text onto region of interest (roi) in img
    roi = img[topleft[1]:topleft[1]+h, topleft[0]:topleft[0]+w, :]
    cv2.addWeighted(patch[0:h, 0:w, :], ALPHA, roi, 1 - ALPHA, 0, roi)
    return img


class BBoxVisualization():
    """BBoxVisualization class implements nice drawing of boudning boxes.

    # Arguments
      cls_dict: a dictionary used to translate class id to its name.
    """

    def __init__(self, cls_dict):
        self.cls_dict = cls_dict
        self.colors = gen_colors(len(cls_dict))

    def draw_bboxes(self, img, box, conf, cls, mqtt_client):
        """Draw detected bounding boxes on the original image."""
        count = 1
        defect_index = []
        severity = []
        location_x = []
        location_y = []
        defect_length = []
        defect_width = []
        defect_size = []
        for bb, cf, cl in zip(box, conf, cls):
            cl = int(cl)
            y_min, x_min, y_max, x_max = bb[0], bb[1], bb[2], bb[3] 
            img_h, img_w, _ = img.shape
            length = y_max-y_min
            width = x_max - x_min
            box_size = length * width

              
            """
                1) Num of defects x1
                2) wait for 6 message per defects x6
                3) recieve another defects x6
            """
  

            
            """
            i = int(img_h-(img_h*0.05))
            cv2.rectangle(img, (0,i), (img_w, img_h), (0, 0, 0), -1)
            # ABC:123
            cv2.putText(img, "Discontinuity_1  Severity:    Location:        Length:    Width:    Size:    ", (10, i), cv2.FONT_HERSHEY_SIMPLEX,0.3, (225, 255, 255), 1, cv2.LINE_AA)
            
            #(x_min),(y_max)
            cv2.putText(img, str(x_min), (60, i), cv2.FONT_HERSHEY_SIMPLEX,0.3, (225, 255, 255), 1, cv2.LINE_AA) 
            cv2.putText(img, str(y_min), (120, i), cv2.FONT_HERSHEY_SIMPLEX,0.3, (225, 255, 255), 1, cv2.LINE_AA)

            #(y_max-y_min)*(x_max-x_min)
            cv2.putText(img, str((y_max-y_min)*(x_max-x_min)), (100, 10), cv2.FONT_HERSHEY_SIMPLEX,1, (225, 255, 255), 1, cv2.LINE_AA)
            """
            color = self.colors[cl]
            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, 2)
            txt_loc = (max(x_min+2, 0), max(y_min+2, 0))
            cv2.putText(img, str(count), (max(x_max-30, 0), max(y_min+30, 0)), cv2.FONT_HERSHEY_SIMPLEX,0.8,color, 2, cv2.LINE_AA)
            cls_name = self.cls_dict.get(cl, 'CLS{}'.format(cl))
            txt = '{} {:.2f}'.format(cls_name, cf)
            print("Discontinuity_{}  Severity:{} Location:({},{}) Length:{} Width:{} Size:{}".format(count,cls_name,x_min/12.5,(img_h-y_max)/12.5,length/12.5,width/12.5,box_size/156.25)) 
            img = draw_boxed_text(img, txt, txt_loc, color)
            defect_index.append(count)
            severity.append(str(cls_name))
            location_x.append(x_min)
            location_y.append(img_h-y_max)
            defect_length.append(length)
            defect_width.append(width)
            defect_size.append(box_size)  
            count+=1
        count = count - 1
        mqtt_client.publish("topic/test", str(count))
        j = 0
        for j in range(0,count):
            print("Sent defect {}".format(j))
            mqtt_client.publish("topic/test", str(severity[j]))
            temp = round((location_x[j]/12.5),2)
            mqtt_client.publish("topic/test", str(temp))
            temp = round((location_y[j]/12.5),2)
            mqtt_client.publish("topic/test", str(temp))
            temp = round((defect_length[j]/12.5),2)
            mqtt_client.publish("topic/test", str(temp))
            temp = round((defect_width[j]/12.5),2)
            mqtt_client.publish("topic/test", str(temp))
            temp = round((defect_size[j]/156.25),2)
            mqtt_client.publish("topic/test", str(temp))
            mqtt_client.publish("topic/test", str(999))

        print("Image HxW: {} x {}".format(img_h,img_w))
        print("Number of object = {}".format(count))
        print("\r\n")
        cv2.imwrite('image_raw.jpg', img) 
        return img
'''
# Border  

   
# Reading an image in default mode 
img1 = cv2.imread(img) 
   
# Window name in which image is displayed 
window_name = 'Img'
  
# Using cv2.copyMakeBorder() method 
image = cv2.copyMakeBorder(img1, 3, 3, 3, 3, cv2.BORDER_CONSTANT,(0,0,0)) 
  
# Displaying the image  
cv2.imshow(window_name, img1) 
cv2.imwrite('Border_image_01.jpg', img1)

#Overlay
s_img = cv2.imread(img1)
l_img = cv2.imread("/home/developer/workspace/tf_trt_models/Report format background.jpg")
x_offset=110
y_offset=270
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
cv2.imwrite('Report_1_1.jpg', l_img) 

'''




 
