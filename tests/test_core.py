""" Тесты различных комбинаций для 3-x игроков """
import unittest

from src.core import Choice, play


class TestPlay(unittest.IsolatedAsyncioTestCase):
    """ Покрыты случаи для всех комбинаций для 3 игроков """

    async def test_bad_case_zero_players(self):
        """ Ноль игроков """
        with self.assertRaises(ValueError):
            play(round_data=[])

    async def test_bad_case_one_player(self):
        """ Один игрок """
        with self.assertRaises(ValueError):
            play([Choice.PAPER])

    async def test_good_case_simple_1(self):
        """ Победа первого """
        res = play([Choice.PAPER, Choice.ROCK])
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_simple_2(self):
        """ Победа второго """
        res = play(round_data=[Choice.ROCK, Choice.PAPER])
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_simple_3(self):
        """ Победа первого """
        res = play([Choice.SCISSORS, Choice.ROCK])
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_simple_4(self):
        """ Победа второго """
        res = play([Choice.ROCK, Choice.SCISSORS])
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_simple_5(self):
        """ Победа первого """
        res = play([Choice.SCISSORS, Choice.ROCK])
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_simple_6(self):
        """ Победа второго """
        res = play([Choice.SCISSORS, Choice.PAPER])
        self.assertEqual(res, Choice.SCISSORS)

    async def test_good_case_simple_7(self):
        """ Ничья - одинаковые знаки у двух игроков """
        res = play([Choice.PAPER, Choice.PAPER])
        self.assertEqual(res, None)

    async def test_good_case_simple_8(self):
        """ Ничья - одинаковые знаки у двух игроков """
        res = play([Choice.SCISSORS, Choice.SCISSORS])
        self.assertEqual(res, None)

    async def test_good_case_9(self):
        """ Победа - два ножниц, один бумага → побеждают ножницы (SSP) """
        res = play([Choice.SCISSORS, Choice.SCISSORS, Choice.PAPER])
        self.assertEqual(res, Choice.SCISSORS)

    async def test_good_case_10(self):
        """ Победа - два бумаги, один ножницы → побеждают ножницы (PPS) """
        res = play([Choice.PAPER, Choice.PAPER, Choice.SCISSORS])
        self.assertEqual(res, Choice.SCISSORS)

    async def test_good_case_11(self):
        """ Победа - два камня, один бумага → побеждает бумага (дубль test_good_case_8) """
        res = play([Choice.ROCK, Choice.ROCK, Choice.PAPER])
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_12(self):
        """ Победа - два ножниц, один камень → побеждает камень (SSR) """
        res = play([Choice.SCISSORS, Choice.SCISSORS, Choice.ROCK])
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_13(self):
        """ Ничья - все три игрока выбрали бумагу (PPP) """
        res = play([Choice.PAPER, Choice.PAPER, Choice.PAPER])
        self.assertEqual(res, None)

    async def test_good_case_14(self):
        """ Ничья - все три игрока выбрали камень (RRR) """
        res = play([Choice.ROCK, Choice.ROCK, Choice.ROCK])
        self.assertEqual(res, None)

    async def test_good_case_15(self):
        """ Ничья - все три игрока выбрали ножницы (SSS) """
        res = play([Choice.SCISSORS, Choice.SCISSORS, Choice.SCISSORS])
        self.assertEqual(res, None)
