#!/usr/bin/python
# Boggle Solver
# Big bad boggle solver that will solve any properly formatted (square) boggle board (imported as csv)

from __future__ import print_function
import csv

def import_board(in_file):
	with open(in_file, 'rb') as csvfile:
		pre_board = []
		x_index = 0
		csv_rows = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in csv_rows:
			pre_board.append(row)
		this_board = [[0 for x in range((len(pre_board)))] for y in range(len(pre_board))]
		for row in pre_board:
			this_board[x_index] = row[0].split(',')
			x_index+=1
		return this_board
		
def import_dictionary(in_file):
	with open(in_file, 'rb') as dictfile:
		dict = dictfile.readlines()
		dict = [x.strip() for x in dict]
	return dict
	
def write_board(in_board):
	print("* " * (len(in_board[0])+2))
	for r in in_board:
		print("* ", end='')
		for c in r:
			print(str(c)+" ", end='')
		print("*")
	print("* " * (len(in_board[0])+2))	

def find_char(path, word, in_board):
	char = word[len(path)]
	neighbours = get_neighbours(path[-1], in_board)
	for c in neighbours:
		if len(path) == len(word):
			return path
		else:
			if in_board[c[0]][c[1]] == char and c not in path:
				if (len(path)+1) == len(word): return (path+[c])
				else:
					new_path = find_char((path+[c]), word, in_board)
					if len(new_path) == len(word) : return new_path
					else : return path			
	return path

def get_neighbours(index, in_board):
	neighbours = []
	n = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
	for nn in n:
		if ((0 <= (index[0]+nn[0]) < len(in_board[0])) and (0 <= (index[1]+nn[1]) < len(in_board[0]))) : neighbours.append([(index[0]+nn[0]),(index[1]+nn[1])])
	return neighbours

def find_in_board(word, in_board):
	path = []
	starting_points = []
	for x in range(len(in_board[0])):
		for y in range(len(in_board[0])):
			if in_board[x][y] == word[0] : starting_points.append([x,y])
	if len(starting_points) == 0 : return None
	for point in starting_points:
		path = find_char([point], word, in_board)
		if len(path) == len(word) : return path
		else : return None
	

def solve_board(dict_list, in_board):
	found_words = []
	for word in dict_list:
		found_path = find_in_board(word, in_board)
		if found_path != None : found_words.append(word)
	return found_words 

def score_board(words):
	score = 0
	for word in words:
		if len(word) == 3 or len(word) == 4 : score+=1
		elif len(word) == 5 : score+=2
		elif len(word) == 6 : score+=3
		elif len(word) == 7 : score+=5
		elif len(word) >= 8 : score+=11
	return score
	
board = import_board("testboard.csv")
dictionary = import_dictionary("dict1.txt")
write_board(board)
found = solve_board(dictionary, board)
print(found)
score = score_board(found)
print("Total score: "+str(score))
#word = find_in_board("ahead", board)
#print(word)
