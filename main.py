import requests
from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio

async def start(update, context):
    await update.message.reply_text("""
    Merhaba ben ahmet baytören tarafından yapılmış bir kripto takip botuyum.
    Instagram : https://www.instagram.com/g0dvll
    Github : https://github.com/ahmetbaytoren
    Kripto Fiyatları için >> /kripto
    """)

def get_coin_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data=requests.get(url).json()
    return float(data['price'])

async def kripto(update, context):
    while True:
        bitcoin_price=get_coin_price('BTCUSDT')
        etherium_price=get_coin_price('ETHUSDT')

        coin_prices=(f"Bitcoin: ${bitcoin_price}\n"
                     f"Ethereum : ${ethereum_price}")

        await update.message.reply_text(coin_prices)
        await asyncio.sleep(10)

app = ApplicationBuilder().token('8878819552:AAEBSn1kDltGkfm0IM52sxlWp56LzK0Zb9o').build()

app.add_handler(CommandHandler('start',start))
app.add_handler(CommandHandler('kripto',kripto))

app.run_polling()
