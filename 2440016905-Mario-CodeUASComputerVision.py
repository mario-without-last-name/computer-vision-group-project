import cv2
import numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image1 = cv2.imread('avengers-5-characters-shang-chi_1.jpg')
image2 = cv2.imread('delay-mcu.jpg')
images = [image1, image2]

for image in images:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
    )

    for (x, y, w, h) in faces:
        rataRataTingkatKemerahan = 0
        tingkatKemerahan = 0
        for xx in range(x, x+w):
            for yy in range(y, y+h):
                biru, hijau, merah = image[yy, xx]
                if (int(merah) > int(hijau) + int(biru)):
                    tingkatKemerahan = tingkatKemerahan + (int(merah) - (int(hijau) + int(biru)))
        rataRataTingkatKemerahan = tingkatKemerahan / (w * h)
        print(round(rataRataTingkatKemerahan, 1))

        # cv2.imshow("A face from image", image[y:y+h, x:x+w])
        # cv2.waitKey(0)

        # cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)

        if (rataRataTingkatKemerahan >= 50):
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(image, 'MERAH', (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)
            cv2.putText(image, 'tidak merah', (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

# import cv2
# import numpy

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# image1 = cv2.imread('avengers-5-characters-shang-chi_1.jpg')
# image2 = cv2.imread('delay-mcu.jpg')
# images = [image1, image2]

# for image in images:
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(50, 50),
#         # flags = cv2.CV_HAAR_SCALE_IMAGE
#     )

#     for (x, y, w, h) in faces:
#         avg_color_per_row = numpy.average(image[y:y+h, x:x+w], axis=0)
#         avg_color = numpy.average(avg_color_per_row, axis=0)
#         # [blue green red]
#         print(avg_color)
#         # print(avg_color[2])
#         cv2.imshow("A face from image", image[y:y+h, x:x+w])
#         cv2.waitKey(0)
        
#         if ((avg_color[2] - (avg_color[1] + avg_color[0]) / 2) / avg_color[2] >= 0.5):
#             cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
#             cv2.putText(image, 'IS RED', (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
#         else:
#             cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)
#             cv2.putText(image, 'not red', (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    
#     cv2.imshow("Faces found", image)
#     cv2.waitKey(0)