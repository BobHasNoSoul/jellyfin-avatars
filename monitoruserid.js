// Function to extract the userId from the URL
function getUserIdFromURL() {
  const url = window.location.href;
  // Match userId in query parameters (e.g., ?userId=xxx or &userId=xxx)
  const userIdMatch = url.match(/[?&]userId=([^&]+)/i);
  // Alternatively, check if userId is in the hash (e.g., #/userdetails/xxx)
  const hashMatch = url.match(/#\/[^?]*\/([a-f0-9-]{32,36})/i);
  return userIdMatch ? userIdMatch[1] : (hashMatch ? hashMatch[1] : null);
}

// Function to check and store the userId
function monitorAndStoreUserId() {
  const userId = getUserIdFromURL();
  if (userId) {
    sessionStorage.setItem('lsuserid', userId);
    console.log('Stored userId in sessionStorage:', userId);
  } else {
    console.log('No userId found in URL');
  }
}

// Check immediately when the script loads
monitorAndStoreUserId();

// Set up observers for SPA navigation
const observer = new MutationObserver(monitorAndStoreUserId);
observer.observe(document.body, {
  childList: true,
  subtree: true
});

window.addEventListener('hashchange', monitorAndStoreUserId);
window.addEventListener('popstate', monitorAndStoreUserId);
