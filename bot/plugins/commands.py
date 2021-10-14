#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
        update_channel = cinimafactory2
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text=Mo_Tech_YT.MO_TECH_YT_14,
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 📢 Join My Update Channel 📢", url=f"https://t.me/{cinimafactory2}")]
              ])
            )
            return

    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '♻️ՏᎻᎪᎡᎬ ᎷᎬ♻️', url="https://t.me/share/url?url=%20https://t.me/cinimafactory2"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🔥ᎷᎽ ᎠᎬᏙ', url='https://t.me/Techno_ka_magic'),
        InlineKeyboardButton('ՏϴႮᎡᏟᎬ ᏟϴᎠᎬ🧾', url ='https://t.me/joinchat/Nl6kfq6CW_tlYWM9')
    ],[
        InlineKeyboardButton('ՏႮᏢᏢϴᎡͲ 🛠', url='https://t.me/asbotz')
    ],[
        InlineKeyboardButton('ᎻᎬᏞᏢ ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('ᎻϴᎷᎬ ⚡', callback_data='start'),
        InlineKeyboardButton('ᎪᏴϴႮͲ 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('ᏟᏞϴՏᎬ 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('ᎻϴᎷᎬ ⚡', callback_data='start'),
        InlineKeyboardButton('ᏟᏞϴՏᎬ 🔐', callback_data='close')
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
