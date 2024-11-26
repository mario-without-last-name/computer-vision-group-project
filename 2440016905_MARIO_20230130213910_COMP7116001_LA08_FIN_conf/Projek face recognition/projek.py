import cv2 
import numpy as np
import face_recognition

# ambil gambar dari file yang uda di sediain
imgTrain = face_recognition.load_image_file('./jennyTraining.jpg')
# ubah warna gambar tersebut menjadi rgb
imgTrain = cv2.cvtColor(imgTrain, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('./ImageAttendance/jenny.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# mencari lokasi wajah
faceLoc = face_recognition.face_locations(imgTrain)[0]
encodeTrain = face_recognition.face_encodings(imgTrain)[0]
# memberikan kotak kepada lokasi wajah yang telah di temukan
cv2.rectangle(imgTrain, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

#Ini untuk mengecek apakah wajahnya itu sama atau tidak
results = face_recognition.compare_faces([encodeTrain], encodeTest)
#Semakin pendek jaraknya maka semakin mirip mukanya
faceDis = face_recognition.face_distance([encodeTrain], encodeTest)

# memberikan tulisan pada gambar apakah sama(true) atau tidak(false) 
# dan jarak kemiripan antara gambar test dengan Train
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 2)

# menampilkan gambar Train dan test
cv2.imshow('Train', imgTrain)
cv2.imshow('Test', imgTest)
cv2.waitKey(0)


