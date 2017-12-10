from requests import get
import numpy as np
from PIL import Image
import io
import cv2 as cv

key = 'AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc'

lat = input('latitude: ')
lon = input('longitude: ')

head = input('heading level: ')
cnt = 1
for heading in range(0,360,int(head)):
    gurl = "https://maps.googleapis.com/maps/api/streetview?size" \
           "=600x540" \
           "&location="+lat+"," \
           + lon+ "&fov=120&heading="+str(heading)+"&pitch=0&key" \
                                                     "=AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc"
    r = get(gurl, stream=True)
    mg = Image.open(io.BytesIO(r.content))
    image=np.array(mg)
    finimg = cv.cvtColor(image,cv.COLOR_BGR2RGB)
    cv.imshow('frame',finimg)
    filnam = "ID"+str(cnt)+".png"
    print("Saving Image as "+filnam)
    cv.imwrite(filnam,finimg)
    cnt = cnt+1
    cv.waitKey(1)

cv.waitKey(0)
cv.destroyAllWindows()