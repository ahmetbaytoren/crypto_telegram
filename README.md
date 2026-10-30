🚀 Crypto Tracker Telegram Bot

<div align="center">

📈 Track Cryptocurrency Prices Directly From Telegram

A lightweight Python-powered Telegram bot that fetches real-time cryptocurrency prices using the Binance API.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white) ![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white) ![Binance](https://img.shields.io/badge/API-Binance-F0B90B?style=for-the-badge&logo=binance&logoColor=black) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Developed by Ahmet Baytören

Features • Installation • Usage • Configuration • Contributing

</div>

🌟 Overview

Crypto Tracker Telegram Bot is a simple yet powerful cryptocurrency tracking application built with Python.

It allows users to monitor cryptocurrency prices directly through Telegram without visiting cryptocurrency exchanges or opening additional applications.

Powered by the Binance public API, the bot retrieves the latest market prices and delivers them directly to your Telegram chat.

Whether you're a crypto enthusiast, a Python beginner, or a developer interested in Telegram bot development, this project is a great starting point.

✨ Features

<table>
<tr>
<td width="50%">

📊 Real-Time Prices

Get the latest cryptocurrency prices directly from Binance.

</td>
<td width="50%">

🤖 Telegram Integration

Interact with your cryptocurrency tracker through simple commands.

</td>
</tr>
<tr>
<td width="50%">

₿ Bitcoin Tracking

Monitor the BTC/USDT trading pair.

</td>
<td width="50%">

Ξ Ethereum Tracking

Monitor the ETH/USDT trading pair.

</td>
</tr>
<tr>
<td width="50%">

⚡ Lightweight & Fast

Built with Python and asynchronous programming.

</td>
<td width="50%">

🔓 No Binance API Key

Uses Binance's public market data endpoint.

</td>
</tr>
</table>

📸 Preview

<div align="center">

Command	Description
/start	Welcome message and bot information
/kripto	Cryptocurrency price information

Example Telegram Response

text
₿ Bitcoin: $67,450.25
Ξ Ethereum: $3,520.80


Illustrative prices only. Actual prices depend on market conditions.

</div>

🛠️ Built With
Technology	Description
🐍 Python	Core programming language
🤖 python-telegram-bot	Telegram Bot API integration
🌐 Binance API	Live cryptocurrency market data
⚡ Asyncio	Asynchronous task management
📡 Requests	HTTP communication
📋 Requirements

Before getting started, make sure you have:

Python 3.9 or newer
A Telegram account
A Telegram bot token
An active internet connection

No Binance account or private Binance API key is required.

🚀 Installation

Follow the instructions below to set up your own cryptocurrency tracking bot.

1. Clone the Repository
bash
git clone https://github.com/ahmetbaytoren/crypto-tracker-telegram-bot.git

bash
cd crypto-tracker-telegram-bot

2. Install Dependencies
bash
pip install -r requirements.txt


Or install the packages manually:

bash
pip install python-telegram-bot requests

3. Create Your Telegram Bot

You need a Telegram bot token to run your own instance.

Open Telegram.
Search for @BotFather.
Send /start.
Send /newbot.
Choose a name for your bot.
Choose a unique username ending with bot.
Copy the API token provided by BotFather.

<details>
<summary>🔑 Where can I get my Telegram Bot Token?</summary>

Open Telegram BotFather and follow the instructions above.

BotFather will provide a token similar to this:

text
123456789:YOUR_SECRET_BOT_TOKEN


Never share your real token or upload it to GitHub.

</details>

4. Configure Your Environment

Set your Telegram bot token as an environment variable.

Linux / macOS

bash
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"


Windows PowerShell

powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"


Your Python application should read the token from the environment rather than storing it directly in source code.

5. Start the Bot
bash
python main.py


🎉 Congratulations! Your Telegram cryptocurrency bot is now running.

💬 Usage

After launching your application, open Telegram and search for your bot's username.

Available Commands
Command	Function
/start	Start the bot and display the welcome message
/kripto	Get Bitcoin and Ethereum prices
Start Command
text
/start


The bot welcomes the user and provides information about the project and available commands.

Cryptocurrency Command
text
/kripto


The bot retrieves the latest BTC/USDT and ETH/USDT prices from Binance and sends them to Telegram.

🌐 Binance API

This project uses Binance's public ticker price endpoint.

API Endpoint

text
https://api.binance.com/api/v3/ticker/price

Supported Trading Pairs
Cryptocurrency	Symbol
Bitcoin	BTCUSDT
Ethereum	ETHUSDT
Example Request
python
import requests

def get_coin_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data = requests.get(url).json()
    return float(data["price"])

Example API Response
json
{
    "symbol": "BTCUSDT",
    "price": "67450.25000000"
}


The API returns the latest available ticker price for the requested trading pair.

Official documentation:

Binance Spot API Documentation

📁 Project Structure
text
crypto-tracker-telegram-bot/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md

File	Description
main.py	Main application
requirements.txt	Python dependencies
.env.example	Example environment configuration
.gitignore	Files excluded from Git
LICENSE	Project license
README.md	Project documentation
🔐 Security

Your Telegram bot token is private information.

Please follow these security practices:

Never publish your Telegram bot token.
Store credentials in environment variables.
Never commit .env files.
Regenerate your token if it becomes publicly exposed.
Do not share private configuration files.

Example .gitignore:

gitignore
.env
venv/
__pycache__/
*.pyc

🗺️ Roadmap

Planned improvements and possible future features:

Telegram bot integration
Binance API integration
Bitcoin price tracking
Ethereum price tracking
Support for additional cryptocurrencies
Interactive Telegram keyboards
Custom cryptocurrency selection
Price alerts and notifications
24-hour price change tracking
Cryptocurrency charts
Database integration
Docker support
Cloud deployment guide
🤝 Contributing

Contributions, suggestions, and bug reports are always welcome!

To contribute:

Fork this repository.
Create a new feature branch.
Make your changes.
Commit your changes.
Push your branch.
Open a Pull Request.
bash
git checkout -b feature/my-feature
git add .
git commit -m "Add my feature"
git push origin feature/my-feature


Let's make this project better together!

👨‍💻 Developer

<div align="center">

Ahmet Baytören

Python Developer | Open Source Enthusiast

![GitHub](https://img.shields.io/badge/GitHub-ahmetbaytoren-181717?style=for-the-badge&logo=github)

![Instagram](https://img.shields.io/badge/Instagram-g0dvll-E4405F?style=for-the-badge&logo=instagram&logoColor=white)

</div>

📄 License

This project is distributed under the MIT License.

See the LICENSE file for more information.

<div align="center">

⭐ If you like this project, give it a star!

Your support motivates further development.

Made with ❤️ and Python

© Ahmet Baytören

</div>
