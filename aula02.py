import cv2

cap = cv2.VideoCapture(0) #Indice 0 seria minha webcam principal
largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'XVID')
#nome do arquvio, codec, frame rate, tamanho L A
gravador = cv2.VideoWriter('video_01.avi', codec, 20, (largura, altura))

while True:
    ret,frame = cap.read() #ret armazena o booleano e o frame armazena o frame mesmo
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gravador.write(frame)
    if not ret: #se ret não armazenar os booleanos ele vai printar erro e fechar tudo
        print('Erro na captura')
        break

    #cv2.imshow('Captura de imagem_cor', frame) 
    cv2.imshow('Captura de imagem_cinza', frame_gray) #exibe a imagem da nossa webcam

    if cv2.waitKey(1) & 0xFF == ord('q'): #faz ele ter um atraso de 1ms e adiciona a função de fechar com a tecla "q"
        break

cap.release()
cv2.destroyAllWindows()
gravador.release()