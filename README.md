# Phased array Ultrasonic (PAUT) inspection Defect detection using Single Shot MultiBox Detector (SSD) network

This project aims to develop a system by using convolutional neutral network (CNN) to detect defects in the composite laminates automatically in order to increase the accuracy and efficiently in ultrasonic inspection: the autonomous inspection system will be mainly focus on the requirement of international aviation standards. In the aviation industry, ultrasonic testing (UT) is a reliable method to examine the integrity of composites components. Meanwhile, the phased-array probes are commonly are utilised to boost the inspection process and visualize the scanning result. Delamination, which is critical failure mode to the composite material, will be the training dataset used in this project. Hence, this inspection system is not applicable for a non-laminate defects, such as linear crack.

In order to achieve the project goal, integration of programme codes is the key elements. Autonomous inspection system is a complex and multidisciplinary system. therefore, it is not practical and realistic to be completed by a low-level system, like automatic UT scanner or a high-level system, such as detection program independently. System integration and cooperation are essential elements. Generally, advanced systems focus on complex calculations, which is detection algorithms. The underlying system focuses on direct motion control. At the same time, communication is established between the two layers for cooperation. In this project, due to the limited duration and resource, it will focus on the high-level system development.

There are some other advantages from this system development except for ultrasonic images defect detection. In this project, the delamination defect images of ultrasonic inspection are used. Other kinds of defects or inspection methods, such as thermography inspection, images can be the dataset of the Single Shot MultiBox Detector (SSD) network to evaluate the components and specimens in the industries. As the result, it can improve the efficiency of the inspection processes.


# Expected outcomes

 Identify discontinuities and classify the defects into two main categories by severity on the ultrasonic C-scan images
 Locate and size the discontinuities in the ultrasonic C-scan images
 Build a convolutional neural network-based defect detection model for ultrasonic C-scan
 Gather the network inference results and defect information in the inspection report

![image]()

