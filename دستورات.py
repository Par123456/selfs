from pyrogram import Client, filters, idle , errors
from pyrogram.types import *
from pyrogram.raw import functions , base , types
import os
try:
    import pyromod.listen
except ImportError:
    os.system("python3 -m pip install pyromod")

api_id = 29042268
api_hash = '54a7b377dd4a04a58108639febe2f443'
app = Client("araz", api_id, api_hash)

# ---------- متن‌های راهنما ----------
help1 = """
   **Mute**
❋ `.mute` ⤳ (`ɪɴʙᴜɪʟᴛ ᴍᴜᴛᴇ`)
❋ `.unmute` ⤳ (`ᴜɴᴍᴜᴛᴇ`)
❋ `.allunmute` ⤳ (`ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴜᴛᴇ`)"""

help3 = """
   **Group Helper**
❋ **ɪғ ʏᴏᴜ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀᴛ**
❋ `.ban` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.unban` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.setmute` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.delmute` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.setchatphoto` ⤳ (`ᴏɴʟʏ ʀᴇᴘʟʏ`)
❋ `.setchattitle` ⤳ (`ɴᴀᴍᴇ`)
❋ `.setchatbio` ⤳ (`ʙɪᴏ`)
❋ `.setchatusername` ⤳ (`ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.pin` ⤳ (`ᴏɴʟʏ ʀᴇᴘʟʏ`)
❋ `.unpin` ⤳ (`ᴏɴʟʏ ʀᴇᴘʟʏ`)
❋ `.unpinall` ⤳ (`ɴᴏ ʀᴇᴘʟʏ`)
❋ `.deletechannel` ⤳ (`ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.deletegroup` ⤳ (`ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.delallmsguser` ⤳ (`ᴏɴʟʏ ʀᴇᴘʟʏ`)
❋ `.slowmod` ⤳ (`ɴᴜᴍ`)
❋ `.delete` ⤳ (`ɴᴜᴍ`)
❋ `.tadmin`
❋ `.delethistory`"""

help4 = """
   **Time**
❋ `.timename` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.2timename` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.timebio` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.2timebio` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.3timebio` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋⤳**ꜱᴇᴛʙɪᴏ ᴡɪᴛʜ(**`.setbio`**)**\n⤳__Bio Must Be lower Than 45 Character__

❋ `.fontname` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋⤳**ꜱᴇᴛɴᴀᴍᴇ ᴡɪᴛʜ(**`.setname`**)**

   **Profile Photo**
❋ `.setprofile` ⤳ (`ʀᴇᴘʟʏ`)
❋ `.delprofile`"""

help5 = """
   **Helpful Section**
❋ `.setname` ⤳ (`ɴᴀᴍᴇ`)
❋ `.setlastname` ⤳ (`ʟᴀsᴛɴᴀᴍᴇ`)
❋ `.setbio` ⤳ (`ʙɪᴏ`)
❋⤳**ʟᴏᴡᴇʀ ᴛʜᴀɴ 64 ᴄʜᴀʀ ɪꜰ ᴡᴀɴɴᴀ ᴜꜱᴇ ᴛɪᴍᴇʙɪᴏ**
❋ `.fontfa` ⤳ (`ᴘᴇʀsɪᴀɴ ғᴏɴᴛ`)
❋ `.fonten` ⤳ (`ᴇɴɢʟɪsʜ ғᴏɴᴛ`)
❋ `.clone` ⤳ (`ᴄʟᴏɴᴇ ᴜsᴇʀ`)
❋ `.block` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.unblock` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.join` ⤳ (`ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.creatchannel` ⤳ (`ɴᴀᴍᴇ`)
❋ `.creatsupergroup` ⤳ (`ɴᴀᴍᴇ`)
❋ `.creatgroup` ⤳ (`ɴᴀᴍᴇ`)
❋ `.searchwiki` ⤳ (`ʟɪɴᴋ ɴᴀᴍᴇ`)
❋ `.mention` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.get_message` ⤳ (`ʀᴇᴘʟʏ`)
❋ `.voice` ⤳ (`ᴛᴇxᴛ`)
❋ `.searchapp` ⤳ (`ᴀᴘᴘ ɴᴀᴍᴇ`)
❋ `.sms` ⤳ (`ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ`)"""

help6 = """
   **server info**
❋ `.ping` ⤳ (`ꜱᴛᴀᴛᴜꜱ`)
❋ `.on_off_status` ⤳ (`ꜱᴛᴀᴛᴜꜱ`)
❋ `.cpu`
❋ `.memory`
❋ `.system-inf`

   **information**
❋ `.file_info` ⤳ (`ꜰɪʟᴇ ɪɴꜰᴏ`)
❋ `.inf` ⤳ (`ᴄʜᴀᴛ ɪɴꜰᴏ`)
❋⤳@ᴛʜɪꜱ/ᴜꜱᴇʀɴᴀᴍᴇ
❋ `.id` ⤳ (`ᴜꜱᴇʀ ɪɴꜰᴏ`)
❋⤳ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ """

help7 = """
    **Enemy**
❋ `.setenemy` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.friend` ⤳ (`ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.allf` ⤳ (`ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴇɴᴇᴍʏ`)"""

help8 = """
    **Instagram**
❋ `.instalogin` ⤳ (`ʟᴏɢɪɴ`)
❋ `.imloged` ⤳ (`ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʟᴏɢɪɴ`)
❋ ɪғ ʏᴏᴜ ʟᴏɢᴇᴅ ɪɴ ᴛᴏ ɪɴꜱᴛᴀ
❋ `.mypageinfo` ⤳ (`ʏᴏᴜʀ ɪɴꜰᴏ`)
❋ `.follow` ⤳ (`ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.unfollow` ⤳ (`ᴜsᴇʀɴᴀᴍᴇ`)
❋ `.instagetuser` ⤳ (`ᴜꜱᴇʀ ɪɴꜰᴏ`)
❋ `.edit_firstname` ⤳ (`ɴᴀᴍᴇ`)
❋ `.edit_biography` ⤳ (`ʙɪᴏ`)
❋ `.instadl` ⤳ (`ᴅᴏᴡɴʟᴏᴀᴅ ᴘᴏꜱᴛ`)
⤳ ᴇɴᴛᴇʀ ᴘᴏꜱᴛ ᴜʀʟ
❋ `.story` ⤳ (`ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴛᴏʀʏ`)
⤳ ᴇɴᴛᴇʀ ᴘᴀɢᴇ ᴜꜱᴇʀɴᴀᴍᴇ"""

help9 = """
    **Practical Tools**
❋ `.tp` ⤳ (`ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ᴘɪᴄ`)
❋ `.ts` ⤳ (`ᴘɪᴄ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ`)
❋ `.tg` ⤳ (`ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ɢɪꜰ`)
   **Timer Pic**
❋ `.dl` ⤳ (`ꜱᴇɴᴅ ᴛᴏ ᴍ.ᴄʜᴀᴛ`)
❋ `waitt` ⤳ (`ꜱᴇɴᴅ ᴛᴏ ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇ`)
    **Spam**
❋ `.spam` ⤳ (`.ꜱᴘᴀᴍ + ɴᴜᴍ ᴏғ ꜱᴘᴀᴍ + ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ`)
❋ `.spm` ⤳ (`.ꜱᴘᴀᴍ + ɴᴜᴍ ᴏғ ꜱᴘᴀᴍ + ᴛᴇxᴛ`)
  **Time**
❋ `.time`
❋ `.timepic`"""

help10 = """
    **First Comment**
❋ `.firstcom` ⤳ (`ᴏɴ ᴏʀ ᴏꜰꜰ`)
❋ `.first_message` ⤳ (`ʀᴇᴘʟʏ`)

    **Send At A Time**
❋ `.text_time`⤳(`ʜʜ:ᴍᴍ`)
⤳ `.text_send_time`⤳(`ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ`)

❋ `.photo_time`⤳(`ʜʜ:ᴍᴍ`)
⤳`.photo_send_time`⤳(`ʀᴇᴘʟʏ ᴛᴏ ᴘɪᴄ`) """

help11 = """
    **Fun**
❋ `Reload`
❋ `.khaymallist`
    😎**Cheating**
❋ `.tas (1-6)`
❋ `.dart`
❋ `.bowling`
❋ `.basketball`
❋ `.football` (1or4)
❋⤳1 = fail , 4 = goll"""

help12 = """
    **Tools**
❋ `.ip` ⤳ (`ɢᴇᴛ ꜱɪᴛᴇ ɪᴘ`)
❋ `whoisip` ⤳ (`ɪᴘ ɪɴꜰᴏ`)
❋ `.nimurl` ⤳ (`ᴜʀʟ ɴɪᴍʙᴀʜᴀ`)
❋ `.qrcode` ⤳ (`ᴍᴀᴋᴇ Qʀᴄᴏᴅᴇ`)
❋ `.screenurl` ⤳ (`ᴡᴡᴡ.ᴜʀʟ.ᴄᴏᴍ`)
❋ `.pindl` ⤳ (`ᴘɪɴᴛᴇʀᴇꜱᴛ ᴅʟ`)
❋ `.dllink` ⤳ (`ᴜʀʟ`)
   **Movie**
❋ `.imdb` ⤳ (`ᴍᴏᴠɪᴇ ɴᴀᴍᴇ`)
   **YouTube**
❋ `.music` (**Not working**)
❋ `.ytdl` (**Not working**)
   **Porn**
❋ `.xnxx`
   **OCR**
❋ `.ocr`
⤳ `ʀᴇᴘʟʏ` """

help13 = """
    **text mode**
❋ `.bold` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.spoiler` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.italic` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.finglish` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.code` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.underline` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.strike` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.emoji` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)"""

help14 = """
    **Auto Answer**
❋ `.answer` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.addan` (`asnwer:javab`)
❋ `.delan`(`answer`)
❋ `.anlist`
❋ `.anclear` """

help15 = """
    **Anti Delete Member**
❋⤳ **ᴍᴜꜱᴛ ʙᴇ ᴀᴅᴍɪɴ**
❋ `.anti_fuck` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋ `.antich` (`-100 + **ᴄʜᴀᴛ-ɪᴅ`)
❋ .limit_del ⤳ (ʟɪᴍɪᴛ ᴏꜰ ᴅᴇʟᴇᴛᴇ ᴍᴇᴍʙᴇʀ)
❋⤳ᴅᴇꜰᴀᴜʟᴛ ʟɪᴍɪᴛ ɪꜱ 4"""

help16 = f"""
  **Code Runner**
❋ `.py`
❋ `.js`
❋ `.php`
❋ `.kotlin`
❋ `.go`
❋ `.java`
❋ `.lua`
  **Code ScreenShot**
❋ `.carbon`
⤳ `ʀᴇᴘʟʏ`
❋ `.exec` (execute code)"""

help17 = """
  **Welcome Menu**
❋ `.welcome` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)
❋⤳`.welcome_add`
❋⤳`.welcome_show`
❋⤳`.welcome_reset` """

# ---------- لیست کاربران و مالک ----------
my_users = [579175468]
users = filters.user(my_users)

my_owners = [579175468]
owners = filters.user(my_owners)

# ---------- هندلر .help ----------
@app.on_message(filters.private & users & filters.command("help"))
async def send_help(app, m: Message):
    all_help = "\n".join([
        help1, help3, help4, help5, help6,
        help7, help8, help9, help10, help11,
        help12, help13, help14, help15, help16, help17
    ])
    await m.reply_text(all_help)

# ---------- هندلر /start ----------
@app.on_message(filters.private & users & filters.command("start"), group=-1)
async def updates(app, m: Message):
    kos = f"@{m.from_user.username}" if m.from_user.username else m.from_user.id
    await app.send_message(
        m.chat.id,
        f"**Hello {m.from_user.first_name}**\n__Welcome to bot__\nFor get help type `.help`\n",
    )
    await app.send_message(my_owners[0], f"✅ User {kos} Started The Bot ✅")

@app.on_message(filters.private & ~users & filters.command("start"), group=-1)
async def updates(app, m: Message):
    await m.delete()

# ---------- پنل مالک ----------
keyboard_idk = ReplyKeyboardMarkup(
    [
        [("Add User"), ("Delete User"), ("User List")],
        [("Add Owner"), ("Delete Owner"), ("Owner List")]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

@app.on_message(filters.private & owners & filters.command("panel"), group=-1)
async def updates(app, m: Message):
    await app.send_message(m.chat.id, "**QuiteCreateCliBot Panel Owner**", reply_markup=keyboard_idk)

# ---------- مدیریت لیست کاربران/مالکان ----------
@app.on_message(filters.private & owners)
async def updates(app, m: Message):
    text = m.text
    if text == "Add User":
        try:
            answer = await app.ask(m.chat.id, '**Send Me User ID**:')
            my_users.append(int(answer.text))
            users.add(int(answer.text))
            await app.send_message(
                m.chat.id,
                f"Successfull\nUser [ `{answer.text}` ] Added to User List"
            )
        except Exception as er:
            await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")

    elif text == "Delete User":
        answer = await app.ask(m.chat.id, '**Send Me User ID**:')
        if int(answer.text) in users:
            try:
                num = my_users.index(int(answer.text))
                my_users.remove(my_users[num])
                users.remove(int(answer.text))
                await app.send_message(
                    m.chat.id,
                    f"Successfull\nUser [ `{answer.text}` ] Deleted From User List"
                )
            except Exception as er:
                await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
        else:
            await app.send_message(m.chat.id, "This is Not in Users List")

    elif text == "User List":
        if my_users:
            user_list = "\n".join([f"֍ {idx+1} -> `{uid}`" for idx, uid in enumerate(my_users)])
            await app.send_message(m.chat.id, f"**User List:**\n{user_list}")
        else:
            await app.send_message(m.chat.id, "**User List is Empty**")

    elif text == "Add Owner":
        answer = await app.ask(m.chat.id, '**Send Me User ID**:')
        try:
            if int(answer.text) in my_users:
                my_owners.append(int(answer.text))
                owners.add(int(answer.text))
                await app.send_message(
                    m.chat.id,
                    f"Successfull\nUser [ `{answer.text}` ] Added to Owner List"
                )
            else:
                await app.send_message(
                    m.chat.id,
                    "این یتیم حتی یوزر هم نیست داش 😐\nاول به یوزرا اضافش کن بعد بیا مالکش کن"
                )
        except Exception as er:
            await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")

    elif text == "Delete Owner":
        answer = await app.ask(m.chat.id, '**Send Me User ID**:')
        if int(answer.text) in my_users:
            try:
                num = my_owners.index(int(answer.text))
                my_owners.remove(my_owners[num])
                owners.remove(int(answer.text))
                await app.send_message(
                    m.chat.id,
                    f"Successfull\nUser [ `{answer.text}` ] Deleted From Owner List"
                )
            except Exception as er:
                await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
        else:
            await app.send_message(m.chat.id, "This is Not in Owners List")

    elif text == "Owner List":
        if my_owners:
            owner_list = "\n".join([f"֍ {idx+1} -> `{uid}`" for idx, uid in enumerate(my_owners)])
            await app.send_message(m.chat.id, f"**Owner List:**\n{owner_list}")
        else:
            await app.send_message(m.chat.id, "**Owner List is Empty**")

# ---------- راه‌اندازی ----------
app.start()
print("started...")
idle()
app.stop()
