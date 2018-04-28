import shapefile
import csv

shape = shapefile.Reader("tl_2017_06_tract/tl_2017_06_tract.shp")
# first feature of the shapefile
recs = shape.shapeRecords()
# for i in range(len(recs)):
#     feature = recs[i]
#
#     first = feature.shape.__geo_interface__
#
#     print(first) # (GeoJSON format)
print(shape.fields)
with open('census.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for x in shape.records():
        if x[1] == '001':
            spamwriter.writerow([x[3], x[2], x[1], x[4], x[5], x[10], x[11]])

reader = csv.reader(open("census.csv"), delimiter=",")
sortedlist = sorted(reader, key=lambda row: row[1], reverse=False)
with open("census_sorted.csv", "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    fileWriter.writerow(["GEOID", "TRACTCE", "COUNTYFP", "NAME", "NAMELSAD", "INTPTLAT", "INTPTLON"])
    for row in sortedlist:
        fileWriter.writerow(row)

