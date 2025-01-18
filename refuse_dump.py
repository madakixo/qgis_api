from qgis.core import QgsProject, QgsVectorLayer, QgsFeatureRequest, QgsSymbol, QgsRendererCategory, QgsCategorizedSymbolRenderer, QgsMarkerSymbol
from qgis.PyQt.QtGui import QColor
from qgis.utils import iface
from qgis.core import QgsCoordinateReferenceSystem, QgsRectangle

def map_refuse_dumps():
    # Load the shapefile containing refuse dump locations in Kaduna State
    layer = QgsVectorLayer("path/to/refuse_dumps_Kaduna.shp", "Refuse Dumps in Kaduna", "ogr")
    
    # Check if the layer was loaded successfully
    if not layer.isValid():
        print("Layer failed to load! Please check the path to your shapefile.")
        return
    
    # Add the refuse dump layer to the QGIS project
    QgsProject.instance().addMapLayer(layer)
    
    # Specify the field name used for categorizing refuse dump types
    field_name = "type"  # Replace this if your field name differs
    
    # Define categories for visualization. Here, we're assuming all features are refuse dumps
    categories = []
    # Create a marker symbol for refuse dumps: red with a black outline
    symbol = QgsMarkerSymbol.createSimple({
        'color': 'red', 
        'size': '5', 
        'outline_color': 'black', 
        'outline_width': '0.5'
    })
    category = QgsRendererCategory("refuse dump", symbol, "Refuse Dump")
    categories.append(category)

    # Use the categories to create a renderer that will style the layer based on the 'type' field
    renderer = QgsCategorizedSymbolRenderer(field_name, categories)

    # Apply the renderer to the layer and refresh to see changes
    if renderer is not None:
        layer.setRenderer(renderer)
    layer.triggerRepaint()

    # Check for and add labels if there's a 'name' field in the shapefile
    if 'name' in [field.name() for field in layer.fields()]:  # Check if 'name' field exists
        layer.setLabelsEnabled(True)
        layer_settings = QgsPalLayerSettings()
        text_format = QgsTextFormat()

        # Configure label settings
        layer_settings.fieldName = "name"  # Field to use for labeling
        layer_settings.placement = QgsPalLayerSettings.Placement.OverPoint  # Place label directly over the point
        text_format.setFont(QgsFontUtils.getStandardTestFont("Arial", 8, QgsFontUtils.FontWeight.Bold))  # Font settings
        text_format.setSize(8)
        layer_settings.setFormat(text_format)

        layer_settings.enabled = True
        layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
        layer.setLabeling(layer_settings)
        layer.triggerRepaint()  # Refresh to apply labels

    # Add a basemap for context - Here we use OpenStreetMap
    urlWithParams = 'type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0'
    osm_layer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')
    if osm_layer.isValid():
        QgsProject.instance().addMapLayer(osm_layer)
        # Ensure the refuse dump layer is above the basemap for visibility
        root = QgsProject.instance().layerTreeRoot()
        osm_node = root.findLayer(osm_layer.id())
        refuse_dump_node = root.findLayer(layer.id())
        root.insertChildNode(1, refuse_dump_node.clone())  # Clone and insert above OSM
        root.removeChildNode(refuse_dump_node)  # Remove original node

    # Center the map on Kaduna State - approximate coordinates
    kaduna_center = QgsPointXY(7.4422, 10.5239)  # Roughly center of Kaduna State
    crs = QgsCoordinateReferenceSystem("EPSG:4326")  # WGS 84 - lat/long
    iface.mapCanvas().setDestinationCrs(crs)
    # Define an extent around Kaduna to zoom the map to
    extent = QgsRectangle(kaduna_center.x() - 1, kaduna_center.y() - 1, kaduna_center.x() + 1, kaduna_center.y() + 1)
    iface.mapCanvas().setExtent(extent)
    iface.mapCanvas().refresh()  # Refresh the map canvas to apply changes

# Execute the function to map out refuse dumps
map_refuse_dumps()


"""
Notes:

Ensure you have internet access for the OpenStreetMap tiles to load.
The iface object is typically provided by QGIS when scripts are run from
the Python console or script editor within QGIS.
Adjust the field_name to match your data's attribute for refuse dump types,
and make sure you have the correct path to your
shapefile.

"""
