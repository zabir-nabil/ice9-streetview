from requests import get
from gis import KML2DICT
from PIL import Image
import logging
from threading import Thread
import os
import numpy as np
import matplotlib.pyplot as plt
import io


key = 'AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc'

loc='wards.kml'



class Dump(object):
    def __init__(self,key,loc,nop=10):
        self.key=key
        self.df = KML2DICT(loc)
        self.nop=nop
        self.threads=[]

        self.logger = logging.getLogger('imageDumper')
        hdlr = logging.FileHandler('fails.log')
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.WARNING)

    def listPartition(self,alist, partition):
        for i in range(0, len(alist), partition):
            yield alist[i:i + partition]


    def multiThread(self,names):

        for name in names:
            print(name)
            if not os.path.exists(name):
                os.makedirs(name)
            else:
                continue
            for d in self.df.generate(name):
                print(d[0], d[1])
                for heading in range(0, 360, 60):
                    gurl = "https://maps.googleapis.com/maps/api/streetview" \
                           "?size=640x640&location={0},{1}&fov=120&heading={2}&pitch=10&key={3}".format(d[0], d[1], heading,
                                                        self.key)
                    try:
                        r = get(gurl, stream=True)
                        mg = Image.open(io.BytesIO(r.content))
                        image = np.array(mg)
                        plt.imsave('{0}/{1}_{2}_{3}.jpg'.format(name,name,d[0],heading),image)

                    except:
                        self.logger.error("<{0},{1}> < {2} >".format(
                            d[0],d[1],name))
                        print('Failed!')
    def run(self):
        keys=list(self.df.getKeys())
        for nms in self.listPartition(keys, int(len(keys)/self.nop)):
            self.threads.append(Thread(target=self.multiThread,kwargs={
                'names':nms},
                   daemon=True))

        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()


a=Dump(key=key,loc=loc)

a.run()

