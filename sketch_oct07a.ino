#include <ESP8266WiFi.h>
#define LED 5
#define FAN 2
const char* ssid = "Fuad";   //enter your wi-fi name
const char* password = "12345678";    //enter the wifi password
unsigned char status_led=0;
unsigned char status_fan=0;
int a;
WiFiServer server(80);

void setup() {

  Serial.begin(115200);  

  pinMode(LED, OUTPUT);
  pinMode(FAN, OUTPUT);
  digitalWrite(LED, HIGH);
  digitalWrite(FAN, HIGH);

  // Connect to WiFi network

  Serial.println();

  Serial.println();

  Serial.print("Connecting to ");

  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {

    delay(500);

    Serial.print(".");

  }

  Serial.println("");

  Serial.println("WiFi connected");
  // Start the server
  server.begin();

  Serial.println("Server started at...");

  Serial.println(WiFi.localIP());
}

void loop() {

  // Check if a client has connected

  WiFiClient client = server.available();
  if (!client) {
    a = 0;
    return;

  }else{
    a = 1;
    
    }
 

  // Wait until the client sends some data

  Serial.println("new client");
  
  while (! client.available())

  {

    delay (1);

  }

 

 

  // Read the first line of the request

  String req = client.readStringUntil('\r');

  Serial.println(req);

  client.flush();

 

  // Match the request

 

  if (req.indexOf("/ledon") != -1)  {

    status_led=1;

    digitalWrite(LED, LOW);

    Serial.println("LED ON");

  }

  else if(req.indexOf("/ledoff") != -1)

  {

    status_led=0;

    digitalWrite(LED,HIGH);

    Serial.println("LED OFF");

  }



   if (req.indexOf("/fanon") != -1)  {

    status_fan=1;

    digitalWrite(FAN, LOW);

    Serial.println("FAN ON");

  }

  else if(req.indexOf("/fanoff") != -1)

  {

    status_fan=0;

    digitalWrite(FAN,HIGH);

    Serial.println("FAN OFF");

  }

// Return the response

client.println("HTTP/1.1 200 OK");

client.println("Content-Type: text/html");

client.println("Connection: close");

client.println("");
client.println("<!DOCTYPE html>");
client.println("<html>");
client.println("<body>");
if(a==1){
  client.println("<h1>1</h1");
  }else{client.println("<h1></h1");}
client.println("</body>");
client.println("</html>");


delay(1);

Serial.println("Client disonnected");

Serial.println("");

 

}
