import discord
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guildnum = 0
        guilds = await self.bot.fetch_guilds(limit=150).flatten()
        for guild in guilds:
            guildnum = guildnum + 1
            guild = self.bot.get_guild(guild.id)
            myname = guild.me.nick
            if myname == "TSD Bot":
                print(f'[+] I\'m in guild {guild.name} {guild.id} + => And my name is already sweet!')
            else:
                print(f'[+] I\'m in guild {guild.name} {guild.id} + => And of course they messed up my name!')
                await guild.me.edit(nick="TSD Bot")
        print(f'Serving {guildnum} guilds')
        print(
            f'Logged in as: {self.bot.user.name}\n ID: {self.bot.user.id}\n API Version: {discord.__version__}\n Bot Version: 1.0.0\n Serving {guildnum} guilds')
        status = discord.Streaming(name='Lofi Hip-Hop - beats to relax/study to',
                                   url='https://www.youtube.com/watch?v=5qap5aO4i9A')
        await self.bot.change_presence(status=discord.Status.online, activity=status)
        print(f'Finally logged in! Phew.. ')
        print(
            '============================================================\n     TSD Bot!\n============================================================')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        greet = "Hallo! Selamat datang di server discord sains data FTMM Unair, aku bot TSD yang akan mengingatkanmu akan mata kuliah, tugas dan event kuliah lain! \n Untuk pertanyaan, kritik dan saran, kamu dapat mention Angga dengan @Bang Komting  dan @Orang Bijak untuk moderator server :D "
        await member.send(greet)
        print(f'[!] New member joined the guild: {member}\n ')
        verifiedRole = discord.utils.get(member.guild.roles, id=753608473157304380)
        await member.add_roles(verifiedRole)
        print(f'[+] Added new member to the designated role')
        for guild in self.bot.guilds:
            await guild.system_channel.send(f'{member} Baru saja masuk server! Selamat datang!')


    @commands.Cog.listener()
    async def on_member_leave(self, member):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        msg = msg.casefold()
        try:
            print(message.author.name, "#", message.channel.name, " : ", msg, )  # Log all chat to stdout
        except AttributeError:
            print("Direct Message received!")
            print(message.author.name, "[#] Direct Channel: ", msg)


def setup(bot):
    bot.add_cog(MainCog(bot))

