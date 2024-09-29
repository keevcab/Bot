import asyncio,random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,GetMessagesRequest,Item,Position
from highrise.models import SessionMetadata

louca = ["🤪Su nivel de locura es de : 100%","🤪Su nivel de locura es de : 99%","🤪Su nivel de locura es de : 50%","🤪Su nivel de locura es de : 0%","🤪Su nivel de locura es de : 1%","🤪Su nivel de locura es de : 2%","🤪Su nivel de locura es de : 64%","🤪Su nivel de locura es de : 22%","🤪Su nivel de locura es de : 19%","🤪Su nivel de locura es de : 88%","🤪Su nivel de locura es de : 39%","🤪Su nivel de locura es de : 40%","🤪Su nivel de locura es de : 92%","🤪Su nivel de locura es de : 74%","🤪Su nivel de locura es de : 10%","🤪Su nivel de locura es de : 9%","🤪Su nivel de locura es de : 77%","🤪Su nivel de locura es de : 82%","🤪Su nivel de locura es de : 66%","🤪Su nivel de locura es de : 11%","🤪Su nivel de locura es de : 15%"]

casa = ["Me caso contigo 💍","Claro que si 💍❤️","No quiero casarme contigo 💍💔","No 💍💔","Yo te amo claro que quiero casarme contigo 💍"]


curativo = ["🔴Has usado una pócima su vida es de : 100%🔴","🔴Has usado una pócima su vida es de : 50%🔴","🔴Has usado una pócima su vida es de : 60%🔴","🔴Has usado una pócima su vida es de : 75%🔴","🔴Has usado una pócima su vida es de : 85%🔴","🔴Has usado una pócima su vida es de : 80%🔴","🔴Has usado una pócima su vida es de : 90%🔴","🔴Has usado una pócima su vida es de : 95%🔴","🔴Has usado una pócima su vida es de : 99%🔴","🔴Has usado una pócima su vida es de : 91%🔴"]

bomba = ["💣🧟‍♂️ Has tirado 1x bombas al Boss Zombie 🧟‍♀️💣","💣🧟 Has tirado 3x bombas al Boss Zombie 🧟💣","💣🧟‍♂️ Has tirado 2x bombas al Boss Zombie 💣🧟‍♀️","💣🧟‍♂️ Has tirado 7x bombas al Boss Zombie 💣🧟‍♂️","💣🧟 Has tirado 4x bombas al Boss Zombie 🧟💣"]

facada = ["🧟🔪 Has matado a 1x Zombie 🔪🧟","🧟🔪 Has matado a 6x Zombie 🔪🧟","🧟🔪 Has matado a 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ Has matado a  8x Zombie 🔪🧟‍♂️","🧟🔪 Has matado a  10x Zombie 🔪🧟","🧟🔪 Has matado a  9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ Has matado a  3x Zombie 🧟‍♂️🔪🧟‍♀️"]

atirar = ["🧟Le has disparado a 5x Zombie🧟","🧟Le has disparado a 1x Zombie🧟","🧟Le has disparado a 8x Zombie🧟","🧟Le has disparado a 3x Zombie🧟","🧟‍♂️Le has disparado a 5x Zombie🧟‍♂️","🧟‍♀️Le has disparado a 10x Zombie🧟‍♀️","🧟🧟‍♀️Le has disparado a 9x Zombie🧟🧟‍♀️"]

play = ["🔴Tu vida es de 50% use : /pocion","🔴Tu vida es de 20% use : /pocion","🔴Tu vida es de 40% use : /pocion","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar","🧟🧟‍♂️ Tienes muchos zombies 🧟‍♀️🧟 🛡 Use : /escudo 🛡","🧟O Zombie Boss Esta  Vindo Use : /bomba ","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar","🧟🧟‍♂️ Tienes muchos zombies 🧟‍♀️🧟 🛡 Use : /escudo 🛡","🔴Tu vida es de 60% use : /pocion","🔴Tu vida es de 10% use : /pocion","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar"
      ,"🧟Los zombies estan viniendo Use : /cuchillazo o /disparar","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar","🧟Los zombies estan viniendo Use : /cuchillazo o /disparar"]

pescar = ["🥈Felicidades has ganado la medalla : Pescador Plata🥈","🥉Felicidades has ganado la medalla : Pescador Bronze🥉","🥉Felicidades has ganado la medalla : Pescador Bronze🥉","🥉Felicidades has ganado la medalla : Pescador Bronze🥉","🥉Felicidades has ganado la medalla : Pescador Bronze🥉","🟡Evento :  /carpa 🟡","⚫️Has pescado 3x Luna de la noche⚫️(+150 Puntos)","⚫️Has pescado 2x Luna de la noche⚫️(+100 Puntos)","⚫️Has pescado 1x Luna de la noche⚫️(+50 Puntos)","🟡Has pescado 1x Caña de la noche 🟡 (MULTIPLO PONTO)","🟡Has pescado 1x Lina de la nocherado🟡 (MULTIPLO PONTO)","🪼🌈Has pescado 1x Pona de la nocheris🪼🌈 (EXTRA Puntos)","🐢Has pescado 3x  Tna de la noche (PERDA DE Puntos)","🦑Has pescado 1x  Lna de la nochee 🦑 (LEGENDARIO)","🦀Has pescado 6x  Cna de la noche 🦀 (COMUM)","🦀Has pescado 2x  Cna de la noche 🦀 (COMUM)","🦀Has pescado 8x  Cna de la noche 🦀 (COMUM)","🪼Has pescado 1x Pona de la noche🪼(EPICO)","🦈Has pescado 2x Tuna de la nocheICO)","🦈Has pescado 5x Tuna de la nocheICO)","🦈Has pescado 8x Tuna de la nocheICO)","🦈Has pescado 1x Tuna de la nocheICO)","🐠Has pescado 1x Tuna de la noche (LEGENDARIO)","🐠Has pescado 3x Pena de la nocheo🐠 (LEGENDARIO)","🐠Has pescado 3x Tuna de la noche (LEGENDARIO)","🐠Has pescado 1x Pena de la nocheo🐠 (LEGENDARIO)","🐠Has pescado 8x Pena de la nocheo🐠 (LEGENDARIO)","🐠Has pescado 10x Pna de la nocheço🐠 (LEGENDARIO)","🐟Has pescado 1x Sana de la nocheE)","🧜🏼‍♀️Has pescado 5x Serna de la nocheO)","🧜🏼‍♀️Has pescado 2x Serna de la nocheO)","🧜🏼‍♀️Has pescado 1x Serna de la nocheO)","🐟Has pescado 3x Sana de la nocheE)","🟡Has pescado 1x Tina de la nocheada🟡 (MULTIPLO PONTO)","☠️🐋Has pescado 3x Bana de la noche☠️🐋 (PERDA DE Puntos)","🐋Has pescado 11x Bna de la nochear🐋(COMUM)","🐋🌈Has pescado 1x Bana de la nocheiris🌈🐋 (EXTRA Puntos)","🥈Felicidades has ganado la medalla : PESCADOR PRATA🥈","🥇Felicidades has ganado la medalla : PESCADOR OURO🥇","🏅Felicidades has ganado la medalla : ESTRELA PESCADOR🏅","💎Evento : /camarão💎"]

cantada = ["Yo era ateo, hasta que vi ese c**o y no supe a quien darle las gracias.","Disculpame, te gustan los hombres o las chicas? Porque yo soy hombre y la tengo chica.","Si la belleza fuera un delito, te hubiesen dado cadena perpetua.","Se te cayó un pétalo... flor de p***a.","Nena, juguemos al 42... vos te pones en 4 y yo en 2.","Tus ojos son dos cerezas. Tus mejillas dos manzanas. Que linda ensalada de frutas haríamos con mi banana.","Diosa... mostrame una, que yo me imagino la otra.","Que regla ni que compás ?!, si no se puede por delante, que sea por detrás.","La pampa tiene el ombú, el ñandú la ligereza y mi bicho acá colgado, tiene una flor de cabeza.","Si se unen los mares con los rios, unamos tus pelos con los míos.","Morocha, juguemos al diptongo... vos lo buscás y yo te la pongo!","Como me gustaría ser tu secador de pelo... para que todos los días me agarres del mango.","Cómo quisiera ser milanesa, para saborear esos limones."]

piada = ["Qual é o prato preferido do Thor? Thorresmo","O que o cavalo foi fazer no orelhão? Passar trote","Qual é o rio mais azedo do mundo? O Rio Solimões","Qual é o lugar mais certo do Brasil? O sertão.","Qual é o vinho que não tem álcool? Ovinho de codorna"]

hate = ["Las personas te odian un 0%","Las personas te odian un 20%","Las personas te odian un 100%","Las personas te odian un 50%","Las personas te odian un 45%","Las personas te odian un 99%","Las personas te odian un 95%","Las personas te odian un 34%","Las personas te odian un 77%","Las personas te odian un 80%","Las personas te odian un 66%","Las personas te odian un 39%","Las personas te odian un 20%","Las personas te odian un 22%","Las personas te odian un 49%"]

amor = ["Las personas te aman un 0%❤️","Las personas te aman un 20%❤️","Las personas te aman un 100%❤️","Las personas te aman un 50%❤️","Las personas te aman un 45%❤️","Las personas te aman un 99%❤️","Las personas te aman un 95%❤️","Las personas te aman un 34%❤️","Las personas te aman un 77%❤️","Las personas te aman un 80%❤️","Las personas te aman un 66%❤️","Las personas te aman un 39%❤️","Las personas te aman un 20%❤️","Las personas te aman un 22%❤️","Las personas te aman un 49%❤️"]


class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("funcionando")
        await self.highrise.walk_to(Position(14 , 1 , 17 , "FrontLeft"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} Entro a la sala, bienvenido/a ❤️")   
        await self.highrise.send_whisper(user.id,f"🤍Bienvenido/a {user.username} si deseas ver mi lista de emote solo escribir !emotes ")
        await self.highrise.send_whisper(user.id,f"Si tienes dificultades con los comandos, solo escribir !help \n\n🤖Vendas de arquivo de bot contact @ShoKytoo.")

        await self.highrise.send_emote("hcc-jetpack")

        await self.highrise.send_emote("hcc-jetpack",user.id) 

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  

        if message.lower().startswith(("!jugar","/jugar","/rps","!rps")):
          choices = ['piedra', 'papel', 'tijera']
          client_chosen = random.choice(choices)
          option = message[5:].strip().lower()

          text_to_emoji = {"piedra": "✊", "papel": "✋", "tijera": "✌️"}

          if option not in choices:
              response = f"Uso de comando inválido :\nExemplo: !rps <{client_chosen}>\nOpções disponíveis:\n{', '.join(choices)}"
              await self.highrise.send_whisper(user.id, response)
              return
          elif option == client_chosen:
              response = "Es un empate. 🤝"
          elif (option == "piedra" and client_chosen == "tijera") or (option == "papel" and client_chosen == "piedra") or (option == "tijera" and client_chosen == "papel"):
              response = f"\nParabéns, você venceu! 🎉\nvocê: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"
          else:
              response = f"\nHas perdido. 😢\nVocê: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"

          await self.highrise.chat(response)

        if message.lower().startswith("!tipall ") and user.username == "ElCordobez":
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.send_message(user.id, "💰Comando inválido")
                  return
              # Checks if the amount is valid
              try:
                  amount = int(parts[1])
              except:
                  await self.highrise.chat("💰Quantidade inválida")
                  return
              # Checks if the bot has the amount
              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount
              if bot_amount < amount:
                  await self.highrise.chat("💰Não há fundos suficientes")
                  return
              # Get all users in the room
              room_users = await self.highrise.get_room_users()
              # Check if the bot has enough funds to tip all users the specified amount
              total_tip_amount = amount * len(room_users.content)
              if bot_amount < total_tip_amount:
                  await self.highrise.chat("💰Não há fundos suficientes para dar gorjeta a todos")
                  return
              # Tip each user in the room the specified amount
              for room_user, pos in room_users.content:
                  bars_dictionary = {
                      10000: "gold_bar_10k",
                      5000: "gold_bar_5000",
                      1000: "gold_bar_1k",
                      500: "gold_bar_500",
                      100: "gold_bar_100",
                      50: "gold_bar_50",
                      10: "gold_bar_10",
                      5: "gold_bar_5",
                      1: "gold_bar_1"
                  }
                  fees_dictionary = {
                      10000: 1000,
                      5000: 500,
                      1000: 100,
                      500: 50,
                      100: 10,
                      50: 5,
                      10: 1,
                      5: 1,
                      1: 1
                  }
                  # Convert the amount to a string of bars and calculate the fee
                  tip = []
                  remaining_amount = amount
                  for bar in bars_dictionary:
                      if remaining_amount >= bar:
                          bar_amount = remaining_amount // bar
                          remaining_amount = remaining_amount % bar
                          for i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]
                  if total > bot_amount:
                      await self.highrise.chat("💰Não há fundos suficientes")
                      return
                  for bar in tip:
                      await self.highrise.tip_user(room_user.id, bar)                   
                      await self.highrise.chat(f"💰Deu para {room_user.username} {amount} {bar}!")

        if message.lower().startswith("!tipme ") and user.username== "ElCordobez":
                try:
                    amount_str = message.split(" ")[1]
                    amount = int(amount_str)
                    bars_dictionary = {
                        10000: "gold_bar_10k",
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    # Get bot's wallet balance
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    # Check if bot has enough funds
                    if bot_amount < amount:
                        await self.highrise.chat("💰Não há fundos suficientes na carteira do bot. ")
                        return
                    # Convert amount to bars and calculate total
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount %= bar
                            tip.extend([bars_dictionary[bar]] * bar_amount)
                            total += bar_amount * bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.chat("💰Não há fundos suficientes para dar a gorjeta no valor especificado. ")
                        return
                    # Send tip to the user who issued the command
                    for bar in tip:
                        await self.highrise.tip_user(user.id, bar)
                    await self.highrise.chat(f"💰Você foi avisado  {amount_str}.")
                except (IndexError, ValueError):
                    await self.highrise.chat("💰Valor de gorjeta inválido. Por favor, especifique um número válido. ")   
                    await self.highrise.chat(f"💰Deu para {user.username} {amount} {bar}!")

        if message.startswith("/pescar"):
            await self.highrise.send_whisper(user.id,"Você Está Pescando 🎣...")

        if message.lower() == "/pescar":
           frase = random.choice(pescar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/bomba":
           frase = random.choice(bomba)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/cuchillazo":
           frase = random.choice(facada)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/pocion":
           frase = random.choice(curativo)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/play":
           frase = random.choice(play)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/disparar":
           frase = random.choice(atirar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/nivel de locura":
           frase = random.choice(louca)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/locura":
           frase = random.choice(louca)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/nos casamos?":
           frase = random.choice(casa)
           await self.highrise.chat(frase)

        if message.startswith("/pescar"):
           await self.highrise.react("clap",user.id)

        if message.startswith("/carpa"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡Has pescado 1x Cana de la nochea🟡 Felicidades has ganado la medalla : (MEGA PESCADOR)")

        if message.startswith("/camaron"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎Has pescado 1x Cana de la nocheiamante💎Felicidades has ganado la medalla : (PESCADOR MASTER DIAMANTE )")                                
        if message.startswith("/curativo"):
           await self.highrise.react("heart",user.id)

        if message.startswith("/escudo"):
           await self.highrise.react("heart",user.id)
           await self.highrise.send_whisper(user.id,f"@{user.username} 🛡 Você Usou O Escudo🛡")

        if message.lower() == "/cuantas personas me aman":
           frase = random.choice(amor)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/amor":
           frase = random.choice(amor)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/cuantas personas me odian":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/odio":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/adivinanza":
           frase = random.choice(piada)
           await self.highrise.chat(frase)

        if message.lower() == "/chamuyo":
           frase = random.choice(cantada)
           await self.highrise.chat(frase)

        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username =="ElCordobez":            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"🕺🏻Lista de emotes gratis:\n\n1.wrong\n2.fashion\n3.gravity\n4.icecream\n5.casual\n6.kiss\n7.no\n8.sad\n9.yes\n10.laughing\n11.hello\n12.wave\n13.shy\n14.tired\n15.flirtywave\n16.greedy\n17.model\n18.bow\n19.curtsy")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n20.snowball\n21.hot\n22.snowangel\n23.charging\n24.confused\n25.telekinesis\n26.float\n27.teleport\n28.maniac\n29.eneryball\n30.snake\n31.frog\n32.superpose\n33.cute\n34.pose7\n35.pose8\n36.pose1\n37.pose5\n38.pose3")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n39.cutey\n40.shuffle\n41.singalong\n42.enthused\n43.letsgoshopping\n44.russian\n45.pennywise\n46.dontstartnow\n47.blackpink\n48.celebrate\n49.gagging\n50.flex\n51.cursing\n52.thumbsup\n53.angry\n54.punk\n55.zombie\n56.sit\n57.fight")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n58.macarena\n59.weird\n60.savage\n61.viralgroove\n62.uwu\n63.sayso\n64.stargazer\n65.pose9\n66.boxer\n67.airguitar\n68.penguin\n69.astronaut\n70.saunter\n71.creepy\n72.watch\n73.revelations\n74.bashful\n75.arabesque\n76.party")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n77.skating\n78.scritchy\n79.bitnervous\n80.timejump\n81.gottago\n82.jingle\n83.hyped\n84.sleigh\n85.surprise\n86.repose\n87.kawaii\n88.touch\n89.foryou\n90.pushit\n91.salute\n92.attention\n93.tiktok\n.94.smooch\n95.launch\n96.fairyfloat\n97.fairytwirl\n98.jetpack")

        if        message.startswith("/lista") or   message.startswith("/emotes") or   message.startswith("!emotes") or         message.startswith("/emote list") or message.startswith("!emoteall") or message.startswith("!emote list") or message.startswith("!lista"):
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("Feo") or      message.startswith("Feo") or      message.startswith("veado") or message.startswith("Veado"):
            await self.highrise.chat(f"Respetame HDP!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("corno") or      message.startswith("Corno") or      message.startswith("Vagabundo") or message.startswith("vagabundo"):
            await self.highrise.chat(f"SEU PAI!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("/usuarios") or      message.startswith("!usuarios"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Hay  {len(room_users)} personas en la sala. ")
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("!bot lindo") or      message.startswith("!Bot lindo") or      message.startswith("/Bot Lindo"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_emote("idle-uwu", user.id)
            await self.highrise.chat(f"Tambien eres linda {user.username} 😳👉👈")

        if message.lower().lstrip().startswith(("Ajuda","/ajuda","-help","ajuda","!help","Help","!ajuda","/help","help")):
            await self.highrise.send_whisper(user.id, f"Hola necesitas ayuda? 👋\n\nComandos livres:\n!wave @user 1-10\n!thumbs @user 1-10\n!wink @user 1-10\n!clap @user 1-10\n!heart @user 1-10\n/fly 0,0,0\n/tele @user\n/emotes\n/loop emote nome | /loop 1-98\n!follow")
            await self.highrise.send_whisper(user.id,f"\n\nJogos\n/jugar\n/pescar\n/rps pedra|papel|tesoura\n/amor\n/odio\n/locura\n/nos casamos?\n/chamuyos\n\nCardapios\n/cardapio1\n/cardapio2\n\nEmote com amigo\n-emote @user")
            await self.highrise.send_whisper(user.id, f"\n\nTodos os comandos são usados com caracteries especiais\n\nCaracteries: ! ou / ou -")
            await asyncio.sleep(10)
            await self.highrise.send_whisper(user.id, f"\n\nComandos de Administador:\n!wave @user 1-100\n!thumbs @user 1-100\n!clap @user 1-100\n!wink @user 1-100\n!heart @user 1-100\n!emote all emote\n/summom @user\n/fly user 0,0,0\n!kick @user\n!wallet\n!fit 1-11\n!tipall [quantia]\n!tipme [quantia]")   
            await self.highrise.send_whisper(user.id, f"\n\nTodos os comandos são usados com caracteries especiais\n\nCaracteries: ! ou / ou -")

        if        message.startswith("Lindo") or      message.startswith("LINDO") or      message.startswith("lindo"):
            await self.highrise.react("heart",user.id,)
            await self.highrise.chat(f"Vos tambien sos linda mi amor {user.username} 🥰🥰")
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("Buen dia") or      message.startswith("Buenos dias") or      message.startswith("bom dia") or message.startswith("BOM DIA"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Buenos dias, excelente jornada! {user.username} 😊🌅")

        if        message.startswith("Buena noche") or      message.startswith("Buenas noches") or      message.startswith("Boa Noite") or message.startswith("BOA NOITE"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Buenas noches, que tengas buen descanso {user.username} 😊🌃🌉")

        if        message.startswith("Buena tarde") or      message.startswith("Buenas tardes") or      message.startswith("Boa Tarde") or message.startswith("BOA TARDE"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Buenas tardes {user.username} ☀️")

        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)

        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or             message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if        message.startswith("😭") or      message.startswith("🥲") or      message.startswith("😓") or             message.startswith("😔") or message.startswith("😥"):
            await self.highrise.send_emote("emote-sad",user.id)

        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or     message.startswith("🙃") or     message.startswith("🤤") or     message.startswith("😋") or     message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)

        if        message.startswith("!wrong") or   message.startswith("wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/fashion") or      message.startswith("fashion") or       message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/gravity") or      message.startswith("gravity") or       message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/icecream") or                                message.startswith("icecream") or message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/casual") or  message.startswith("casual") or     message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/kiss") or      message.startswith("!kiss") or  message.startswith("kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/no") or      message.startswith("no") or            message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/sad") or      message.startswith("!sad") or    message.startswith("sad") or     message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/yes") or      message.startswith("!yes") or    message.startswith("yes") or     message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/lau") or   message.startswith("laughing") or   message.startswith("Laughing") or   message.startswith("/laughing") or   message.startswith("!laughing") or      message.startswith("!lau") or    message.startswith("Lau") or     message.startswith("lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/hello") or message.startswith("hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/wave") or  message.startswith("wave") or     message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/shy") or   message.startswith("shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/tired") or message.startswith("tired") or      message.startswith("!tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/flirt") or message.startswith("flirt") or message.startswith("flirtywave") or message.startswith("flirty") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or  message.startswith("model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or    message.startswith("bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or                              message.startswith("snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or    message.startswith("hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or                              message.startswith("snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or                              message.startswith("charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or                              message.startswith("confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or                            message.startswith("telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or  message.startswith("float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or                              message.startswith("teleport") or      message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or                             message.startswith("eneryball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or  message.startswith("snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or   message.startswith("frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or                              message.startswith("superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or   message.startswith("cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or  message.startswith("pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or  message.startswith("pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or  message.startswith("pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or  message.startswith("pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or  message.startswith("pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or  message.startswith("cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/tik10") or    message.startswith("shuffle") or    message.startswith("Shuffle") or   message.startswith("!shuffle") or    message.startswith("/shuffle") or    message.startswith("!tik10") or      message.startswith("Tik10") or  message.startswith("tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or                              message.startswith("singing") or                              message.startswith("!singalong")  or                             message.startswith("/singalong") or message.startswith("Singalong") or                             message.startswith("singalong") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or                              message.startswith("enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/shop") or      message.startswith("Letsgoshopping") or      message.startswith("letsgoshopping") or      message.startswith("/letsgoshopping") or      message.startswith("!letsgoshopping") or    message.startswith("!shop") or      message.startswith("Shop") or   message.startswith("shop") or   message.startswith("!shopping") or message.startswith("/shopping") or message.startswith("Shopping") or message.startswith("shopping") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or                              message.startswith("russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or                              message.startswith("pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or   message.startswith("!dontstartnow") or   message.startswith("/dontstartnow") or   message.startswith("dontstartnow") or   message.startswith("Dontstartnow") or   message.startswith("tik2") or   message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or                              message.startswith("blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or                              message.startswith("celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or                              message.startswith("gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or   message.startswith("flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or                              message.startswith("cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or                              message.startswith("thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or  message.startswith("angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or   message.startswith("punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or    message.startswith("sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or  message.startswith("fight") or  message.startswith("!swordfight") or message.startswith("/swordfight") or message.startswith("Swordfight") or message.startswith("swordfight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or    message.startswith("ren") or    message.startswith("!macarena") or     message.startswith("/macarena") or      message.startswith("Macarena") or message.startswith("macarena") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or    message.startswith("wei") or message.startswith("!weird") or message.startswith("/weird") or message.startswith("Weird") or message.startswith("weird") or  message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("tik8") or message.startswith("savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("!viralgroove") or message.startswith("/viralgroove") or message.startswith("Viralgroove") or message.startswith("viralgroove") or message.startswith("tik9") or message.startswith("viral") or message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or    message.startswith("uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or  message.startswith("sayso") or message.startswith("tik4") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/star") or    message.startswith("star") or     message.startswith("!star") or      message.startswith("Star") or   message.startswith("!stargazer") or     message.startswith("/stargazer") or   message.startswith("Stargazer") or   message.startswith("stargazer") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or  message.startswith("pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or  message.startswith("boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/airguitar") or    message.startswith("!airguitar") or     message.startswith("airguitar") or      message.startswith("Airguitar") or   message.startswith("Guitar") or     message.startswith("guitar") or   message.startswith("!guitar") or   message.startswith("/guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or   message.startswith("penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or                                message.startswith("astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or    message.startswith("anime") or   message.startswith("saunter") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or   message.startswith("creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or    message.startswith("watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or                                message.startswith("revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or  message.startswith("bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or                                message.startswith("arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or    message.startswith("party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or  message.startswith("skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or  message.startswith("nervous") or   message.startswith("bitnervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("timejump") or message.startswith("time") or   message.startswith("Time") or   message.startswith("!time") or   message.startswith("/time") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("gottago") or  message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or  message.startswith("jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or   message.startswith("hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or        message.startswith("sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/repose") or      message.startswith("!repose") or        message.startswith("repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)
            await self.highrise.chat(f" Te gustará este emote {user.username} 😍")

        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or        message.startswith("kawaii") or       message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or         message.startswith("touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/foryou") or    message.startswith("!foryou") or  message.startswith("foryou") or   message.startswith("Foryou") or   message.startswith("/gift") or      message.startswith("!gift") or          message.startswith("gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or        message.startswith("pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or        message.startswith("salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or        message.startswith("attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)                                                                   

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or        message.startswith("tiktok") or    message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or        message.startswith("smooch") or    message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or        message.startswith("launch") or   message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if        message.startswith("/fairyfloat") or      message.startswith("!fairyfloat") or        message.startswith("fairyfloat") or    message.startswith("Fairyfloat") or message.startswith("96"):
            await self.highrise.send_emote("idle-floating",user.id)

        if        message.startswith("/fairytwirl") or      message.startswith("!fairytwirl") or        message.startswith("fairytwirl") or    message.startswith("Fairytwirl") or message.startswith("97"):
            await self.highrise.send_emote("emote-looping",user.id)

        if        message.startswith("/jetpack") or      message.startswith("!jetpack") or        message.startswith("jetpack") or    message.startswith("Jetpack") or message.startswith("98"):
            await self.highrise.send_emote("hcc-jetpack",user.id)

        if              message.startswith("Jetpack All") or                              message.startswith("/emote all jetpack") or       message.startswith("!emote all jetpack"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("hcc-jetpack", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Jetpack] para {len(room_users)} personas.")

        if              message.startswith("Fairyfloat All") or                              message.startswith("/emote all fairyfloat") or       message.startswith("!emote all fairyfloat"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-floating", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fairyfloat] para {len(room_users)} personas.")

        if              message.startswith("Fairytwirl All") or                              message.startswith("/emote all fairytwirl") or       message.startswith("!emote all fairytwirl"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-looping", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fairytwirl] para {len(room_users)} personas.")

        if              message.startswith("Launch All") or                              message.startswith("/emote all launch") or       message.startswith("!emote all launch"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Launch] para {len(room_users)} personas.")

        if              message.startswith("Smooch All") or                              message.startswith("/emote all smooch") or       message.startswith("!emote all smooch"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Smooch] para {len(room_users)} personas.")

        if              message.startswith("Pushit All") or                              message.startswith("/emote all pushit") or       message.startswith("!emote all pushit"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pushit] para {len(room_users)} personas.")

        if              message.startswith("Gift All") or                              message.startswith("/emote all gift") or       message.startswith("!emote all gift"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gift] para {len(room_users)} personas.")

        if              message.startswith("Attention All") or                              message.startswith("/emote all attention") or       message.startswith("!emote all attention"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Attention] para {len(room_users)} personas.")

        if              message.startswith("Salute All") or                              message.startswith("/emote all salute") or       message.startswith("!emote all salute"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutesalute", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Salute] para {len(room_users)} personas.")

        if              message.startswith("Tiktok All") or                              message.startswith("/emote all tiktok") or       message.startswith("!emote all tiktok"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Tiktok] para {len(room_users)} personas.")

        if              message.startswith("Touch All") or                              message.startswith("/emote all touch") or       message.startswith("!emote all touch"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Touch] para {len(room_users)} personas.")

        if              message.startswith("Kawaii All") or                              message.startswith("/emote all kawaii") or       message.startswith("!emote all kawaii"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Kawaii] para {len(room_users)} personas.")

        if              message.startswith("Hot All") or                              message.startswith("/emote all hot") or       message.startswith("!emote all hot"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Hot] para {len(room_users)} personas.")


        if              message.startswith("Curtsy All") or                              message.startswith("/emote all curtsy") or       message.startswith("!emote all curtsy"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Curtsy] para {len(room_users)} personas.")

        if              message.startswith("Surprise All") or                              message.startswith("/emote all surprise") or       message.startswith("!emote all surprise"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose6", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Surprise] para {len(room_users)} personas.")

        if              message.startswith("Jingle All") or                              message.startswith("/emote all jingle") or       message.startswith("!emote all jingle"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Jingle] para {len(room_users)} personas.")

        if              message.startswith("Creepy All") or                              message.startswith("/emote all creepy") or       message.startswith("!emote all creepy"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Creepy] para {len(room_users)} personas.")

        if              message.startswith("Nervous All") or message.startswith("Bitnervous All") or      message.startswith("!emote all bitnervous") or message.startswith("/emote all bitnervous") or                             message.startswith("/emote all nervous") or       message.startswith("!emote all nervous"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bitnervous] para {len(room_users)} personas.")

        if              message.startswith("Scritchy All") or                              message.startswith("/emote all scritchy") or       message.startswith("!emote all scritchy"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Scritchy] para {len(room_users)} personas.")

        if              message.startswith("Fashion All") or                              message.startswith("/emote all fashion") or       message.startswith("!emote all fashion"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fashion] para {len(room_users)} personas.")

        if              message.startswith("Wrong All") or                              message.startswith("/emote all wrong") or       message.startswith("!emote all wrong"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Wrong] para {len(room_users)} personas.")

        if              message.startswith("Cutey All") or                              message.startswith("/emote all cutey") or       message.startswith("!emote all cutey"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Cutey] para {len(room_users)} personas.")

        if              message.startswith("Hyped All") or                              message.startswith("/emote all hyped") or       message.startswith("!emote all hyped"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Hyped] para {len(room_users)} personas.")

        if              message.startswith("Superpose All") or                              message.startswith("/emote all superpose") or       message.startswith("!emote all superpose"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Superpose] para {len(room_users)} personas.")

        if              message.startswith("Punk All") or                              message.startswith("/emote all punk") or       message.startswith("!emote all punk"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id) 
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Punk] para {len(room_users)} personas.")

        if              message.startswith("Dontstartnow All") or message.startswith("Tiktok2 All") or      message.startswith("!emote all dontstartnow") or message.startswith("/emote all dontstartnow") or                             message.startswith("/emote all tiktok2") or       message.startswith("!emote all tiktok2"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Dontstartnow] para {len(room_users)} personas.")


        if              message.startswith("Savage All") or message.startswith("Tiktok8 All") or      message.startswith("!emote all savage") or message.startswith("/emote all savage") or                             message.startswith("/emote all tiktok8") or       message.startswith("!emote all tiktok8"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Savage] para {len(room_users)} personas.")

        if              message.startswith("Tiktok10 All") or                              message.startswith("/emote all tiktok10") or       message.startswith("!emote all tiktok10"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Tiktok10] para {len(room_users)} personas.")

        if              message.startswith("Viral All") or     message.startswith("!emotr all tiktok9") or        message.startswith("/emote all tiktok9") or    message.startswith("Tiktok9 All") or message.startswith("Viralgroove All") or      message.startswith("!emote all viral") or message.startswith("/emote all viralgroove") or                             message.startswith("/emote all viral") or       message.startswith("!emote all viralgroove"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Viralgroove] para {len(room_users)} personas.")

        if              message.startswith("Blackpink All") or                              message.startswith("/emote all blackpink") or       message.startswith("!emote all blackpink"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Blackpink] para {len(room_users)} personas.")

        if              message.startswith("Gagging All") or                              message.startswith("/emote all gagging") or       message.startswith("!emote all gagging"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gagging] para {len(room_users)} personas.")

        if              message.startswith("Pose3 All") or                              message.startswith("/emote all pose3") or       message.startswith("!emote all pose3"):
          if user.username == "ShoKytoo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose3] para {len(room_users)} personas.")

        if              message.startswith("Pose7 All") or                              message.startswith("/emote all pose7") or       message.startswith("!emote all pose7"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose7] para {len(room_users)} personas.")

        if              message.startswith("Pose5 All") or                              message.startswith("/emote all pose5") or       message.startswith("!emote all pose5"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose5] para {len(room_users)} personas.")

        if              message.startswith("Pose1 All") or                              message.startswith("/emote all pose1") or       message.startswith("!emote all pose1"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose1] para {len(room_users)} personas.")

        if              message.startswith("Pose8 All") or                              message.startswith("/emote all pose8") or       message.startswith("!emote all pose8"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose8] para {len(room_users)} personas.")

        if              message.startswith("Enthused All") or                              message.startswith("/emote all enthused") or       message.startswith("!emote all enthused"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Enthused] para {len(room_users)} personas.")

        if              message.startswith("Singing All") or message.startswith("Sing All") or      message.startswith("!emote all sing") or message.startswith("/emote all sing") or                             message.startswith("/emote all singing") or       message.startswith("!emote all singing"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Singing] para {len(room_users)} personas.")

        if              message.startswith("Teleport All") or                              message.startswith("/emote all teleport") or       message.startswith("!emote all teleport"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Teleporting] para {len(room_users)} personas.")

        if              message.startswith("Telekinesis All") or                              message.startswith("/emote all telekinesis") or       message.startswith("!emote all telekinesis"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Telekinesis] para {len(room_users)} personas.")

        if              message.startswith("Casual All") or                              message.startswith("/emote all casual") or       message.startswith("!emote all casual"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Casual] para {len(room_users)} personas.")

        if              message.startswith("Icecream All") or                              message.startswith("/emote all icecream") or       message.startswith("!emote all icecream"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Icecream] para {len(room_users)} personas.")

        if              message.startswith("Zombie All") or                              message.startswith("/emote all zombie") or       message.startswith("!emote all zombie"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Zombie] para {len(room_users)} personas.")

        if              message.startswith("Celebrate All") or                              message.startswith("/emote all celebrate") or       message.startswith("!emote all celebrate"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Celebrate] para {len(room_users)} personas.")

        if              message.startswith("Kiss All") or                              message.startswith("/emote all kiss") or       message.startswith("!emote all kiss"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Kiss] para {len(room_users)} personas.")

        if              message.startswith("Snowangel All") or                              message.startswith("/emote all snowangel") or       message.startswith("!emote all snowangel"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Snowangel] para {len(room_users)} personas.")

        if              message.startswith("Bow All") or                              message.startswith("/emote all bow") or       message.startswith("!emote all bow"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bow] para {len(room_users)} personas.")

        if              message.startswith("Ice All") or message.startswith("Skating All") or      message.startswith("!emote all ice") or message.startswith("/emote all skating") or                             message.startswith("/emote all ice") or       message.startswith("!emote all skating"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Iceskating] para {len(room_users)} personas.")

        if              message.startswith("Confused All") or                              message.startswith("/emote all confused") or       message.startswith("!emote all confused"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Confused] para {len(room_users)} personas.")

        if              message.startswith("Charging All") or                              message.startswith("/emote all charging") or       message.startswith("!emote all charging"):
          if user.username == "ShoKytoo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Charging] para {len(room_users)} personas.")

        if              message.startswith("Weird All") or message.startswith("Wei All") or      message.startswith("!emote all wei") or message.startswith("/emote all wei") or                             message.startswith("/emote all weird") or       message.startswith("!emote all weird"):
          if user.username == "ShoKytoo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Weird] para {len(room_users)} personas.")

        if              message.startswith("Greedy All") or                              message.startswith("/emote all greedy") or       message.startswith("!emote all greedy"):
          if user.username == "ShoKytoo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Greedy] para {len(room_users)} personas.")

        if              message.startswith("Cursing All") or                              message.startswith("/emote all cursing") or       message.startswith("!emote all cursing"):
          if user.username == "ShoKytoo":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Cursing] para {len(room_users)} personas.")

        if              message.startswith("Russian All") or                              message.startswith("/emote all russian") or       message.startswith("!emote all russian"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Russian] para {len(room_users)} personas.")

        if              message.startswith("Repose All") or                              message.startswith("/emote all repose") or       message.startswith("!emote all repose"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Repose] para {len(room_users)} personas.")

        if              message.startswith("Shop All") or message.startswith("Shopping All") or      message.startswith("!emote all shopping") or message.startswith("/emote all shop") or                             message.startswith("/emote all shopping") or       message.startswith("!emote all shop"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Shopping] para {len(room_users)} personas.")

        if              message.startswith("Macarena All") or message.startswith("Ren All") or      message.startswith("!emote all macarena") or message.startswith("/emote all macarena") or                             message.startswith("/emote all ren") or       message.startswith("!emote all   ren "):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Macarena] para {len(room_users)} personas.")

        if              message.startswith("Snake All") or                              message.startswith("/emote all snake") or       message.startswith("!emote all snake"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Snake] para {len(room_users)} personas.")

        if              message.startswith("Model All") or                              message.startswith("/emote all model") or       message.startswith("!emote all model"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Model] para {len(room_users)} personas.")

        if              message.startswith("Sleigh All") or                              message.startswith("/emote all sleigh") or       message.startswith("!emote all sleigh"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Sleigh] para {len(room_users)} personas.")

        if              message.startswith("Sayso All") or message.startswith("Tiktok4 All") or      message.startswith("!emote all sayso") or message.startswith("/emote all sayso") or                             message.startswith("/emote all tiktok4") or       message.startswith("!emote all tiktok4"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Sayso] para {len(room_users)} personas.")

        if              message.startswith("Uwu All") or                              message.startswith("/emote all uwu") or       message.startswith("!emote all uwu"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Uwu] para {len(room_users)} personas.")

        if              message.startswith("Star All") or                              message.startswith("/emote all star") or       message.startswith("!emote all star"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-stargazer", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Stargazer] para {len(room_users)} personas.")

        if              message.startswith("Pose9 All") or                              message.startswith("/emote all pose9") or       message.startswith("!emote all pose9"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose9", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose9] para {len(room_users)} personas.")

        if              message.startswith("Boxer All") or                              message.startswith("/emote all boxer") or       message.startswith("!emote all boxer"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Boxer] para {len(room_users)} personas.")

        if              message.startswith("Airguitar All") or message.startswith("Guitar All") or      message.startswith("!emote all guitar") or message.startswith("/emote all airguitar") or                             message.startswith("/emote all guitar") or       message.startswith("!emote all airguitar"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-guitar", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Airguitar] para {len(room_users)} personas.")

        if              message.startswith("Penguin All") or message.startswith("Pinguin All") or      message.startswith("!emote all penguin") or message.startswith("/emote all penguin") or                             message.startswith("/emote all pinguin") or       message.startswith("!emote all pinguin"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Penguin] para {len(room_users)} personas.")

        if              message.startswith("Astronaut All") or message.startswith("Zero All") or      message.startswith("!emote all zero") or message.startswith("/emote all zero") or                             message.startswith("/emote all astronaut") or       message.startswith("!emote all astronaut"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Astronaut] para {len(room_users)} personas.")

        if              message.startswith("Saunter All") or   message.startswith("Anime All") or   message.startswith("!emote all anime") or   message.startswith("/emote all anime") or                              message.startswith("/emote all saunter") or       message.startswith("!emote all saunter"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Saunter] para {len(room_users)} personas.")

        if              message.startswith("Flirt All") or     message.startswith("!emote all flirt") or    message.startswith("/emote all flirt") or    message.startswith("!emote all flirty") or     message.startswith("Flirtywave All") or    message.startswith("/emote all flirty") or    message.startswith("/emote all flirt") or                               message.startswith("/emote all flirtywave") or       message.startswith("!emote all flirtywave"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Flirtywave] para {len(room_users)} personas.")

        if              message.startswith("Watch All") or                              message.startswith("/emote all watch") or       message.startswith("!emote all watch"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Watch] para {len(room_users)} personas.")

        if              message.startswith("Revelations All") or                              message.startswith("/emote all revelations") or       message.startswith("!emote all revelations"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Revelations] para {len(room_users)} personas.")

        if              message.startswith("Bashful All") or                              message.startswith("/emote all bashful") or       message.startswith("!emote all bashful"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bashful] para {len(room_users)} personas.")

        if              message.startswith("Arabesque All") or                              message.startswith("/emote all arabesque") or       message.startswith("!emote all arabesque"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose10", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Arabesque] para {len(room_users)} personas.")

        if              message.startswith("Party All") or                              message.startswith("/emote all party") or       message.startswith("!emote all party"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-celebrate", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Party] para {len(room_users)} personas.")

        if              message.startswith("Time All") or                              message.startswith("/emote all time") or       message.startswith("!emote all time"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Time] para {len(room_users)} personas.")

        if              message.startswith("Gottago All") or                              message.startswith("/emote all gottago") or       message.startswith("!emote all gottago"):
          if user.username == "ElCordobez":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gottago] para {len(room_users)} personas.")

        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de bebidas espero que goste 😄")

        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"/tequila , /gim , /vinho , /vinho-branco , /vodka , /whisky , /rum , /champanhe , /cachaça /conhaque , /cerveja , /coca-cola , /suco , /agua , /agua-de-coco , /toddy , /nescau")

        if message.startswith("/coca-cola"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui tienes una refrescante Coca-Cola 🧊🥤 ")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/toddy"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui tienes tu toddy 🥛")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/suco"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui tienes tu jugo, es de fresa, no me quedó otro sabor 🧃")
            await self.highrise.react("thumbs", user.id)
        if message.startswith("/agua"):  
            await self.highrise.send_whisper(user.id,f"🌊aqui está sua deliciosa agua {user.username} diretamente da toneira 🌊")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/agua-de-coco"):  
            await self.highrise.send_whisper(user.id,f"🥥aqui tienes tu agua de coco {user.username} que la disfrutes 🥥")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/nescau"):  
            await self.highrise.send_whisper(user.id,f"aqui está {user.username} seu delicioso nescau 🥛")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/tequila"):  
            await self.highrise.send_whisper(user.id,f"{user.username} disfruta de tu tequila 😄🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/fernet"):
            await self.highrise.send_whisper(user.id,f"que disfrutes de tu fernet {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/conhaque"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu conhaque {user.username} 🥃🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/whisky"):  
            await self.highrise.send_whisper(user.id,f"Aqui esta su Whisky  {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/rum"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Rum 🥃 {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cachaça"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua Cachaça {user.username} não beba muito 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vodka"):  
            await self.highrise.send_whisper(user.id,f"Aqui tienes un poco de vodka {user.username} ")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/champanhe"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Champanhe {user.username} 🍾🥂")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cerveja"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Cerveja {user.username} 🍺")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho-branco"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho-Branco {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de comidas e petiscos espero que goste 😄")

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/camarão , /salada-de-alface , /salada-de-repolho , /macarrão , /pizza , /bolo-de-cenoura")

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/milanesa , /açai , /sorvete , /cupcake , /sorvete , /batata-frita , /espetinho , /pão-de-alho")

        if message.startswith("/pizza"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui tienes pizza, come antes que se enfrie 🍕")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/milanesa"):
            await self.highrise.send_whisper(user.id,f"Aqui tienes tu milanesa, que la disfrutes {user.username} 🥮")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/salada-de-repolho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Deliciosa salada de repolho {user.username} 🥬🥬")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/camarão"):  
            await self.highrise.send_whisper(user.id,f"🍤Aqui Está seu Delicoso Camarão 🍤 {user.username} 🍤")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/macarrão"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu macarrão {user.username} aproveite 🍜🍝")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/salada-de-alface"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua salada de alface {user.username} com um pouco de tomates por cima 🥬🥗")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/bolo-de-cenoura"):  
            await self.highrise.send_whisper(user.id,f"aqui está seu bolo de cenoura  {user.username} 🥕🥮")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/açai"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Açai {user.username} 🍨 Aproveite")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/sorvete"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu sorvete {user.username} 🍦🍨")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/pão-de-alho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua pão de alho {user.username} 🥖🧄")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/batata-frita"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Batata Frita {user.username} aproveite 🍟")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/espetinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Espetinho {user.username} 🍢🍢")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cupcake"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu cupcake {user.username} 🧁")
            await self.highrise.react("thumbs", user.id)

        if        message.startswith("/tp") or      message.startswith("!tp") or      message.startswith("/tele") or          message.startswith("Tp") or          message.startswith("Tele") or  message.startswith("!tele"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "ElCordobez":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)

        if              message.startswith("Carteira") or  message.startswith("Wallet") or    message.startswith("wallet") or       message.startswith("carteira"):
          if user.username == "ElCordobez":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"VALOR TOTAL : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("dance-tiktok14")

        if message.startswith("!kick"):
          if user.username == "ElCordobez":
              pass
          else:
              await self.highrise.chat("Voce não tem permissao para usar esse comando.")
              return
          #separete message into parts
          parts = message.split()
          #check if message is valid "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("formato de banimento errado.")
              return
          #checks if there's a @ in the message
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]
          #check if user is in room
          room_users = (await self.highrise.get_room_users()).content
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break
          if "user_id" not in locals():
              await self.highrise.chat("usuario não encontrado, porfavor arrume a cordenada do codigo")
              return
          #kick user
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return
          #send message to chat
          await self.highrise.chat(f"{username} Foi Banido da sala!!")

        if message == "!fit 1" and user.username == "ElCordobez":
          shirt = ["shirt-n_room32019jerseywhite"]
          pant = ["pants-n_room22019longcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_malenew16', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_malenew16', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairupper06', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairlower16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malediamondsleepy', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[1] adicionado ao bot.") 


        if message == "!fit 2" and user.username == "ElCordobez":
          shirt = ["shirt-n_starteritems2019tankblack"]
          pant = ["pants-n_starteritems2019mensshortsblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=25),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_malenew01', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_malenew01', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018lippiercing', account_bound=False, active_palette=24),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malediamonddroopy', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows11', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[2] adicionado ao bot.")

        if message == "!fit 3"  and user.username == "ElCordobez":
          shirt = ["shirt-f_punklace"]
          pant = ["pants-n_room22019shortcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullpeaked', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightbluntbangs', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straighthighpony', account_bound=False, active_palette=2),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2019flatsblack', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"👕FIT[3] adicionado ao bot.")

        if message == "!fit 4" and user.username == "ElCordobez":
          shirt = ["shirt-n_room22019bratoppink"]
          pant = ["pants-n_room22019undiespink"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='nose-n_01_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='glasses-n_room32019smallshades', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018pillowfullpeaked', account_bound=False, active_palette=9),
                  Item(type='clothing', amount=1, id='eye-n_basic2018falselashes', account_bound=False, active_palette=10),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[4] adicionado ao bot.")

        if message == "!fit 5" and user.username == "ElCordobez":
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["skirt-n_room12019pleatedskirtgrey"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_room22019sillymouth', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),

          ]) 
          await self.highrise.chat(f"👕FIT[5] adicionado ao bot.")

        if message == "!fit 6" and user.username == "ElCordobez":
          shirt = ["shirt-n_room32019longlineteesweatshirtgrey"]
          pant = ["pants-n_starteritems2019cuffedjeansblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018whistlemouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_04', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[6] adicionado ao bot.")

        if message == "!fit 7" and user.username == "ElCordobez":
          shirt = ["shirt-n_starteritems2019pulloverblack"]
          pant = ["pants-n_starteritems2019mensshortsblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew23', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew23', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-vip_f_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[7] adicionado ao bot.")

        if message == "!fit 8" and user.username == "ElCordobez":
          shirt = ["shirt-n_registrationavatars2023arianadress"]
          pant = ["pants-n_room22019undiesblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_basic2019poofbob', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_basic2018straightbangslowpart', account_bound=False, active_palette=82),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023arianaboots', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='eye-n_registrationavatars2023gymgirleyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[8] adicionado ao bot.")

        if message == "!fit 9" and user.username in ["ElCordobez","ShoKytoo"]:
          shirt = ["shirt-n_room12019sweaterwithbuttondowngrey"]
          pant = ["pants-n_room12019formalslackskhaki"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew05', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='eyebrow-n_06', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew04', account_bound=False, active_palette=4),

                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018chippermouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-m_12b', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[9] adicionado ao bot.")

        if message == "!fit 10" and user.username == "ElCordobez":
          shirt = ["shirt-n_winxudcrwrdsone2024winxblueshirt"]
          pant = ["skirt-n_winxudcrwrdsone2024pinkskirtstrawberrys"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_basic2018wavypulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_basic2018sidebangspulledback', account_bound=False, active_palette=1),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakerspink', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='eye-n_basic2018liftedeyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[10] adicionado ao bot.")

        if message == "!fit 11" and user.username == "ElCordobez":
          shirt = ["shirt-n_registrationavatars2023gothguyhoodie"]
          pant = ["pants-n_starteritems2019cuffedjeansblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=6),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-m_23', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='nose-n_01_b', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-m_23', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020blacksocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023furrysneakers', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-vip_f_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='bag-n_registrationavatars2023furrytail', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hat-n_registrationavatars2023wolfears', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[11] adicionado ao bot.")

        if message.lower().lstrip().startswith(("Thumbs","!thumbs","/thumbs","-thumbs","thumbs")) and user.username in ["1DG1","ShoKytoo","ElCordobez"]:
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("thumbs", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫El usuario {target_username} no se encuentra en la sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido, usa los emotes desde 1 al 100")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !thumbs @user 1-10")

        if message.lower().lstrip().startswith(("Wave","!wave","/wave","-wave","wave")) and user.username in ["1DG1","ShoKytoo","ElCordobez"]:
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wave", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫El usuario {target_username} no se encuentra en la sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido, usa los emotes desde 1 al 100")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !wave @user 1-10")

        if message.lower().lstrip().startswith(("Clap","!clap","/clap","-clap","👏","clap")) and user.username in ["1DG1","ShoKytoo","ElCordobez"]:
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("clap", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫El usuario {target_username} no se encuentra en la sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido, usa los emotes desde 1 al 100")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !clap @user 1-10")

        if message.lower().lstrip().startswith(("Heart","!heart","/heart","-heart","❤️","heart")) and user.username in ["1DG1","ShoKytoo","ElCordobez"]:
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("heart", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫El usuario {target_username} no se encuentra en la sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido, usa los emotes desde 1 al 100")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !heart @user 1-10")

        if message.lower().lstrip().startswith(("Clap","!clap","/clap","-clap","👏","clap")): 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("clap", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫o usuário {target_username} não encontrado na sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido de reaçoes escolha um numero entre: 1-10")
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Apenas moderadores podem usar quantias acima de 10!")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !clap @user 1-10")

        if message.lower().lstrip().startswith(("Heart","!heart","/heart","-heart","❤️","heart")): 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("heart", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫o usuário {target_username} não encontrado na sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido de reaçoes escolha um numero entre: 1-10")
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Apenas moderadores podem usar quantias acima de 10!")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !heart @user 1-10")

        if message.lower().lstrip().startswith(("Wave","!wave","/wave","-wave","wave")): 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wave", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫o usuário {target_username} não encontrado na sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido de reaçoes escolha um numero entre: 1-10")
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Apenas moderadores podem usar quantias acima de 10!")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !wave @user 1-10")

        if message.lower().lstrip().startswith(("Thumbs","!thumbs","/thumbs","-thumbs","thumbs")): 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("thumbs", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫o usuário {target_username} não encontrado na sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido de reaçoes escolha um numero entre: 1-10")
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Apenas moderadores podem usar quantias acima de 10!")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !thumbs @user 1-10")

        if message.lower().lstrip().startswith(("Wink","!wink","/wink","-wink","😉","wink")): 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wink", target_user.id)
                      else:
                          await self.highrise.send_whisper(user.id,f"\n🚫o usuário {target_username} não encontrado na sala. ")
              else:
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Numero invalido de reaçoes escolha um numero entre: 1-10")
                  await self.highrise.send_whisper(user.id,f"\n🚫 {user.username} Apenas moderadores podem usar quantias acima de 10!")
          except ValueError:
              await self.highrise.send_whisper(user.id,f"🚫\n {user.username} Use: !wink @user 1-10")

        if message.lower().lstrip().startswith(("-wrong","-fashion","-gravity","-icecream","-casual","-kiss","-no","-yes","-laughing","-hello","-wave","-shy","-tired","-flirty","-flirtywave","-confused","-charging","-hot","-snowball","-curtsy","-bow","-model","-greedy","-snowangel","-pose7","-cute","-superpose","-frog","-snake","-eneryball","-maniac","-teleport","-float","-singing","-telekinesis","-sing","-singalong","-shuffle","-tiktok10","-tik10","-cutey","-pose5","-pose3","-pose1","-pose8","-blackpink","-dontstartnow","-tik2","-tiktok2","-pennywise","-russian","-shopping","-shop","-letsgoshopping","-enthused","-celebrate","-gagging","-flex","-cursing","-thumbsup","-angry","-punk","-zombie","-sit","-fight","-swordfight","-macarena","-weird","-savage","-tiktok8","-tik8","-viralgroove","-viral","-tik9","-tiktok9","-saunter","-astronaut","-penguin","-airguitar","-guitar","-boxer","-pose9","-stargazer","-star","-sayso","-uwu","-jetpack","-fairytwirl","-fairyfloat","-launch","-smooch","-tiktok","-attention","-salute","-pushit","-foryou","-gift","-touch","-kawaii","-repose","-surprise","-sleigh","-hyped","-jingle","-gottago","-time","-timejump","-party","-thumbsub","-scritchy","-skating","-bitnervous","-creepy","-bashful","-revelations","-watch")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: {parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return

                if message.lower().lstrip().startswith("-revelations"):
                        await self.highrise.send_emote("emote-headblowup'", user.id)
                        await self.highrise.send_emote("emote-headblowup'", user_id)

                if message.lower().lstrip().startswith("-bashful"):
                        await self.highrise.send_emote("emote-shy2", user.id)
                        await self.highrise.send_emote("emote-shy2", user_id)

                if message.lower().lstrip().startswith("-thumbsub"):
                        await self.highrise.send_emote("emoji-thumbsup", user.id)
                        await self.highrise.send_emote("emoji-thumbsup", user_id)

                if message.lower().lstrip().startswith("-scritchy"):
                        await self.highrise.send_emote("idle-wild", user.id)
                        await self.highrise.send_emote("idle-wild", user_id)

                if message.lower().lstrip().startswith("-bitnervous"):
                        await self.highrise.send_emote("idle-nervous", user.id)
                        await self.highrise.send_emote("idle-nervous", user_id)

                if message.lower().lstrip().startswith("-creepy"):
                        await self.highrise.send_emote("dance-creepypuppet", user.id)
                        await self.highrise.send_emote("dance-creepypuppet", user_id)

                if message.lower().lstrip().startswith("-party"):
                        await self.highrise.send_emote("emote-celebrate", user.id)
                        await self.highrise.send_emote("emote-celebrate", user_id)

                if message.lower().lstrip().startswith("-skating"):
                        await self.highrise.send_emote("emote-iceskating", user.id)
                        await self.highrise.send_emote("emote-iceskating", user_id)

                if message.lower().lstrip().startswith("-wrong"):
                        await self.highrise.send_emote("dance-wrong", user.id)
                        await self.highrise.send_emote("dance-wrong", user_id)

                if message.lower().lstrip().startswith("-fashion"):
                        await self.highrise.send_emote("emote-fashionista", user.id)
                        await self.highrise.send_emote("emote-fashionista", user_id)

                if message.lower().lstrip().startswith("-gravity"):              
                        await self.highrise.send_emote("emote-gravity", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)

                if message.lower().lstrip().startswith("-icecream"):
                        await self.highrise.send_emote("dance-icecream", user.id)
                        await self.highrise.send_emote("dance-icecream", user_id)

                if message.lower().lstrip().startswith("-casual"):
                        await self.highrise.send_emote("idle-dance-casual", user.id)
                        await self.highrise.send_emote("idle-dance-casual", user_id)

                if message.lower().lstrip().startswith("-kiss"):
                        await self.highrise.send_emote("emote-kiss", user.id)
                        await self.highrise.send_emote("emote-kiss", user_id)

                if message.lower().lstrip().startswith("-no"):
                        await self.highrise.send_emote("emote-no", user.id)
                        await self.highrise.send_emote("emote-no", user_id)

                if message.lower().lstrip().startswith("-sad"):
                        await self.highrise.send_emote("emote-sad", user.id)
                        await self.highrise.send_emote("emote-sad", user_id)

                if message.lower().lstrip().startswith("-yes"):
                        await self.highrise.send_emote("emote-yes", user.id)
                        await self.highrise.send_emote("emote-yes", user_id)

                if message.lower().lstrip().startswith("-laughing"):
                        await self.highrise.send_emote("emote-laughing", user.id)
                        await self.highrise.send_emote("emote-laughing", user_id)

                if message.lower().lstrip().startswith("-hello"):
                        await self.highrise.send_emote("emote-hello", user.id)
                        await self.highrise.send_emote("emote-hello", user_id)

                if message.lower().lstrip().startswith("-wave"):
                        await self.highrise.send_emote("emote-wave", user.id)
                        await self.highrise.send_emote("emote-wave", user_id)

                if message.lower().lstrip().startswith("-shy"):
                        await self.highrise.send_emote("emote-shy", user.id)
                        await self.highrise.send_emote("emote-shy", user_id)

                if message.lower().lstrip().startswith("-tired"):
                        await self.highrise.send_emote("emote-tired", user.id)
                        await self.highrise.send_emote("emote-tired", user_id)

                if message.lower().lstrip().startswith("-flirtywave"):
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                if message.lower().lstrip().startswith("-flirty"):
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                if message.lower().lstrip().startswith("-confused"):
                        await self.highrise.send_emote("emote-confused", user.id)
                        await self.highrise.send_emote("emote-confused", user_id)

                if message.lower().lstrip().startswith("-charging"):
                        await self.highrise.send_emote("emote-charging", user.id)
                        await self.highrise.send_emote("emote-charging", user_id)

                if message.lower().lstrip().startswith("-snowangel"):
                        await self.highrise.send_emote("emote-snowangel", user.id)
                        await self.highrise.send_emote("emote-snowangel", user_id)

                if message.lower().lstrip().startswith("-hot"):
                        await self.highrise.send_emote("emote-hot", user.id)
                        await self.highrise.send_emote("emote-hot", user_id)

                if message.lower().lstrip().startswith("-superpose"):
                        await self.highrise.send_emote("emote-superpose", user.id)
                        await self.highrise.send_emote("emote-superpose", user_id)

                if message.lower().lstrip().startswith("-frog"):
                        await self.highrise.send_emote("emote-frog", user.id)
                        await self.highrise.send_emote("emote-frog", user_id)

                if message.lower().lstrip().startswith("-cute"):
                        await self.highrise.send_emote("emote-cute", user.id)
                        await self.highrise.send_emote("emote-cute", user_id)

                if message.lower().lstrip().startswith("-pose7"):
                        await self.highrise.send_emote("emote-pose7", user.id)
                        await self.highrise.send_emote("emote-pose7", user_id)

                if message.lower().lstrip().startswith("-snake"):
                        await self.highrise.send_emote("emote-snake", user.id)
                        await self.highrise.send_emote("emote-snake", user_id)

                if message.lower().lstrip().startswith("-eneryball"):
                        await self.highrise.send_emote("emote-energyball", user.id)
                        await self.highrise.send_emote("emote-energyball", user_id)

                if message.lower().lstrip().startswith("-maniac"):
                        await self.highrise.send_emote("emote-maniac", user.id)
                        await self.highrise.send_emote("emote-maniac", user_id)

                if message.lower().lstrip().startswith("-teleport"):
                        await self.highrise.send_emote("emote-teleporting", user.id)
                        await self.highrise.send_emote("emote-teleporting", user_id)

                if message.lower().lstrip().startswith("-float"):
                        await self.highrise.send_emote("emote-float", user.id)
                        await self.highrise.send_emote("emote-float", user_id)

                if message.lower().lstrip().startswith("-telekinesis"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-telekinesis", user_id)

                if message.lower().lstrip().startswith("-snowball"):
                        await self.highrise.send_emote("emote-snowball", user.id)
                        await self.highrise.send_emote("emote-snowball", user_id)

                if message.lower().lstrip().startswith("-curtsy"):
                        await self.highrise.send_emote("emote-curtsy", user.id)
                        await self.highrise.send_emote("emote-curtsy", user_id)

                if message.lower().lstrip().startswith("-bow"):
                        await self.highrise.send_emote("emote-bow", user.id)
                        await self.highrise.send_emote("emote-bow", user_id)

                if message.lower().lstrip().startswith("-model"):
                        await self.highrise.send_emote("emote-model", user.id)
                        await self.highrise.send_emote("emote-model", user_id)

                if message.lower().lstrip().startswith("-greedy"):
                        await self.highrise.send_emote("emote-greedy", user.id)
                        await self.highrise.send_emote("emote-greedy", user_id)

                if message.lower().lstrip().startswith("-sing"):
                        await self.highrise.send_emote("idle_singing", user.id)
                        await self.highrise.send_emote("idle_singing", user_id)

                if message.lower().lstrip().startswith("-shuffle"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                if message.lower().lstrip().startswith("-singing"):
                        await self.highrise.send_emote("idle_singing", user.id)
                        await self.highrise.send_emote("idle_singing", user_id)

                if message.lower().lstrip().startswith("-singalong"):
                        await self.highrise.send_emote("idle_singing", user.id)
                        await self.highrise.send_emote("idle_singing", user_id)

                if message.lower().lstrip().startswith("-cutey"):
                        await self.highrise.send_emote("emote-cutey", user.id)
                        await self.highrise.send_emote("emote-cutey", user_id)

                if message.lower().lstrip().startswith("-tik10"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                if message.lower().lstrip().startswith("-tiktok10"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                if message.lower().lstrip().startswith("-pose5"):
                        await self.highrise.send_emote("emote-pose5", user.id)
                        await self.highrise.send_emote("emote-pose5", user_id)

                if message.lower().lstrip().startswith("-pose1"):
                        await self.highrise.send_emote("emote-pose1", user.id)
                        await self.highrise.send_emote("emote-pose1", user_id)

                if message.lower().lstrip().startswith("-pose8"):
                        await self.highrise.send_emote("emote-pose8", user.id)
                        await self.highrise.send_emote("emote-pose8", user_id)

                if message.lower().lstrip().startswith("-pose3"):
                        await self.highrise.send_emote("emote-pose3", user.id)
                        await self.highrise.send_emote("emote-pose3", user_id)

                if message.lower().lstrip().startswith("-blackpink"):
                        await self.highrise.send_emote("dance-blackpink", user.id)
                        await self.highrise.send_emote("dance-blackpink", user_id)

                if message.lower().lstrip().startswith("-dontstartnow"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                if message.lower().lstrip().startswith("-tik2"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                if message.lower().lstrip().startswith("-tiktok2"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                if message.lower().lstrip().startswith("-pennywise"):
                        await self.highrise.send_emote("dance-pennywise", user.id)
                        await self.highrise.send_emote("dance-pennywise", user_id)

                if message.lower().lstrip().startswith("-russian"):
                        await self.highrise.send_emote("dance-russian", user.id)
                        await self.highrise.send_emote("dance-russian", user_id)

                if message.lower().lstrip().startswith("-shopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                if message.lower().lstrip().startswith("-shop"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                if message.lower().lstrip().startswith("-letsgoshopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                if message.lower().lstrip().startswith("-enthused"):
                        await self.highrise.send_emote("idle-enthusiastic", user.id)
                        await self.highrise.send_emote("idle-enthusiastic", user_id)

                if message.lower().lstrip().startswith("-weird"):
                        await self.highrise.send_emote("dance-weird", user.id)
                        await self.highrise.send_emote("dance-weird", user_id)

                if message.lower().lstrip().startswith("-macarena"):
                        await self.highrise.send_emote("dance-macarena", user.id)
                        await self.highrise.send_emote("dance-macarena", user_id)

                if message.lower().lstrip().startswith("-swordfight"):
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                if message.lower().lstrip().startswith("-fight"):
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                if message.lower().lstrip().startswith("-celebrate"):
                        await self.highrise.send_emote("emoji-celebrate", user.id)
                        await self.highrise.send_emote("emoji-celebrate", user_id)

                if message.lower().lstrip().startswith("-gagging"):
                        await self.highrise.send_emote("emoji-gagging", user.id)
                        await self.highrise.send_emote("emoji-gagging", user_id)

                if message.lower().lstrip().startswith("-flex"):
                        await self.highrise.send_emote("emoji-flex", user.id)
                        await self.highrise.send_emote("emoji-flex", user_id)

                if message.lower().lstrip().startswith("-cursing"):
                        await self.highrise.send_emote("emoji-cursing", user.id)
                        await self.highrise.send_emote("emoji-cursing", user_id)

                if message.lower().lstrip().startswith("-thumbsup"):
                        await self.highrise.send_emote("emoji-thumbsup", user.id)
                        await self.highrise.send_emote("emoji-thumbsup", user_id)

                if message.lower().lstrip().startswith("-angry"):
                        await self.highrise.send_emote("emoji-angry", user.id)
                        await self.highrise.send_emote("emoji-angry", user_id)

                if message.lower().lstrip().startswith("-punk"):
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)

                if message.lower().lstrip().startswith("-zombie"):
                        await self.highrise.send_emote("emote-zombierun", user.id)
                        await self.highrise.send_emote("emote-zombierun", user_id)

                if message.lower().lstrip().startswith("-sit"):
                        await self.highrise.send_emote("idle-loop-sitfloor", user.id)
                        await self.highrise.send_emote("idle-loop-sitfloor", user_id)

                if message.lower().lstrip().startswith("-savage"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                if message.lower().lstrip().startswith("-tik8"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                if message.lower().lstrip().startswith("-tiktok8"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                if message.lower().lstrip().startswith("-sayso"):
                        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
                        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

                if message.lower().lstrip().startswith("-star"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)

                if message.lower().lstrip().startswith("-uwu"):
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await self.highrise.send_emote("idle-uwu", user_id)

                if message.lower().lstrip().startswith("-viral"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                if message.lower().lstrip().startswith("-viralgroove"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                if message.lower().lstrip().startswith("-tik9"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                if message.lower().lstrip().startswith("-penguin"):
                        await self.highrise.send_emote("dance-pinguin", user.id)
                        await self.highrise.send_emote("dance-pinguin", user_id)

                if message.lower().lstrip().startswith("-airguitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)

                if message.lower().lstrip().startswith("-guitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)

                if message.lower().lstrip().startswith("-boxer"):
                        await self.highrise.send_emote("emote-boxer", user.id)
                        await self.highrise.send_emote("emote-boxer", user_id)

                if message.lower().lstrip().startswith("-pose9"):
                        await self.highrise.send_emote("emote-pose9", user.id)
                        await self.highrise.send_emote("emote-pose9", user_id)

                if message.lower().lstrip().startswith("-stargazer"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)

                if message.lower().lstrip().startswith("-saunter"):
                        await self.highrise.send_emote("dance-anime", user.id)
                        await self.highrise.send_emote("dance-anime", user_id)

                if message.lower().lstrip().startswith("-astronaut"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                if message.lower().lstrip().startswith("-timejump"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user_id)

                if message.lower().lstrip().startswith("-time"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user_id)

                if message.lower().lstrip().startswith("-gottago"):
                        await self.highrise.send_emote("idle-toilet", user.id)
                        await self.highrise.send_emote("idle-toilet", user_id)

                if message.lower().lstrip().startswith("-jingle"):
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                        await self.highrise.send_emote("dance-jinglebell", user_id)

                if message.lower().lstrip().startswith("-jetpack"):
                        await self.highrise.send_emote("hcc-jetpack", user.id)
                        await self.highrise.send_emote("hcc-jetpack", user_id)

                if message.lower().lstrip().startswith("-fairytwirl"):
                        await self.highrise.send_emote("emote-looping", user.id)
                        await self.highrise.send_emote("emote-looping", user_id)

                if message.lower().lstrip().startswith("-fairyfloat"):
                        await self.highrise.send_emote("idle-floating", user.id)
                        await self.highrise.send_emote("idle-floating", user_id)

                if message.lower().lstrip().startswith("-smooch"):
                        await self.highrise.send_emote("emote-kissing-bound", user.id)
                        await self.highrise.send_emote("emote-kissing-bound", user_id)

                if message.lower().lstrip().startswith("-launch"):
                        await self.highrise.send_emote("emote-launch", user.id)
                        await self.highrise.send_emote("emote-launch", user_id)

                if message.lower().lstrip().startswith("-tiktok"):
                        await self.highrise.send_emote("dance-tiktok11", user.id)
                        await self.highrise.send_emote("dance-tiktok11", user_id)

                if message.lower().lstrip().startswith("-attention"):
                        await self.highrise.send_emote("emote-salute", user.id)
                        await self.highrise.send_emote("emote-salute", user_id)

                if message.lower().lstrip().startswith("-watch"):
                        await self.highrise.send_emote("emote-creepycute", user.id)
                        await self.highrise.send_emote("emote-creepycute", user_id)

                if message.lower().lstrip().startswith("-salute"):
                        await self.highrise.send_emote("emote-cutesalute", user.id)
                        await self.highrise.send_emote("emote-cutesalute", user_id)

                if message.lower().lstrip().startswith("-pushit"):
                        await self.highrise.send_emote("dance-employee", user.id)
                        await self.highrise.send_emote("dance-employee", user_id)

                if message.lower().lstrip().startswith("-foryou"):
                        await self.highrise.send_emote("emote-gift", user.id)
                        await self.highrise.send_emote("emote-gift", user_id)

                if message.lower().lstrip().startswith("-gift"):
                        await self.highrise.send_emote("emote-gift", user.id)
                        await self.highrise.send_emote("emote-gift", user_id)

                if message.lower().lstrip().startswith("-touch"):
                        await self.highrise.send_emote("dance-touch", user.id)
                        await self.highrise.send_emote("dance-touch", user_id)

                if message.lower().lstrip().startswith("-kawaii"):
                        await self.highrise.send_emote("dance-kawai", user.id)
                        await self.highrise.send_emote("dance-kawai", user_id)

                if message.lower().lstrip().startswith("-repose"):
                        await self.highrise.send_emote("sit-relaxed", user.id)
                        await self.highrise.send_emote("sit-relaxed", user_id)

                if message.lower().lstrip().startswith("-surprise"):
                        await self.highrise.send_emote("emote-pose6", user.id)
                        await self.highrise.send_emote("emote-pose6", user_id)

                if message.lower().lstrip().startswith("-sleigh"):
                        await self.highrise.send_emote("emote-sleigh", user.id)
                        await self.highrise.send_emote("emote-sleigh", user_id)

                if message.lower().lstrip().startswith("-hyped"):
                        await self.highrise.send_emote("emote-hyped", user.id)
                        await self.highrise.send_emote("emote-hyped", user_id)

    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:

        response = await self.highrise.get_messages(conversation_id)
        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            message = response.messages[0].content
            print (message)

        if message.lower().lstrip().startswith(("Ajuda","/ajuda","-help","ajuda","!help","Help","!ajuda","/help","help")):
            await self.highrise.send_message(conversation_id, f"Olá Prescisa de ajuda? 👋\n\nComandos livres:\n!wave @user 1-10\n!thumbs @user 1-10\n!wink @user 1-10\n!clap @user 1-10\n!heart @user 1-10\n/fly 0,0,0\n/tele @user\n/emotes\n/loop emote nome | /loop 1-98\n!follow")
            await self.highrise.send_message(conversation_id, f"\n\nJogos\n/play\n/pescar\n/rps pedra|papel|tesoura\n/amor\n/odio\n/loucura\n/casa cmg?\n/cantada\n/piada\n\nCardapios\n/cardapio1\n/cardapio2\n\nEmote com amigo\n-emote @user")
            await self.highrise.send_message(conversation_id, f"\n\nTodos os comandos são usados com caracteries especiais\n\nCaracteries: ! ou / ou -")
            await asyncio.sleep(10)
            await self.highrise.send_message(conversation_id, f"\nComandos de Administador:\n!wave @user 1-100\n!thumbs @user 1-100\n!clap @user 1-100\n!wink @user 1-100\n!heart @user 1-100\n!emote all emote\n/summom @user\n/fly @user 0,0,0\n!kick @user\n!wallet\n!fit 1-11\n!tipall [quantia]\n!tipme [quantia]")   
            await self.highrise.send_message(conversation_id, f"\n\nTodos os comandos são usados com caracteries especiais\n\nCaracteries: ! ou / ou -")


        if message.lower().lstrip().startswith(("!emotes","!emotes","/emotes","!emote list","!list","/list","!lista","/lista","/emote list")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"🕺🏻Lista de emotes gratis:\n\n1.wrong\n2.fashion\n3.gravity\n4.icecream\n5.casual\n6.kiss\n7.no\n8.sad\n9.yes\n10.laughing\n11.hello\n12.wave\n13.shy\n14.tired\n15.flirtywave\n16.greedy\n17.model\n18.bow\n19.curtsy")
            await self.highrise.send_message(conversation_id, f"\n20.snowball\n21.hot\n22.snowangel\n23.charging\n24.confused\n25.telekinesis\n26.float\n27.teleport\n28.maniac\n29.eneryball\n30.snake\n31.frog\n32.superpose\n33.cute\n34.pose7\n35.pose8\n36.pose1\n37.pose5\n38.pose3")
            await self.highrise.send_message(conversation_id, f"\n39.cutey\n40.shuffle\n41.singalong\n42.enthused\n43.letsgoshopping\n44.russian\n45.pennywise\n46.dontstartnow\n47.blackpink\n48.celebrate\n49.gagging\n50.flex\n51.cursing\n52.thumbsup\n53.angry\n54.punk\n55.zombie\n56.sit\n57.fight")
            await self.highrise.send_message(conversation_id, f"\n58.macarena\n59.weird\n60.savage\n61.viralgroove\n62.uwu\n63.sayso\n64.stargazer\n65.pose9\n66.boxer\n67.airguitar\n68.penguin\n69.astronaut\n70.saunter\n71.creepy\n72.watch\n73.revelations\n74.bashful\n75.arabesque\n76.party")
            await self.highrise.send_message(conversation_id, f"\n77.skating\n78.scritchy\n79.bitnervous\n80.timejump\n81.gottago\n82.jingle\n83.hyped\n84.sleigh\n85.surprise\n86.repose\n87.kawaii\n88.touch\n89.foryou\n90.pushit\n91.salute\n92.attention\n93.tiktok\n.94.smooch\n95.launch\n96.fairyfloat\n97.fairytwirl\n98.jetpack")

    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")

    async def teleporter(self, message: str)-> None:
        """
            Teleports the user to the specified user or coordinate
            Usage: /teleport <username> <x,y,z>
                                                                """
        #separates the message into parts
        #part 1 is the command "/teleport"
        #part 2 is the name of the user to teleport to (if it exists)
        #part 3 is the coordinates to teleport to (if it exists)
        try:
            command, username, coordinate = message.split(" ")
        except:

            return

        #checks if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break
        #if the user_id isn't defined, the user isn't in the room
        if "user_id" not in locals():

            return

        #checks if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = coordinate.split(",")
        except:

            return

        #teleports the user to the specified coordinate
        await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)

                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)

        # If no matching function is found
        return              


    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username == "ElCordobez":
            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "ElCordobez":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)

        if message.lower().startswith("!tipall ") and user.username == "ShoKytoo":
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.send_message(user.id, "💰Comando inválido!")
                  return
              # Checks if the amount is valid
              try:
                  amount = int(parts[1])
              except:
                  await self.highrise.chat("💰Quantidade inválida!")
                  return
              # Checks if the bot has the amount
              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount
              if bot_amount < amount:
                  await self.highrise.chat("💰Não há gorjetas suficientes")
                  return
              # Get all users in the room
              room_users = await self.highrise.get_room_users()
              # Check if the bot has enough funds to tip all users the specified amount
              total_tip_amount = amount * len(room_users.content)
              if bot_amount < total_tip_amount:
                  await self.highrise.chat("💰Não há gorjetas suficientes para dar a  todos! ")
                  return
              # Tip each user in the room the specified amount
              for room_user, pos in room_users.content:
                  bars_dictionary = {
                      10000: "gold_bar_10k",
                      5000: "gold_bar_5000",
                      1000: "gold_bar_1k",
                      500: "gold_bar_500",
                      100: "gold_bar_100",
                      50: "gold_bar_50",
                      10: "gold_bar_10",
                      5: "gold_bar_5",
                      1: "gold_bar_1"
                  }
                  fees_dictionary = {
                      10000: 1000,
                      5000: 500,
                      1000: 100,
                      500: 50,
                      100: 10,
                      50: 5,
                      10: 1,
                      5: 1,
                      1: 1
                  }
                  # Convert the amount to a string of bars and calculate the fee
                  tip = []
                  remaining_amount = amount
                  for bar in bars_dictionary:
                      if remaining_amount >= bar:
                          bar_amount = remaining_amount // bar
                          remaining_amount = remaining_amount % bar
                          for i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]
                  if total > bot_amount:
                      await self.highrise.chat("💰Não há gorjetas suficientes!")
                      return
                  for bar in tip:
                      await self.highrise.tip_user(room_user.id, bar)           
                      await self.highrise.chat(f"💰{room_user.username} Recebeu uma gorjeta de {amount} golds!")

        if              message.startswith("Carteira") or  message.startswith("Wallet") or    message.startswith("wallet") or       message.startswith("carteira"):
          if user.username == "ElCordobez":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"VALOR TOTAL : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("emote-blowkisses")

    async def on_user_move(self, user: User, pos: Position) -> None:
        print (f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} ha salido de la sala")
        await self.highrise.chat(f"Hasta la proxima @{user.username}! 😭")
        await self.highrise.send_emote("hcc-jetpack")