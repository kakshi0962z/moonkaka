from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", callback_data="settings_back_helper"
            )
        ],  
            [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+ZRhHTR-_xu1kNjE5"),
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴏᴜʀᴄᴇ ✨", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
