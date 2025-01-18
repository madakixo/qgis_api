#madakixo

####### script for adding watermark on shp to pdf




# Import necessary modules from QGIS and PyQt libraries
from qgis.core import QgsProject, QgsPrintLayout, QgsLayoutItemLabel, QgsLayoutItemPicture, QgsLayoutExporter
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtCore import QRectF

# Get the current QGIS project instance
project = QgsProject.instance()

# Create a new print layout for adding watermarks
layout = QgsPrintLayout(project)
layout.initializeDefaults()

# Define settings for text watermark
text_watermark = "JAYYMADDCLICKE"
text_opacity = 0.5  # Opacity from 0 (fully transparent) to 1 (fully opaque)

# Create and configure a text label for the watermark
label = QgsLayoutItemLabel(layout)
label.setText(text_watermark)  # Set the text of the watermark
label.setFont(QFont("Arial", 50))  # Set font and size
# Set color with transparency; convert opacity to an alpha value (0-255)
label.setFontColor(QColor(128, 128, 128, int(255 * text_opacity)))
label.adjustSizeToText()  # Automatically size label to fit text
label.attemptMove(QgsLayoutPoint(10, 10, QgsUnitTypes.LayoutMillimeters))  # Position in millimeters
layout.addLayoutItem(label)  # Add the label to the layout

# Define settings for image watermark
image_path = '/path/to/your/watermark/image.png'  # Update this path to your image file
image_opacity = 0.3  # Opacity from 0 (fully transparent) to 1 (fully opaque) #default 0.3

# Create and configure an image for the watermark
pic = QgsLayoutItemPicture(layout)
pic.setPicturePath(image_path)  # Path to the watermark image
# Set the size of the image in millimeters
pic.attemptResize(QgsLayoutSize(100, 100, QgsUnitTypes.LayoutMillimeters))
pic.setOpacity(image_opacity)  # Apply transparency to the image
# Position the image watermark (coordinates in millimeters)
pic.attemptMove(QgsLayoutPoint(50, 50, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(pic)  # Add the image to the layout

# Prepare to export the layout with watermarks to a PDF
exporter = QgsLayoutExporter(layout)

# Export the layout to PDF
# Note: 'output.pdf' can be changed to any filename you prefer
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
