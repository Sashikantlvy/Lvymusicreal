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
          InlineKeyboardButton("🥀ᴅᴇᴠᴇʟᴏᴘᴇʀ🥀", url="https://t.me/ABOUT_SASHIKANT"),
          ],
               [
                InlineKeyboardButton("ʀᴇᴘᴏ", url="https://telegra.ph/file/78be765f35211e764a9d5.mp4"),
]
        [
          InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/statusdairy2"),
    ] 
        [
          InlineKeyboardButton("˹ѕᴄαꝛ ꭙ ꝛσʙσᴛ˼", url="https://t.me/SCAR_X_ROBOT?startgroup=true"),
          InlineKeyboardButton("˹νσн ꭙ мυѕιᴄ˼🥀", url="https://t.me/VOH_MUSIC_BOT?startgroup=true")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/388664b8e357f59298277.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
