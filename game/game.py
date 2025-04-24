from game.models import Player, Computer
from game.settings import GAME_LEVELS, GAME_LEVELS_CONVERT
from game.exceptions import InvalidInputError
from game.score import save_result
from datetime import datetime

def play_game():
    name = input("Введите ваше имя: ")
    print("Выберите уровень игры:")
    print("1 - Short (5 раундов)")
    print("2 - Medium (8 раундов)")
    print("3 - Long (10 раундов)")
    
    level = input("Ваш выбор (1/2/3): ")
    if level not in GAME_LEVELS:
        raise InvalidInputError("Ошибка: Неверный выбор уровня!")

    rounds = GAME_LEVELS[level]
    level_name = GAME_LEVELS_CONVERT[rounds]

    player = Player(name)
    computer = Computer()
    print(f"\nИгра начинается! Уровень: {level_name}, Раундов: {rounds}")
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    current_round = 1
    while current_round <= rounds:
        print(f"\nРаунд {current_round}:")
        
        while True:
            user_input = input('Кинуть кубик (нажмите "Enter"): ')
            if user_input != "":
                print('Бросок не сделан!!! Нажмите "Enter" для повторного броска.')
                continue

            player_roll = player.roll_dice()
            computer_roll = computer.roll_dice()

            print(f"Вы бросили кубик: 🎲 {player_roll}")
            print(f"Компьютер бросил кубик: 🎲 {computer_roll}")

            if player_roll > computer_roll:
                delta = player_roll - computer_roll
                player.update_score(delta)
                print(f"Вы выигрываете раунд! +{delta} очков")
                break
            elif computer_roll > player_roll:
                delta = computer_roll - player_roll
                player.update_score(-delta)
                print(f"Вы проигрываете раунд! -{delta} очков")
                break
            else:
                print("Ничья! Переброс кубиков...")

        current_round += 1

    print("\nИгра окончена!")
    print(f"Время начала: {start_time}")
    print(f"Игрок: {player.name}")
    print(f"Уровень: {level_name}")
    print(f"Итоговый счет: {player.score:+d}")
    
    save_result(player.name, rounds, player.score)