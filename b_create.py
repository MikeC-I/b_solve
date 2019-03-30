#!/usr/bin/python
# Boggle board creator
# Can create an 'official' Boggle board (based on the actual letter dice in the official game) 
# or a random board where each space is randomly assigned a letter with equal distribution of any given size

import random
import string
import csv

def b_board():
	this_board = [[0 for x in range(4)] for y in range(4)]
	x_index = 0
	y_index = 0
	die1 = ["r","i","f","o","b","x"]
	die2 = ["i","f","e","h","e","y"]
	die3 = ["d","e","n","o","w","s"]
	die4 = ["u","t","o","k","n","d"]
	die5 = ["h","m","s","r","a","o"]
	die6 = ["l","u","p","e","t","s"]
	die7 = ["a","c","i","t","o","a"]
	die8 = ["y","l","g","k","u","e"]
	die9 = ["q","b","m","j","o","a"]
	die10 = ["e","h","i","s","p","n"]
	die11 = ["v","e","t","i","g","n"]
	die12 = ["b","a","l","i","y","t"]
	die13 = ["e","z","a","v","n","d"]
	die14 = ["r","a","l","e","s","c"]
	die15 = ["u","w","i","l","r","g"]
	die16 = ["p","a","c","e","m","d"]
	dies_left = [die1,die2,die3,die4,die5,die6,die7,die8,die9,die10,die11,die12,die13,die14,die15,die16]
	for x in range(4):
		for y in range(4):
			this_die = random.randint(0, (len(dies_left)-1))
			this_board[x_index][y_index] = dies_left[this_die][random.randint(0, 5)]
			del dies_left[this_die]
			#print(str(x_index) + " " + str(y_index) + " " + str(this_letter))
			y_index = y_index + 1
		x_index = x_index + 1
		y_index = 0
	return this_board
	
def r_board(size = 4):
	x_index = 0
	y_index = 0
	this_board = [[0 for x in range(size)] for y in range(size)]
	for x in range(size):
		for y in range(size):
			this_char = random.choice(string.ascii_lowercase)
			this_board[x_index][y_index] = this_char
			y_index = y_index + 1
		x_index = x_index + 1
		y_index = 0
	return this_board

def write_board(out_file, board):
	with open(out_file,"wb") as f:
			writer = csv.writer(f)
			writer.writerows(board)
	
write_board("testboard.csv",b_board())
