from requests import get
from gis import KmltoPd
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
import easyCV as cv

key = 'AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc'

df = KmltoPd('new.csv')

for name in df.getKeys():
    print(name)
    if not os.path.exists(name):
        os.makedirs(name)
    for d in df.generate(name):
        print(d[0], d[1])
        for heading in range(0, 360, 60):
            gurl = "https://maps.googleapis.com/maps/api/streetview?size=600x540&location={0},{1}&fov=120&heading={2}&pitch=10&key={3}".format(d[0], d[1], heading, key)
            r = get(gurl, stream=True)
            mg = Image.open(io.BytesIO(r.content))
            image = np.array(mg)
            plt.imsave('{0}/{1}_{2}_{3}.jpg'.format(name,name,d[0],
                                                    heading),
                       image)
            cv.imshow('frame', cv.cvtColor(image, cv.COLOR_BGR2RGB))
            cv.waitKey(1)

cv.destroyAllWindows()
