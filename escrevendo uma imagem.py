#Escrevendo uma imagem, transformando ela em escala de cinza e salvando com outra extensão

import cv2

img = cv2.imread('cachorro.jpg', cv2.IMREAD_GRAYSCALE) #Lembrar de colocar o "_" e as letras em maiúsculo
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Salva a imagem do cachorro colorido em uma cópia em Preto e branco (até msm com
#nova extensão se quiser
cv2.imwrite('Novaimagem.png', img)


