#include <WiFi.h>
#include <WebSocketsServer.h>

WebSocketsServer webSocket(8080);

const char* username = "Orange_wifi_50D9";
const char* password = "n39B2aDYMAE";

void onWebSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t length) {
  switch (type) {
    case WStype_DISCONNECTED:
      Serial.printf("[%u] Disconnected!\n", num);
      break;
    case WStype_CONNECTED:
      Serial.printf("[%u] Connected!\n", num);
      break;
    case WStype_TEXT:
      Serial.printf("[%u] Text: %s\n", num, payload);
      webSocket.broadcastTXT(payload, length);
      break;
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.begin("your-ssid", "your-password");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("WiFi connected!");

  webSocket.begin();
  webSocket.onEvent(onWebSocketEvent);
}

void loop() {
  webSocket.loop();
}
