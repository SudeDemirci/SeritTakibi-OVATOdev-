import cv2
import numpy as np

# Resmi tanımlıyoruz
resim = cv2.imread('yol8.jpg')

# Beyaz şeritleri algılaması için renk filtrelemesi
alt_beyaz = np.array([0, 0, 200], dtype=np.uint8)
ust_beyaz = np.array([180, 40, 255], dtype=np.uint8)

hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

# Sarı, yeşil ve gri renkleri algılamaması için renk filtrelemesi
alt_sari = np.array([0, 0, 0], dtype=np.uint8)
ust_sari = np.array([0, 0, 0], dtype=np.uint8)

alt_yesil = np.array([0, 0, 0], dtype=np.uint8)
ust_yesil = np.array([0, 0, 0], dtype=np.uint8)

alt_gri = np.array([0, 0, 0], dtype=np.uint8)
ust_gri = np.array([0, 0, 0], dtype=np.uint8)

# Beyaz renkten başka bir renk algılamaması için renk filtrelemesi
beyaz_maske = cv2.inRange(hsv_resim, alt_beyaz, ust_beyaz)


sadece_beyaz_bolgeler = cv2.bitwise_and(resim, resim, mask=beyaz_maske)

kenarlar = cv2.Canny(sadece_beyaz_bolgeler, 50, 150)

cizgiler = cv2.HoughLinesP(kenarlar, 1, np.pi / 180, threshold=50, minLineLength=10, maxLineGap=10)

# Şeritleri fotoğrafa çizmek için
for cizgi in cizgiler:
    x1, y1, x2, y2 = cizgi[0]
    cv2.line(resim, (x1, y1), (x2, y2), (0, 255, 0), 2)  

cv2.imshow('Yol Seritli', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
