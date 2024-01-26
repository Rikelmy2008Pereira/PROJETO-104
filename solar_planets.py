import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
cv2.putText(img,"Mercurio",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Venus",(225,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Terra",(330,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Marte",(420,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Jupiter",(645,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Saturno",(845,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Urano",(1050,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(img,"Netuno",(1200,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)


cv2.imshow("resultado", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.destroyAllWindows()
