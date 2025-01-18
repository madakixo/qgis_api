###Here's a simple example to load a vector layer, apply a style, and zoom to its extent:
from qgis.core import QgsProject, QgsVectorLayer
from qgis.utils import iface

# Load a vector layer
vlayer = QgsVectorLayer("path/to/your/shapefile.shp", "My Layer", "ogr")

# Check if layer is valid
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    # Add layer to project
    QgsProject.instance().addMapLayer(vlayer)

    # Set layer style (example: change color for all features to blue)
    vlayer.renderer().symbol().setColor(QColor("blue"))
    vlayer.triggerRepaint()

    # Zoom to the layer's extent
    iface.mapCanvas().setExtent(vlayer.extent())
    iface.mapCanvas().refresh()
