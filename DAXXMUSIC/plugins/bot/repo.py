from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴋʏᴀ 😂🤡
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🍃", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"),
          InlineKeyboardButton("🥀ᴏᴡɴᴇʀ🍃", url="https://t.me/ABOUT_SASHIKANT"),
          ],
               [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/STATUSDAIRY2"),

],
[
              InlineKeyboardButton("˹ανα ꭙ мυѕιᴄ˼🥀", url=f"https://t.me/AVA_X_MUSIC_BOT?startgroup=true"),
              InlineKeyboardButton("︎˹ѕᴄαꝛ ꭙ ꝛσʙσᴛ˼", url=f"https://t.me/SCAR_X_ROBOT?startgroup=true"),
              ],
              [
              InlineKeyboardButton("ʀᴇᴘᴏ", url=f"https://telegra.ph/file/78be765f35211e764a9d5.mp4"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/d0c9034e51bdb3f88033e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
