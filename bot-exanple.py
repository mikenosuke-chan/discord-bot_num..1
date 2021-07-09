import discord
import datetime

TOKEN = 'ODQ5Mjk3NTQ1ODcyMjc3NTI0.YLZH-g.aoj_jcO17HOIE4nnQWTCDh0QUNI'

client = discord.Client()
jtime = []
ltime = []
channel = []
user = []


@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
	if message.author.bot:
		return

	if message.content.find('k!') == 0 or message.content.find('K!') == 0:

		if 'help' in message.content:
			await message.channel.send("""```	k!help この画面を表示します
	k!chelp コマンドごとのヘルプを表示します(k!chelp [コマンド名])
	k!view ユーザーのVCへのログイン状況をDMに送ります(bot導入後にVCに参加した人のみ)
	k!setting 各種設定をいじれます(詳細はk!chelp setting)
	k!rec VCの録音をします
	k!vote 投票を行います、(期間の設定はデフォルトで1日)```""")


@client.event
async def on_voice_state_update(memb, bef, aft):
	print(memb)
	if memb in user[]:
		writenum = user.index(memb)
	else
		user.append(memb)
	if bef.channel and aft.channel:
		print("Move " + bef.channel.name + " to " + aft.channel.name)
		channel = channel + ' と ' + aft.channel.name
	elif bef.channel:
		print("leave " + bef.channel.name)
		ltime.append(datetime.datetime.now())
		print(datetime.datetime.now())
	elif aft.channel:
		print("join " + aft.channel.name)
		jtime.append(datetime.datetime.now())
		channel.append(aft.channel.name)
		

def finalsave(jtime, ltime, user, channel):
	f = open(f'{discord.guild.name}.txt', 'a')
	f.write(f'{user} 氏 の {channel} へ の ログイン 情報\n参加した時間 {jtime} - 参加時間 {ltime - jtime}\n\n')
	f.close

client.run(TOKEN)
