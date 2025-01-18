## you should see a new layer named "Marked_Locations" with points corresponding to your coordinates

from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsField
from qgis.PyQt.QtCore import QVariant
import csv

def mark_locations():
    # Define the coordinates in a CSV file for simplicity. 
    # Here, we'll assume the file has columns: 'name', 'longitude', 'latitude'
    csv_file = 'path/to/your/coordinates.csv'
    
    # Create a new memory layer for points
    point_layer = QgsVectorLayer("Point?crs=EPSG:4326", "Marked_Locations", "memory")
    pr = point_layer.dataProvider()
    
    # Add fields to the layer for name and coordinates
    pr.addAttributes([QgsField("name", QVariant.String), 
                      QgsField("longitude", QVariant.Double), 
                      QgsField("latitude", QVariant.Double)])
    point_layer.updateFields()
    
    # Read from CSV and add points to the layer
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(row['longitude']), float(row['latitude']))))
            feat.setAttributes([row['name'], float(row['longitude']), float(row['latitude'])])
            pr.addFeatures([feat])
    
    # Add the new layer to the project
    QgsProject.instance().addMapLayer(point_layer)
    
    # Optionally, save the layer to a shapefile
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "ESRI Shapefile"
    options.fileEncoding = "UTF-8"
    
    QgsVectorFileWriter.writeAsVectorFormat(point_layer, "marked_locations.shp", options)

# Run the function
mark_locations()


"""

Explanation:
CSV File: The script assumes you have a CSV file with headers name, longitude, and latitude. 
Make sure your CSV file matches this format.

Vector Layer: A new point layer is created in memory, using EPSG:4326 (WGS84) as the coordinate reference system.
Adding Points: Each row from the CSV is converted into a point feature in the layer, with attributes for name and coordinates.

Layer Addition: The new layer is added to the current QGIS project.
Saving to Shapefile: Optionally, the memory layer is saved as a shapefile for persistent storage.

Instructions:
Create a CSV file with the coordinates you want to mark. An example row might look like:
name,longitude,latitude
Eiffel Tower,2.294694,48.858451
Open QGIS and make sure your raster and other shapefile layers are loaded.
Open the Python Console (Plugins > Python Console).
Modify the csv_file path in the script to point to your CSV file.
Copy and Paste the script into the console.
Run the script.

"""


############################################################################
