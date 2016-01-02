



"""
Takes in a string, which is tab separated and newline separated, and outputs
a graph, in a to-be-determined format. 
"""


# import marisa_trie as trie
from pytrie import SortedStringTrie as trie

from time import time

words = open('englishWords.txt', 'r')
wordlines = words.readlines()
wordlines = [l.strip() for l in wordlines]
one = [1 for i in xrange(len(wordlines))]
zipped = zip(wordlines, one)
T = trie(zipped)



def boardToGraph(board):
	rows = board.split('\n')
	matrix = [row.split('\t') for row in rows]
	if len(matrix) != 5 or len(matrix[0]) != 5:
		print matrix
		print "something is wrong"
		raise Exception("Something is wrong")

	node_set = set()
	node_dict = {}
	for i in range(25):
		d = {}
		r = i%5
		c=int(i/5)
		entry = matrix[r][c]
		d['id'] = i
		d['val'] = entry
		neighbors = set()
		rs = [p for p in [r-1,r,r+1] if p >=0 and p <5]
		cs = [p for p in [c-1,c,c+1] if p >=0 and p <5]
		for row in rs:
			for col in cs:
				if row==r and col==c:
					continue
				new_id = row + col*5
				neighbors.add(new_id)
		d['neighbors'] = neighbors
		node_dict[i]=d
	return node_dict



# graph = boardToGraph(input_string)
# print graph
# That works!


def is_prefix(string):

	result = (len(T.items(prefix=string)) != 0)
	# print "string: " + string + " is " + str(result)
	return result
	# return True
	# if len(string) <=8:
	# 	return True
	# return False

def is_word(string):
	has = T.has_key(string)
	# if has:
	# 	print string + " is a word"
	return has

def dfs(node_dict, string_so_far, ids_so_far, master_set):
	if len(string_so_far) >=4 and is_word(string_so_far):
		master_set.add(string_so_far)

	most_recent_id = ids_so_far[-1]
	this_node = node_dict[most_recent_id]
	neighbors = this_node['neighbors']
	new_neigbors = [n for n in neighbors if n not in ids_so_far]
	if len(new_neigbors) == 0:
		return
	if not is_prefix(string_so_far):
		return
	for bordering in new_neigbors:
		new_string_so_far = string_so_far + node_dict[bordering]['val']
		new_ids = list(ids_so_far)
		new_ids.append(bordering)
		dfs(node_dict, new_string_so_far, new_ids, master_set)
	return

def words_from_board(board):
	graph = boardToGraph(board)
	master_set = set()
	for i in range(25):
		print str(i)
		print "\n"
		node = graph[i]
		id_list = [i]
		string_so_far = node['val']
		dfs(graph, string_so_far, id_list, master_set)
		print master_set
		print "\n\n\n\n\n"
	return master_set


# input_string = "1a\t2a\t3a\t4a\t5a\n" +\
# 							 "1b\t2b\t3b\t4b\t5b\n" +\
# 							 "1c\t2c\t3c\t4c\t5c\n" +\
# 							 "1d\t2d\t3d\t4d\t5d\n" +\
# 							 "1e\t2e\t3e\t4e\t5e"

start = time()
input_string = "s\tt\te\tz\tz\n" +\
							 "z\tz\tv\tz\tz\n" +\
							 "z\te\ti\tz\tz\n" +\
							 "z\tm\ta\tz\tz\n" +\
							 "z\ta\tg\ti\tc"

s = words_from_board(input_string)

print "\n\n\n\n\n"
for i in s:
	print i


print "time taken is " + str(time() - start)


# print is_word("cereal")







	

