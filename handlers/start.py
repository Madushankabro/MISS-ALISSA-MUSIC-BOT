from config import BOT_NAME as bot_username
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
   await message.reply_text(
        f""" <b>Hi {message.from_user.first_name}!

βοΈ I am ππππ πΌπππππΌ πππππΎ π½ππ, an open-source bot that lets you play music in your Telegram groups.
Maintained by @kasu_bro π±π°


βοΈ Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βοΈ Add Alissa Music Bot to Your Group βοΈ", url="t.me/MissAlissaMisicBot?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π₯ Group π₯", url="https://t.me/epusthakalayabots_chat"
                    ),
                    InlineKeyboardButton(
                        "π£ Channel π£", url="https://t.me/epusthakalaya_bots"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β Dev β", url="https://t.me/kasu_bro"
                    ),
                    InlineKeyboardButton(
                        "πΎ Source Code πΎ", url="https://github.com/Madushankabro/MISS-ALISSA-MUSIC-BOT"
                    )    
                ],
            ]
        )
    )
@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π£ Channel π£", url="https://t.me/epusthakalaya_bots"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!

βοΈUsers CommandsβοΈ
/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

βοΈAdmins onlyβοΈ
/player - open Music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π£ Channel π£", url="https://t.me/epusthakalaya_bots"
                    )
                ]
            ]
        )
    )   

