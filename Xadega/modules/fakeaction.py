from asyncio import sleep

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from Xadega import ubot
from Xadega.config import *
from Xadega.modules.bot import add_command_help
from Xadega.utils.data import *
from Xadega.utils.misc import *

commands = {
    "ftyping": enums.ChatAction.TYPING,
    "fvideo": enums.ChatAction.RECORD_VIDEO,
    "faudio": enums.ChatAction.RECORD_AUDIO,
    "fround": enums.ChatAction.RECORD_VIDEO_NOTE,
    "fphoto": enums.ChatAction.UPLOAD_PHOTO,
    "fsticker": enums.ChatAction.CHOOSE_STICKER,
    "fdocument": enums.ChatAction.UPLOAD_DOCUMENT,
    "flocation": enums.ChatAction.FIND_LOCATION,
    "fgame": enums.ChatAction.PLAYING,
    "fcontact": enums.ChatAction.CHOOSE_CONTACT,
    "fstop": enums.ChatAction.CANCEL,
    "fscreen": "screenshot",
}


@ubot.on_message(filters.command(list(commands), PREFIX) & filters.me)
async def fakeactions_handler(client, message: Message):
    cmd = message.command[0]
    try:
        sec = int(message.command[1])
        if sec > 60:
            sec = 60
    except:
        sec = None
    await message.delete()
    action = commands[cmd]
    try:
        if action != "screenshot":
            if sec and action != enums.ChatAction.CANCEL:
                await client.send_chat_action(chat_id=message.chat.id, action=action)
                await sleep(sec)
            else:
                return await client.send_chat_action(
                    chat_id=message.chat.id, action=action
                )
        else:
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.1)
    except Exception as e:
        return await client.send_message(
            message.chat.id,
            f"**ERROR:** `{e}`",
            reply_to_message_id=ReplyCheck(message),
        )


add_command_help(
    "fakeaction",
    [
        ["ftyping [detik]", "Menampilkan Pengetikan Palsu dalam obrolan."],
        ["fgame [detik]", "Menampilkan sedang bermain game Palsu dalam obrolan."],
        [
            "faudio [detik]",
            "Menampilkan tindakan merekam suara palsu dalam obrolan.",
        ],
        [
            "fvideo [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            "fround [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            "fphoto [detik]",
            "Menampilkan tindakan mengirim foto palsu dalam obrolan.",
        ],
        [
            "fsticker [detik]",
            "Menampilkan tindakan memilih Sticker palsu dalam obrolan.",
        ],
        [
            "fcontact [detik]",
            "Menampilkan tindakan Share Contact palsu dalam obrolan.",
        ],
        [
            "flocation [detik]",
            "Menampilkan tindakan Share Lokasi palsu dalam obrolan.",
        ],
        [
            "fdocument [detik]",
            "Menampilkan tindakan tengirim Document/File palsu dalam obrolan.",
        ],
        [
            "fscreen [jumlah]",
            "Menampilkan tindakan screenshot palsu. (Gunakan di Obrolan Pribadi)",
        ],
        ["fstop", "Memberhentikan tindakan palsu dalam obrolan."],
    ],
)

