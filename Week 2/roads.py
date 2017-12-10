from requests import get
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
import easyCV as cv



roads_key = "AIzaSyArJa7wGdi-b35P6sXb66Fpj2drwkLUiEg"
roads_URL = "https://roads.googleapis.com/v1/snapToRoads?path=23" \
          ".772263," \
      "90.418274|23.770826,90.420516|23.770529," \
      "90.422790|23.767902,90.414880&interpolate=true&key={0}".format(
    roads_key)

maps_key = 'AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc'

positions = get(roads_URL)

jpos = json.loads(positions.text)

locations = []

for pos in jpos['snappedPoints']:
    locations.append(pos['location'])

for n, location in enumerate(locations[::2]):
    for heading in range(0, 360, 60):
        gurl = str("https://maps.googleapis.com/maps/api/streetview" \
                   "?size" \
                   "=600x540" \
                   "&location={0},{1}&fov=90&heading=" + str(
            heading) + "&pitch=10&key={2}").format(location['latitude'],
                                                 location[
                                                     'longitude'],maps_key)
        r = get(gurl, stream=True)
        mg = Image.open(io.BytesIO(r.content))
        image = np.array(mg)
        plt.imsave('roads/' + str(n) + '_' + str(heading) + '.jpg',
                   image)
        cv.imshow('frame', cv.cvtColor(image, cv.COLOR_BGR2RGB))
        cv.waitKey(1)

cv.destroyAllWindows()
