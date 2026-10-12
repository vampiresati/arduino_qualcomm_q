#include <Arduino_RouterBridge.h>

const int LED_PIN = LED_BUILTIN;

void on_alexa_led(bool state) {
  // UNO Q's built-in LED may be active-low.
  digitalWrite(LED_PIN, state ? LOW : HIGH);
}

void off_alexa_led(bool state) {
  // UNO Q's built-in LED may be active-low.
  digitalWrite(LED_PIN, state ? HIGH : LOW);
}



void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);

  Bridge.begin();
  Bridge.provide("on_alexa_led", on_alexa_led);
  Bridge.provide("off_alexa_led", off_alexa_led);

}

void loop() {
  // Wait for RPC calls from the Linux/Python application.

}
