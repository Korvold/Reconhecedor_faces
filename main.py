import cv2 
import mediapipe as mp

#iniciar o opencv e o mediapipe

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Ler as informaçoes da WebCam
    verificador, frame = webcam.read()
    if not verificador:
        break
    # Reconhecer os rostos
    lista_rostos = reconhecedor_rostos.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenhar os rostos 
            desenho.draw_detection(frame, rosto)

    cv2.imshow("Detectador de faces", frame)

    #quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()