Week 1 Summary :
--------------------------------------------------------------------------------------------------------------------------

https://youtu.be/Fb7oqcbGYeQ

> We can grab images based on a location using 'Google Street View Image API'


> Limitations : Resolution 640x640, 25k map loads per 24 hours

We were trying to get 360 panorama for the whole time, but it seems Google doesn't provide 360 panorama for every
location. 


For example, we can request pano_id for location 22.9005, 89.5024
https://maps.googleapis.com/maps/api/streetview/metadata?location=22.9005%2C89.5024&key=AIzaSyCviDo0j3-AdFzULn2T-nuOOFmW3PwfhLc
from this json file we can get the pano_id : "mVAKzTiH1jBeo9FhR0zHkg"

Now, we can get the panorama from this pano_id : https://maps.googleapis.com/maps/api/streetview?pano=mVAKzTiH1jBeo9FhR0zHkg&size=600x400

But, it's not 360 panorama. There are some external services which manages to give 360 panorama images (we haven't tested them) but most of them 
are experimental and there's restriction on mining streetview data from external sources.


`No access to APIs or Content except through the Service. You will not access the Maps API(s) or the Content except through 
the Service. For example, you must not access map tiles or imagery through interfaces or channels (including undocumented 
Google interfaces) other than the Maps API(s).`

 