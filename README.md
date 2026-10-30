🚀 Crypto Tracker Telegram Bot

A simple, lightweight, and easy-to-use Telegram bot that tracks real-time cryptocurrency prices using the Binance API.

With this bot, you can instantly check Bitcoin (BTC) and Ethereum (ETH) prices in USDT directly from Telegram.

Whether you are a cryptocurrency enthusiast, a beginner developer, or someone learning Python Telegram bot development, this project provides a simple starting point for building your own cryptocurrency tracking bot.

✨ Features
📈 Real-Time Cryptocurrency Prices: Fetches the latest cryptocurrency prices from Binance.
₿ Bitcoin Tracking: Get the current BTC/USDT price.
Ξ Ethereum Tracking: Get the current ETH/USDT price.
🤖 Telegram Integration: Easily interact with the bot through Telegram commands.
⚡ Automatic Updates: Displays cryptocurrency prices at regular intervals.
🌐 Binance API: Uses Binance's public market data API. No Binance API key is required.
🐍 Python-Based: Built with Python and the python-telegram-bot library.
🛠️ Open Source: Free to use, modify, and improve.
📸 Bot Preview

When you start the bot using the /start command, you will receive a welcome message.

Example:

text
Hello! I am a cryptocurrency tracking bot.

Created by Ahmet Baytören.

Instagram: https://www.instagram.com/g0dvll
GitHub: https://github.com/ahmetbaytoren

For cryptocurrency prices, use:
/kripto


When you send /kripto, the bot retrieves cryptocurrency prices from Binance.

Example response:

text
Bitcoin: $67450.25
Ethereum: $3520.80


Prices shown above are illustrative examples and not live market prices.

🧰 Technologies Used
Technology	Purpose
Python 3	Main programming language
python-telegram-bot	Telegram Bot API integration
Binance API	Cryptocurrency market data
Requests	HTTP requests
Asyncio	Asynchronous programming
📋 Requirements

Before installing the project, make sure you have:

Python 3.9 or newer.
A Telegram account.
A Telegram bot token from BotFather.
An internet connection.

You do not need a Binance account or Binance API key because the project uses Binance's public ticker endpoint.

⚙️ Installation Guide

Follow these steps to create and run your own cryptocurrency tracking bot.

1. Clone the Repository

Open your terminal and run:

bash
git clone https://github.com/ahmetbaytoren/crypto-tracker-telegram-bot.git


Navigate to the project directory:

bash
cd crypto-tracker-telegram-bot

2. Install Dependencies

Install the required Python packages:

bash
pip install python-telegram-bot requests

3. Create Your Own Telegram Bot

You need to create a Telegram bot before running the application.

Open Telegram.
Search for @BotFather.
Start a conversation by sending /start.
Send the /newbot command.
Enter a display name for your bot.
Choose a unique username ending in bot.
BotFather will generate an API token for your bot.
Copy your token and keep it private.

Important: Never share your Telegram bot token publicly or upload it to GitHub.

4. Configure Your Bot Token

Open the Python source file and configure your bot token using an environment variable.

For Linux and macOS:

bash
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"


For Windows PowerShell:

powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"


Your Python application should read the token like this:

python
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not configured.")

5. Run the Application

Start your bot:

bash
python main.py


If everything is configured correctly, your Telegram bot will start polling for incoming messages.

🤖 How to Use the Bot

Once your bot is running, open Telegram and search for the username you selected during the BotFather setup.

Available Commands
Command	Description
/start	Starts the bot and displays the welcome message.
/kripto	Retrieves Bitcoin and Ethereum prices from Binance.
Starting the Bot

Send:

text
/start


The bot will introduce itself and show the available commands.

Checking Cryptocurrency Prices

Send:

text
/kripto


The bot will retrieve the latest BTC/USDT and ETH/USDT prices.

🔌 Binance API Integration

This project uses Binance's public cryptocurrency ticker endpoint.

API Endpoint:

text
https://api.binance.com/api/v3/ticker/price


To retrieve Bitcoin's price:

text
https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT


To retrieve Ethereum's price:

text
https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT


Example API response:

json
{
    "symbol": "BTCUSDT",
    "price": "67450.25000000"
}


The bot converts the returned price into a floating-point number and sends it to the Telegram user.

No private Binance API credentials are required.

📁 Project Structure

A recommended project structure:

text
crypto-tracker-telegram-bot/
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

File Descriptions
main.py: Main Telegram bot application.
requirements.txt: Required Python dependencies.
.gitignore: Prevents sensitive files from being uploaded.
.env.example: Example environment configuration.
README.md: Project documentation.
🔒 Security

Security is important when running Telegram bots.

Please follow these recommendations:

Never publish your Telegram bot token.
Never commit .env files to GitHub.
Use environment variables to store sensitive credentials.
Regenerate your bot token if it is accidentally exposed.
Avoid sharing private configuration files.

Example .gitignore:

gitignore
.env
venv/
__pycache__/
*.pyc

🛠️ Troubleshooting
Bot Does Not Start

Make sure that:

Python is installed correctly.
All dependencies are installed.
Your Telegram bot token is valid.
Your internet connection is working.
Invalid Telegram Token

If you receive an authentication error, check your token through BotFather.

Binance API Errors

If cryptocurrency prices cannot be retrieved:

Check your internet connection.
Make sure Binance's API is accessible.
Verify the trading symbol.
Check whether you have exceeded API rate limits.
Bot Stops Responding

Make sure your Python application is still running. The bot must remain active to receive Telegram updates.

🚀 Future Improvements

This project can be extended with additional features.

Some ideas for future versions:

Add more cryptocurrencies.
Add Solana (SOL), BNB, XRP, and Dogecoin (DOGE).
Add inline Telegram keyboards.
Allow users to select their preferred cryptocurrencies.
Add price alerts and notifications.
Add percentage change tracking.
Add 24-hour high and low prices.
Add cryptocurrency charts.
Add database support.
Add automatic scheduled price updates.
Add Docker support.
Add deployment instructions for cloud servers.

Contributions and suggestions are welcome!

🤝 Contributing

Contributions are welcome!

If you want to improve this project:

Fork this repository.
Create a new branch.
bash
git checkout -b feature/new-feature

Make your changes.
Commit your changes.
bash
git commit -m "Add new feature"

Push your branch.
bash
git push origin feature/new-feature

Open a Pull Request.

Feel free to report bugs, suggest improvements, or contribute new features.

👨‍💻 Author

Ahmet Baytören

Instagram: @g0dvll
GitHub: @ahmetbaytoren
📄 License

This project is open-source. You are welcome to explore, modify, and learn from the source code.

If you redistribute or modify this project, please retain the original author attribution.

For a clearly defined open-source license, see the MIT License.

⭐ Support

If you find this project useful:

Give the repository a ⭐ Star.
Fork the project.
Share it with other Python and cryptocurrency enthusiasts.
Contribute to its development.

Thanks for checking out Crypto Tracker Telegram Bot!

Made with ❤️ and Python by Ahmet Baytören.
