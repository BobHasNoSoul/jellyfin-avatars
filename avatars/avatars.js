// Function to update the user image
async function updateUserImage(imagePath) {
  // Fetch userId from sessionStorage and credentials from localStorage
  const userId = sessionStorage.getItem('lsuserid');
  const jsonCredentials = localStorage.getItem('jellyfin_credentials');

  if (!userId) {
    console.error('User ID not found in sessionStorage.');
    alert('User ID not found. Please log in again.');
    return;
  }

  if (!jsonCredentials) {
    console.error('Credentials not found in localStorage.');
    alert('Credentials not found. Please log in again.');
    return;
  }

  // Parse credentials to get AccessToken
  try {
    const credentials = JSON.parse(jsonCredentials);
    const apiKey = credentials.Servers[0].AccessToken;

    if (!apiKey) {
      console.error('API key (AccessToken) not found in credentials.');
      alert('API key not found. Please log in again.');
      return;
    }

    // Construct the URL for the API request
    const apiUrl = `/Users/${userId}/Images/Primary`;

    // Construct the image URL relative to the current page
    const currentPageUrl = window.location.href;
    const baseUrl = currentPageUrl.substring(0, currentPageUrl.lastIndexOf('/') + 1);
    const imageUrl = baseUrl + imagePath;

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
      credentials: 'include',
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Authorization': `MediaBrowser Client="Jellyfin Web", Device="Firefox", DeviceId="TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTI5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTI5LjB8MTcyMzE5OTk0MTczOQ11", Version="10.9.7", Token="${apiKey}"`,
        'Content-Type': contentType,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=4'
      },
      body: base64String,
      mode: 'cors'
    });

    if (uploadResponse.ok) {
      // Notify the user of success and ask if they want to go back
      const userConfirmed = confirm('User image updated successfully! Do you want to go back to the home page?');
      if (userConfirmed) {
        window.location.href = '/web/#/home.html';
      }
    } else {
      const errorData = await uploadResponse.json();
      console.error('Server Error Details:', errorData);
      throw new Error(`Failed to update user image. Status: ${uploadResponse.status}, Details: ${errorData.detail}`);
    }
  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred while updating the user image.');
  }
}

// Helper function to convert Blob to Base64 string
function blobToBase64(blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result.split(',')[1]);
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
}

// Create back button element
document.addEventListener('DOMContentLoaded', () => {
  const backButton = document.createElement('button');
  backButton.textContent = '← Back';
  backButton.style.position = 'fixed';
  backButton.style.top = '10px';
  backButton.style.left = '10px';
  backButton.style.padding = '8px 12px';
  backButton.style.backgroundColor = '#333';
  backButton.style.color = 'white';
  backButton.style.border = 'none';
  backButton.style.borderRadius = '4px';
  backButton.style.cursor = 'pointer';
  backButton.style.zIndex = '1000';

  // Add hover effect
  backButton.addEventListener('mouseover', () => {
    backButton.style.backgroundColor = '#555';
  });
  backButton.addEventListener('mouseout', () => {
    backButton.style.backgroundColor = '#333';
  });

  // Add click event to go back
  backButton.addEventListener('click', () => {
    window.history.back();
  });

  // Append button to body
  document.body.appendChild(backButton);
});
