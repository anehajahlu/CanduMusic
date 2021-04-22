from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋! Saya dapat memutar musik dalam obrolan suara Grup Telegram.\n\n▹ Apakah Anda ingin saya memutar musik di obrolan suara grup Telegram Anda? Silakan klik \'📚 Panduan Menggunakan BOT 📚\' tombol di bawah untuk mengetahui bagaimana cara menggunakan saya.\n\n📚 Tambahkan [Candu Assistant Music](https://t.me/@CanduMusicBot) ke grup Anda untuk memutar musik di obrolan suara grup Anda.\n\n▹ Info & perintah selengkapnya yang disebutkan di [Cara & Menggunakan](https://telegra.ph/BOT-Music-Man-Voice-Chat-Group-04-16)\n\nManaged By [Vckyyy](https://t.me/VckyouuBitch)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📚 Panduan Menggunakan Bot 📚", url="https://t.me/Lunatic0de/20")
                  ],[
                    InlineKeyboardButton(
                        "🛡️ Group Support 🛡️", url="https://t.me/VcgSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "📣 Support Channel 📣", url="https://t.me/Vckyouuu"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**▹ Pemutar Musik Sedang Online **""",
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
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
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
