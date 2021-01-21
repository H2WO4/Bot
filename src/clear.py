# Supprime tous les messages en relations avec le bots (commandes et résultats)
async def clearChannel(ctx) -> None:
    # On prend les 30 derniers messages
    messages = await ctx.message.channel.history(limit=30).flatten()
    for i in messages:
        try:
            # On checke les deux cas de figure et supprime
            if i.author.id == ctx.bot.user.id:
                await i.delete(delay = 0.0)
            if i.content[0] == ".":
                await i.delete(delay = 0.0)
        except:
            pass

# Supprime tous les messages
async def emptyChannel(ctx) -> None:
    # On prend les 100 derniers messages
    messages = await ctx.message.channel.history(limit=100).flatten()
    for i in messages:
        try:
            await i.delete(delay = 0.0)
        except:
            pass
