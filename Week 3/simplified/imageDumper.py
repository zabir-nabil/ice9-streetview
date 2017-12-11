from gis import KML2DICT
import pickle as pkl
key = 'AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc'

df = KML2DICT('wards.kml')
dump={}
for name in df.getKeys():
    print(name)
    temp=[]
    for d in df.generate(name):
        for heading in range(0, 360, 60):
            gurl = "https://maps.googleapis.com/maps/api/streetview" \
                   "?size=640x640&location={0},{1}&fov=120&heading={2}&pitch=10&key={3}".format(d[0], d[1], heading, key)
            temp.append(gurl)
    dump[name]=temp

pkl.dump(dump,open('links.pkl','wb'))
print('Done!')
