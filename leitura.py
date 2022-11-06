# ESTE SCRIPT FARÁ A LEITURA DE UMA IMAGEM COM A BIBLIOTECA DO OPENCV
# E EXIBIRÁ ALGUMAS INFORMAÇÕES SOBRE A IMAGEM

import cv2
print(cv2.__version__)

img = cv2.imread("nazare.jpg")
print(img)
print(img.shape)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
