import datetime
from discord.ext import commands



class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['schedule', 'jd'])
    async def jadwal(self, ctx, day=None):
        def check_date():
            date_today = str(datetime.datetime.today())
            date_today = date_today.split('.')
            date_today = date_today[0].split()
            today = datetime.datetime.today().weekday()
            if today == 6:
                today = 'minggu'
            elif today == 5:
                today = 'sabtu'
            elif today == 4:
                today = 'jumat'
            elif today == 3:
                today = 'kamis'
            elif today == 2:
                today = 'rabu'
            elif today == 1:
                today = 'selasa'
            elif today == 0:
                today = 'senin'
            date_today.append(today)
            return date_today

        async def get_subjects():
            host_keys = {'edu18': '136396', 'edu19': '660668', 'edu20': '381496'}
            senin = ['MAS207', 'MAT110']
            selasa = ['SIA107', 'TNM102']
            rabu = ['NOP103', 'NOP104']
            kamis = ['MAS239', 'BAE110', 'SIA108']
            jumat = ['MAT110_2', 'SIA108_2']
            debug = ['MAS207', 'MAT110']

            date_today = check_date()
            if date_today[2] == 'senin':
                return senin
            elif date_today[2] == 'selasa':
                return selasa
            elif date_today[2] == 'rabu':
                return rabu
            elif date_today[2] == 'kamis':
                return kamis
            elif date_today[2] == 'jumat':
                return jumat
            elif date_today[2] == 'sabtu':
                await ctx.send('Hari ini tidak ada kelas apapun :)')
                await ctx.send('gunakan `tsd jadwal <hari>` untuk mengecek hari lain')
            elif date_today[2] == 'minggu':
                await ctx.send('Hari ini tidak ada kelas apapun :)')
                await ctx.send('gunakan `tsd jadwal <hari>` untuk mengecek hari lain')

        async def get_specific_schedule(x):
            MAS207 = {'07:00': ['SDA1', 'https://zoom.us/j/92666852918'],
                      '09:40': ['SDA2', 'https://zoom.us/j/95461487382']}

            MAT110 = {'14:50': ['SDA1', 'https://zoom.us/j/96366777327',
                                'SDA2', 'https://zoom.us/j/96443905384']}

            SIA107 = {'07:00': ['SDA1', 'https://zoom.us/j/91541352717'],
                      '13:00': ['SDA2', 'https://zoom.us/j/94916583986']}

            TNM102 = {'08:50': ['SDA1', 'https://zoom.us/j/94276736195',
                                'SDA2', 'https://zoom.us/j/93284411468']}

            NOP103 = {'08:50': 'MKWU'}
            NOP104 = {'10:40': 'MKWU'}

            MAS239 = {'07:00': ['SDA2', 'https://zoom.us/j/93985512080'],
                      '10:40': ['SDA1', 'https://zoom.us/j/99943384628'],
                      '13:00': ['SDA3', 'https://zoom.us/j/96859444609']}

            BAE110 = {'08:50': ['SDA1', 'https://zoom.us/j/95772478055']}

            SIA108 = {'14:50': ['SDA3', 'https://zoom.us/j/97422116310']}

            MAT110_2 = {'07:00': ['SDA1', 'https://zoom.us/j/96366777327',
                                  'SDA2', 'https://zoom.us/j/96443905384']}

            SIA108_2 = {'08:50': ['SDA2', 'https://zoom.us/j/96502228919'],
                        '14:50': ['SDA1', 'https://zoom.us/j/96139291096']}

            schedule = ""
            name = ""
            if 'MAS207' == x:
                schedule = MAS207
                name = 'Metode Statistika'
            elif 'MAT110' == x:
                schedule = MAT110
                name = 'Matematika Lanjut'
            elif 'SIA107' == x:
                schedule = SIA107
                name = 'Algoritma Pemrograman I'
            elif 'TNM102' == x:
                schedule = TNM102
                name = 'Teknologi Hijau'
            elif 'NOP103' == x:
                schedule = NOP103
                name = 'Pancasila'
            elif 'NOP104' == x:
                schedule = NOP104
                name = 'Kewarganegaraan'
            elif 'MAS239' == x:
                schedule = MAS239
                name = 'Metode Statistika (Praktikum)'
            elif 'BAE110' == x:
                schedule = BAE110
                name = 'Bahasa Inggris'
            elif 'SIA108' == x:
                schedule = SIA108
                name = 'Algoritma Pemrograman I (Praktikum)'
            elif 'MAT110_2' == x:
                schedule = MAT110_2
                name = 'Matematika Lanjut'
            elif 'SIA108_2' == x:
                schedule = SIA108_2
                name = 'Algoritma Pemrograman I'

            schedulestr = str(schedule)
            schedulestr = schedulestr.split("'")

            for words in schedulestr:
                if '0' not in words:
                    schedulestr.remove(words)

            if len(schedulestr) == 2:
                time0 = schedulestr[0]
                kelas = schedulestr[1]
                await ctx.send(f'\n{name}\n{time0} : {kelas}\n')
                await ctx.send('⠀⠀⠀⠀⠀⠀⠀⠀')

            elif len(schedulestr) == 3:
                time0 = schedulestr[0]
                kelas = schedulestr[1]
                link = schedulestr[2]
                await ctx.send(f'\n{name}\n{time0} : {kelas} <{link}>\n')
                await ctx.send('⠀⠀⠀⠀⠀⠀⠀⠀')

            elif len(schedulestr) == 5:
                time0 = schedulestr[0]
                kelas = schedulestr[1]
                link = schedulestr[2]
                kelas2 = schedulestr[3]
                link2 = schedulestr[4]
                await ctx.send(f'\n{name}\n{time0} : {kelas} <{link}>\n{time0} : {kelas2} <{link2}>\n')
                await ctx.send('⠀⠀⠀⠀⠀⠀⠀⠀')

            elif len(schedulestr) == 6:
                time0 = schedulestr[0]
                kelas = schedulestr[1]
                link = schedulestr[2]
                time2 = schedulestr[3]
                kelas2 = schedulestr[4]
                link2 = schedulestr[5]
                await ctx.send(f'\n{name}\n{time0} : {kelas} <{link}>\n{time2} : {kelas2} <{link2}>\n')
                await ctx.send('⠀⠀⠀⠀⠀⠀⠀⠀')


            elif len(schedulestr) == 9:
                time0 = schedulestr[0]
                kelas = schedulestr[1]
                link = schedulestr[2]
                time2 = schedulestr[3]
                kelas2 = schedulestr[4]
                link2 = schedulestr[5]
                time3 = schedulestr[6]
                kelas3 = schedulestr[7]
                link3 = schedulestr[8]
                await ctx.send(f'\n{name}\n{time0} : {kelas} <{link}>\n{time2} : {kelas2} <{link2}>\n{time3} : {kelas3} <{link3}>\n')
                await ctx.send('⠀⠀⠀⠀⠀⠀⠀⠀')

        async def get_schedule(day):
            matkul = []
            if day is None:
                matkul = await get_subjects()

            elif day == 'senin':
                matkul = ['MAS207', 'MAT110']
            elif day == 'selasa':
                matkul = ['SIA107', 'TNM102']
            elif day == 'rabu':
                matkul = ['NOP103', 'NOP104']
            elif day == 'kamis':
                matkul = ['MAS239', 'BAE110', 'SIA108']
            elif day == 'jumat':
                matkul = ['MAT110_2', 'SIA108_2']
            elif day == 'sabtu':
                await ctx.send('Nggak ada mata kuliah :D')
            elif day == 'minggu':
                await ctx.send('Nggak ada mata kuliah :D')

            for sub in matkul:
                await get_specific_schedule(sub)

        await get_schedule(day=day)


def setup(bot):
    bot.add_cog(Reminder(bot))
