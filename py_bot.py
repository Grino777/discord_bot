import discord
from discord.ext import commands
from discord import utils
import config

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())


@client.event
async def on_ready():
    print('BOT CONNECTED!')


@client.command(pass_context=True)
async def kick_everyone(ctx):
    '''Удаление всех участников с ролью @everyone'''
    start = discord.Embed(
        title='⌚ | Начало удаления участников',
        description=f'`Подождите, идёт процесс удаления...`',
        color=0x02d800
    )
    await ctx.send(embed=start)

    embed = discord.Embed(
        title='Неудачное удаление.',
        description='`Произошла ошибка при удаление участников, пожалуйста проверьте код селф-бота.`',
        color=0xff0000
    )

    roleID = 311475360606715904
    role = utils.get(ctx.guild.roles, id=roleID)
    for member in role.members:
        if len(member.roles) == 1:
            await member.kick(reason=None)

    top = discord.Embed(
        title='Успешное удаление',
        description='`Участники удалены. `',
        color=0x02d800
    )

    await ctx.send(embed=top)


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    """Очистка чата на n сообщений ( по умолчанию 100 )."""
    await ctx.channel.purge(limit=amount + 1)


#Сonnect
client.run(config.TOKEN)
