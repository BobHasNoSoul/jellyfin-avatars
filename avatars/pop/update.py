from bs4 import BeautifulSoup

# Load the HTML file
input_file = 'pop.html'  # Path to your input HTML file
output_file = 'poptest.html'  # Path to save the modified HTML file

# Read the HTML content from the file
with open(input_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Remove the download attribute from the <a> tags and add onclick handlers to <img> tags
for a_tag in soup.find_all('a', href=True):
    # Replace <a> tags with their contents (i.e., <img> tags)
    a_tag.unwrap()

for img_tag in soup.find_all('img', src=True):
    # Add the onclick attribute to the <img> tags
    img_tag['onclick'] = f"updateUserImage('{img_tag['src']}')"
    img_tag['style'] = 'cursor: pointer;'  # Add cursor pointer style

# Add JavaScript function to the <head> section
script_tag = soup.new_tag('script')
script_tag.string = """
// Function to update the user image
async function updateUserImage(imagePath) {
  // Fetch credentials from sessionStorage
  const jsonCredentials = sessionStorage.getItem('json-credentials');
  const apiKey = sessionStorage.getItem('api-key'); // Get the API key from session storage

  if (jsonCredentials && apiKey) {
    const credentials = JSON.parse(jsonCredentials);
    const userId = credentials.Servers[0].UserId;

    // Check if the userId and apiKey are retrieved correctly
    if (!userId) {
      console.error('User ID not found in sessionStorage.');
      alert('User ID not found. Please log in again.');
      return;
    }

    if (!apiKey) {
      console.error('API key not found in sessionStorage.');
      alert('API key not found. Please log in again.');
      return;
    }

    // Construct the URL for the API request
    const apiUrl = `/Users/${userId}/Images/Primary`;

    // Construct the image URL relative to the current page
    const currentPageUrl = window.location.href; // Get the full URL of the current page
    const baseUrl = currentPageUrl.substring(0, currentPageUrl.lastIndexOf('/') + 1); // Remove the filename from the URL
    const imageUrl = baseUrl + imagePath; // Append the image path to the base URL

    try {
      // Fetch the image as a Blob
      const response = await fetch(imageUrl);
      if (!response.ok) {
        throw new Error('Failed to fetch image.');
      }
      const blob = await response.blob();

      // Convert Blob to Base64
      const base64String = await blobToBase64(blob);

      // Determine the MIME type of the image from the blob
      const contentType = blob.type;

      // Send the POST request with the Base64-encoded image data
      const uploadResponse = await fetch(apiUrl, {
        method: 'POST',
        credentials: 'include', // Ensure credentials are included
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
          'Accept': '*/*',
          'Accept-Language': 'en-GB,en;q=0.5',
          'Authorization': `MediaBrowser Client="Jellyfin Web", Device="Firefox", DeviceId="TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTI5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTI5LjB8MTcyMzE5OTk0MTczOQ11", Version="10.9.7", Token="${apiKey}"`,
          'Content-Type': contentType, // Set Content-Type to the MIME type of the image
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-origin',
          'Priority': 'u=4'
        },
        body: base64String, // Send only the Base64-encoded data
        mode: 'cors' // Handle cross-origin requests
      });

      if (uploadResponse.ok) {
        // Notify the user of success and ask if they want to go back
        const userConfirmed = confirm('User image updated successfully! Do you want to go back to the home page?');
        if (userConfirmed) {
          // Redirect to the specified URL
          window.location.href = '/web/#/home.html';
        }
      } else {
        const errorData = await uploadResponse.json();
        console.error('Server Error Details:', errorData); // Log the server error details
        throw new Error(`Failed to update user image. Status: ${uploadResponse.status}, Details: ${errorData.detail}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while updating the user image.');
    }
  } else {
    alert('User credentials not found or API key not found.');
  }
}

// Helper function to convert Blob to Base64 string
function blobToBase64(blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result.split(',')[1]); // Extract Base64 part
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
}
"""

# Add the script tag to the <head> section
head_tag = soup.head
head_tag.append(script_tag)

# Write the modified HTML to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print(f"Modified HTML saved to {output_file}")
