#!/usr/bin/python3
from random import random

class DiceRoller:
    @staticmethod
    def roll_dice(dice):
        # count = 0
        roll_sum = 0.0
        # while(count < dice):
        #     roll_sum += random()
        #     count += 1

        for die in range(dice):
            die = die
            roll_sum += random()


        return roll_sum / float(dice)
