#!/usr/bin/env python3
import random
from colorama import init
from termcolor import colored
import time
init()
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
moves = ['rock', 'paper', 'scissors']
thegameStyles = ['rocker', 'random', 'reflect', 'cycle']
"""The Player class is the parent class for all of the Players
in this game"""
# Asma's Game


class My_Genius_Players:

    #  definning the players Moves:
    def __init__(self):
        self.my_challenger_move = random.choice(moves)
        self.my_last_move = random.choice(moves)
# we will start the Game with 0 Score.
        self.score = 0

    def move(self):

        return 'rock'
# definning the learn.
    def learn(self, my_move, theCH_move):

        self.my_challenger_move = theCH_move
        self.my_last_move = my_move
# We have(Random,Reflect,Cycle ,Rocker and human);defining their moves.
# 2/A player that chooses its moves randomly:


class RandomPlayerStar(My_Genius_Players):

    def move(self):
        return random.choice(moves)
# 4A player that cycles through the three moves :


class CyclePlayerTornado(My_Genius_Players):
    def move(self):
        if self.my_last_move == 'rock':
            return 'paper'
        elif self.my_last_move == 'paper':
            return 'scissors'
        else:
            return 'rock'
# 3Aplayer that remembers&imitates what humanP did in the previous round:


class ReflectPlayerWater(My_Genius_Players):

    def move(self):
        return self.my_challenger_move
# 5A player human
# If the player enters a move that is not valid;


class HumanPlayerPower(My_Genius_Players):

    def move(self):
        while(True):

            userinput = input(colored("your turn:  ", "yellow")).lower()
            if userinput in moves:
                return userinput
            else:
                print('Opps!try again!')
# definning the beats ;who will gets more points:


def beats(first, second):

    return ((first == 'rock' and second == 'scissors') or
            (first == 'scissors' and second == 'paper') or
            (first == 'paper' and second == 'rock'))
# definning the game class ;who is going to play


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
# defining what is going to happen in each Round(move,learn,beats&Score);

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

        if beats(move1, move2):
            print("")
            print(colored(" Nice Try,", "cyan"))
            print(
                "you wanna know who won, " +
                "I've already told you I've the baddest players ever!")
            time.sleep(2)
            print("")
            print(colored("player1 wins!yaaaay ,okay ", "blue"))
            self.player1.score += 1

        elif beats(move2, move1):
            print("")
            print(colored(" Nice Try,", "cyan"))
            print("you wanna know who won,")
            print("I've already told you I've the baddest players ever!")
            time.sleep(2)
            print("")
            print(colored("player2 wins!ohh,you got lucky,silly!", "blue"))
            self.player2.score += 1
        else:
            print("")
            print(colored(" Nice Try,", "cyan"))
            print("you wanna know who won, " +
                  "I've already told you I've the baddest players ever!")

            time.sleep(2)
            print("")
            print(colored("Tie,lets see who can break it!!", "red"))
# definningthe Game using loop
# (Game start,Round No,Game over,Scors&winner)in5rounds;
    def play_game(self):

        print("choose between;rock,paper or scissors:    ")
        print(colored("Game Start!,Here we Go Leaders!", "red"))
        print("")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
            print("")
            time.sleep(3)
            print(colored("The FINAL SCORE IS:", "green"))
            print(f"Player 1: {self.player1.score} " +
                  f"Player 2: {self.player2.score}")
            print(colored(
                "Life is either a daring adventure or nothing at all" +
                ",Try again.", "yellow"))
# print("It just a Game ! Thank you for playing with us!"
            print("")
            user_choice = input(
                colored("Do you dare to play again?" +
                        "(yes or No)", "red", "on_white"))
            if user_choice in ["Yes", "yes"]:
                pass
            elif user_choice in ["No", "no"]:
                break
            else:
                break
        if self.player1.score > self.player2.score:
            print("Player 1 Wins!!yaaaay ,okay!")
        elif self.player1.score < self.player2.score:
            print("Player 2 Wins!!ohhhhh,  you got lucky, silly!")
        else:
            print("OPPES!!NO WINNER! ,It must be my ex programmer's fault lol")


# The game should call each player's move method once in each round;
if __name__ == '__main__':

    while(True):

        thegameStyle = input(
            "Are you sure you want to challenge my baddest players " +
            "Give it a try, I dare you to win lol! :    ").lower()
        if thegameStyle in thegameStyles:
            break

    if thegameStyle == "rocker":
        game = Game(HumanPlayerPower(), My_Genius_Players())
    elif thegameStyle == "random":
        game = Game(HumanPlayerPower(), RandomPlayerStar())
    elif thegameStyle == "reflect":
        game = Game(HumanPlayerPower(), ReflectPlayerWater())
    else:
        game = Game(HumanPlayerPower(), CyclePlayerTornado())

    game.play_game()
