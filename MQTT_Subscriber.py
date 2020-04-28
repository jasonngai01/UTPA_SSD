#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import cv2
import csv

raw_path = '/home/developer/workspace/tf_trt_models/image_raw.jpg'
raw_image = cv2.imread(raw_path)
window_name = 'Image'
boarder_image = cv2.copyMakeBorder(raw_image, 3, 3, 3, 3, cv2.BORDER_CONSTANT,(119,119,119))
#cv2.imshow('border_image',boarder_image)

# This is the Subscriber
stage = 0
message_buf = []
total_num = 0



"""
stage 0 -> expect total number of defects
stage 1 -> messages of a defect (Severity)
stage 2 -> messages of a defect (Location_x)
stage 3 -> messages of a defect (Location_y)
stage 4 -> messages of a defect (Length)
stage 5 -> messages of a defect (Width)
stage 6 -> messages of a defect (Size)
stage 7 -> end of packets 999
"""

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/test")

def on_message(client, userdata, msg):
    global message_buff
    ai_message = msg.payload.decode()
    message_buf.append(ai_message)
    #print(int(message_buf[0]))
    #print(message_buf)
    limit = 7*(int(message_buf[0]))+1
    if(len(message_buf) == limit):
        print("All Packets Received")
        print("===========================================================")
        print("General Info:")
        background = cv2.imread('/home/developer/workspace/mqtt/background.jpg')
        print("Total packets = {}\r\n".format(message_buf[0]))
        j = 0
        j_limit = int(message_buf[0])+1
        while(j<j_limit):
            intervals = 8+7*(j-2)
            print(j)
            if(j==1):
                print("Discontinuity_{}  Severity:{} Location:({},{}) Length:{} Width:{} Size:{}".format(j,message_buf[1],message_buf[2],message_buf[3],message_buf[4],message_buf[5],message_buf[6],message_buf[7]))
                message1 = message_buf[1] + "    " + message_buf[2] + "," + message_buf[3] + "   " + message_buf[4] + "    " + message_buf[5] + "   " + message_buf[6]
                cv2.putText(background, message1, (290, 836), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 1, cv2.LINE_AA)
            if((j>1)and(j<5)):
                print("Discontinuity_{}  Severity:{} Location:({},{}) Length:{} Width:{} Size:{}".format(j,message_buf[intervals],message_buf[1+intervals],message_buf[2+intervals],message_buf[3+intervals],message_buf[4+intervals],message_buf[5+intervals],message_buf[6+intervals]))
                message2 = message_buf[0+intervals] + "    " + message_buf[1+intervals] + "," + message_buf[2+intervals] + "   " + message_buf[3+intervals] + "    " + message_buf[4+intervals] + "   " + message_buf[5+intervals]
                cv2.putText(background, message2, (290, (856+20*(j-2))), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 1, cv2.LINE_AA)
            print("===========================================================")
            j+=1
        #cv2.imshow("test",background)
        with open('image_list.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                print(row)
        x_offset=110
        y_offset=270
        global boarder_image
        background[y_offset:y_offset+boarder_image.shape[0], x_offset:x_offset+boarder_image.shape[1]] = boarder_image
        saved_name = 'Report_'+row[0]+'.jpg'
        print("Successfully written to :",saved_name)
        cv2.imwrite(saved_name,background)
        cv2.imshow('Report',background)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        client.disconnect()


    
client = mqtt.Client()
client.connect("192.168.0.143",1883,60)

client.on_connect = on_connect
client.on_message = on_message





 

client.loop_forever()
