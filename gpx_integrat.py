#importing GPS data from a GPX file




from qgis.core import QgsProject, QgsVectorLayer, QgsDataSourceUri, QgsFeatureRequest
from qgis.PyQt.QtCore import QVariant
import os

def integrate_gps_data():
    try:
        # Path to your GPX file
        gpx_file = 'path/to/your/file.gpx'
        
        # Check if the file exists
        if not os.path.isfile(gpx_file):
            raise FileNotFoundError(f"GPX file not found: {gpx_file}")
        
        # Load the GPX file as a vector layer
        uri = QgsDataSourceUri()
        uri.setParam("type", "waypoints")
        uri.setParam("crs", "EPSG:4326")
        uri.setParam("path", gpx_file)
        
        # Load waypoints. Change 'type' to 'routes' or 'tracks' for routes or tracks respectively.
        gpx_layer = QgsVectorLayer(uri.uri(), "GPS_Waypoints", "ogr")
        
        if not gpx_layer.isValid():
            raise ValueError("The GPX layer failed to load. Check the file format or permissions.")
        
        # Add the layer to the current project
        QgsProject.instance().addMapLayer(gpx_layer)
        
        # Optionally, if you want to filter or manipulate the data
        # request = QgsFeatureRequest().setFilterExpression("name = 'SomeName'")
        # filtered_features = [f for f in gpx_layer.getFeatures(request)]
        
        print("GPS data integrated successfully.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Execute the function
integrate_gps_data()


"""
Explanation:
GPX File: This script assumes you have a GPX file containing waypoints, tracks, or routes. 
You can change the type parameter in the URI to load different parts of the GPX data.
Loading as Vector Layer: QGIS can directly load GPX files using the OGR provider. 
Here, we're loading waypoints; for tracks or routes, you'd change the type to tracks or routes.
Layer Validation: The script checks if the layer was loaded successfully, providing feedback if it wasn't.
Adding to Project: The GPS data layer is then added to the current QGIS project.
Feature Filtering: There's a commented-out section showing how you could filter features by attribute. 
This can be useful if you only want to see or work with specific GPS points based on names or other attributes in the GPX file.

Additional Considerations:
CRS: The script uses EPSG:4326, but if your project uses a different CRS or if your GPS data is in another system, 
you might want to transform the data.
Styling: After adding the layer, you can style it in QGIS's layer properties for better visibility or 
to differentiate between waypoints, routes, or tracks.
Direct GPS Device: If you're directly interfacing with a GPS device, 
you would need additional libraries or QGIS plugins like GPS Tools to manage real-time data or data transfer from the device.

"""




