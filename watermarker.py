from qgis.core import QgsProject, QgsPrintLayout, QgsLayoutItemLabel, QgsLayoutItemPicture, QgsLayoutExporter
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtCore import QRectF

# Get the current project instance
project = QgsProject.instance()

# Create a new layout
layout = QgsPrintLayout(project)
layout.initializeDefaults()

# Text Watermark
text_watermark = "JAYYMADDCLICKE"
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


"""
Text Watermark Transparency: The opacity of the text watermark is set using QColor with an alpha value.
Here, int(255 * text_opacity) calculates the alpha value based on the text_opacity (0 to 1).
An alpha of 255 is fully opaque, and 0 is fully transparent.
Image Watermark Transparency: The opacity for the image watermark is directly controlled by setOpacity(), 
where the value ranges from 0 to 1 (0 being fully transparent and 1 fully opaque).

Instructions:
Open QGIS and load your map project.
Open the Python Console (Plugins > Python Console).
Copy and Paste this script into the console or a Python file in QGIS.
Change image_path to the actual path of your watermark image on your system.
Adjust text_opacity and image_opacity to control how transparent each watermark appears.
Values range from 0 (fully transparent) to 1 (fully opaque).
Modify other settings like font, size, position, etc., as needed.
Run the script to generate your PDF with watermarks.

"""
