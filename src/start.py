import random
from src.core import Choice, PlayerChoice
from src.winner_determiner import WinnerDeterminer


choices = {
    1: Choice.ROCK,
    2: Choice.SCISSORS,
    3: Choice.PAPER
}


choices_verbose = {
    Choice.ROCK: "Камень",
    Choice.SCISSORS: "Ножницы",
    Choice.PAPER: "Бумага"
}


def generate_players(num_players) -> list[PlayerChoice]:
    """ Генерация игроков и их случайного выбора """
    players: list[PlayerChoice] = []
    for num_player in range(num_players-1):
        player_choice = PlayerChoice(player_number=num_player+2, player_choice=choices[random.randint(1, 3)])
        print(f"Пользователь {player_choice.player_number} выбрал {choices_verbose[player_choice.player_choice]}")
        players.append(player_choice)
    return players


def start_game(num_players: int):
    """ Запуск игры """
    try:
        choice_num = int(input("Игра началась: Выберите:\nКАМЕНЬ-1\nНОЖНИЦЫ-2\nБУМАГА-3\nВаш выбор: "))
    except ValueError:
        print("Вы указали количество пользователей в неверном формате")
        return
    if 1 <= choice_num <= 3:
        user_choice = choices[choice_num]
        print(f"Пользователь ВЫ выбрал - {choices_verbose[user_choice]}")
        players_choices = generate_players(num_players)
        game_res = WinnerDeterminer().determine(user_choice=user_choice, players_choice=players_choices)
        
        if game_res is None:
            print("Ничья")
            return
        if game_res.is_winner:
            print(f"Вы победили! Другие победители {game_res.another_winners}")
        else:
            print(f"Вы проиграли! Победили {game_res.another_winners}")
    else:
        print("Вы выбрали невалидное значение. Выберите значение в диапазоне от 1 до 3")

def main():
    print("Запускам игру \"Камень-Ножницы-Бумага!\"")
    try:
        num_players = int(input("Укажите количество игроков от 2 до 6: "))
    except ValueError:
        print("Вы указали количество пользователей в неверном формате")
        return
    if 2 <= num_players <= 6:
        start_game(num_players)
    else:
        print("Вы указали неверное количество игроков. Доступно от 2 до 6 игроков")