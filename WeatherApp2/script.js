const apiKey = '65b2edfc76c5b032c60c6aed4f58e32d';

function searchWeather() {
    const locationInput = document.getElementById('locationInput').value;
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${locationInput}&appid=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            displayCurrentWeather(data);
            return fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${locationInput}&appid=${apiKey}`);
        })
        .then(response => response.json())
        .then(data => {
            displayForecast(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            alert('Error fetching weather data. Please try again.');
        });
}

function displayCurrentWeather(data) {
    const currentWeatherContainer = document.getElementById('currentWeather');
    currentWeatherContainer.innerHTML = `
        <h2>${data.name}, ${data.sys.country}</h2>
        <p>${data.weather[0].description}</p>
        <p>Temperature: ${kelvinToCelsius(data.main.temp)}°C</p>
        <p>Humidity: ${data.main.humidity}%</p>
        <p>Wind Speed: ${data.wind.speed} m/s</p>
        <img src="http://openweathermap.org/img/w/${data.weather[0].icon}.png" alt="Weather Icon">
    `;
}

function displayForecast(data) {
    const forecastContainer = document.getElementById('forecast');
    forecastContainer.innerHTML = '';

    // Extract data for the next 5 days (assuming data is provided in 3-hour intervals)
    const forecastData = data.list.filter(item => item.dt_txt.includes('12:00:00'));

    forecastData.forEach(forecastItem => {
        const date = new Date(forecastItem.dt_txt);
        forecastContainer.innerHTML += `
            <div class="forecast-item">
                <p>${formatDate(date)}</p>
                <p>${kelvinToCelsius(forecastItem.main.temp)}°C</p>
                <p>Humidity: ${forecastItem.main.humidity}%</p>
                <p>Wind Speed: ${forecastItem.wind.speed} m/s</p>
                <img src="http://openweathermap.org/img/w/${forecastItem.weather[0].icon}.png" alt="Weather Icon">
            </div>
        `;
    });
}

function kelvinToCelsius(kelvin) {
    return (kelvin - 273.15).toFixed(2);
}

function formatDate(date) {
    const options = { weekday: 'short', month: 'short', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}
