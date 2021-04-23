from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""✨HI, Selamat Datang!

Bot Music adalah proyek yang dirancang untuk memutar, secara sesederhana mungkin, musik dalam grup anda melalui obrolan suara yang baru diperkenalkan oleh Telegram.

❓Bagaimana cara menggunakannya?
Tekan tombol » [📚 Penjelasan & Perintah BOT 📚](https://telegra.ph/text-04-22-3) untuk melihat daftar lengkap & Penjelasanya""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡ My Instagram ⚡", url="https://www.instagram.com/Vckyouuu")
                  ],[
                    InlineKeyboardButton(
                        "🛡️ Group Support", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel Support", url="https://t.me/Vckyouuu"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**▹ Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/Vckyouuu"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/Vckyouuu"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""• Berikut Perintah Untuk member dalam grup :

/play <nama lagu>  - Untuk Memutar lagu yang Anda minta melalui youtube
/dplay <nama lagu>  - Untuk Memutar lagu yang Anda minta melalui deezer
/playlist - Untuk Menampilkan daftar putar Lagu sekarang
/song <nama lagu> - Untuk Mendownload lagu di YouTube 
/video <nama lagu> - Untuk Mendownload Video di YouTube dengan detail
/deezer <nama lagu> - Untuk Mendownload lagu dari deezer 
/saavn <nama lagu> - Untuk Mendownload lagu dari website saavn
/search <nama lagu> - Untuk Mencari Video di YouTube dengan detail


• Berikut perintah yang hanya admin dalam group :

/pause - Untuk Menjeda pemutaran Lagu
/resume - Untuk Melanjutkan pemutaran Lagu yang di pause
/skip - Untuk Menskip pemutaran lagu ke Lagu berikutnya
/end - Untuk Memberhentikan pemutaran Lagu
/userbotjoin - Untuk Mengundang asisten ke obrolan Anda
/admincache - Untuk MemRefresh admin list""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        text="❌ Close",
                        callback_data='cls')
                    )
                ]
            ]
        )
   )

