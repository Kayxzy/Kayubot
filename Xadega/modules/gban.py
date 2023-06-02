from asyncio import sleep

from pyrogram import filters

from Xadega import ubot
from Xadega.config import *
from Xadega.modules.bot import add_command_help
from Xadega.utils.data import *
from Xadega.utils.misc import *

add_command_help(
    "gban",
    [
        [
            "gban [username atau reply]",
            "Untuk memblokir user dari semua grup yang anda adminin",
        ],
        [
            "ungban [username atau reply]",
            "Untuk menghapus blokir user dari semua grup yang anda adminin",
        ],
        ["gbanlist", "Untuk menampilkan daftar gbanned"],
    ],
)


@ubot.on_message(filters.command("cgban", ".") & filters.user(OWNER_ID))
@ubot.on_message(filters.command("gban", PREFIX) & filters.me)
async def gban_cuk(c, m):
    anu = await extract_user(m)
    if not anu:
        return await m.reply(
            "__Silahkan balas ke user atau gunakan id atau username user__"
        )
    try:
        ak = await c.get_users(anu)
    except:
        return await m.reply("__Tidak menemukan user tersebut__")
    fullname = f"{ak.first_name} {ak.last_name or ''}"
    ppk = await all_grup(c.me.id)
    iso = 0
    ggl = 0
    msg = await m.reply("__Processing...__")
    for x in ppk:
        chat = x["grup"]
        if ak.id != OWNER_ID or ak.id != c.me.id:
            try:
                await c.ban_chat_member(chat, ak.id)
                iso += 1
                await sleep(1)
            except Exception:
                ggl += 1
                await sleep(1)
        elif ak.id == c.me.id:
            return await msg.edit("**Apakah kamu bodoh mau gban akunmu sendiri**")
        else:
            return await msg.edit("**Apakah kamu bodoh mau gban pembuat saya**")
    await add_gban(c.me.id, ak.id, fullname)
    return await msg.edit(
        f"**Global Banned**\n✅ **Berhasil** : {iso} Chat\n❌ **Gagal**: {ggl} Chat\n👾 **User**: {fullname}"
    )


@ubot.on_message(filters.command("ungban", PREFIX) & filters.me)
async def ungban_cuk(c, m):
    anu = await extract_user(m)
    if not anu:
        return await m.reply(
            "__Silahkan balas ke user atau gunakan id atau username user__"
        )
    try:
        ak = await c.get_users(anu)
    except:
        return await m.reply("__Tidak menemukan user tersebut__")
    fullname = f"{ak.first_name} {ak.last_name or ''}"
    ppk = await all_grup(c.me.id)
    iso = 0
    ggl = 0
    msg = await m.reply("__Processing...__")
    for x in ppk:
        chat = x["grup"]
        if ak.id != OWNER_ID or ak.id != c.me.id:
            try:
                await c.unban_chat_member(chat, ak.id)
                iso += 1
                await sleep(1)
            except Exception:
                ggl += 1
                await sleep(1)
        elif ak.id == c.me.id:
            return await msg.edit("**Sepertinya tidak ada yang perlu di ungban**")
        else:
            return await msg.edit("**Sepertinya tidak ada yang perlu di ungban**")
    await del_gban(c.me.id, ak.id)
    return await msg.edit(
        f"**Global Unbanned**\n✅ **Berhasil** : {iso} Chat\n❌ **Gagal**: {ggl} Chat\n👾 **User**: {fullname}"
    )


@ubot.on_message(filters.command("gbanlist", PREFIX) & filters.me)
async def gbanlist_cuk(c, m):
    msg = "**Daftar Global Banned**\n\n"
    anu = await all_gban(c.me.id)
    if anu is False:
        return await m.reply("**Belum ada daftar global banned**")
    d = 0
    for x in anu:
        try:
            ex = x["user"]
            ss = x["nama"]
            d += 1
        except:
            continue
        msg += f"{d}. {ex} | `{ss}`\n"
    await m.reply(msg)
