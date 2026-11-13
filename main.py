import discord
from discord.ext import commands
import requests
import pyttsx3

motor = pyttsx3.init()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}!')

@bot.command()
async def start(ctx):
    await ctx.send('Seja bem vindo')


@bot.command()
async def tempohj(ctx, *, cidade):
    url = f'https://wttr.in/{cidade}?format=%c+%C+%x+%h+%t+%f+%H+%L+%w+%l+%m+%M+%p+%P+%e+%u+%D+%S+%z+%s+%d+%T+%Z'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        await ctx.send(resposta.text)


@bot.command()
async def pokemon(ctx, *, nome):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome.lower()}'
 
    resposta = requests.get(url)
 
    if resposta.status_code == 200:
        dados = resposta.json()
        especie = requests.get(dados['species']['url']).json()
 
        if especie['is_mythical']:
            raridade = 'Mítico'
        elif especie['is_legendary']:
            raridade = 'Lendário'
        else:
            raridade = 'Comum'
 
        await ctx.send(
            f"{dados['name'].capitalize()}\n"
            f"Número na Pokédex: {dados['id']}\n"
            f"Peso: {dados['weight'] / 10} kg\n"
            f"Tamanho: {dados['height'] / 10} m\n"
            f"Raridade: {raridade}"
        )
    else:
        await ctx.send('Pokémon não encontrado')


@bot.command()
async def facts(ctx):
    url = 'https://uselessfacts.jsph.pl/random.json'

    fato = requests.get(url)

    if fato.status_code == 200:
        resposta = fato.json()
        await ctx.send(resposta['text'])

        motor.say(resposta['text'])
        motor.runAndWait()

@bot.command()
async def cachorro(ctx):
    url = 'https://dog.ceo/api/breeds/image/random'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        await ctx.send(dados['message'])

    




bot.run('')
