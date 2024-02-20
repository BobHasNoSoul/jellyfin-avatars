import os

# Get a list of all .gif files in the current directory
gif_files = [filename for filename in os.listdir() if filename.endswith(".gif")]

# Create the HTML content for the images
image_html = ""
for gif_file in gif_files:
    image_html += f'<a href="{gif_file}" download><img src="{gif_file}" alt="Image" loading="lazy"></a>\n'

# Read the HTML template
with open("template.html", "r") as template_file:
    template_content = template_file.read()

# Find the gallery section and insert the image HTML
start_marker = '<div class="gallery">'
end_marker = '</div>'
start_index = template_content.find(start_marker) + len(start_marker)
end_index = template_content.find(end_marker, start_index)

# Insert the image HTML into the template
updated_content = template_content[:start_index] + image_html + template_content[end_index:]

# Save the updated HTML as "fixed.html"
with open("fixed.html", "w") as fixed_file:
    fixed_file.write(updated_content)
