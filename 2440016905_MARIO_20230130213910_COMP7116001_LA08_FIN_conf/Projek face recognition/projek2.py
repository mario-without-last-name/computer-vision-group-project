import cv2 
import numpy as np
import face_recognition
import os
from datetime import datetime

#buat nampung gambar
path = 'ImageAttendance'
images = []
classNames = []
myList = os.listdir(path)

#Masukkin semua gambar dan class ke dalam list
for cls in myList:
    curImg = cv2.imread(path+'/'+cls)
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

#Encoding Function yang menghitung semua encodings dari gambar yang ada
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# membuat sebuah fungsi yang berfungsi untuk mengambil nama dan waktu untuk di tulis kedalam database
# dalam kasus ini kami menggunakan file csv atau excel
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            #Untuk ngambil namanya saja
            entry = line.split(',')
            nameList.append(entry[0])

        #Untuk ngambil waktu saat attendance    
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {dtString}')

# menyimpan data gambar(nama) kedalam variable encodeListKnown
encodeListKnown = findEncodings(images)

#Untuk mengambil image dari webcam
cap = cv2.VideoCapture(0)

# terus melakukan pengecekan selama webcam menyala
while True:
    success, img = cap.read()
    #Mereduce size dari gambar agar proses dapat berjalan lebih cepat
    imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Mencarri lokasi muka di dalam gambar pada webcam
    faceCurFrame = face_recognition.face_locations(imgS)
    #Mengencode gambar pada webcam
    encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # melakukan pengecekan antara gambar dari webcam dengan gambar yang telah kita simpan sebelumnya
    for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        #Mencari nilai index yang terkecil
        matchIndex = np.argmin(faceDis)

        #Menampilkan nama dari index yang terkecil
        if matches[matchIndex]:
            # name = classNames[matchIndex].upper()
            name = classNames[matchIndex]
            y1,x2,y2,x1 = faceLoc
            #Untuk menyesuaikan dengan gambar yang telah di resize
            # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            #Menandai wajah dengan kotak
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            #Menampilkan nama dari wajah yang terdeteksi
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            #Masukkin data attendace ke csv
            markAttendance(name)

    #Untuk menampilkan webcam
    cv2.imshow('webcam', img)
    cv2.waitKey(1)
    