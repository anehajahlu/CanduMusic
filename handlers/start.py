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
                        "Group Support", url="https://t.me//t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/Vckyouuu"
                    )
                ]
            ]
        )
   )

