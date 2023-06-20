import requests
import telegram
import asyncio

async def send_dog_photo():
    # Fetch random dog image URL from Dog API
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]
    else:
        print("Failed to retrieve dog image from API.")
        return
    
    # Set up Telegram bot
    bot_token = "6177428008:AAEewf2ZGq657fvMqJ6oqH4tYoYvpaP68p8"
    chat_id = "1285682450"

    bot = telegram.Bot(token=bot_token)

    # Send dog image via Telegram bot
    await bot.send_photo(chat_id=chat_id, photo=image_url)

async def run_code_periodically():
    while True:
        await send_dog_photo()
        await asyncio.sleep(6 * 60 * 60)  # Sleep for 6 hours

asyncio.run(run_code_periodically())
