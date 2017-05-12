#%matplotlib inline
import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader("/Users/sabamundlay/Desktop/independent_study/routes_bus_nyc_jan2017 2/routes_bus_nyc_jan2017.shp")
sf_1 = shp.Reader("/Users/sabamundlay/Downloads/stops_bus_nyc_jan2017/stops_bus_nyc_jan2017.shp")

plt.figure()
for shape in sf.shapeRecords():
    print(shape.record)
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()