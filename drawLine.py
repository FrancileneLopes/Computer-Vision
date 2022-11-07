# Desenhando uma linha

import cv2

img = cv2.imread('nazare.jpg')

# imagem, coordenadas de inicio, cordenadas de fim, cor, grossura
cv2.line(img, (9, 9), (89, 89), (180, 150, 65), 8)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()