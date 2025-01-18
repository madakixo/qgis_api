from qgis.core import QgsProject, QgsPrintLayout, QgsLayoutItemLabel, QgsLayoutItemPicture, QgsLayoutExporter
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtCore import QRectF

# Get the current project instance
project = QgsProject.instance()

# Create a new layout
layout = QgsPrintLayout(project)
layout.initializeDefaults()

# Text Watermark
text_watermark = "WATERMARK"
text_opacity = 0.5  # Opacity from 0 (fully transparent) to 1 (fully opaque)

label = QgsLayoutItemLabel(layout)
label.setText(text_watermark)
label.setFont(QFont("Arial", 50))
label.setFontColor(QColor(128, 128, 128, int(255 * text_opacity)))  # Adjust opacity
label.adjustSizeToText()
label.attemptMove(QgsLayoutPoint(10, 10, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(label)

# Image Watermark
image_path = '/path/to/your/watermark/image.png'  # Update this path to your image
image_opacity = 0.3  # Opacity from 0 (fully transparent) to 1 (fully opaque)

pic = QgsLayoutItemPicture(layout)
pic.setPicturePath(image_path)
pic.attemptResize(QgsLayoutSize(100, 100, QgsUnitTypes.LayoutMillimeters))  # Adjust size as needed
pic.setOpacity(image_opacity)  # Set the opacity of the image
pic.attemptMove(QgsLayoutPoint(50, 50, QgsUnitTypes.LayoutMillimeters))  # Position of the image
layout.addLayoutItem(pic)

# Set up exporter
exporter = QgsLayoutExporter(layout)

# Export to PDF (change 'output.pdf' to your desired file name)
result = exporter.exportToPdf('output.pdf', QgsLayoutExporter.PdfExportSettings())
if result == QgsLayoutExporter.Success:
    print("Watermark added and exported to PDF successfully.")
else:
    print("Failed to export layout to PDF.")
