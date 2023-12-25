from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴋʏᴀ 😂🤡
**"""




@app.on_message(filters.command("qazwsxedcrfvtgbyhnujmiklop"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🍃", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"),
          InlineKeyboardButton("🥀ᴅᴇᴠᴇʟᴏᴘᴇʀ🥀", url="https://t.me/ABOUT_SASHIKANT"),
          ],
               [
                InlineKeyboardButton("ʀᴇᴘᴏ", url="https://telegra.ph/file/78be765f35211e764a9d5.mp4"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/7308ef404bd3d6b7ad9be.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
