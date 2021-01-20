# Phased array Ultrasonic (PAUT) inspection Defect detection using Single Shot MultiBox Detector (SSD) network

  This project aims to develop a system by using convolutional neutral network (CNN) to detect defects in the composite laminates automatically in order to increase the accuracy and efficiently in ultrasonic inspection.

  In this project, the delamination defect images of ultrasonic inspection are used. Other kinds of defects or inspection methods, such as thermography inspection, images can be the dataset of the Single Shot MultiBox Detector (SSD) network to evaluate the components and specimens in the industries. As the result, it can improve the efficiency of the inspection processes.

# 1. Expected outcomes

Identify discontinuities and classify the defects into two main categories by severity on the ultrasonic C-scan images
Locate and size the discontinuities in the ultrasonic C-scan images
Build a convolutional neural network-based defect detection model for ultrasonic C-scan
Gather the network inference results and defect information in the inspection report

![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/objective.png)

# 2. Methodology
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/Methodology.png)

# 2.1Dataset Preparation 
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/Dataset%20preparation.png)

# 2.2 Hardware
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/Hardware.png)

# 2.3 Configuration 
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/Configuration.png)

# 2.4 Software
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/software.png)

# 2.5 Training Overview
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/Training%20overview.png)

# 2.6 System Overview
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/reporting%20system.png)

# 2.7 Report example
![image](https://github.com/jasonngai01/UTPA_SSD/blob/master/image/Inspection%20report%20example.png)

# 3. Usage

3.1 Usage of scripts
1. Jason_Demo_FYP_Auto.sh: To execute all the prgram function automatically
2. Carmera_tf_trt.py: To execute the defect detection function
3. Resize_image.py: Resize the input image
4. Visualization.py: To generate the boundary boxes information
5. MQTT_Subscriber.py: To receive the defect information from camera_tf_trt.py
6. Image_list.csv: To store the input image information




