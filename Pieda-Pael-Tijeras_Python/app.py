import mysql.connector
import random
from colorama import Fore

# Conexion a la base de datos
conexion = mysql.connector.connect(
    user='root',
    password=' ',
    host='localhost',
    database='PaperRockTijera'
)

# Crear un objeto cursor para ejecutar comandos SQL
cursor = conexion.cursor()

#Modo de juego player vs player
def play_jvj():
    def jvj():
        #Solicitamos los nombres de los jugadores
        nombre1 = input("Usuario de player1: ")
        nombre2 = input("Usuario de player2: ")
        #Esta variable se encrga decontar las rondas
        rounds_players=0
        #Todas estas variables son para despues añadir los datos a la bd
        j1_wins=0
        j2_wins=0
        j1_defeat=0
        j2_defeat=0
        j1_draw=0
        j2_draw=0
        papel1=0
        piedra1=0
        tijera1=0
        papel2=0
        piedra2=0
        tijera2=0
        #Seran 3 rondas
        while rounds_players<3:
            print()
            
            #se lee la decision del j1
            decision1=input("Piedra(1)\nPapel(2)\ntijera(3)\n"+nombre1+" Elija una opción:")

            #esta amnera el proximo jugador no ve lo que elijio el j1
            for x in range(100):
                print()

            #se lee la decision del j2
            decision2=input("Piedra(1)\nPapel(2)\ntijera(3)\n"+nombre2+" Elija una opción: ")

            #Debido a que hay dos maneras de responder(con la palabra o el numero), necesiro que
            #la variable tenga la palabra para mas adelante
            if decision1=="1":
                decision1="Piedra"
                #se acumula las veces que a sido elegido esta opcion
                piedra1+=1

            elif decision1== "2":
                decision1="Papel"
                #se acumula las veces que a sido elegido esta opcion
                papel1+=1

            else: 
                decision1="Tijera"
                #se acumula las veces que a sido elegido esta opcion
                tijera1+=1

            #Lo mismo de anteriormente, solo que pera el j2
            if decision2=="1":
                decision2="Piedra"
                #se acumula las veces que a sido elegido esta opcion
                piedra2+=1

            elif decision2== "2":
                decision2="Papel"
                #se acumula las veces que a sido elegido esta opcion
                papel2+=1

            else: 
                decision2="Tijera"
                #se acumula las veces que a sido elegido esta opcion
                tijera2+=1
        
            print()

            #Imprecionde las desiciones de los jugadores, ademas tiene una decoracion visual.
            print(Fore.BLUE+"decision  de ",nombre1,":", decision1+Fore.RESET)
            print(Fore.RED+"decision  de ",nombre2,":", decision2+Fore.RESET)
            print()

            #comparamos las decisiones
            #si las dos decisiones son igaules la ronda queda en empate
            if decision1 == decision2:
                print(Fore.MAGENTA+"Empate, jueguen de nuevo."+Fore.RESET)
                #se almacena el empate
                j1_draw+=1
                j2_draw+=1
            #amediante los posibles casos, sabremos quien gano
            elif (
                (decision1 == "Piedra" and decision2 == "Tijera")
                or (decision1 == "Tijera" and decision2 == "Papel")
                or (decision1 == "Papel" and decision2 == "Piedra")        

            ):
                print(Fore.GREEN+nombre1+" a ganado la ronda"+Fore.RESET)
                #se almacena la vitoria y derrota de cada jugador
                j1_wins += 1
                j2_defeat +=1
            else:
                print(Fore.GREEN+nombre2+" a ganado la ronda"+Fore.RESET)
                #se almacena la vitoria y derrota de cada jugador
                j2_wins += 1
                j1_defeat +=1

            #se cuantea la ronda(1/3)
            rounds_players += 1
            #en el caso que un jugador halla ganado 2 rondas segidas
            if j1_wins==2 or j2_wins==2:
                rounds_players=5
    

            print(f"Resultados: {nombre1} : {j1_wins} - {j2_wins} : {nombre2}")
        # determinamos el ganador del las 3 rondas
        if j1_wins > j2_wins:
            print(Fore.GREEN+"¡Felicidades! "+nombre1+Fore.RESET)
            #se alamcena los nombres de los perdedores y gandores
            ganador=nombre1
            perdedor=nombre2
            empate="--"


        elif j1_wins < j2_wins:
            print(Fore.GREEN+"¡Felicidades! "+nombre2+Fore.RESET)
            #se alamcena los nombres de los perdedores y gandores
            ganador=nombre2
            perdedor=nombre1
            empate="--"
        else:
            print(Fore.MAGENTA+"El juego terminó en empate."+Fore.RESET)
            #se almacena el empate
            j1_draw +=1
            j2_draw +=1
            ganador="--"
            perdedor="--"
            empate="Empate"

        #añadiendo parametros en la tabla player
        sql_1 = "INSERT INTO player (nombre,wins,draw,defeat,piedra,papel,tijera) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        #dentro de la variables valores_1 estan todas las variables con la infromacion que emos almacenado durante esta ronda
        valores_1 = (nombre1, j1_wins, j1_draw, j1_defeat, piedra1, papel1, tijera1)
        #este objeto ejecutara el conmado de sql
        cursor.execute(sql_1, valores_1)
        
        sql_2 = "INSERT INTO player (nombre,wins,draw,defeat,piedra,papel,tijera) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        #dentro de la variables valores_1 estan todas las variables con la infromacion que emos almacenado durante esta ronda
        valores_2 = (nombre2, j2_wins, j2_draw, j2_defeat, piedra2, papel2, tijera2)
        #este objeto ejecutara el conmado de sql
        cursor.execute(sql_2, valores_2)

        #añadiendo parametros en la tabla partida
        sql_3="INSERT INTO Partida (Ganador, Perdedor, Empate) VALUES(%s, %s, %s)"
        #dentro de la variables valores_1 estan todas las variables con la infromacion que emos almacenado durante esta ronda
        valores_3= (ganador,perdedor, empate)
        #este objeto ejecutara el conmado de sql
        cursor.execute(sql_3, valores_3)

    #preguntamos si se volvera a jugar
    def again():
        return input(Fore.CYAN+"¿Quieres jugar de nuevo? (s/n): "+Fore.RESET).lower() == 's'

    #el while se ejecuta si again=="s"
    while True:
        jvj()
        if not again():
            break
    
#Modo de juego player vs bot
def bot():
    def play_game():
        #desiganmos las opciones del bot en una lista
        bot = ["piedra", "papel", "tijera"]
        #Esta variable se encrga decontar las rondas
        rounds_playes = 0
        #Todas estas variables son para despues añadir los datos a la bd
        user_wins = 0
        user_defeat = 0
        user_draw = 0
        bot_wins = 0
        bot_defeat = 0
        bot_draw = 0
        papel1=0
        piedra1=0
        tijera1=0
        papel2=0
        piedra2=0
        tijera2=0

        #Seran 3 rondas
        while rounds_playes < 3:
            print()
            #se lee la decision del j1
            decision1=input("\nPiedra(1)\nPapel(2)\ntijera(3)\nElija una opción:")

            #mediante un random se elijira la opcion del bot
            decision2 = random.choice(bot)

            #Debido a que hay dos maneras de responder(con la palabra o el numero), necesiro que
            #la variable tenga la palabra para mas adelante
            if decision1=="1":
                decision1="Piedra"
                #se acumula las veces que a sido elegido esta opcion
                piedra1+=1
            elif decision1== "2":
                decision1="Papel"
                #se acumula las veces que a sido elegido esta opcion
                papel1+=1

            else: 
                decision1="Tijera"
                #se acumula las veces que a sido elegido esta opcion
                tijera1+=1

            #Decision del bot
            if decision2=="piedra":
                #se acumula las veces que a sido elegido esta opcion
                piedra2+=1
            elif decision2== "papel":
                #se acumula las veces que a sido elegido esta opcion
                papel2+=1
            else:
                #se acumula las veces que a sido elegido esta opcion
                tijera2+=1
            #mostramos lo que el usuario elijio y el bot
            print()
            print(Fore.BLUE+"lo que elegiste:", decision1+Fore.RESET)
            print()
            print(Fore.YELLOW+"lo que eligió el bot:", decision2+Fore.RESET)
            print()


            #comparamos las decisiones
            #si las dos decisiones son igaules la ronda queda en empate
            if decision1 == decision2:
                print(Fore.MAGENTA+"Empate, jueguen de nuevo."+Fore.RESET)
                #se alamcena el empate
                user_draw+=1
                bot_draw+=1
            
            #amediante los posibles casos, sabremos quien gano
            elif (
                (decision1 == "Piedra" and decision2 == "Tijera")
                or (decision1 == "Tijera" and decision2 == "Papel")
                or (decision1 == "Papel" and decision2 == "Piedra")
            ):
                print(Fore.GREEN+"Ganaste esta ronda."+Fore.RESET)
                #se alamcena los nombres de los perdedores y gandores
                user_wins += 1
                bot_defeat +=1
            else:
                print(Fore.RED+"Perdiste esta ronda."+Fore.RESET)
                #se alamcena los nombres de los perdedores y gandores
                bot_wins += 1
                user_defeat +=1

            #se cuantea la ronda(1/3)
            rounds_players += 1
            #en el caso que un jugador halla ganado 2 rondas segidas
            if bot_wins==2 or user_wins==2:
                rounds_players=5
            print(f"Resultados: Usuario {user_wins} - {bot_wins} Bot")
        

        #Se determian el mejor de las 3 rondas
        if user_wins > bot_wins:
            print(Fore.GREEN+"¡Felicidades! Ganaste el juego."+Fore.RESET)
            #se alamcena los nombres de los perdedores y gandores
            ganador="Usuario"
            perdedor="Bot"
            empate="--"
        elif user_wins < bot_wins:
            print(Fore.RED+"Lo siento, perdiste el juego."+Fore.RESET)
            #se alamcena los nombres de los perdedores y gandores
            ganador="Bot"
            perdedor="Usuario"
            empate="--"
        else:
            print(Fore.MAGENTA+"El juego terminó en empate."+Fore.RESET)
            #se alamcena los nombres de los perdedores y gandores
            user_draw +=1
            bot_draw +=1
            ganador="--"
            perdedor="--"
            empate="Empate"
        #añadiendo parametros en la tabla player
        sql_1_bot= "INSERT INTO player (nombre,wins,draw,defeat,piedra,papel,tijera) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        #dentro de la variables valores_1 estan todas las variables con la infromacion que emos almacenado durante esta ronda
        valores_1_bot = ("usuario", user_wins, user_draw, user_defeat, piedra1, papel1, tijera1)
        #este objeto ejecutara el conmado de sql
        cursor.execute(sql_1_bot, valores_1_bot)
        
        sql_2_bot = "INSERT INTO player (nombre,wins,draw,defeat,piedra,papel,tijera) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        #dentro de la variables valores_1 estan todas las variables con la infromacion que emos almacenado durante esta ronda
        valores_2_bot = ("bot",bot_wins, bot_draw, bot_defeat, piedra2, papel2, tijera2)
        #este objeto ejecutara el conmado de sql
        cursor.execute(sql_2_bot, valores_2_bot)


        #añadiendo parametros en la tabla partida
        sql_3_bot="INSERT INTO Partida (Ganador, Perdedor, Empate) VALUES(%s, %s, %s)"
        #dentro de la variables valores_1 estan todas las variables con la infromacion que emos almacenado durante esta ronda
        valores_3_bot= (ganador,perdedor, empate)
        #este objeto ejecutara el conmado de sql
        cursor.execute(sql_3_bot, valores_3_bot)
    
    #preguntamos si se volvera a jugar
    def play_again():
        return input(Fore.CYAN+"¿Quieres jugar de nuevo? (s/n): "+Fore.RESET).lower() == 's'

    #el while se ejecuta si again=="s"
    while True:
        play_game()
        if not play_again():
            break
    
#Menu de inicio
def inicio():
    usuarios = input("cuantos jugadores van a jugar(1 o 2): ")
    if usuarios == "1":
        bot()
    elif usuarios == "2":
        play_jvj()


#ejecucion del juego
inicio()
# se utiliza para confirmar los cambios realizados en la base de datos y cerrar la conexión
conexion.commit()
conexion.close()



#       ---pruebas---
#cursor.execute("SELECT * FROM Partida")

# Obtener todos los resultados
#resultados = cursor.fetchall()

# Mostrar los resultados en la consola
#for resultado in resultados:
#    print(resultado)
# Confirmar los cambios y cerrar la conexión


