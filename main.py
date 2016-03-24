import cv,sys

Name_File=sys.argv[1]

img=cv.LoadImage(Name_File,cv.CV_LOAD_IMAGE_GRAYSCALE)
img_th=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,1)

img_adth=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,3)

temp=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,3)

cv.NamedWindow("This will give image with contours")
cv.NamedWindow("Please Input the  Image")
cv.NamedWindow("Image with Contour wil be shown")

cv.Threshold(img,img_th,127,255,cv.CV_THRESH_BINARY_INV)

mem=cv.CreateMemStorage()
nc=cv.FindContours(img_th,mem,cv.CV_RETR_LIST,cv.CV_CHAIN_APPROX_SIMPLE,(0,0))	
print len(nc)

cv.DrawContours(img_adth,nc,cv.CV_RGB(255,0,0),cv.CV_RGB(0,255,0),2,2,8) 

cv.CvtColor(img,temp,cv.CV_GRAY2BGR)
cv.Add(temp,img_adth,temp)
cv.ShowImage("Input Image",img)
cv.ShowImage("Contour",img_adth)
cv.ShowImage("Image with Contour",temp)


if cv.WaitKey(0) % 0x100 == 27:
	cv.DestroyWindow("Input Image")
	cv.DestroyWindow("Contour")
	cv.DestroyWindow("Image with Contour")

