""" Модуль для определения победителей игры """
from dataclasses import dataclass
from src.core import Choice, PlayerChoice, play


@dataclass
class ResData:
    """ Результат игры """
    is_winner: bool
    another_winners: list[int]


class WinnerDeterminer:
    """ Определит победителя по результатам игры """

    def determine(self, user_choice: Choice, players_choice: list[PlayerChoice]):
        """ Метод определения победителей в игре """
        play_input = [player_choice.player_choice for player_choice in players_choice]
        play_input.append(user_choice)
        winner_choice = play(play_input)
        if winner_choice is None:
            return None
        another_winners = [
            player_choice.player_number
            for player_choice in players_choice
            if player_choice.player_choice == winner_choice and player_choice.player_number != 1
        ]
        return ResData(is_winner=user_choice == winner_choice, another_winners=another_winners)
