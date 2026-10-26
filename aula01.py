import cv2
imagem = cv2.imread('teste.jpg') #Processa minha imagem em pixels e armazena dentro de imagem
cv2.imshow('Primeira imagem', imagem) #Processa minha imagem e mostra na tela
cv2.waitKey(0)
cv2.destroyAllWindows()
print(imagem.shape) #Mede o tamanho da minha imagem