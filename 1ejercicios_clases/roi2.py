import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'tesseract'

image = cv2.imread('test.png')
text = pytesseract.image_to_string(image)
print('Texto: ', text)
cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()