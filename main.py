import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped

# إعدادات البوت الخاصة بك (تم وضعها مباشرة)
API_ID = 38828593
API_HASH = "e98b905f88b9795e7af2e9b58bc18fe9"
BOT_TOKEN = "8271537891:AAHNYXhfvR1Vz3o60pcO_C60gKofeMv21cI"

app = Client("QuranStream", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

# رابط الإذاعة (قرآن مكة المكرمة 24 ساعة)
STREAM_URL = "https://broadcast.quran.com.sa/radio/8006/radio.mp3"

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("البوت يعمل بنجاح! أضفني للقناة كمسؤول (Admin) ثم أرسل أمر /play هنا للبدء.")

@app.on_message(filters.command("play"))
async def play(client, message):
    chat_id = message.chat.id
    try:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(STREAM_URL),
            stream_type=StreamType().pulse_stream,
        )
        await message.reply_text("تم تشغيل البث المباشر للقرآن الكريم بنجاح (24/7).")
    except Exception as e:
        await message.reply_text(f"حدث خطأ: {e}\nتأكد من فتح البث المباشر يدوياً في القناة لأول مرة.")

app.start()
call_py.run()
