# SilencerBot 9000 – The Silence Guardian for Developers

SilencerBot 9000 is an advanced noise monitoring device designed for developer spaces. When conversations exceed the acceptable noise level, the bot instantly reacts by sending a message to the company's Discord, reminding the team to maintain a quiet environment.

## How It Works

1. **Noise Sensor** – A digital sound sensor connected to an Arduino monitors the noise levels in the room.
2. **Arduino as a Signal Processor** – When the noise surpasses a predefined threshold, Arduino sends a signal to the computer.
3. **Python Communication Program** – A Python script receives the signal from Arduino and sends an HTTP request to the server.
4. **API Server (Express.js)** – The API server written in Express.js processes the request and forwards it to the Discord bot.
5. **Discord Bot** – The bot posts a message on the company’s Discord server, notifying the team to keep the noise down.

Ideal for companies where developers love to debate… but sometimes forget that others are trying to work! 🚀

## Tech Stack
- **Hardware:** Arduino, Sound Sensor
- **Software:** Python, Express.js, Discord Bot, HTTP API
