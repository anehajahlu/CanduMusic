from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm Music Player Telegram!

Aku Pemutar Musik, Aku Akan Menghiburmu Di Voice Chat Grup!. Developed by [AFTER](https://t.me/afterdaytoxic).

Tambahin Aku Di Grupmu, Dan Jangan Lupa Sama Assistennya Diundang Ke Grup!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฃ OWNERKU!", url="https://t.me/afterdaytoxic")
                  ],[
                    InlineKeyboardButton(
                        "๐ฌ GROUP!", url="https://t.me/humangabutguys"
                    ),
                    InlineKeyboardButton(
                        "๐ CHANNEL!", url="https://t.me/captionanakmuda"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "๐ CARA MENGGUNAKAN AKU!", url="https://telegra.ph/แตสท-๐ก๐ฒ๐๐ด๐ฑ๐ช-04-07"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**SAVIRA MUSIC ON / AKTIF! โ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Channel", url="https://t.me/captionanakmuda")
                ]
            ]
        )
   )


