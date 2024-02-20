import os
import urllib.parse

# Directory containing the new image files
image_directory = "./"  # Replace with the actual path to your image directory

# Read the existing HTML file
with open("popculture.html", "r") as file:
    html_content = file.read()

# Generate HTML for new image links
new_image_html = ""
for filename in os.listdir(image_directory):
    if filename.lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".webp")):
        # Encode the filename to handle spaces and special characters
        encoded_filename = urllib.parse.quote(filename)
        new_image_html += f'<a href="{encoded_filename}" download><img src="{encoded_filename}" alt="Image"></a>\n'

# Find the location where you want to add the new images in your HTML file
# You can specify a placeholder comment or any other unique identifier in your HTML to find the location
# For example, if you have <!-- INSERT_NEW_IMAGES_HERE --> in your HTML, you can use that as the identifier.
insert_location = "<!-- INSERT_NEW_IMAGES_HERE -->"

# Insert the new image HTML at the specified location
html_content = html_content.replace(insert_location, new_image_html + insert_location)

# Write the updated HTML back to the file
with open("index.html", "w") as file:
    file.write(html_content)

