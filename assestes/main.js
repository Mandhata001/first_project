 // OpenWeatherMap API key
 const apiKey = 'YOUR_API_KEY';
 const city = 'YourCity'; // Replace 'YourCity' with the name of your city

 fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
     .then(response => response.json())
     .then(data => {
         const weatherInfo = document.getElementById('weather-info');
         weatherInfo.innerHTML = `
             <p>Temperature: ${data.main.temp}°C</p>
             <p>Weather: ${data.weather[0].description}</p>
         `;
     })
     .catch(error => {
         console.log('Error fetching weather data:', error);
     });