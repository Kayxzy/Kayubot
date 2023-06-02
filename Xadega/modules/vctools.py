from pyrogram import enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall

from Xadega import ubot
from Xadega.config import PREFIX
from Xadega.modules.bot import add_command_help
from Xadega.utils.misc import get_arg

add_command_help(
    "vctools",
    [
        ["startvc", "Untuk Memulai video call group."],
        ["stopvc", "Untuk Memberhentikan video call group."]
    ],
)


@ubot.on_message(filters.command("startvc", PREFIX) & filters.me)
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    sup = await message.reply("__Memproses...__")
    args = f"**Memulai Panggilan Grup**\n• **Chat Id:** `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=await client.resolve_peer(message.chat.id),
                    random_id=client.rnd_id() // 9000000000,
                )
            )
        else:
            args += f"\n• **Title :** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=await client.resolve_peer(message.chat.id),
                    random_id=client.rnd_id() // 9000000000,
                    title=vctitle,
                )
            )
        await sup.edit(args)
    except Exception as e:
        return await sup.edit(f"**INFO :** `{e}`")


@ubot.on_message(filters.command("stopvc", PREFIX) & filters.me)
async def end_vc_(client, message):
    chat_id = message.chat.id
    msg = await message.reply("__Memproses...__")
    try:
        full_chat = (
            await client.invoke(
                GetFullChannel(channel=await client.resolve_peer(chat_id))
            )
        ).full_chat
        await client.invoke(DiscardGroupCall(call=full_chat.call))
        await msg.edit(f"**Mengakhiri panggilan grup di**\n**Chat ID :** `{chat_id}`")
    except Exception as e:
        return await msg.edit(f"**INFO :** `{e}`")