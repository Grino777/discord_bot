import discord
from discord.ext import commands
from discord import utils
import config


def main():
    client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print('BOT CONNECTED!')

    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
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
    @commands.has_permissions(administrator=True)  # Доступ только у адм.
    async def clear(ctx, amount=100):
        """Очистка чата на n сообщений ( по умолчанию 100 )."""
        await ctx.channel.purge(limit=amount + 1)

    # @client.command(pass_context=True)
    # async def kick(ctx, member: discord.Member, *, reason=None):
    #     channel = client.get_channel(1041795071026139256)
    #     author_roles_id = ctx.author.roles
    #     for i in author_roles_id:
    #         if i.id in [config.GM_ID, config.FRIEND_ID]:
    #             await ctx.channel.purge(limit=1)
    #             await ctx.send('+')
    #             # await member.kick(reason=reason)
    #             # await channel.send(f'Кто: {ctx.author}, кого: {member}')
    #             # await ctx.send(f'Кто: {ctx.author}, кого: {member.mention}')

    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear_msg_by_id(ctx, id):
        """Удаление сообщений определенного пользователя на канале"""
        ...

    # Сonnect
    client.run(config.TOKEN)


if __name__ == '__main__':
    main()
