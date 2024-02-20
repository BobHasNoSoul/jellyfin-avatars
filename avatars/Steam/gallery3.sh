#!/bin/bash

# Get all image file names in the current folder
images=$(ls *.jpg *.jpeg *.png *.gif 2>/dev/null)

# Check if there are any images
if [ -z "$images" ]; then
  echo "No images found in the current folder."
  exit 1
fi

# Prompt user for gallery title
read -p "Enter the title of the gallery: " gallery_title

# Prompt user for HTML file name
read -p "Enter the name of the HTML file (without extension): " html_filename

# Create the HTML file
html_file="$html_filename.html"
cat <<EOT > "$html_file"
<!DOCTYPE html>
<html>
<head>
<title>$gallery_title</title>
<style>
  body {
    background-color: #1a1a1a;
    color: #f0f0f0;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  header {
    background-color: #333;
    padding: 10px;
    text-align: center;
  }
  header img {
    max-height: 100px;
  }
  .gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(184px, 1fr));
    grid-gap: 4px;
    padding: 10px;
  }
  .gallery img {
    max-width: 100%;
    height: auto;
    border: 1px solid #666;
  }
</style>
</head>
<body>
<header>
  <img src="logo.png" alt="Logo">
</header>
<h1>$gallery_title</h1>
<div class="gallery">
EOT

# Add image tags for each image
for img in $images; do
  echo "<a href=\"$img\" download><img src=\"$img\" alt=\"Image\"></a>" >> "$html_file"
done

# Close the HTML file
echo "</div></body></html>" >> "$html_file"

echo "Gallery created: $html_file"

