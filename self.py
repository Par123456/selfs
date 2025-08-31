
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, filters, idle, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent, ChatPermissions
from pyrogram.raw import functions
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.raw.functions.contacts import GetBlocked
from pyrogram.raw.functions.messages import GetAllStickers
from requests import get as GET
from wikipedia import search, page
from pytz import timezone
from datetime import date, datetime
import instagram_private_api as insta
from pyrogram.filters import create
from random import choice
from plugins import font, fosh_saz, DLX, fontinname, create_time, create_time2, get_size, generateimage, snippet, read, write, if_not_exist_creat, run_codi, create_tarikh, moon_or_sun, json_read, dast_del, have_sec, write_a
from time import time
from gtts import gTTS
import os
from ipapi import location
from PIL import Image
from socket import gethostbyname
from platform import python_version, uname
from uptime import uptime
from time import strftime, gmtime
from re import match, findall
from time import sleep
import qrcode
from psutil import virtual_memory, cpu_freq, cpu_percent, cpu_count
from base64 import b64encode
from decimal import Decimal, getcontext
import json
import sys
from io import StringIO

os.chdir(os.path.dirname(os.path.abspath(__file__)))

enemy = []
mutey = []
now = ""
galbe = ["🤍", "🖤", "🤎", "💜", "💙", "💚", "💛", "🧡", "❤️"]
ez_emoji = ["😀", "😃", "😄", "😁", "😆", "😅", "🗿", "🤣", "😭", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🤗", "🙃", "🙂", "☺️", "😊", "😏", "😌", "😉", "🤭", "😶", "🤔", "🤪", "😜", "😝", "😛", "😋", "😔", "😑", "😐", "🤨", "🧐", "🙄", "😒", "😤", "😠", "😡", "🤬", "☹️", "😰", "🤫", "🤐", "😬", "😳", "🥺", "😟", "😕", "🙁", "😨", "😧", "😦", "😮", "😯", "😲", "😱", "🤯", "😢", "😥", "😓", "😞", "😣", "😖", "😩", "😫", "🤤", "🥱", "🤮", "😇", "😵", "🤥", "🤓", "😎", "🤑", "🤠"]
answer = []
javab = []
Src_vrsion = "v2.2"

if not os.path.isfile("data.json"):
    with open("data.json", "w") as fjr:
        fjr.write('{"limitDel": 4, "welcome": "off", "firstcom": "off", "timename": "off", "timename2": "off", "timebio": "off", "timebio2": "off", "timebio3": "off", "fontname": "off", "fuck": "off", "anti_del": "off", "autoan": "off", "boldmode": "off", "emojimode": "off", "underline": "off", "italicmode": "off", "codemode": "off", "strike": "off", "spoilermode": "off"}')
if not os.path.isfile("fucking.json"):
    with open("fucking.json", "w") as fjr:
        fjr.write('{"fuck": "off"}')
if_not_exist_creat("time.txt")
if_not_exist_creat("user.txt")
if_not_exist_creat("db.txt")
if_not_exist_creat("anti_del_chat.txt")
if_not_exist_creat("send_time_text.txt")
if_not_exist_creat("firstcommentmsg.txt")
if_not_exist_creat("welcome_add_text.txt")
if_not_exist_creat("userbio.txt")  # Assuming needed for bio

api_id = 29042268
api_hash = '54a7b377dd4a04a58108639febe2f443'
app = Client("SourceMate", api_id, api_hash, device_model="Abc", system_version="Linux")

with app:
    app.send_message("oneGooglebot", "/start")
    app.send_message("gamee", "/start")
    try:
        app.join_chat("@sourcemate")
    except:
        pass

def mak():
    with app:
        m = app.send_message("me", ".").id
        app.delete_messages("me", m)

def job():
    a = json_read("data.json")
    if read("time.txt") != datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"):
        try:
            if a["timename"] == "on":
                app.invoke(functions.account.UpdateProfile(last_name=f'{create_time()}'))
            if a["timename2"] == "on":
                app.invoke(functions.account.UpdateProfile(last_name=f'{create_time2()}'))
            if a["timebio"] == "on":
                app.invoke(functions.account.UpdateProfile(about=f'{read("userbio.txt")} {create_time()}'))
            if a["timebio2"] == "on":
                app.invoke(functions.account.UpdateProfile(about=f'{read("userbio.txt")} {create_time2()}'))
            if a["timebio3"] == "on":
                app.invoke(functions.account.UpdateProfile(about=f'{moon_or_sun()} | {read("userbio.txt")} | {create_time2()} | {create_tarikh()}'))
            if a["fontname"] == "on":
                app.invoke(functions.account.UpdateProfile(first_name=f'{fontinname(read("user.txt"))}'))
        except:
            pass
        write("time.txt", datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"))

def antidelmember():
    a = json_read("data.json")
    chat_id_kiri = read("anti_del_chat.txt")
    if a["anti_del"] == "on":
        ban_konande = []
        band = []
        kok = []
        db = ""
        chif = app.get_chat_members(chat_id_kiri, filter=enums.ChatMembersFilter.BANNED)
        for i in chif:
            ban_konande.append(i.restricted_by.id)
            band.append(i.user.id)
        for b in ban_konande:
            kir = f"{b}:{ban_konande.count(b)}\n"
            if kir not in db:
                db += f"{b}:{ban_konande.count(b)}\n"   
                kok.append(b)
        write("db.txt", db)
        database = open("db.txt", "r")
        for k in range(1, len(kok) + 1):
            kirkhar = database.readline().split(":")
            if int(kirkhar[1]) >= a['limitDel']:
                try:
                    app.ban_chat_member(chat_id_kiri, kirkhar[0])
                    app.send_message(chat_id_kiri, f'**i Banned: {kirkhar[0]}**\n Because He/She Banned Members Above limit\n\n        **@sourcemate**')
                    for i in band:
                        app.unban_chat_member(chat_id_kiri, i)
                except Exception as er:
                    app.send_message("me", f"❋ **ERROR** :\n(`{er}`)")

@app.on_message(filters.linked_channel)
def first(app, m: Message):
    chat_id, text = m.chat.id, m.text
    a = json_read("data.json")
    if a["firstcom"] == "on":
        msgr = read("firstcommentmsg.txt").split(":")
        if text != "@sourcemate":
            if msgr[0] == "text":
                m.reply(msgr[1])
            elif msgr[0] == "sticker":
                m.reply_sticker(msgr[1])
            elif msgr[0] == "animation":
                m.reply_animation(msgr[1])
            else:
                m.reply("__ERROR:__\nMessage Not Set\n    **sourcemate**")

def filt(_, __, m: Message):
    try:
        if m.from_user.id in enemy:
            return True
        else:
            return False
    except:
        pass

if_user_is_enemy = create(filt)
@app.on_message(if_user_is_enemy)
def enym(app, m: Message):
    app.send_message(m.chat.id, fosh_saz(text="."), reply_to_message_id=m.id)

def fbky(_, __, m: Message):
    try:
        if m.from_user.id in mutey:
            return True
        else:
            return False
    except:
        pass

if_user_is_mutey = create(fbky)
@app.on_message(if_user_is_mutey)
def muty(app, m: Message):
    app.delete_messages(m.chat.id, m.id)

@app.on_message(filters.new_chat_members, group=6)
def welcomebot(app, m: Message):
    a = json_read("data.json")
    welcome_kos = read("welcome_add_text.txt")
    welcome_message = (f"""Hello {m.from_user.mention} !\nWelcome To **{m.chat.title}** 👋😼\n📆Date: `{date.today().strftime("%Y/%m/%d")}`\n⌛️Time: `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")}`\n{welcome_kos if welcome_kos else ""}""")
    if a["welcome"] == "on":
        app.send_message(m.chat.id, welcome_message)

@app.on_message(filters.text, group=6)
def autoanwer(app, m: Message):
    text = m.text
    a = json_read("data.json")
    if a["autoan"] == "on":
        if text in answer:
            num = answer.index(text)
            app.send_message(m.chat.id, javab[num], reply_to_message_id=m.id)
            sleep(9)

@app.on_message(filters.text & filters.me)
@app.on_edited_message(filters.text & filters.me)
def updates(app, m: Message):
    global api
    global enemy
    global mutey
    global lang
    global now
    text = m.text
    json_database = json_read("data.json")
    if json_database["boldmode"] == "on":
        m.edit_text(f"**{text}**")
    elif json_database["italicmode"] == "on":
        m.edit_text(f"__{text}__")
    elif json_database["codemode"] == "on":
        m.edit_text(f"`{text}`")
    elif json_database["underline"] == "on":
        m.edit_text(f"<u>{text}</u>")
    elif json_database["emojimode"] == "on":
        m.edit_text(f"{text} {choice(ez_emoji)}")
    elif json_database["strike"] == "on":
        m.edit_text(f"~~{text}~~")
    elif json_database["spoilermode"] == "on":
        m.edit_text(f"||{text}||")
    if text.startswith(".fontfa"):
        lang = "fa"
        kobs = font(text=text.replace(".fontfa ", ""), lang=lang)
        app.edit_message_text(m.chat.id, m.id, kobs)
    elif text.startswith(".fonten"):
        lang = ""
        kobs = font(text=text.replace(".fonten ", ""), lang=lang)
        app.edit_message_text(m.chat.id, m.id, kobs)
    elif text.startswith(".clone"):
        try:
            if m.reply_to_message:
                userSelfp = m.reply_to_message.from_user.id
                b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(userSelfp)))
                kiri = app.get_users(m.reply_to_message.from_user.id)
                user_id_get = m.reply_to_message.from_user.id
            else:
                text = text.replace(" ", "").replace(".clone", "")
                user_id_get = app.get_users(text).id
                kiri = app.get_users(user_id_get)
                b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
            app.edit_message_text(m.chat.id, m.id, text=f"""
    **Cloner**
❋ `Firstname`⤳ (`{b.users[0].first_name if b.users[0].first_name else '--'}`)
❋ `Lastname`⤳ (`{(b.users[0].last_name if b.users[0].last_name else '--')}`)
❋ `Bio`⤳ (`{(b.full_user.about if b.full_user.about else '--')}`)""")
            loudo = app.download_media(kiri.photo.big_file_id)
            app.set_profile_photo(photo=loudo)
            app.update_profile(first_name=b.users[0].first_name)
            app.update_profile(last_name=(b.users[0].last_name if b.users[0].last_name else ""))
            app.update_profile(bio=(b.full_user.about if b.full_user.about else ""))
            app.edit_message_text(m.chat.id, m.id, "❋ Clone Successfully Completed")
            os.remove(loudo)
        except errors.exceptions.bad_request_400.UsernameNotOccupied:
            app.send_message(m.chat.id, f"❋ Username Not Valid ❋")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".block"):
        app.block_user(m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1])
        m.edit_text(f"❋ {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Blocked ")
    elif text.startswith(".unblock"):
        app.unblock_user(m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1])
        m.edit_text(f"❋ {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Unblocked ")
    elif text.startswith(".left"):
        try:
            if text.split()[1]:
                app.leave_chat(text.split()[1], delete=True)
                m.edit_text(f"❋ Successfully Left From [ `{text.split()[1]}` ]")
            else:
                app.send_message(m.chat.id, f"Bye :)")
                app.leave_chat(m.chat.id, delete=True)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".join "):
        try:
            link = text.replace(".join ", "")
            link = link.replace('+', 'joinchat/')
            app.join_chat(link)
            app.send_message(m.chat.id, f'❋ Successfully Joined To [ {link} ]', disable_web_page_preview=True)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".delethistory":
        try:
            app.invoke(functions.channels.DeleteHistory(channel=app.resolve_peer(channel=m.chat.id), max_id=0))
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
        else:
            app.send_message(m.chat.id, f"❋ Chat Cleared")
    elif text.startswith(".ban"):
        try:
            app.ban_chat_member(m.chat.id, (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
            app.send_message(m.chat.id, f"❋ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully Banned !")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".unban"):
        try:
            app.unban_chat_member(m.chat.id, (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
            app.send_message(m.chat.id, f"❋ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully UnBanned !")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".clear_member"):
        target = text.split()[1]
        m.edit_text(f"❋ Target Chat: `{target}`\n__Start Ban members__ . . .")
        for member in app.get_chat_members(target):
            try:
                app.ban_chat_member(target, member.user.id)
            except errors.FloodWait as e:
                app.send_message("me", f"❋ Wait For {e.x} Seconds")
                sleep(e.x)
                app.send_message("me", f"❋ **Flood Wait Has Ended**🥳\nSend [ `.clear_member {target}` ] Again")
            except errors.exceptions.bad_request_400.UserAdminInvalid:
                app.send_message("me", f"**❋ You Are Not Admin in** ( `{target}` )")
                pass
            except errors.exceptions.bad_request_400.BadRequest:
                app.send_message("me", f"**❋ Clear Members of ( {target} ) Has Been Ended**")
                pass
            except Exception as er:
                app.send_message("me", f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".delmute"):
        try:
            app.unban_chat_member(m.chat.id, (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
            app.send_message(m.chat.id, f"❋ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully UnMuted !")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setmute"):
        try:
            app.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, ChatPermissions())
            app.send_message(m.chat.id, f"❋ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Muted")
        except:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".setchatphoto"):
        try:
            if m.reply_to_message.photo:
                app.set_chat_photo(chat_id=m.chat.id, photo=m.reply_to_message.photo.file_id)
                app.send_message(m.chat.id, f"❋ Chat Photo Changed")
            else:
                app.set_chat_photo(chat_id=m.chat.id, video=m.reply_to_message.video.file_id)
                app.send_message(m.chat.id, f"❋ Chat Photo Changed")
        except:
            m.edit_text(f"❋ Please Reply To Photo or Video")
    elif text.startswith(".setprofile"):
        try:
            if m.reply_to_message.photo:
                down = app.download_media(m.reply_to_message)
                app.set_profile_photo(photo=down)
                app.send_message(m.chat.id, f"❋ Your Profile Photo Changed")
                os.remove(down)
            elif m.reply_to_message.video:
                down = app.download_media(m.reply_to_message)
                app.set_profile_photo(video=down)
                app.send_message(m.chat.id, f"❋ Your Profile Video Changed")
                os.remove(down)
            else:
                app.send_message(m.chat.id, f"❋ Please Reply To Message")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".delprofile"):
        try:
            photos = app.get_chat_photos("me")
            app.delete_profile_photos(next(photos).file_id)
            app.send_message(m.chat.id, f"❋ Your Profile photo Deleted")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif ".delchatphoto" == text:
        try:
            app.delete_chat_photo(m.chat.id)
            m.reply(f"❋ Chat Photo Cleared")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setchattitle"):
        try:
            kx = text.replace(".setchattitle", "")[1::]
            app.set_chat_title(m.chat.id, kx.strip())
            m.reply(f"❋ Chat Name changed To[ `{kx}` ]")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setchatbio"):
        try:
            kx = text.replace(".setchatbio", "")[1::]
            app.set_chat_description(m.chat.id, kx)
            m.reply(f"❋ Chat Bio changed To [ `{kx}` ]")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif ".pin" == text:
        if m.reply_to_message:
            try:
                m.pin(disable_notification=False)
                m.edit_text(f'❋ Pinned')
            except Exception as er:
                m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
        else:
            m.edit_text(f"❋ Please Reply To Message")
    elif ".unpin" == text:
        if m.reply_to_message:
            try:
                m.unpin()
                m.edit_text(f'❋ Unpinned')
            except Exception as er:
                m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
        else:
            m.edit_text(f"❋ Please Reply To message")
    elif ".unpinall" == text:
        try:
            app.unpin_all_chat_messages(m.chat.id)
            m.edit_text(f'❋ All Message Unpinned')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setchatusername"):
        try:
            kx = text.split()[1]
            app.set_chat_username(m.chat.id, kx)
            m.edit_text(f'❋ Chat Username Changed [ `{kx}` ]')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".creatchannel"):
        try:
            kx = text.split()[1]
            app.create_channel(title=f'{kx}')
            m.edit_text(f'❋ Channel [ `{kx}` ] Created')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".creatsupergroup"):
        try:
            kx = text.split()[1]
            app.create_supergroup(title=f'{kx}')
            m.edit_text(f'❋ Supergroup [ `{kx}` ] Created')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".creatgroup"):
        try:
            kx = text.split()[1]
            app.create_group(title=f'{kx}')
            m.edit_text(f'❋ Group [ `{kx}` ] Created')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".delallmsguser"):
        try:
            app.delete_user_history(m.chat.id, (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
            m.edit_text(f"All message From {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Deleted")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".slowmod"):
        try:
            kx = text.split()[1]
            app.set_slow_mode(m.chat.id, int(kx))
            m.edit_text(f'❋ Slow Mode is on Second : {kx}')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setname"):
        try:
            kx = text.replace(".setname", "")[1::]
            app.invoke(functions.account.UpdateProfile(first_name=kx))
            write("user.txt", text.replace(".setname", "")[1::])
            m.edit_text(f'❋ Your Name ɪs Updated To [ `{kx}` ]')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setlastname"):
        try:
            kx = text.replace(".setlastname", "")[1::]
            app.invoke(functions.account.UpdateProfile(last_name=kx))
            m.edit_text(f'❋ Your Lastname is Updated To [ `{kx}` ]')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setbio"):
        try:
            kx = text.replace(".setbio", "")[1::]
            app.invoke(functions.account.UpdateProfile(about=kx))
            write("userbio.txt", text.replace(".setbio", "")[1::])
            m.edit_text(f'❋ Your Bio Updated To⤳[ `{kx}` ]')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".bold"):
        if text.split()[1] == "on":
            json_database.update({"boldmode": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Bold Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"boldmode": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Bold Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".welcome_add"):
        write("welcome_add_text.txt", text.replace(".welcome_add", "")[1::])
        m.edit_text(f"❋ Successfully Added To Welcome Message")
    elif text.startswith(".welcome_reset"):
        write("welcome_add_text.txt", "")
        m.edit_text(f"❋ Successfully Welcome Message Reset")
    elif text.startswith(".welcome_show"):
        m.edit_text(read("welcome_add_text.txt"))
    elif text.startswith(".spoiler"):
        if text.split()[1] == "on":
            json_database.update({"spoilermode": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Spoiler Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"spoilermode": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Spoiler Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".italic"):
        if text.split()[1] == "on":
            json_database.update({"italicmode": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ italic Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"italicmode": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ italic Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".code"):
        if text.split()[1] == "on":
            json_database.update({"codemode": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Code Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"codemode": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Code Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".strike"):
        if text.split()[1] == "on":
            json_database.update({"strike": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Strike Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"strike": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Strike Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".underline"):
        if text.split()[1] == "on":
            json_database.update({"underline": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Underline Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"underline": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Underline Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".emoji"):
        if text.split()[1] == "on":
            json_database.update({"emojimode": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Emoji Mode is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"emojimode": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Emoji Mode is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".searchwiki"):
        results_1 = ""
        res_1 = 1
        try:
            search_results = search(text.replace(".searchwiki", "")[1::])
            if search_results:
                for pg in search_results:
                    url = page(pg).url
                    results_1 += f'❋ <a href={url}>{pg}</a>\n'
                    res_1 += 1
                m.edit_text(f"❋ ᴛʜᴇʀᴇ's ʏᴏᴜʀ ʀᴇsᴜʟᴛ ❋ \n\n{results_1}", parse_mode="html")
            else:
                m.edit_text("No results found")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".ip"):
        try:
            HOSTNAME = m.reply_to_message.text if m.reply_to_message else text.split()[1]
            app.edit_message_text(m.chat.id, m.id, f'❋ The [`{HOSTNAME}`] iP address is [`{gethostbyname(HOSTNAME)}`]')
        except:
            app.edit_message_text(m.chat.id, m.id, f'❋ The `{HOSTNAME}` Not valid !!')
    elif text.startswith(".whoisip"):
        try:
            HOSTIP = m.reply_to_message.text if m.reply_to_message else text.split()[1]
            source = location(ip=HOSTIP, key=None)
            app.edit_message_text(m.chat.id, m.id, f"""
❋ `iP` ⤳  (`{source["ip"]}`)
❋ `City` ⤳  (`{source["city"]}`)
❋ `Region` ⤳  (`{source["region"]}`)
❋ `Country` ⤳  (`{source["country"]}`)\n(`{source["country_name"]}`)
❋ `Area Code` ⤳  (`{source["country_calling_code"]}`)
❋ `Language` ⤳  (`{source["languages"]}`)
❋ `Owner` ⤳  (`{source["org"]}`)""")
        except:
            app.edit_message_text(m.chat.id, m.id, f'❋ The `{HOSTIP}` Not valid !!')
    elif text.startswith(".firstcomment"):
        try:
            if text.split()[1] == "on":
                json_database.update({"firstcom": "on"})
                write("data.json", json.dumps(json_database))
                m.edit_text(f"❋ First comment is **ON**")
            elif text.split()[1] == "off":
                json_database.update({"firstcom": "off"})
                write("data.json", json.dumps(json_database))
                m.edit_text(f"❋ First comment is **OFF**")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".antich"):
        try:
            write("anti_del_chat.txt", text.split()[1])
            m.edit_text(f"֍ 𝗢𝗸 :)\nChat ID: `{text.split()[1]}`")
        except Exception as er:
            m.edit_text(f"├ • `ERROR` ⤳\n(`{er}`)")
    elif text.startswith(".mention"):
        if m.reply_to_message:
            try:
                m.edit_text(f"{m.reply_to_message.from_user.mention}")
            except:
                m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
        else:
            try:
                m.edit_text(f"<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>")
            except:
                m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text == ".dl":
        try:
            down = app.download_media(m.reply_to_message)
            if m.reply_to_message.caption:
                caption = m.reply_to_message.caption
            else:
                caption = ""
            app.send_document(m.chat.id, down, caption=caption)
            os.remove(down)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == "waitt":
        try:
            down = app.download_media(m.reply_to_message)
            app.send_document("me", down, caption="😈")
            os.remove(down)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".tp":
        try:
            down = app.download_media(m.reply_to_message)
            if down is None:
                m.edit_text(f"**ERROR!**\n\n__Please Reply To A Sticker__")
            else:
                os.rename(down, 'sticker.jpg')
                app.send_photo(m.chat.id, f"sticker.jpg", caption="**Sticker** To **Picture** By __sourcemate__", reply_to_message_id=m.id)
                os.remove(f"sticker.jpg")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".ts":
        try:
            down = app.download_media(m.reply_to_message)
            if down is None:
                m.edit_text(f"**ERROR!**\n\n__Please Reply To A Photo__")
            else:
                os.rename(down, 'sticker.webp')
                app.send_sticker(m.chat.id, f"sticker.webp", reply_to_message_id=m.id)
                os.remove(f"sticker.webp")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".tg":
        try:
            down = app.download_media(m.reply_to_message)
            if down is None:
                m.edit_text(f"**ERROR!**\n\n__Please Reply To A Photo__")
            else:
                os.rename(down, 'animation.gif')
                app.send_animation(m.chat.id, f"animation.gif", reply_to_message_id=m.id)
                os.remove(f"animation.gif")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".dllink"):
        i = 1
        url = (m.reply_to_message.text if m.reply_to_message else text.split()[1])
        try:
            if '/' in url:
                filename = url.split('/')[-1]
                r = GET(url, allow_redirects=True, stream=True)
                total = int(r.headers.get('content-length'))
                app.edit_message_text(m.chat.id, m.id, f"""𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱\n❋ ғɪʟᴇ ɴᴀᴍᴇ : `{filename}`\n❋ ғɪʟᴇsɪᴢᴇ : `{total/1024/1024:.3f} ᴍʙ`\n❋ ᴛɪᴍᴇ : `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")}`\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n❋ ᴡᴀɪᴛ ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ""")
                with open(filename, 'wb') as file:
                    for data in r.iter_content(chunk_size=1024):
                        file.write(data)
                m.edit_text(f"""𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱\n❋ ғɪʟᴇ ɴᴀᴍᴇ : `{filename}`\n❋ ғɪʟᴇsɪᴢᴇ : `{total/1024/1024:.3f} ᴍʙ`\n❋ ᴛɪᴍᴇ : `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")}`\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n❋ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇᴅ\n❋ ᴡᴀɪᴛ ғᴏʀ ᴜᴘʟᴏᴀᴅ""")
                app.send_document(m.chat.id, f"{filename}", caption=f"""𝗨𝗽𝗹𝗼𝗮𝗱\n❋ ғɪʟᴇ ɴᴀᴍᴇ : `{filename}`\n❋ ғɪʟᴇsɪᴢᴇ : `{total/1024/1024:.3f} ᴍʙ`\n❋ ᴛɪᴍᴇ : `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")}`""")
                app.delete_messages(m.chat.id, m.id)
                os.remove(filename)
        except:
            m.edit_text(f"❋ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʟɪɴᴋ ɪs ɴᴏᴛ ᴅᴏᴡɴʟᴏᴀᴅᴀʙʟᴇ")
    elif text.startswith(".sticker"):
        try:
            im = Image.open(GET(f"http://www.flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=colgate-logo&&text={text.replace('.sticker', '')[1::]}&fontsize=100", stream=True).raw)
            im.save('sticker.png')
            os.rename('sticker.png', 'sticker.webp')
            app.send_sticker(m.chat.id, f"sticker.webp", reply_to_message_id=m.id)
            os.remove(f"sticker.webp")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".error"):
        try:
            imn = Image.open(GET(f"http://http.cat/{text.replace('.error', '')[1::]}.jpg", stream=True).raw)
            imn.save('sticker.jpg')
            os.rename('sticker.jpg', 'sticker.webp')
            app.send_sticker(m.chat.id, f"sticker.webp", reply_to_message_id=m.id)
            os.remove(f"sticker.webp")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif m.text == ".get_message":
        if m.reply_to_message:
            app.send_message(m.chat.id, m.reply_to_message, reply_to_message_id=m.id)
        else:
            app.send_message(m.chat.id, m, reply_to_message_id=m.id)
    elif m.text == ".time":
        try:
            for i in range(0, 10):
                kir = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
                app.edit_message_text(m.chat.id, m.id, f"**Time:** `{kir}`")
                sleep(1)
        except Exception as er:
            m.edit_text(er)
    elif m.text == ".timepic":
        try:
            generateimage(datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S"))
            os.rename('time_image.jpg', 'sticker.webp')
            app.send_sticker(m.chat.id, f"sticker.webp", reply_to_message_id=m.id)
            os.remove(f"sticker.webp")
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".send_coment"):
        t = text.replace(".send_coment", "")[1::]
        sending_text = (read("send_time_text.txt") if read("send_time_text.txt") else ".")
        app.delete_messages(m.chat.id, m.id)
        app.send_message("me", f"❋ I Will Send [`{sending_text}`] at {t} Comment \n\n__In This Chat:__ [`{m.chat.id}`] ")
        chait = m.reply_to_message.chat.id if m.reply_to_message else m.chat.id
        mesig = m.reply_to_message if m.reply_to_message else m
        while True:
            count = app.get_discussion_replies_count(chait, mesig.id)
            sleep(0.1)
            if int(count) >= (int(t) - 1):
                app.send_message(m.chat.id, sending_text, reply_to_message_id=mesig.id)
                break
    elif text.startswith(".coment_text"):
        if m.reply_to_message.text:
            fileud = m.reply_to_message.text
            write("send_time_text.txt", fileud)
            m.edit_text(f"❋ The Message Of [ `.send_coment` ] is {fileud}")
        else:
            m.edit_text(f"❋ Please Reply To A Text Message")
    elif text.startswith(".text_time"):
        t = text.replace(".text_time", "")[1::]
        sending_time = have_sec(t)
        sending_text = (read("send_time_text.txt") if read("send_time_text.txt") else ".")
        app.delete_messages(m.chat.id, m.id)
        app.send_message("me", f"❋ I Will Send [`{sending_text}`] At [**{sending_time}**]\n\n__In This Chat:__ [`{m.chat.id}`]")
        while True:
            a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
            if sending_time == a:
                app.send_message(m.chat.id, sending_text, reply_to_message_id=(m.reply_to_message.id if m.reply_to_message else m.id))
                break
    elif text.startswith(".photo_time"):
        sending_time = text.replace(".photo_time", "")[1::] + ":00"
        sending_text = read("send_time_photo.txt")
        app.delete_messages(m.chat.id, m.id)
        down = app.download_media(sending_text)
        app.send_message("me", f"❋ I Will Send photo At [**{sending_time}**]\n\n__In This Chat:__ [`{m.chat.id}`]")
        while True:
            a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
            if sending_time == a:
                app.send_photo(m.chat.id, down, reply_to_message_id=(m.reply_to_message.id if m.reply_to_message else m.id))
                break
    elif text.startswith(".text_send_time"):
        if m.reply_to_message.text:
            fileud = m.reply_to_message.text
            write("send_time_text.txt", fileud)
            m.edit_text(f"❋ The Message Of [ `.text_time` ] is {fileud}")
        else:
            m.edit_text(f"❋ Please Reply To A Text Message")
    elif text.startswith(".photo_send_time"):
        if m.reply_to_message.photo:
            fileud = m.reply_to_message.photo.file_id
            write("send_time_photo.txt", fileud)
            m.edit_text(f"❋ The Photo Of [ `.photo_time` ]👇\n\nFile id: {fileud}")
        else:
            m.edit_text(f"**❋ Please reply to a photo**")
    elif text == ".ping":
        try:
            up_a = (strftime('%H:%M:%S', gmtime(uptime())))
            svmem = virtual_memory()
            app.edit_message_text(m.chat.id, m.id, f"""
    **pdzSelf Status**
    
❋ `User` ⤳ ( `{app.get_me().first_name}` )
❋ `Uptime` ⤳ (`{up_a}`)
❋ `Ram Usage` ⤳ (`{get_size(svmem.used)}`)
❋ `Python Version` ⤳ (`{python_version()}`)
❋ `Source Version` ⤳ (`{Src_vrsion}`) 
❋ `Library` ⤳ (`Pyrogram`)""")
        except Exception as er:
            m.edit_text(er)
    elif text == ".cpu":
        try:
            cpufreq = cpu_freq()
            app.edit_message_text(m.chat.id, m.id, f"""
❋ `Physical Cores` ⤳  (`{cpu_count(logical=False)}`)
❋ `Total Cores` ⤳  (`{cpu_count(logical=True)}`)
❋ `Max Frequency` ⤳  (`{cpufreq.max:.2f}Mhz`)
❋ `Min Frequency` ⤳  (`{cpufreq.min:.2f}Mhz`)
❋ `Cuttent Frequency` ⤳  (`{cpufreq.current:.2f}Mhz`)
❋ `CPU Usage` ⤳  (`{cpu_percent()}%`)""")
        except Exception as er:
            m.edit_text(er)
    elif text == ".memory":
        try:
            svmem = virtual_memory()
            app.edit_message_text(m.chat.id, m.id, f"""
❋ `Total` ⤳ (`{get_size(svmem.total)}`)
❋ `Available` ⤳ (`{get_size(svmem.available)}`)
❋ `Used` ⤳ (`{get_size(svmem.used)}`)
❋ `Percentage` ⤳ (`{svmem.percent}%`)""")
        except Exception as er:
            m.edit_text(er)
    elif text == ".system-inf":
        try:
            kirithokhmi = uname()
            app.edit_message_text(m.chat.id, m.id, f"""
❋ `System` ⤳ (`{kirithokhmi.system}`)
❋ `Node Name` ⤳ (`{kirithokhmi.node}`)
❋ `Release` ⤳ (`{kirithokhmi.release}`)
❋ `Version` ⤳ (`{kirithokhmi.version}`)
❋ `Machine` ⤳ (`{kirithokhmi.machine}`)
❋ `Processor` ⤳ (`{kirithokhmi.processor}`)""")
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".voice"):
        try:
            audio = gTTS(text=text.replace(".voice", "")[1::], lang='en')
            audio.save("voice.ogg")
            app.send_audio(m.chat.id, "voice.ogg")
            app.delete_messages(m.chat.id, m.id)
            os.remove("voice.ogg")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".qrcode"):
        try:
            qr_str = (m.reply_to_message.text if m.reply_to_message else text.replace('.qrcode', '')[1::])
            if qr_str is None:
                m.edit_text(f"**ERROR!**\n\n__Please Reply To A Text Message__")
            else:
                qr = qrcode.make(qr_str)
                qr.save("QrCode.png")
                app.send_photo(m.chat.id, f"QrCode.png", caption=f"QrCode ⤳(`{qr_str}`)", reply_to_message_id=m.id)
                os.remove("QrCode.png")
        except Exception as er:
            m.edit_text(f"**ERROR!** \n\n{er}")
    elif text.startswith(".spam"):
        try:
            if x := findall(".spam \d+", text)[0]:
                ui = findall("\d+", x)[0]
                sts = findall("\d+\s+.+", text)[0].replace(ui, "")
            for i in range(0, int(ui)):
                app.send_message(m.chat.id, sts)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".spm"):
        try:
            if x := findall(".spm \d+", text)[0]:
                ui = findall("\d+", x)[0]
                sts = findall("\d+\s+.+", text)[0].replace(ui, "")
            for i in range(0, int(ui)):
                if m.reply_to_message:
                    app.send_message(m.chat.id, sts, reply_to_message_id=m.id)
                else:
                    m.edit_text("**Please Reply**")
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".py"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.py', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="python3", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".kotlin"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.kotlin', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="kotlin", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".js"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.js', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="javascript", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".php"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.php', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="php", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".lua"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.lua', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="lua", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".go"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.go', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="go", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".java"):
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.java', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Wait__\n\n**Code** :\n`{code}`")
            rund_c = run_codi(lang="java", code=code)
            app.send_message(m.chat.id, rund_c, reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif m.text == ".carbon":
        try:
            code = (m.reply_to_message.text if m.reply_to_message else text.replace('.carbon', '')[1::])
            app.edit_message_text(m.chat.id, m.id, f"__Making Screenshot from Your Code...__\n\n**Code** :\n`{code}`")
            params = {'code': code, "paddingVertical": "56px", "paddingHorizontal": "57px", "backgroundImage": None, "backgroundImageSelection": None, "backgroundMode": "color", "backgroundColor": "rgba(0, 255, 160, 1)", "dropShadow": True, "dropShadowOffsetY": "9px", "dropShadowBlurRadius": "12px", "theme": "Dracula", "language": "auto", "fontFamily": "Hack", "fontSize": "18px", "lineHeight": "250%", "windowControls": True, "widthAdjustment": True, "lineNumbers": True, "firstLineNumber": 1, "exportSize": "2x", "watermark": False, "squaredImage": False, "hiddenCharacters": True, "width": 680}
            snippet(params)
            app.send_photo(m.chat.id, f"i.png", caption=f":)", reply_to_message_id=m.id)
            os.remove(f"i.png")
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".exec"):
        try:
            m.edit_text(f"""**INPUT**\n`{text}`\n\n**OUTPUT**\nWait ...""")
            codeOut = StringIO()
            sys.stdout = codeOut
            exec(str(text.replace(".exec ", "")))
            sys.stdout = sys.__stdout__
            results = codeOut.getvalue().strip()
            bic = True if results.strip() != '' else False
            if len(results) >= 3800:
                write("results.txt", str(results))
                m.edit_text(f"""**INPUT**\n`{text}`\n\n**OUTPUT**\n In File👇👹""")
                m.reply_document("results.txt")
                os.remove("results.txt")
            else:
                m.edit_text(f"""**INPUT**\n`{text}`\n\n**OUTPUT**\n`{results if bic else 'Successful'}`""")
            codeOut.close()
        except Exception as er:
            app.send_message(m.chat.id, f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".ocr":
        try:
            if m.reply_to_message.photo:
                m.edit_text("Wait For **8** Second . . .")
                app.send_photo("@oneGooglebot", m.reply_to_message.photo.file_id, caption="")
                sleep(8)
                a = app.get_chat_history("@oneGooglebot", limit=1)
                a = next(a)
                text_ocr = a.text.replace("💭 OCR detected:", "")
                m.edit_text("**OCR** __Detected Successfully :)__")
                m.reply(f"**❋ OCR Result:**`{text_ocr}`", quote=True)
            else:
                m.edit_text("**Please Reply to a Photo**")
        except Exception as er:
            app.send_message(m.chat.id, f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".delete"):
        mmd = app.get_chat_member(m.chat.id, "me")
        rasi = dast_del(text=mmd)
        if rasi:
            try:
                reu = int(text.replace(".delete", ""))
                if isinstance(reu, int):
                    kalc = 0
                    for msg in app.get_chat_history(m.chat.id):
                        if reu != kalc:
                            msg.delete(revoke=True)
                            kalc += 1
                        else:
                            break
                    m.reply(f"❋ `{kalc}` **Messages Successfully Deleted !**", quote=False)
                else:
                    m.reply("❋ Please Enter a Number")
            except Exception as er:
                app.send_message(m.chat.id, f"❋ **ERROR** :\n(`{er}`)")
        else:
            m.reply("❋ You Dont Have Delete message Permission")
    elif text.startswith(".file_info"):
        getcontext().prec = 3
        try:
            if m.reply_to_message.document:
                m.edit_text(f"""❋ Name ⤳ (`{m.reply_to_message.document.file_name}`)
❋ Type ⤳ (`{m.reply_to_message.document.mime_type}`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.document.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Date ⤳ (`{m.reply_to_message.document.date}`)
❋ File iD ⤳ (`{m.reply_to_message.document.file_id}`)""")
            elif m.reply_to_message.photo:
                m.edit_text(f"""❋ Size ⤳ (`{m.reply_to_message.photo.width}×{m.reply_to_message.photo.height}`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.photo.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Date ⤳ (`{m.reply_to_message.photo.date}`)
❋ File iD ⤳ (`{m.reply_to_message.photo.file_id}`)""")
            elif m.reply_to_message.video:
                m.edit_text(f"""❋ Type ⤳ (`{m.reply_to_message.video.mime_type}`)
❋ Size ⤳ (`{m.reply_to_message.video.width}×{m.reply_to_message.video.height}`)
❋ Duration ⤳ (`{m.reply_to_message.video.duration}s`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.video.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Date ⤳ (`{m.reply_to_message.video.date}`)
❋ Support Streaming ⤳ (`{m.reply_to_message.video.supports_streaming}`)
❋ File iD ⤳ (`{m.reply_to_message.video.file_id}`)""")
            elif m.reply_to_message.animation:
                m.edit_text(f"""❋ Size ⤳ (`{m.reply_to_message.animation.width}×{m.reply_to_message.animation.height}`)
❋ Type ⤳ (`{m.reply_to_message.animation.mime_type}`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.animation.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Duration ⤳ (`{m.reply_to_message.animation.duration}s`)
❋ Date ⤳ (`{m.reply_to_message.animation.date}`)
❋ File iD ⤳ (`{m.reply_to_message.animation.file_id}`)""")
            elif m.reply_to_message.sticker:
                m.edit_text(f"""❋ Size ⤳ (`{m.reply_to_message.sticker.width}×{m.reply_to_message.sticker.height}`)
❋ Name ⤳ (`{m.reply_to_message.sticker.file_name}`)
❋ Type ⤳ (`{m.reply_to_message.sticker.mime_type}`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.sticker.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Emoji ⤳ (`{m.reply_to_message.sticker.emoji}`)
❋ Is Animated ⤳ (`{m.reply_to_message.sticker.is_animated}`)
❋ Is Video ⤳ (`{m.reply_to_message.sticker.is_video}`)
❋ Sticker Set ⤳ (`{"https://t.me/addstickers/"+m.reply_to_message.sticker.set_name if m.reply_to_message.sticker.set_name else "--"}`)
❋ Date ⤳ (`{m.reply_to_message.sticker.date}`)
❋ File iD ⤳ (`{m.reply_to_message.sticker.file_id}`)""")
            elif m.reply_to_message.voice:
                m.edit_text(f"""❋ Type ⤳ (`{m.reply_to_message.voice.mime_type}`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.voice.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Duration ⤳ (`{m.reply_to_message.voice.duration}s`)
❋ Date ⤳ (`{m.reply_to_message.voice.date}`)
❋ File iD ⤳ (`{m.reply_to_message.voice.file_id}`)""")
            elif m.reply_to_message.audio:
                m.edit_text(f"""❋ Title ⤳ (`{m.reply_to_message.audio.title}`)
❋ Performer ⤳ (`{m.reply_to_message.audio.performer}`)
❋ Type ⤳ (`{m.reply_to_message.audio.mime_type}`)
❋ File Name ⤳ (`{m.reply_to_message.audio.file_name}`)
❋ File Size ⤳ (`{Decimal(int(m.reply_to_message.audio.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❋ Duration ⤳ (`{m.reply_to_message.audio.duration}s`)
❋ Date ⤳ (`{m.reply_to_message.audio.date}`)
❋ File iD ⤳ (`{m.reply_to_message.audio.file_id}`)""")
            elif m.reply_to_message.text:
                m.edit_text(f"**Please Reply To A Media/file**")
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".first_message"):
        try:
            if m.reply_to_message.animation:
                write("firstcommentmsg.txt", f"animation:{m.reply_to_message.animation.file_id}")
                m.reply("**Gif** Successfully Saved")
            elif m.reply_to_message.sticker:
                write("firstcommentmsg.txt", f"sticker:{m.reply_to_message.sticker.file_id}")
                m.reply("**Sticker** Successfully Saved")
            elif m.reply_to_message.text:
                write("firstcommentmsg.txt", f"text:{m.reply_to_message.text}")
                m.reply("**Text** Successfully Saved")
            else:
                m.reply("Please Reply to **Gif** or **Sticker** or **Text**")
        except Exception as er:
            m.edit_text(er)
    elif text == ".status":
        getcontext().prec = 3
        try:
            start = time()
            pv = 0; group = 0; Channel = 0; ch_creator = 0; gp_creator = 0; Bot = 0
            for ii in app.get_dialogs():
                if ii.chat.type in ['ChatType.GROUP', 'ChatType.SUPERGROUP']:
                    group += 1
                    if ii.chat.is_creator:
                        gp_creator += 1
                elif ii.chat.type == "ChatType.PRIVATE":
                    pv += 1
                elif ii.chat.type == "ChatType.CHANNEL":
                    Channel += 1
                    if ii.chat.is_creator:
                        ch_creator += 1
                elif ii.chat.type == "ChatType.BOT":
                    Bot += 1
            blocked = app.invoke(GetBlocked(offset=0, limit=0))
            stickered = app.invoke(GetAllStickers(hash=0))
            end = time()
            m.reply_text(f"""**Private Chats:** `{pv}`\n  •• `Bots: {Bot}`\n**Groups:** `{group}`\n  •• `Creator: {gp_creator}`\n**Channels:** `{Channel}`\n  •• `Creator: {ch_creator}`\n**Blocked Users:** `{blocked.count}`\n**Total Stickers Pack Installed:** `{len(list(stickered.sets))}`\nits Took: {Decimal(end) - Decimal(start)}s""")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".tadmin":
        try:
            b = "❋ **Admins** :\n\n"
            c = 1; k = 0
            a = app.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
            for i in a:
                if not i.user.is_deleted:
                    b += "├" + str(c) + " ↬ [" + (i.user.mention if i.user.id else "--") + "]\n"
                    c += 1
                else:
                    k += 1
            if k != 0:
                b += f"├ **Deleted Account Admin** : `{k}`\n└— **Count** : `{k + c - 1}`"
            else:
                b += f"└—  \n **Count** : `{k + c - 1}`"
            m.reply(b)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".game"):
        try:
            games = ["Neon Blaster", "Neon Blaster 2", "Block Buster", "Gravity Ninja", "Hexonix", "Geometry Run 3D", "Disco Ball", "Tube Runner", "Little Plane", "MotoFx 2", "Space Traveler", "Groovy Ski"]
            jdkh = choice(games)
            m.edit_text(f"**Game name:** `{jdkh}`")
            result = app.get_inline_bot_results("gamee", jdkh)
            app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".inf"):
        if text.split()[1] == "@this":
            user = m.chat.id
        else:
            user = text.split()[1]
        user = app.get_chat(user)
        try:
            if user.photo:
                down = app.download_media(user.photo.big_file_id)
                app.send_photo(m.chat.id, down, f"""__Chat info__

❋ **Title** : `{user.title}`
❋ **ID** : `{user.id}`
❋ **Username** : `@{user.username if user.username else '--'}`
❋ **Members** : `{user.members_count}`
❋ **Dc ID** : `{user.dc_id}`
❋ **Is Creator** : `{user.is_creator}`
❋ **Is Verified** : `{user.is_verified}`
❋ **Is Restricted** : `{user.is_restricted}`
❋ **Is Scam** : `{user.is_scam}`
❋ **Is Fake** : `{user.is_fake}`
❋ **Sticker Set** : `{"https://t.me/addstickers/"+user.sticker_set_name if hasattr(user, 'sticker_set_name') and user.sticker_set_name else "--"}`
❋ **Description** : `{user.description}`""", reply_to_message_id=m.id)
                os.remove(down)
            else:
                app.send_message(m.chat.id, f"""__Chat info__

❋ **Title** : `{user.title}`
❋ **ID** : `{user.id}`
❋ **Username** : `@{user.username if user.username else '--'}`
❋ **Members** : `{user.members_count}`
❋ **Dc ID** : `{user.dc_id}`
❋ **Is Creator** : `{user.is_creator}`
❋ **Is Verified** : `{user.is_verified}`
❋ **Is Restricted** : `{user.is_restricted}`
❋ **Is Scam** : `{user.is_scam}`
❋ **Is Fake** : `{user.is_fake}`
❋ **Sticker Set** : `{"https://t.me/addstickers/"+user.sticker_set_name if hasattr(user, 'sticker_set_name') and user.sticker_set_name else "--"}`
❋ **Description** : `{user.description}`""", reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".id"):
        try:
            user_id_get = (m.reply_to_message.from_user.id if m.reply_to_message else app.get_users(text.split()[1]).id)
            user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
            count_photo = app.get_chat_photos_count(user_id_get)
            kiri = app.get_users(user_id_get)
            if kiri.photo:
                down = app.download_media(kiri.photo.big_file_id)
                app.send_photo(m.chat.id, down, f"""__User info__

❋ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❋ **LastName** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❋ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❋ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❋ **Profile Picture Count** : `{count_photo}`
❋ **Common Chats Count** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
❋ **BIO** : `{user.full_user.about if user.full_user.about else "--"}`
❋ **Scam** : `{user.users[0].scam}`
❋ **Can pin message** : `{user.full_user.can_pin_message}`
❋ **Contact** : `{user.users[0].contact}`
❋ **Bot** : `{user.users[0].bot}`
❋ **Verified** : `{user.users[0].verified}`
❋ **Deleted** : `{user.users[0].deleted}`
❋ **Phone Calls Available** : `{user.full_user.phone_calls_available}`
❋ **Phone Calls Private** : `{user.full_user.phone_calls_private}`
❋ **Video Calls Available** : `{user.full_user.video_calls_available}`
❋ **Access hash** : `{user.users[0].access_hash}`
❋ **Blocked** : `{user.full_user.blocked}`
`{f"❋ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""", reply_to_message_id=m.id)
                os.remove(down)
            else:
                app.send_message(m.chat.id, f"""__User info__

❋ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❋ **LastName** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❋ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❋ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❋ **Profile Picture Count** : `{count_photo}`
❋ **Common Chats Count** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
❋ **BIO** : `{user.full_user.about if user.full_user.about else "--"}`
❋ **Scam** : `{user.users[0].scam}`
❋ **Can pin message** : `{user.full_user.can_pin_message}`
❋ **Contact** : `{user.users[0].contact}`
❋ **Bot** : `{user.users[0].bot}`
❋ **Verified** : `{user.users[0].verified}`
❋ **Deleted** : `{user.users[0].deleted}`
❋ **Phone Calls Available** : `{user.full_user.phone_calls_available}`
❋ **Phone Calls Private** : `{user.full_user.phone_calls_private}`
❋ **Video Calls Available** : `{user.full_user.video_calls_available}`
❋ **Access hash** : `{user.users[0].access_hash}`
❋ **Blocked** : `{user.full_user.blocked}`
`{f"❋ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""", reply_to_message_id=m.id)
        except errors.exceptions.bad_request_400.UsernameNotOccupied:
            app.send_message(m.chat.id, f"❋ User Not Valid ❋")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".searchapp"):
        resu = ""
        i = 1
        try:
            req = GET(f"https://sidepath.ga/api/farsroid.php?url={text.replace('.searchapp', '')[1::]}").json()
            if req["ok"]:
                for res in req["Results"]:
                    resu += f"""❋ {i}     {res["tag"]}
{res["link"]}\n\n"""
                    i += 1
                app.edit_message_text(m.chat.id, m.id, resu)
            else:
                m.edit_text(f"❋ App Not Found")
        except:
            m.edit_text(f"❋ App Not Found")
    elif text.startswith(".xnxx"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .")
        try:
            xn_dl = DLX({text.split()[1]})
            app.edit_message_text(m.chat.id, m.id, f"• **Link** ⤳\n(`{xn_dl}`)")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".instadl"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .")
        s = ""
        i = 1
        try:
            req = GET(f"https://sidepath.ga/api/instagram.php?url={text.split()[1]}").json()["Results"]
            for res in req["post"]:
                if res:
                    app.send_document(m.chat.id, res, caption=f"Slide Number {i}")
                    i += 1
            app.send_message(m.chat.id, f" **Successful** ")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".story"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .")
        s = ""
        i = 1
        try:
            req = GET(f"https://sidepath.ga/api/story.php?url={text.split()[1]}").json()
            if req["ok"]:
                for res in req["Results"]["story"]:
                    if res:
                        app.send_document(m.chat.id, res["downloadUrl"], caption=f"Story Number {i} of {text.split()[1]}")
                        i += 1
            app.send_message(m.chat.id, f" **Successful** ")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".pindl"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .")
        try:
            req = GET(f"https://api.otherapi.tk/pinterest?url={text.replace('.pindl', '')[1::]}").json()["pinterest"]
            app.send_photo(m.chat.id, req["image"], caption=f"__Image__ Downloaded From **Pinterest**", reply_to_message_id=m.id)
        except:
            app.send_video(m.chat.id, req["video"], caption=f"__Video__ Downloaded From **Pinterest**", reply_to_message_id=m.id)
    elif text.startswith(".screenurl"):
        try:
            m.edit_text(f"**Successful**\nWait For Uploading")
            im = Image.open(GET(f"https://sidepath.ga/api/scr.php?url=https://{text.replace('.screenurl', '')[1::]}", stream=True).raw)
            im.save('screenshot.png')
            app.send_photo(m.chat.id, f'screenshot.png', reply_to_message_id=m.id)
            os.remove(f"screenshot.png")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".imdb"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .\n\n`Movie/Series` ⤳ (`{text.replace('.imdb', '')[1::]}`)")
        try:
            keqr = GET(f"https://sidepath.ga/api/imdb.php?name={text.replace('.imdb', '')[1::]}").json()
            req = keqr["Results"]
            so = f"""\n✞ {req["actor"]}"""
            sjdt = so.replace("'}", "")
            sejp = sjdt.replace("{'", "")
            xqav = sejp.replace("', '", "\n✞ ")
            xcnv = xqav.replace("': '", " : ")
            app.send_photo(m.chat.id, req["image"], caption=f"""
❋ **Name** : `{req["name"]}`
❋ **Rate** : `{req["rate"]}`
❋ **Time** : `{req["time"]}`
❋ **Genre** : `{req["genre"]}`
❋ **Creator** : `{req["creator"]}`
❋ **Actor** : `{xcnv}`
❋ **Description** :
__{req["description"]}__
❋ **Trailer** : `{req["trailer"]}`""", reply_to_message_id=m.id)
        except Exception as er:
            m.edit_text(er)
    elif text.startswith(".shorturl"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .")
        s = ""
        try:
            req = GET(f"https://api.codebazan.ir/shortlink/?url={text.split()[1]}").json()
            if req["ok"]:
                for res in req["result"].values():
                    if res:
                        s += f"❋ {res}\n"
                m.edit_text(s)
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".nimurl"):
        app.edit_message_text(m.chat.id, m.id, f"**Wait**⤳Sending Request to Api . . .")
        try:
            req = GET(f"https://sidepath.ga/api/nimbaha.php?link={text.split()[1]}").json()
            if req["ok"] == "true":
                kir = req["download_link"]
                m.edit_text(f"Your Nimbaha Link ⤳\n❋ {kir}")
            else:
                m.edit_text(f"**Invalid Link**")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".setenemy"):
        try:
            if m.reply_to_message:
                if m.reply_to_message.from_user.id not in enemy:
                    if m.reply_to_message.from_user.id != app.get_me().id:
                        enemy.append(m.reply_to_message.from_user.id)
                        app.edit_message_text(m.chat.id, m.id, f'❋ {m.reply_to_message.from_user.mention} Added To Enemy List')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User {m.reply_to_message.from_user.mention} Already in Enemy List')
            else:
                if app.get_users(text.split()[1]).id not in enemy:
                    if app.get_users(text.split()[1]).id != app.get_me().id:
                        enemy.append(app.get_users(text.split()[1]).id)
                        app.edit_message_text(m.chat.id, m.id, f'❋ <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Added To Enemy List')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Already in Enemy List')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".friend"):
        try:
            if m.reply_to_message:
                if m.reply_to_message.from_user.id in enemy:
                    enemy.remove(m.reply_to_message.from_user.id)
                    app.edit_message_text(m.chat.id, m.id, f'❋ User {m.reply_to_message.from_user.mention} Removed From Enemy list')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User {m.reply_to_message.from_user.mention} is Not exist in Enemy list')
            else:
                if app.get_users(text.split()[1]).id in enemy:
                    enemy.remove(app.get_users(text.split()[1]).id)
                    app.edit_message_text(m.chat.id, m.id, f'❋ User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Removed From Enemy list')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> is Not exist in Enemy list')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".mute"):
        try:
            if m.reply_to_message:
                if m.reply_to_message.from_user.id not in mutey:
                    if m.reply_to_message.from_user.id != app.get_me().id:
                        mutey.append(m.reply_to_message.from_user.id)
                        app.edit_message_text(m.chat.id, m.id, f'❋ {m.reply_to_message.from_user.mention} Added To Mute List')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User {m.reply_to_message.from_user.mention} Already in mutes List')
            else:
                if app.get_users(text.split()[1]).id not in mutey:
                    if app.get_users(text.split()[1]).id != app.get_me().id:
                        mutey.append(app.get_users(text.split()[1]).id)
                        app.edit_message_text(m.chat.id, m.id, f'❋ <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Added To Mute List')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Already in Mute List')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".unmute"):
        try:
            if m.reply_to_message:
                if m.reply_to_message.from_user.id in mutey:
                    mutey.remove(m.reply_to_message.from_user.id)
                    app.edit_message_text(m.chat.id, m.id, f'❋ User {m.reply_to_message.from_user.mention} Removed From Mute list')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User {m.reply_to_message.from_user.mention} is Not in Mute list')
            else:
                if app.get_users(text.split()[1]).id in mutey:
                    mutey.remove(app.get_users(text.split()[1]).id)
                    app.edit_message_text(m.chat.id, m.id, f'❋ User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Removed From mute list')
                else:
                    app.edit_message_text(m.chat.id, m.id, f'❋ This User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> is Not exist in mute list')
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == ".allf":
        een = ""
        t_een = 1
        if len(enemy) >= 1:
            for user in enemy:
                een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
                t_een += 1
            app.edit_message_text(m.chat.id, m.id, f"❋ Enemy List is cleaned\n{een}")
            enemy.clear()
        else:
            app.edit_message_text(m.chat.id, m.id, f"❋ Enemy List is Empty ")
    elif text == ".allunmute":
        eem = ""
        t_eem = 1
        if len(mutey) >= 1:
            for user in mutey:
                eem += f"{t_eem} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
                t_eem += 1
            app.edit_message_text(m.chat.id, m.id, f"❋ Mute List is cleaned\n{eem}")
            mutey.clear()
        else:
            app.edit_message_text(m.chat.id, m.id, f"❋ Mute List is Empty ")
    elif text.startswith(".timename"):
        if text.split()[1] == "on":
            json_database.update({"timename": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeName is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"timename": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeName is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".2timename"):
        if text.split()[1] == "on":
            json_database.update({"timename2": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeName v2 is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"timename2": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeName v2 is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".timebio"):
        if text.split()[1] == "on":
            json_database.update({"timebio": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeBio is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"timebio": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeBio is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".2timebio"):
        if text.split()[1] == "on":
            json_database.update({"timebio2": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeBio v2 is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"timebio2": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeBio v2 is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".3timebio"):
        if text.split()[1] == "on":
            json_database.update({"timebio3": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeBio v3 is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"timebio3": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ TimeBio v3 is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".fontname"):
        if text.split()[1] == "on":
            json_database.update({"fontname": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Fontname is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"fontname": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Fontname is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".welcome"):
        try:
            if text.split()[1] == "on":
                json_database.update({"welcome": "on"})
                write("data.json", json.dumps(json_database))
                m.edit_text(f"❋ Welcome Mode is **ON**")
            elif text.split()[1] == "off":
                json_database.update({"welcome": "off"})
                write("data.json", json.dumps(json_database))
                m.edit_text(f"❋ Welcome Mode is **OFF**")
            elif text.split()[1] is None:
                m.edit_text(f"**Error**\n❋ `.welcome` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)\n├⤳`add` (`-100 + **ᴄʜᴀᴛ-ɪᴅ`)\n├⤳`del` (`-100 + **ᴄʜᴀᴛ-ɪᴅ`)\n├⤳`clear`\n├⤳`list`")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".firstcom"):
        if text.split()[1] == "on":
            json_database.update({"firstcom": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ First Comment is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"firstcom": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ First Comment is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".anti_fuck"):
        if text.split()[1] == "on":
            json_database.update({"anti_del": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Anti Delete Member Mode  is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"anti_del": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Anti Delete Member Mode **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".on_off_status"):
        mh = ""
        a = json_read("data.json")
        pairs = a.items()
        for key, value in pairs:
            mh += f"❋ {key} -> {value}\n"
        m.edit_text(f"{mh}")
    elif text.startswith(".answer"):
        if text.split()[1] == "on":
            json_database.update({"autoan": "on"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Auto Answer is **ON**")
        elif text.split()[1] == "off":
            json_database.update({"autoan": "off"})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❋ Auto Answer is **OFF**")
        else:
            m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
    elif text.startswith(".addan"):
        an = text.replace(".addan", "")[1::].split(":")[0]
        en = text.replace(".addan", "")[1::].split(":")[1]
        answer.append(an)
        javab.append(en)
        m.edit_text(f"❋ Answer Successfully Added\n[{an} -> {en}]")
    elif text.startswith(".anclear"):
        if len(answer) >= 1:
            answer.clear()
            javab.clear()
            m.edit_text(f"❋ Successful!\nAnswer List Cleared")
        else:
            app.edit_message_text(m.chat.id, m.id, f"❋ Answer List is Empty ")
    elif text.startswith(".delan"):
        if text.replace(".delan", "")[1::] in answer:
            num = answer.index(text.replace(".delan", "")[1::])
            answer.remove(answer[num])
            javab.remove(javab[num])
            m.edit_text(f"❋ Successfully\nRemoved From Asnwer List")
        else:
            m.edit_text(f"❋ This is Not in Asnwer List")
    elif text.startswith(".anlist"):
        s = ""
        op = 1
        if len(answer) >= 1:
            for i in range(0, len(answer)):
                s += f"❋ {op}: {answer[i]} -> {javab[i]}\n"
                op += 1
            m.edit_text(f"❋ **Answer List:**\n{s}")
        else:
            app.edit_message_text(m.chat.id, m.id, f"❋ Answer List is Empty ")
    elif text.startswith(".sms"):
        try:
            if match(r"09[0-9]{9}", text.split()[1]):
                app.edit_message_text(m.chat.id, m.id, f"❋ Sending Message To [ `{text.split()[1]}` ]")
                # Assuming sms function is defined in plugins
                sms(text.split()[1])
                app.edit_message_text(m.chat.id, m.id, f"❋ **Successful!**\nAll Message Sent To [ `{text.split()[1]}` ]")
            else:
                app.edit_message_text(m.chat.id, m.id, f"❋ Wrong Number [ `{text.split()[1]}` ]")
        except Exception as er:
            app.edit_message_text(m.chat.id, m.id, f"❋ Please Enter Number")
    elif text.startswith(".instalogin"):
        try:
            m.edit_text(f'.instalogin {text.split()[1].split(":")[0]}')
            api = insta.Client(text.split()[1].split(":")[0], text.split()[1].split(":")[1])
            get = api.username_info((text.split()[1].split(":")[0]))["user"]
            m.edit_text(f"""𝗜𝗻𝘀𝘁𝗮 𝗛𝗲𝗹𝗽𝗲𝗿\n\n❋ Your Login Confirmed""")
        except:
            m.edit_text(f"❋ Login Failed")
        else:
            write("insta_username.txt", text.split()[1].split(":")[0])
    elif text == ".imloged":
        try:
            log = api.authenticated_user_id
            m.edit_text(f"❋ Login Successfully")
        except:
            m.edit_text(f"❋ Login UnSuccessfully")
    elif text == ".mypageinfo":
        try:
            get = api.username_info(read("insta_username.txt"))["user"]
            m.edit_text(f"""𝗜𝗻𝘀𝘁𝗮 𝗛𝗲𝗹𝗽𝗲𝗿\n   ❋ **ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ɪɴꜰᴏ**\n❋ Follower : `{get["follower_count"]}`\n❋ Following : `{get["following_count"]}`\n❋ Following Tag : `{get["following_tag_count"]}`\n❋ Media Count : `{get["media_count"]}`\n❋ User iD : `{get["pk"]}`""")
        except NameError:
            m.edit_text(f"❋ ᴘʟᴇᴀꜱᴇ ʟᴏɢɪɴ ꜰɪʀꜱᴛ")
    elif text.startswith(".instagetuser"):
        try:
            get = api.username_info(text.split()[1])["user"]
            m.edit_text(f"""𝗜𝗻𝘀𝘁𝗮 𝗛𝗲𝗹𝗽𝗲𝗿\n❋ {text.split()[1]} Account info\n❋ Follower: `{get["follower_count"]}`\n❋ Following : `{get["following_count"]}`\n❋ Following Tag: `{get["following_tag_count"]}`\n❋ Media Count : `{get["media_count"]}`\n❋ User iD: `{get["pk"]}` """)
        except NameError:
            m.edit_text(f"❋ Please Login First")
        except insta.errors.ClientError:
            m.edit_text(f"❋ User Not Found")
    elif text.startswith(".follow"):
        try:
            api.friendships_create(api.username_info(text.split()[1])["user"]["pk"])
        except NameError as er:
            m.edit_text(f"❋ The User Was UnFollowed\n{er}")
        except insta.errors.ClientError:
            m.edit_text(f"❋ User Not Found")
        else:
            m.edit_text(f"❋ The User Was Followed")
    elif text.startswith(".unfollow"):
        try:
            api.friendships_destroy(api.username_info(text.split()[1])["user"]["pk"])
        except NameError:
            m.edit_text(f"❋ Please Login First")
        except insta.errors.ClientError:
            m.edit_text(f"❋ User Not Found")
        else:
            m.edit_text(f"❋ The User Was UnFollowed")
    elif text.startswith(".edit_firstname"):
        try:
            api.edit_profile(first_name=(m.reply_to_message.text if m.reply_to_message else text.replace(".edit_firstname", "")[1::]))
        except NameError:
            m.edit_text(f"❋ Please Login First")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text.startswith(".edit_biography"):
        try:
            api.edit_profile(biography=(m.reply_to_message.text if m.reply_to_message else text.replace(".edit_biography", "")[1::]))
        except NameError:
            m.edit_text(f"❋ Please Login First")
        except Exception as er:
            m.edit_text(f"❋ **ERROR** :\n(`{er}`)")
    elif text == "Reload":
        reloadl = ["`start Reloading`",
"░░░░░░░░░░░░░░",
"▒░░░░░░░░░░░░░",
"▒▒░░░░░░░░░░░░",
"▒▒▒░░░░░░░░░░░",
"▒▒▒▒░░░░░░░░░░",
"▒▒▒▒▒░░░░░░░░░",
"▒▒▒▒▒▒░░░░░░░░",
"▒▒▒▒▒▒▒░░░░░░░",
"▒▒▒▒▒▒▒▒░░░░░░",
"▒▒▒▒▒▒▒▒▒░░░░░",
"▒▒▒▒▒▒▒▒▒▒░░░░",
"▒▒▒▒▒▒▒▒▒▒▒░░░",
"▒▒▒▒▒▒▒▒▒▒▒▒░░",
"▒▒▒▒▒▒▒▒▒▒▒▒▒░",
"▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▒▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▓▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
"Reloading.",
"Reloading..",
"Reloading...",
"Reloading.",
"Reloading..",
"Reloading...",
"Reloading.",
"Reloading..",
"Reloading...",
"`Reloaded! :)`",
]
        for i in reloadl:
            app.edit_message_text(m.chat.id, m.id, i)
    elif text.startswith(".tas"):
        if 0 < int(text.split()[1]) < 7:
            app.delete_messages(m.chat.id, m.id)
            while True:
                msg = app.send_dice(m.chat.id, "🎲")
                if msg.dice.value != int(text.split()[1]):
                    msg.delete()
                else:
                    break
        else:
            m.edit_text(f"Please Send A Number Between 1 To 6")
    elif text == ".dart":
        app.delete_messages(m.chat.id, m.id)
        while True:
            msg = app.send_dice(m.chat.id, "🎯")
            if msg.dice.value != 6:
                msg.delete()
            else:
                break
    elif text == ".bowling":
        app.delete_messages(m.chat.id, m.id)
        while True:
            msg = app.send_dice(m.chat.id, "🎳")
            if msg.dice.value != 6:
                msg.delete()
            else:
                break
    elif text == ".basketball":
        app.delete_messages(m.chat.id, m.id)
        while True:
            msg = app.send_dice(m.chat.id, "🏀")
            if msg.dice.value != 4:
                msg.delete()
            else:
                break
    elif text.startswith(".football"):
        if int(text.split()[1]) in [1, 4]:
            app.delete_messages(m.chat.id, m.id)
            while True:
                msg = app.send_dice(m.chat.id, "⚽")
                if msg.dice.value != int(text.split()[1]):
                    msg.delete()
                else:
                    break
        else:
            m.edit_text(f"Please Send A Number Between 1 To 4")
    elif text.startswith(".khaymallist"):
        m.edit_text(f" در لیست خایمال ثبت شد.")
    elif "!help" == text:
        svmem = virtual_memory()
        bot_results = app.get_inline_bot_results("inline46_Bot", "Helper")
        app.send_inline_bot_result(m.chat.id, bot_results.query_id, bot_results.results[0].id)
        app.edit_message_text(m.chat.id, m.id, f"**ʜᴇʟᴘ ᴘᴀɴᴇʟ ꜱᴇɴᴛ . . .**\n\n__ᴄᴘᴜ__ : `{cpu_percent()}%`\n__ʀᴀᴍ__ : `{svmem.percent}%`")

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
❋⤳**ꜱᴇᴛʙɪᴏ ᴡɪᴛʜ(**`.setbio`**)**
⤳__Bio Must Be lower Than 45 Character__

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

help16 = """
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

mark = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('ᴇɴᴇᴍʏ 🧩', callback_data='eny'),
            InlineKeyboardButton('ᴍᴜᴛᴇ 🍄', callback_data='mute')
        ],
        [
            InlineKeyboardButton('ɢʀᴏᴜᴘ 🍒', callback_data='group'),
            InlineKeyboardButton('ᴘʀᴀᴄᴛɪᴄᴀʟ 🍔', callback_data='prc')
        ],
        [
            InlineKeyboardButton('ᴀɴᴛɪ ᴅᴇʟ ᴍᴇᴍʙᴇʀ 🛡', callback_data='anti_delete_member')
        ],
        [
            InlineKeyboardButton('ᴛᴏᴏʟꜱ 🔧', callback_data='tool'),
            InlineKeyboardButton('ᴘʀᴏꜰɪʟᴇ 🌵', callback_data='profile')
        ],
        [
            InlineKeyboardButton('ꜰᴜɴ 🗿', callback_data='fun'),
            InlineKeyboardButton('ᴛᴇxᴛ ᴍᴏᴅᴇ 🃏', callback_data='textmode')
        ],
        [
            InlineKeyboardButton('ʜᴇʟᴘꜰᴜʟʟ 🐢', callback_data='helpful'),
            InlineKeyboardButton('ɪɴꜰᴏ 🧸', callback_data='info')
        ],
        [
            InlineKeyboardButton('ꜰɪʀꜱᴛ ᴄᴏᴍᴍᴇɴᴛ 🚁', callback_data='first'),
        ],
        [
            InlineKeyboardButton('ᴄᴏᴅᴇʀ ᴏᴘᴛɪᴏɴ💻', callback_data='eval'),
            InlineKeyboardButton('ᴀᴜᴛᴏ ᴀɴꜱᴡᴇʀ🦦', callback_data='autoan')
        ],
        [
            InlineKeyboardButton('ᴡᴇʟᴄᴏᴍᴇ 🤝‌', callback_data='welcome'),
            InlineKeyboardButton('ɪɴꜱᴛᴀɢʀᴀᴍ 🐥', callback_data='insta')
        ],
        [
            InlineKeyboardButton('ᴄʟᴏꜱᴇ 🍂', callback_data='close')
        ],
    ]
)

dast = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ʙᴀᴄᴋ 🍂", callback_data='back')
        ]
    ]
)

openpanelbot = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Panel", switch_inline_query_current_chat='panel')
        ]
    ]
)

keyboard_idk = ReplyKeyboardMarkup(
    [
        [
            ("Add User"),
            ("Delete User"),
            ("User List")
        ],
        [
            ("Add Owner"),
            ("Delete Owner"),
            ("Owner List")
        ]
    ], one_time_keyboard=True, resize_keyboard=True)

my_users = [579175468]
users = filters.user(my_users)

my_owners = [579175468]
owners = filters.user(my_owners)

@app.on_inline_query()
def answer(client, inline_query):
    if inline_query.from_user.id in my_users:
        inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title="Helper",
                    input_message_content=InputTextMessageContent(
                        f"__Hello {inline_query.from_user.first_name}\n Welcome To HelperBot "
                    ),
                    description="Helper Panel",
                    reply_markup=mark
                )
            ],
            cache_time=1
        )

@app.on_callback_query(users)
async def test(app, call):
    if call.data == "back":
        await app.edit_inline_text(call.inline_message_id, f"User: `{call.from_user.first_name}`\n**Main Menu**", reply_markup=mark)
    elif call.data == "eny":
        await app.edit_inline_text(call.inline_message_id, help7, reply_markup=dast)
    elif call.data == "mute":
        await app.edit_inline_text(call.inline_message_id, help1, reply_markup=dast)
    elif call.data == "group":
        await app.edit_inline_text(call.inline_message_id, help3, reply_markup=dast)
    elif call.data == "prc":
        await app.edit_inline_text(call.inline_message_id, help9, reply_markup=dast)
    elif call.data == "anti_delete_member":
        await app.edit_inline_text(call.inline_message_id, help15, reply_markup=dast)
    elif call.data == "fun":
        await app.edit_inline_text(call.inline_message_id, help11, reply_markup=dast)
    elif call.data == "tool":
        await app.edit_inline_text(call.inline_message_id, help12, reply_markup=dast)
    elif call.data == "profile":
        await app.edit_inline_text(call.inline_message_id, help4, reply_markup=dast)
    elif call.data == "textmode":
        await app.edit_inline_text(call.inline_message_id, help13, reply_markup=dast)
    elif call.data == "helpful":
        await app.edit_inline_text(call.inline_message_id, help5, reply_markup=dast)
    elif call.data == "info":
        await app.edit_inline_text(call.inline_message_id, help6, reply_markup=dast)
    elif call.data == "first":
        await app.edit_inline_text(call.inline_message_id, help10, reply_markup=dast)
    elif call.data == "insta":
        await app.edit_inline_text(call.inline_message_id, help8, reply_markup=dast)
    elif call.data == "eval":
        await app.edit_inline_text(call.inline_message_id, help16, reply_markup=dast)
    elif call.data == "autoan":
        await app.edit_inline_text(call.inline_message_id, help14, reply_markup=dast)
    elif call.data == "welcome":
        await app.edit_inline_text(call.inline_message_id, help17, reply_markup=dast)
    elif call.data == "close":
        await app.edit_inline_text(call.inline_message_id, "**Closed!**")

@app.on_callback_query(~users)
def test(app, call):
    call.answer("دست نزن بچه 🗿", show_alert=True)

@app.on_message(filters.private & owners & filters.command("panel"), group=-1)
async def updates(app, m: Message):
    await app.send_message(m.chat.id, "**QuiteCreateCliBot Panel Owner**", reply_markup=keyboard_idk)

@app.on_message(filters.private & users & filters.command("start"), group=-1)
async def updates(app, m: Message):
    kos = f"@{m.from_user.username}" if m.from_user.username else m.from_user.id
    await app.send_message(m.chat.id, f"**Hello {m.from_user.first_name}**\n__Welcome to bot__\nFor get Panel type [ `!help` ]\n     ", reply_markup=openpanelbot)
    await app.send_message(my_owners[0], f"✅ User {kos} Started The Bot ✅")

@app.on_message(filters.private & ~users & filters.command("start"), group=-1)
async def updates(app, m: Message):
    await m.delete()

@app.on_message(filters.private & owners)
async def updates(app, m: Message):
    text = m.text
    if text == "Add User":
        try:
            answer = await app.ask(m.chat.id, '**Send Me User ID**:')
            my_users.append(int(answer.text))
            users.add(int(answer.text))
            await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Added to User List")
        except Exception as er:
            await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
    elif text == "Delete User":
        answer = await app.ask(m.chat.id, '**Send Me User ID**:')
        if int(answer.text) in my_users:
            try:
                num = my_users.index(int(answer.text))
                my_users.remove(my_users[num])
                users.remove(int(answer.text))
                await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Deleted From User List")
            except Exception as er:
                await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
        else:
            await app.send_message(m.chat.id, f"This is Not in Users List")
    elif text == "User List":
        try:
            s = ""
            op = 1
            if len(my_users) >= 1:
                for i in range(0, len(my_users)):
                    s += f"֍ {op} -> `{my_users[i]}`\n"
                    op += 1
                await app.send_message(m.chat.id, f"**User List:**\n{s}")
            else:
                await app.send_message(m.chat.id, f"**User List is Empty**")
        except Exception as er:
            await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
    elif text == "Add Owner":
        answer = await app.ask(m.chat.id, '**Send Me User ID**:')
        try:
            if int(answer.text) in my_users:
                my_owners.append(int(answer.text))
                owners.add(int(answer.text))
                await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Added to Owner List")
            else:
                await app.send_message(m.chat.id, f"این یتیم حتی یوزر هم نیست داش 😐\nاول به یوزرا اضافش کن بعد بیا مالکش کن")
        except Exception as er:
            await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
    elif text == "Delete Owner":
        answer = await app.ask(m.chat.id, '**Send Me User ID**:')
        if int(answer.text) in my_owners:
            try:
                num = my_owners.index(int(answer.text))
                my_owners.remove(my_owners[num])
                owners.remove(int(answer.text))
                await app.send_message(m.chat.id, f"Successfull\nUser [ `{answer.text}` ] Deleted From Owner List")
            except Exception as er:
                await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")
        else:
            await app.send_message(m.chat.id, f"This is Not in Owners List")
    elif text == "Owner List":
        try:
            s = ""
            op = 1
            if len(my_owners) >= 1:
                for i in range(0, len(my_owners)):
                    s += f"֍ {op} -> `{my_owners[i]}`\n"
                    op += 1
                await app.send_message(m.chat.id, f"**Owner List:**\n{s}")
            else:
                await app.send_message(m.chat.id, f"**Owner List is Empty**")
        except Exception as er:
            await app.send_message(m.chat.id, f"❋ `ERROR` ⤳\n(`{er}`)")

async def main():
    await app.start()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job, "interval", seconds=60)
    scheduler.start()
    print("started...")
    app.send_message("me", "Hello bro i'm Updated/Run :)\nMore details: @AnishtaYin\n\n.      **@AnishtaYiN**")
    await idle()
    await app.stop()

if __name__ == '__main__':
    asyncio.run(main())
