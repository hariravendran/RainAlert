# RainAlert

**RainAlert** is a Python application that sends SMS alerts to your phone, notifying you when it's going to rain in your area. Simply provide your latitude and longitude of your location (From latlong.net or GoogleMaps), and RainAlert will check the weather forecast using the OpenWeatherMap API and send you an SMS via Twilio if rain is expected that day.

## Features

- **Daily Weather Check**: Automatically checks the weather every morning at 7 AM.
- **SMS Alerts**: Sends alerts directly to your phone if rain is forecasted.
- **Customizable City**: Easily change the city for which you want weather alerts.

## Technologies Used

- **Python**: Developed in Python using PyCharm.
- **OpenWeatherMap API**: Provides weather data. [API Documentation](https://openweathermap.org/api)
- **Twilio API**: Used for sending SMS notifications. [Twilio API Documentation](https://www.twilio.com/docs/usage/api)
- **PythonAnywhere**: Hosts the application and runs the script at scheduled times.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/RainAlert.git
   cd RainAlert
   ```

2. **Install Required Packages**:
   Make sure you have `requests` and `twilio` installed:
   ```bash
   pip install requests twilio
   ```

3. **API Keys**:
   - Sign up for [OpenWeatherMap](https://openweathermap.org/) and obtain your API key. 
   - Sign up for [Twilio](https://www.twilio.com/) to get your Account SID, Auth Token, and a source phone number.

4. **Configuration**:
   Open the configuration file (e.g., `config.py`) and update it with your:
   - OpenWeatherMap API key
   - Latitude and longitude of your location
   - Twilio Account SID
   - Twilio Auth Token
   - Twilio phone number
   - Your phone number (where you want to receive alerts)

5. **Running the Application**:
   Run the script manually to test:
   ```bash
   python rain_alert.py
   ```

6. **Scheduling**:
   Deploy your application on PythonAnywhere and set it to run every morning at 7 AM.

## Compiling the Application

To create a standalone executable, use the Inno Compiler. Follow the [Inno Setup Documentation](https://jrsoftware.org/isinfo.php) for instructions on how to compile your Python script into an executable.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/hariravendran/RainAlert/blob/main/license.txt) file for details.

## Contributing

Feel free to open issues or submit pull requests to improve the application. Contributions are welcome!

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing weather data.
- [Twilio](https://www.twilio.com/) for enabling SMS functionality.

---

Keep your umbrella handy! ☔️
