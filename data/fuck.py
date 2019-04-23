import sys
f = sys.argv[1]
out = sys.argv[2]
out = open(out, 'w')
with open(f) as f:
	for line in f:
		line = line.strip()
		line = '(TOP ' + line + ')\n'
		out.write(line)
