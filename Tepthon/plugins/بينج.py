# ======================================================================================================================================
# ping -> edited ping with pic by  @PPF22
# كتابة الملف لسورس تيبثون فقط ممنوع نسبه لنفسك
# تخمط دليل فشلك اخمط وكول اني مطور 😂😂

import os
from datetime import datetime

from Tepthon import zedub

#
from . import hmention, reply_id

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/502a2c9751c3c06222c51.jpg"
)

JM_TXT = os.environ.get("PING_TEXT") or "مـن لا يتعلم من الماضي لا يرحمه المستقبل  . 🖤"


@zedub.zed_cmd(pattern="بنك$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    zed = await edit_or_reply(
        event, "<b><i>  ❤️⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃟✨ البــــنك... 🍀⃝⃝⃟🍂 </b></i>", "html"
    )
    end = datetime.now()
    await roz.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>┏━━━━━━━┓\n┃ ✦ {ms}\n┃ ✦ <b>{hmention}</b>\n┗━━━━━━━┛"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================
