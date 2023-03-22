import cv2

decode = cv2.QRCodeDetector()
val = decode.detectAndDecode(cv2.imread("My_1st_QR.png"))

print("Decoded text is: ", val)