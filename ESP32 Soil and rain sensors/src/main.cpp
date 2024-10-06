#include <Wire.h>
#include <PMserial.h>

// for onboard LED
#define LED 2

#include "Simple-Rain-Sensor-SOLDERED.h"
#define SENSOR_A0_PIN 34
#define SENSOR_D0_PIN 4
// Create the sensor object
simpleRainSensor rainSensor(SENSOR_A0_PIN, SENSOR_D0_PIN);

#include "Simple-Soil-Sensor-SOLDERED.h"
#define SENSOR_A1_PIN 35
#define SENSOR_D1_PIN 32
simpleSoilSensor soilSensor(SENSOR_A1_PIN, SENSOR_D1_PIN);

// For server
#include <WiFi.h>
#include "AsyncTCP.h"
#include "ESPAsyncWebServer.h"

// Creds for WiFi
// https://stackoverflow.com/questions/62314497/access-of-outer-environment-variable-in-platformio
#define XSTR(x) #x
#define STR(x) XSTR(x)
const char *wifi_ssid = STR(WIFI_SSID);
const char *wifi_pwd = STR(WIFI_PWD);

// server setup
AsyncWebServer server(80);
AsyncEventSource events("/events");

// global variables for webpage
float rain_raw_reading;
float rain_resistance;
float rain_percentage;
bool is_raining;
float soil_raw_reading;
float soil_resistance;
float soil_moist_percentage;
bool is_soil_moist;

// for api
#include <HTTPClient.h>
#include <ArduinoJson.h>
// json data for post API
StaticJsonDocument<250> jsonDocument;
char buffer[250];
const char *api_uri = STR(API_POST_PATH);

// 404 response
void notFound(AsyncWebServerRequest *request)
{
  request->send(404, "text/plain", "Not found");
}

// processor for the HTML response - handles the update in variables
String processor(const String &var)
{
  if (var == "rain_raw_reading")
  {
    return String(rain_raw_reading);
  }
  else if (var == "rain_resistance")
  {
    return String(rain_resistance);
  }
  else if (var == "rain_percentage")
  {
    return String(rain_percentage);
  }
  else if (var == "is_raining")
  {
    return String(is_raining);
  }
  else if (var == "soil_raw_reading")
  {
    return String(soil_raw_reading);
  }
  else if (var == "soil_resistance")
  {
    return String(soil_resistance);
  }
  else if (var == "soil_moist_percentage")
  {
    return String(soil_moist_percentage);
  }
  else if (var == "is_soil_moist")
  {
    return String(is_soil_moist);
  }
  else
    return String("Error");
}

// main HTML
const char index_html[] PROGMEM = R"rawliteral(<!DOCTYPE HTML><html><body>
<h2>Rain raw reading: <span id="rain_raw_reading">%rain_raw_reading%</span></h2>
<h2>Rain resistance: <span id="rain_resistance">%rain_resistance%</span>&Ohm;</h2>
<h2>Rain percentage: <span id="rain_percentage">%rain_percentage%</span>&percnt;</h2>
<h2>Is it raining ? <span id="is_raining">%is_raining%</span></h2>
<h2>Soil raw reading: <span id="soil_raw_reading">%soil_raw_reading%</span></h2>
<h2>Soil resistance: <span id="soil_resistance">%soil_resistance%</span>&Ohm;</h2>
<h2>Soil moist percentage <span id="soil_moist_percentage">%soil_moist_percentage%</span>&percnt;</h2>
<h2>Is soil moist ? <span id="is_soil_moist">%is_soil_moist%</span></h2>
</body>
<script>
if (!!window.EventSource) {
 var source = new EventSource('/events');
 
 source.addEventListener('open', function(e) {
  console.log("Events Connected");
 }, false);
 source.addEventListener('error', function(e) {
  if (e.target.readyState != EventSource.OPEN) {
    console.log("Events Disconnected");
  }
 }, false);
 
 source.addEventListener('rain_raw_reading', function(e) {
  console.log("rain_raw_reading", e.data);
  document.getElementById("rain_raw_reading").innerHTML = e.data;
 }, false);

 source.addEventListener('rain_resistance', function(e) {
  console.log("rain_resistance", e.data);
  document.getElementById("rain_resistance").innerHTML = e.data;
 }, false);

 source.addEventListener('rain_percentage', function(e) {
  console.log("rain_percentage", e.data);
  document.getElementById("rain_percentage").innerHTML = e.data;
 }, false);

 source.addEventListener('is_raining', function(e) {
  console.log("is_raining", e.data);
  let value;
  if (e.data === 1 || e.data === "1"){
    value = true
  } else {
    value = false
  }
  document.getElementById("is_raining").innerHTML = value;
 }, false);

 source.addEventListener('soil_raw_reading', function(e) {
  console.log("soil_raw_reading", e.data);
  document.getElementById("soil_raw_reading").innerHTML = e.data;
 }, false);

 source.addEventListener('soil_resistance', function(e) {
  console.log("soil_resistance", e.data);
  document.getElementById("soil_resistance").innerHTML = e.data;
 }, false);

 source.addEventListener('soil_moist_percentage', function(e) {
  console.log("soil_moist_percentage", e.data);
  document.getElementById("soil_moist_percentage").innerHTML = e.data;
 }, false);

 source.addEventListener('is_soil_moist', function(e) {
  console.log("is_soil_moist", e.data);
  let value;
  if (e.data === 1 || e.data === "1"){
    value = true
  } else {
    value = false
  }
  document.getElementById("is_soil_moist").innerHTML = value;
 }, false);
}
</script>

</html>)rawliteral";

void setup()
{
  Serial.begin(115200); // Begin Serial communication so we can see the output
  rainSensor.begin();   // Init the Simple Rain Sensor

  rainSensor.setThreshold(35.5); // Set the threshold for reading is it raining or not
  // Sensor calibration isn't needed but it helps with getting more relevant readings.
  // To calibrate the sensor, first run this sketch with the line of code below commented:
  // rainSensor.calibrate(76.4);

  // Place the sensor in water - so it's as wet as you're ever going to want to measure.
  // Note the reading of the Rain percentage, and then write that value in the calibrate function.
  // What this does is essentially make the range of measurement smaller so the data you get is more relevant.
  // Optionally, Invert the LED on the board
  // rainSensor.invertLED(true);

  soilSensor.begin(); // Init the Simple Soil Humidity Sensor
  // Sensor calibration isn't needed but it helps with getting more relevant readings.
  // To calibrate the sensor, first run this sketch with the line of code below commented:
  // soilSensor.calibrate(65.5);

  // Place the sensor in water- so it's as moist as you're ever going to want to measure.
  // Note the reading of the Moist percentage, and then write that value in the calibrate function.
  // What this does is essentially make the range of measurement smaller so the data you get is more relevant.

  pinMode(LED, OUTPUT);

  // Set the device as a Station and Soft Access Point simultaneously
  WiFi.mode(WIFI_STA);
  // displays wifi logins in serial console for debugging - remove for security purposes
  Serial.println("wifi_ssid: ");
  Serial.println(wifi_ssid);
  Serial.println("wifi_pwd: ");
  Serial.println(wifi_pwd);
  WiFi.begin(wifi_ssid, wifi_pwd);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Setting as a Wi-Fi Station..");
  }
  Serial.print("Station IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  // Define a route to serve the HTML page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request)
            {
              Serial.println("ESP32 Web Server: New request received:"); // for debugging
              Serial.println("GET /");                                   // for debugging
              request->send_P(200, "text/html", index_html, processor);
              // request->send(200, "text/plain", "Hello World!");
            });

  // Handle Web Server Events
  events.onConnect([](AsyncEventSourceClient *client)
                   {
    if(client->lastId()){
      Serial.printf("Client reconnected! Last message ID that it got is: %u\n", client->lastId());
    }
    // send event with message "hello!", id current millis
    // and set reconnect delay to 1 second
    client->send("hello!", NULL, millis(), 10000); });

  // server handlers
  server.onNotFound(notFound);
  server.addHandler(&events);
  // Start the server
  server.begin();
}

// turns the onboard led on and off rapidly - used if WiFi connection issues
void rapidLEDFiring()
{
  for (int i = 0; i < 10; i++)
  {
    digitalWrite(LED, HIGH);
    Serial.println("LED is on");
    delay(10);
    digitalWrite(LED, LOW);
    Serial.println("LED is off");
  }
}

// add an attribute to the json document
void addJsonAttribute(const char *tag, const float value)
{
  jsonDocument[tag] = value;
}

void sendToApi()
{
  Serial.println("Sending to API");
  serializeJson(jsonDocument, buffer);
  // print json before sending
  serializeJsonPretty(jsonDocument, Serial);
  Serial.print(F("\n"));
  // check connected to WIFI
  if (WiFi.status() == WL_CONNECTED)
  {
    WiFiClient client;
    HTTPClient http;
    const String api_transfer_protocol = "http://";
    const String path = api_transfer_protocol + String(api_uri);
    http.begin(client, path);
    // Specify content-type header
    http.addHeader("Content-Type", "application/json");
    // Send HTTP POST request
    String requestBody;
    serializeJson(jsonDocument, requestBody);
    int httpResponseCode = http.POST(requestBody);
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    http.end();
  }
  else
  {
    Serial.println("WiFi Disconnected");
    // rapid firing of led to show issues with API connection
    rapidLEDFiring();
  }
  // clear json after sending
  jsonDocument.clear();
}

void loop()
{
  Serial.println();
  Serial.println();

  digitalWrite(LED, HIGH);
  Serial.println("LED is on");
  Serial.println();

  // Print the readings to Serial

  // Raw reading is essentially a reading of the analog value on the easyC board
  rain_raw_reading = rainSensor.getRawReading();
  events.send(String(rain_raw_reading).c_str(), "rain_raw_reading", millis());
  addJsonAttribute("rain_raw_reading", rain_raw_reading);

  // The resistance is calcualted through a constant
  rain_resistance = rainSensor.getResistance();
  events.send(String(rain_resistance).c_str(), "rain_resistance", millis());
  addJsonAttribute("rain_resistance", rain_resistance);

  // Print percentage of rain detected on sensor
  rain_percentage = rainSensor.getValue();
  events.send(String(rain_percentage).c_str(), "rain_percentage", millis());
  addJsonAttribute("rain_percentage", rain_percentage);

  // Print is it raining or not
  // Once again, you may adjust this threshold with setThreshold
  is_raining = rainSensor.isRaining();
  events.send(String(is_raining).c_str(), "is_raining", millis());
  addJsonAttribute("is_raining", is_raining);

  // Raw reading is essentially a reading of the analog value on SENSOR_A0_PIN
  soil_raw_reading = soilSensor.getRawReading();
  events.send(String(soil_raw_reading).c_str(), "soil_raw_reading", millis());
  addJsonAttribute("soil_raw_reading", soil_raw_reading);

  // The resistance is calcualted through a constant
  soil_resistance = soilSensor.getResistance();
  events.send(String(soil_resistance).c_str(), "soil_resistance", millis());
  addJsonAttribute("soil_resistance", soil_resistance);

  // Print percentage of 'moistness' of sensor
  soil_moist_percentage = soilSensor.getValue();
  events.send(String(soil_moist_percentage).c_str(), "soil_moist_percentage", millis());
  addJsonAttribute("soil_moist_percentage", soil_moist_percentage);

  // Print is the soil moist or not
  // Once again, you may adjust this threshold with the small potentiometer on the board
  is_soil_moist = soilSensor.isMoist();
  events.send(String(is_soil_moist).c_str(), "is_soil_moist", millis());
  addJsonAttribute("is_soil_moist", is_soil_moist);

  Serial.println('Sensor readings completed');

  Serial.println('\n');
  sendToApi();
  digitalWrite(LED, LOW);
  Serial.println("LED is off");
  delay(60000); // Wait a bit until the next reading
}