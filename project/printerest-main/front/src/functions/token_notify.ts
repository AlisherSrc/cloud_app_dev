export function checkTokenPeriodically() {
    const token = localStorage.getItem('token');  // Retrieve token from localStorage
  
    if (!token) {
      console.log('No token found.');
      return;
    }
  
    // Define the Cloud Function URL (replace with your actual function URL)
    const functionUrl = "https://us-central1-printerest-cloud.cloudfunctions.net/notify-1";
  
    // Define the interval (e.g.,  1 minute = 60000 milliseconds)
    const interval = 600000000000000000;  // 3 minutes
  
    // Use setInterval to periodically check the token
    setInterval(() => {
      // Send a request to the Cloud Function with the token
      fetch(functionUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          token: token  // Pass the JWT token
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.valid === false) {
          alert('Your session has expired. Please log in again.');
          // Optionally, log out the user or redirect them to the login page
        } else {
          console.log('Token is still valid.');
        }
      })
      .catch(error => console.error('Error:', error));
    }, interval);
  }