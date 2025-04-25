from game.game import play_game
from game.score import get_results
from game.exceptions import InvalidInputError

def main():
    while True:
        print("\nДобро пожаловать в игру 'Кости'!")
        print("1 - Играть")
        print("2 - Посмотреть результаты")
        print("3 - Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                play_game()
            except InvalidInputError as e:
                print(e)
        elif choice == "2":
            get_results()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()