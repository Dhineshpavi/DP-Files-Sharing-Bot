#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>■ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : <a href='tg://user?id={OWNER_ID}'>𝗜𝘁'𝘀 𝗠𝗲</a>\n■ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : <code>𝗣𝘆𝘁𝗵𝗼𝗻𝟯</code>\n■ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲 : <a href='https://t.me/DP_BOTZ'>𝗖𝗹𝗶𝗰𝗸</a>\n■ 𝗠𝗼𝘃𝗶𝗲𝘀 : <a href='https://t.me/movies_days'>𝗧𝗮𝗺𝗶𝗹 𝗠𝗼𝘃𝗶𝗲𝘀</a>\n■ 𝗔𝗻𝗶𝗺𝗲𝘀  : <a href='https://t.me/AnimesWorldTamil'>𝗧𝗮𝗺𝗶𝗹 𝗔𝗻𝗶𝗺𝗲𝘀</a>\n■ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 : <a href='https://t.me/AnimesWorldTamil'>𝐃𝐩_𝐁𝐨𝐭𝐳</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "Close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
