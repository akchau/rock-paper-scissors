""" Тесты различных сценариев для 3-x игроков """
import unittest

from src.core import Choice, PlayerChoice
from src.winner_determiner import ResData, WinnerDeterminer


class TestDetermine(unittest.IsolatedAsyncioTestCase):
    """ Различные кейсы с 2 и 3 пользователями """

    def test_good_case_1(self):
        """ Победа пользователя """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[PlayerChoice(player_choice=Choice.ROCK, player_number=2)]
        )
        self.assertEqual(res, ResData(is_winner=True, another_winners=[]))

    def test_good_case_2(self):
        """ Ничья - одинаковые символы """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[PlayerChoice(player_choice=Choice.PAPER, player_number=2)]
        )
        self.assertIsNone(res)

    def test_good_case_3(self):
        """  Проигрыш пользователя """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[PlayerChoice(player_choice=Choice.SCISSORS, player_number=2)]
        )
        self.assertEqual(res, ResData(is_winner=False, another_winners=[2]))

    def test_good_case_4(self):
        """ Победа пользователя вместе с другим пользователем """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[
                PlayerChoice(player_choice=Choice.ROCK, player_number=2),
                PlayerChoice(player_choice=Choice.PAPER, player_number=3)
            ]
        )
        self.assertEqual(res, ResData(is_winner=True, another_winners=[3]))

    def test_good_case_5(self):
        """ Ничья - все показали бумагу """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[
                PlayerChoice(player_choice=Choice.PAPER, player_number=2),
                PlayerChoice(player_choice=Choice.PAPER, player_number=3)
            ]
        )
        self.assertIsNone(res)

    def test_good_case_6(self):
        """ Пользователь проиграл вместе с другим пользователем """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[
                PlayerChoice(player_choice=Choice.SCISSORS, player_number=2),
                PlayerChoice(player_choice=Choice.PAPER, player_number=3)
            ]
        )
        self.assertEqual(res, ResData(is_winner=False, another_winners=[2]))

    def test_good_case_7(self):
        """ Ничья - все показали разные предметы """
        res = WinnerDeterminer().determine(
            user_choice=Choice.PAPER,
            players_choice=[
                PlayerChoice(player_choice=Choice.SCISSORS, player_number=2),
                PlayerChoice(player_choice=Choice.ROCK, player_number=3)
            ]
        )
        self.assertIsNone(res)
