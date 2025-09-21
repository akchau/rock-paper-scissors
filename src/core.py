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


__win_combinations = {
    Choice.PAPER: Choice.ROCK,
    Choice.ROCK: Choice.SCISSORS,
    Choice.SCISSORS: Choice.PAPER
}


def play(round_data: list[Choice]) -> None | Choice:
    """
    Выбор победившего хода
    Args:
        round_data (RoundData): Ходы игроков
    Raises:
        ValueError: Ошибка при валидации ходов
    Returns:
        None | Choice: Победивший ход или ничья если None
    """
    if len(round_data) < 2:
        raise ValueError("Недостаточное количество игроков")
    win_choice = round_data[0]
    one_comb = True
    for item in round_data[1:]:
        if item == win_choice:
            continue
        if __win_combinations[item] == win_choice:
            if not one_comb:
                return None
            win_choice = item
        one_comb = False
    if one_comb:
        return None
    return win_choice
