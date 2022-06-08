# import gmplot package

from gmplot import *
  
latitude_list = [30.3358376, 30.307977, 30.3216419, 30.3427904,
                  30.378598, 30.3548185, 30.3345816, 30.387299,
                    30.3272198, 30.3840597, 30.4158, 30.340426,
                             30.3984348, 30.3431313, 30.273471]
  
longitude_list = [77.8701919, 78.048457, 78.0413095, 77.886958,
                  77.825396, 77.8460573, 78.0537813, 78.090614,
                    78.0355272, 77.9311923, 77.9663, 77.952092,
                            78.0747887, 77.9555512, 77.9997158]
  
gmap4 = gmplot.GoogleMapPlotter.from_geocode("Dehradun, India")
  
# heatmap plot heating Type
# points on the Google map
gmap4.heatmap( latitude_list, longitude_list )
  
gmap4.draw( "C:\\Users\\mnaim\\OneDrive\\Desktop\\Coding VSCO\\ADA\\map20.html" )