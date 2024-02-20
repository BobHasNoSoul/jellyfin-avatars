#!/bin/bash

# Get all image file names in the current folder
images=$(ls *.jpg *.jpeg *.png *.gif 2>/dev/null)

# Check if there are any images
if [ -z "$images" ]; then
  echo "No images found in the current folder."
  exit 1
fi

# Create the HTML file
html_file="gallery.html"
cat <<EOT > "$html_file"
<!DOCTYPE html>
<html>
<head>
<title>Image Gallery</title>
</head>
<body>
<h1>Image Gallery</h1>
EOT

# Add image tags for each image
for img in $images; do
  echo "<a href=\"$img\" download><img src=\"$img\" alt=\"Image\"></a>" >> "$html_file"
done

# Close the HTML file
echo "</body></html>" >> "$html_file"

echo "Gallery created: $html_file"

