""" Тесты различных комбинаций для 3-x игроков """
import unittest

from core import Choice, play, PlayerChoice, RoundData


class TestPlay(unittest.IsolatedAsyncioTestCase):
    """ Покрыты случаи для всех комбинаций для 3 игроков """

    async def test_bad_case_zero_players(self):
        """ Ноль игроков """
        with self.assertRaises(ValueError):
            play(
                round_data=RoundData(
                    players_check=[]
                )
            )

    async def test_bad_case_one_player(self):
        """ Один игрок """
        with self.assertRaises(ValueError):
            play(
                round_data=RoundData(
                    players_check=[
                        PlayerChoice(player_number=1, player_choice=Choice.PAPER)
                    ]
                )
            )

    async def test_good_case_simple_1(self):
        """ Победа первого """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_simple_2(self):
        """ Победа второго """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_simple_3(self):
        """ Победа первого """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_simple_4(self):
        """ Победа второго """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS)
                ]
            )
        )
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_simple_5(self):
        """ Победа первого """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_simple_6(self):
        """ Победа второго """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, Choice.SCISSORS)

    async def test_good_case_simple_7(self):
        """ Ничья - одинаковые знаки у двух игроков """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_simple_8(self):
        """ Ничья - одинаковые знаки у двух игроков """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_simple_9(self):
        """ Ничья - одинаковые знаки у двух игроков """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_1(self):
        """ Ничья - в игре 3 разных знака """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=3, player_choice=Choice.SCISSORS)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_2(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=3, player_choice=Choice.SCISSORS)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_3(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=3, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_4(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=3, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_5(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=3, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, None)


    async def test_good_case_6(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=3, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_7(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=3, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_8(self):
        """ Ничья - в игре 3 разных знака. """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=3, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_9(self):
        """ Победа - два ножниц, один бумага (SSP) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=3, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, Choice.SCISSORS)

    async def test_good_case_10(self):
        """ Ничья - два бумаги, один ножницы (PPS) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=3, player_choice=Choice.SCISSORS)
                ]
            )
        )
        self.assertEqual(res, Choice.SCISSORS)

    async def test_good_case_11(self):
        """ Ничья - два камня, один бумага (RRP) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=3, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, Choice.PAPER)

    async def test_good_case_12(self):
        """ Ничья - два ножниц, один камень (SSR) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=3, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, Choice.ROCK)

    async def test_good_case_13(self):
        """ Ничья - все три игрока выбрали бумагу (PPP) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=2, player_choice=Choice.PAPER),
                    PlayerChoice(player_number=3, player_choice=Choice.PAPER)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_14(self):
        """ Ничья - все три игрока выбрали камень (RRR) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=2, player_choice=Choice.ROCK),
                    PlayerChoice(player_number=3, player_choice=Choice.ROCK)
                ]
            )
        )
        self.assertEqual(res, None)

    async def test_good_case_15(self):
        """ Ничья - все три игрока выбрали ножницы (SSS) """
        res = play(
            round_data=RoundData(
                players_check=[
                    PlayerChoice(player_number=1, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=2, player_choice=Choice.SCISSORS),
                    PlayerChoice(player_number=3, player_choice=Choice.SCISSORS)
                ]
            )
        )
        self.assertEqual(res, None)
