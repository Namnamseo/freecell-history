import argparse
import os
from os import path

parser = argparse.ArgumentParser(description='Freecell history manager.')
parser.add_argument('--check', '-c', action='store_true',
	help='Check this game.')
parser.add_argument('--add', '-a',  action='store_true',
	help='Add this game to the history')
parser.add_argument('number', type=int,
	help='Corresponding game number.')


args = parser.parse_args()

adding = args.add
checking = args.check
n = args.number

s = '%07d' % n
fdir  = s[:3]
ffile = s[3:5] + '.txt'
fpath = path.join(fdir, ffile)

def getFile(ind, mode):
	return open(fpath, mode)

def readData(ind):
	if not path.isfile(fpath):
		return []
	f = getFile(ind, 'r')
	dat = f.read().strip().split('\n')
	f.close()
	return dat

if adding and checking:
	print("You can't specify both.")
elif not adding and not checking:
	print("You have to specify one of them.")
else:
	cur_ind = '%02d' % (n%100)
	data = readData(n)
	if cur_ind in data:
		print("You've already played that game.")
	elif adding:
		data.append(cur_ind)
		data = sorted(data)
		if not path.isdir(fdir):
			os.mkdir(fdir)
		f = getFile(n, 'w')
		f.write('\n'.join(data))
		f.close()
		print('Successfully wrote : %s' % fpath)
		print('Content : ' + ' '.join(data))