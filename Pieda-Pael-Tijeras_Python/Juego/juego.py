import random
from colorama import Fore


def jvj(nombre1, nombre2):
    rounds_players=0
    j1_wins=0
    j2_wins=0
    j1_derrotas=0
    j2_derrotas=0
    j1_draw=0
    j2_draw=0

    while rounds_players<3:
        print()
        decision1=input("\nPiedra(1)\nPapel(2)\ntijera(3)\nElija una opción:")
        for x in range(100):
            print()
        decision2=input("Elija una opción: \nPiedra(1)\nPapel(2)\ntijera(3)\n")
        print()
        print(Fore.BLUE+"decision  de ",nombre1,":", decision1+Fore.RESET)
        print(Fore.RED+"decision  de ",nombre2,":", decision2+Fore.RESET)
        print()
        if decision1 == decision2:
            print(Fore.MAGENTA+"Empate, jueguen de nuevo."+Fore.RESET)
        elif (
            (decision1 == "piedra" and decision2 == "tijera")
            or (decision1 == "tijera" and decision2 == "papel")
            or (decision1 == "papel" and decision2 == "piedra")        
            or (decision1 == "1" and decision2 == "3")
            or (decision1 == "3" and decision2 == "2")
            or (decision1 == "2" and decision2 == "1")
        ):
            print(Fore.GREEN+nombre1+" a ganado la ronda"+Fore.RESET)
            j1_wins += 1
            j1_derrotas +=1
        else:
            print(Fore.GREEN+nombre2+" a ganado la ronda"+Fore.RESET)
            j2_wins += 1
            j2_derrotas +=1


        rounds_players += 1
        print(f"Resultados: {nombre1} : {j1_wins} - {j2_wins} : {nombre2}")
    # Determine the winner of the best-of-three
    if j1_wins > j2_wins:
        print(Fore.GREEN+"¡Felicidades! "+nombre1+Fore.RESET)


    elif j1_wins < j2_wins:
        print(Fore.GREEN+"¡Felicidades! "+nombre2+Fore.RESET)
    else:
        print(Fore.MAGENTA+"El juego terminó en empate."+Fore.RESET)
        j1_draw +=1
        j2_draw +=1

    def again():
            return input(Fore.CYAN+"¿Quieres jugar de nuevo? (s/n): "+Fore.RESET).lower() == 's'


    while True:
        again()
        if not again():
            break




def bot():
    def play_game():
        bot = ["piedra", "papel", "tijera"]
        user_wins = 0
        bot_wins = 0
        rounds_playes = 0


        while rounds_playes < 3:
            print()
            decision1 = input("elige entre piedra, papel o tijera: ")
            decision2 = random.choice(bot)


            print()
            print(Fore.BLUE+"lo que elegiste:", decision1+Fore.RESET)
            print()
            print(Fore.YELLOW+"lo que eligió el bot:", decision2+Fore.RESET)
            print()


            if decision1 == decision2:
                print(Fore.MAGENTA+"Empate, jueguen de nuevo."+Fore.RESET)
            elif (
                (decision1 == "piedra" and decision2 == "tijera")
                or (decision1 == "tijera" and decision2 == "papel")
                or (decision1 == "papel" and decision2 == "piedra")
            ):
                print(Fore.GREEN+"Ganaste esta ronda."+Fore.RESET)
                user_wins += 1
            else:
                print(Fore.RED+"Perdiste esta ronda."+Fore.RESET)
                bot_wins += 1


            rounds_playes += 1
            print(f"Resultados: Usuario {user_wins} - {bot_wins} Bot")


        # Determine the winner of the best-of-three
        if user_wins > bot_wins:
            print(Fore.GREEN+"¡Felicidades! Ganaste el juego."+Fore.RESET)
        elif user_wins < bot_wins:
            print(Fore.RED+"Lo siento, perdiste el juego."+Fore.RESET)
        else:
            print(Fore.MAGENTA+"El juego terminó en empate."+Fore.RESET)


    def play_again():
        return input(Fore.CYAN+"¿Quieres jugar de nuevo? (s/n): "+Fore.RESET).lower() == 's'


    while True:
        play_game()
        if not play_again():
            break


def inicio():
    usuarios = input("cuantos jugadores van a jugar(1 o 2): ")
    if usuarios == "1":
        bot()
    elif usuarios == "2":
        nombre1 = input("Usuario de player1: ")
        nombre2 = input("Usuario de player2: ")
        jvj(nombre1,nombre2)


#bloque pricipal
inicio()