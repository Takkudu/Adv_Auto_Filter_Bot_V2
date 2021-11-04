#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG 

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = "<b>┈••✿ cinema factory ✿••┈\n\n➠𝐂ʜᴀɴɴᴇʟ :https://t.me/cinemafactory_all\n\n➠Gʀᴏᴜᴘ : https://t.me/cinimafactory2</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⭕️ 𝙎𝙃𝘼𝙍𝙀 ⭕️', url='https://t.me/share/url?url=https://t.me/cinimafactory2')
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/cinimafactory2'),
                    InlineKeyboardButton('‼️ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url='https://t.me/cinemafactory_all')
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⭕️ 𝙎𝙃𝘼𝙍𝙀 ⭕️', url='https://t.me/share/url?url=https://t.me/CinemaFactory_All')
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋 💬', url='https://t.me/cinimafactory2'),
                    InlineKeyboardButton('‼️ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url='https://t.me/cinemafactory_all')
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 ⚠️', url="https://t.me/CinemaFactory_All"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('🛡️ 🄶🅁🄾🅄🄿', url='https://t.me/Techno_KaMagic'),
        InlineKeyboardButton('👼 𝘾𝙍𝙀𝘼𝙏𝙊𝙍', url ='https://t.me/Techn_oKa_Magic')
        ],[
        InlineKeyboardButton('⚔️ 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ⚔️', url ='https://t.me/ASBOTZ')
        ],[
        InlineKeyboardButton('🤠 𝙃𝙀𝙇𝙋', callback_data="help"),
        InlineKeyboardButton('🔐 𝘾𝙇𝙊𝙎𝙀', callback_data="close")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/605bf4fdea60c9923cab1.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('𝙃𝙤𝙢𝙚 🏘', callback_data='start'),
        InlineKeyboardButton('𝘼𝙗𝙤𝙪𝙩 👿', callback_data='about')
    ],[
        InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/605bf4fdea60c9923cab1.jpg",
        caption=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝙃𝙤𝙢𝙚 🏘', callback_data='start'),
        InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
