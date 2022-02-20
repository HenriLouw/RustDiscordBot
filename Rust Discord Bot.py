import discord 
import requests
import json
from discord.ext import commands, tasks
from itertools import cycle
import os
from dotenv import load_dotenv

load_dotenv(find_dotenv())

#Set Prefix
bot = commands.Bot(command_prefix = '!') 
status = cycle(['-_- You just got beamed you Loser', 'Created by MrT1TAN#3244'])

#Set Message when Bot is online
@bot.event 
async def on_ready():
  change_status.start()
  print('Hello, my name is -_-')


#Set Bot status
@tasks.loop(seconds=15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

#Noti when someone joins
@bot.event
async def on_member_join(ctx, member):
  print(f'{member} has joined the Server.')
  channel = bot.get_channel(649722167897882625)
  role_auto = discord.utils.get(ctx.guild.roles, name='{Plebs}')
  await ctx.add_roles(role_auto)
  await channel.send(member.mention + 'Welcome to the server. You received `@Plebs` role')

#Send message to Specific Channel via IDs
async def Hello(ctx):
  channel = bot.get_channel(649722167897882625)
  await channel.send('Hello')

#Noti when someone leaves!!!
@bot.event
async def on_member_remove(ctx, member):
  print(f'{member} has left the server.')
  await ctx.send('PLayer left the server')
  
@bot.command()
@commands.has_role('Main Group')
async def testing(ctx):
  channel = bot.get_channel(649722167897882625)
  await channel.send('Testing permisions')


#-_-Shitter
@bot.command()
async def shitter(ctx, member : discord.Member):
  await ctx.send(member.mention + ' is a shitter')

#Beamed Loser
@bot.command(aliases =['-_-', 'Beamed'])
async def beamed(ctx, member : discord.Member):
  await ctx.send(member.mention + ' **-_- You just got Beamed you Fucking Loser!** \n https://imgur.com/ak3Rhqw.png')

#Channel message purge
@bot.command()
async def clear(ctx, amount=3):
  await ctx.channel.purge(limit=amount)

#Reminder command
@bot.command() 
async def reminder(ctx):
  channel = bot.get_channel(803245557963161640)
  embed = discord.Embed(
    title = '-_- Information about Todays Wipe', 
    description =  'All players playing STEVIOUS 2x MONDAYS',
    colour = discord.Colour.red()
  )
  embed.set_footer(text='Made by MrT1TAN#3244')
  embed.set_image(url='https://imgur.com/Yw5Qdpt.png')
  embed.set_thumbnail(url='https://imgur.com/zf2vV3D.png')
  embed.set_author(name='MrT1TAN', 
  icon_url='https://imgur.com/zf2vV3D.png')
  embed.add_field(name='Wipe Time', value='`Server wipes at 4:30PM CET`', inline=False)
  embed.add_field(name='Build Spot', value='`HQM Quarry/Launch Site`', inline=False)
  embed.add_field(name='Server IP:', value='`client.connect 151.80.230.129:28015`', inline=False)
  embed.add_field(name='PLAYERS', value='Hidden' + '\nMrT1TAN' + '\nRuski'+ '\nKuma'+ '\nBuckz'+ '\nBubbi'+'\nKrym'+ '\nVenox'+'\nPigasaur'+ '\nCapital'+ '\nRay X', inline=False)
  await channel.send(embed=embed)

#Embed Players (hours)
@bot.command() 
async def players(ctx):
  await ctx.send('Busy fetching data!', delete_after=3.0)
  titan_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198376916629&appid=252490')
  titan = titan_request.text

  hidden_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198298530950&appid=252490')
  hidden = hidden_request.text

  buckz_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198363560338&appid=252490')
  buckz = buckz_request.text

  kuma_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198219252535&appid=252490')
  kuma = kuma_request.text

  guac_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198278748318&appid=252490')
  guac = guac_request.text

  bubbi_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198321729743&appid=252490')
  bubbi = bubbi_request.text

  ruski_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198130936061&appid=252490')
  ruski = ruski_request.text

  capital_request = requests.get('https://beta.decapi.me/steam/hours?id=76561198404937526&appid=252490')
  capital = capital_request.text
  embed = discord.Embed(
    title = '-_- Players', 
    description =  'All players in -_-',
  colour = discord.Colour.red()
  )

  embed.set_footer(text='Made by MrT1TAN#3244')
  #embed.set_image(url='https://imgur.com/zf2vV3D.png')
  embed.set_thumbnail(url='https://imgur.com/zf2vV3D.png')
  embed.set_author(name='MrT1TAN', 
  icon_url='https://imgur.com/zf2vV3D.png')
  embed.add_field(name='Captain', value='-Hidden'+ ' (' + hidden + ')', inline=True)
  embed.add_field(name='Co-Captain', value='-Ruski'+ ' (' + ruski + ')', inline=False)
  embed.add_field(name='Players', value='-MrT1TAN'+ ' (' + titan + ')' +  '\n -Buckz' + ' (' + buckz + ')' + '\n -Kuma' + ' (' + kuma + ')' + '\n-Guac' + ' (' + guac + ')' +'\n-Bubbi'+ ' (' + bubbi + ')' + '\n-Capital'+ ' (' + capital + ')', inline=False)

  await ctx.send(embed=embed)

#Recruit Embed
@bot.command() 
async def Recruiting(ctx):
  await ctx.send('Busy fetching data!', delete_after=3.0)
  
  embed = discord.Embed(
    title = '-_- are Recruiting', 
    description =  'We are Currently looking for new players.',
    colour = discord.Colour.blue()
  )

  embed.set_footer(text='Made by MrT1TAN#3244')
  embed.set_thumbnail(url='https://imgur.com/zf2vV3D.png')
  embed.set_author(name='Ruski')
  embed.add_field(name='Requirements', value='Hours: 2000+' + '\n Age: 16+'+ '\n Region: EU or NA (We play EU)'+'\n Language: Fluent English'+ '\n Active: Very Active', inline=True)


  await ctx.send(embed=embed)


#SDT Command 
@bot.command(aliases =['sdt']) 
async def SDT(ctx):
  server = requests.get('https://api.rust-servers.info/status/4081%27')

  server_info = server.json()
  server_player = server_info['players']
  server_status = server_info['status']
  server_max_players = server_info['players_max']
  server_fps = server_info['fps']
  server_uptime = server_info['uptime']
  await ctx.send('Busy fetching data!', delete_after=3.0)
  
  embed = discord.Embed(
    title = 'Stevious 2x SOLO/DUO/TRIO', 
    description =  'Information about SDT',
    colour = discord.Colour.red()
  )
  embed.set_footer(text='Made by MrT1TAN#3244')
  embed.set_thumbnail(url='https://imgur.com/18uRJQq.png')
  embed.set_author(name='MrT1TAN', 
  icon_url='https://imgur.com/RxT6DaN.png')
  embed.add_field(name='Server IP:', value='`client.connect 54.37.245.113:28015`', inline=False)
  embed.add_field(name='Server Status:', value=  '`' + server_status + '`', inline=False)
  embed.add_field(name='Players Online:', value=  '`' + server_player + ' players to beam -_-`', inline=False)
  embed.add_field(name='Player Cap:', value= '`' +  server_max_players + '`', inline=False)
  embed.add_field(name='Average Server FPS:', value= '`' + server_fps + '`', inline=False)
  embed.add_field(name='Wipe:', value='`Wipes weekly on Thursday at 3.30PM CET.`', inline=False)
  embed.add_field(name='Last Server Restart:', value= '`' + server_uptime + '`', inline=False)
  
  await ctx.send(embed=embed)


#Mondays Command
@bot.command(aliases =['mondays']) 
async def MONDAYS(ctx):
  server = requests.get('https://api.rust-servers.info/status/4087')

  server_info = server.json()
  server_player = server_info['players']
  server_status = server_info['status']
  server_max_players = server_info['players_max']
  server_fps = server_info['fps']
  server_uptime = server_info['uptime']
  await ctx.send('Busy fetching data!', delete_after=3.0)
  
  embed = discord.Embed(
    title = 'Stevious 2x MONDAYS', 
    description =  'Information about Mondays Server',
    colour = discord.Colour.red()
  )
  embed.set_footer(text='Made by MrT1TAN#3244')
  embed.set_thumbnail(url='https://imgur.com/18uRJQq.png')
  embed.set_author(name='MrT1TAN', 
  icon_url='https://imgur.com/RxT6DaN.png')
  embed.add_field(name='Server IP:', value='`client.connect 151.80.230.129:28015`', inline=False)
  embed.add_field(name='Server Status:', value=  '`' + server_status + '`', inline=False)
  embed.add_field(name='Players Online:', value=  '`' + server_player + ' players to beam -_-`', inline=False)
  embed.add_field(name='Player Cap:', value= '`' +  server_max_players + '`', inline=False)
  embed.add_field(name='Average Server FPS:', value= '`' + server_fps + '`', inline=False)
  embed.add_field(name='Wipe:', value='`Wipes weekly on Thursday at 3.30PM CET.`', inline=False)
  embed.add_field(name='Last Server Restart:', value= '`' + server_uptime + '`', inline=False)
  
  await ctx.send(embed=embed)

bot.run(os.getenv('BOT_TOKEN'))