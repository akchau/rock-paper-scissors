""" Ядро игры для определения победителя """
import dataclasses
from enum import Enum


class Choice(Enum):
    """ Варианты ходов """
    PAPER = "paper"
    ROCK = "rock"
    SCISSORS = "scissors"



@dataclasses.dataclass
class PlayerChoice:
    """ Контейнер для хранения хода игрока """
    player_number: int
    player_choice: Choice


@dataclasses.dataclass
class RoundData:
    """ Контейнер для хранения ходов игроков в раунде """
    players_check: list[PlayerChoice]


__win_combinations = {
    Choice.PAPER: Choice.ROCK,
    Choice.ROCK: Choice.SCISSORS,
    Choice.SCISSORS: Choice.PAPER
}


def play(round_data: RoundData) -> None | Choice:
    """
    Выбор победившего хода
    Args:
        round_data (RoundData): Ходы игроков
    Raises:
        ValueError: Ошибка при валидации ходов
    Returns:
        None | Choice: Победивший ход или ничья если None
    """
    if len(round_data.players_check) < 2:
        raise ValueError("Недостаточное количество игроков")
    win_choice = round_data.players_check[0].player_choice
    one_comb = True
    for item in round_data.players_check[1:]:
        if item.player_choice == win_choice:
            continue
        if __win_combinations[item.player_choice] == win_choice:
            if not one_comb:
                return None
            win_choice = item.player_choice
        one_comb = False
    if one_comb:
        return None
    return win_choice
