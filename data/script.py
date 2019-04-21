
def yeet(fin, fout):
	with open(fin) as fin, open(fout, 'w') as fout:
		for line in fin:
			line = line[0] + 'TOP' + line[1:]
			fout.write(line)

for fin, fout in zip(['02-21.goldtags', '22.goldtags', '23.goldtags'], ['02-21.goldtags.fixed', '22.goldtags.fixed', '23.goldtags.fixed']):
	yeet(fin, fout)
