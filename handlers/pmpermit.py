from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo, Saya adalah **Layanan Asisten Musik.**\n\n ❗️ Rules:\n   -Silahkan Ketik /Start @CanduMusicBot\n   - Jangan spam Lagu biar ga error \n\n 👉 **KIRIM LINK UNDANGAN GRUP ATAU NAMA PENGGUNA JIKA USERBOT TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n ⛑ **Group Support :** @VcgSupportGroup - **Owner** @VckyouuBitch\n\n")
  return                        
