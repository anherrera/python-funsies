def sierpinski(n):
	pattern = draw(n, 'L', 0)
	return pattern

def draw(n, pattern, idx):
	if idx == n:
		return pattern
	else:
		return draw(n, make_triangle(pattern), idx+1)

def make_triangle(pattern):
	output = pattern
	output += "\n"
	output += next_to_each_other(pattern)
	return output

def next_to_each_other(pattern):
	lines = pattern.splitlines()
	widest = len(max(lines, key=len)) + 1

	for idx, line in enumerate(lines):
		lines[idx] = line.ljust(widest) + lines[idx]

	return "\n".join(lines)


level0 = 'L'
assert sierpinski(0) == level0
print(sierpinski(0))

level1 = '''
L
L L
'''.strip()
assert sierpinski(1) == level1
print(sierpinski(1))

level2 = '''
L
L L
L   L
L L L L
'''.strip()
assert sierpinski(2) == level2
print(sierpinski(2))

level3 = '''
L
L L
L   L
L L L L
L       L
L L     L L
L   L   L   L
L L L L L L L L
'''.strip()
assert sierpinski(3) == level3
print(sierpinski(3))

level4 = '''
L
L L
L   L
L L L L
L       L
L L     L L
L   L   L   L
L L L L L L L L
L       L       L
L L     L L     L L
L   L   L   L   L   L
L L L L L L L L L L L L
L       L       L       L
L L     L L     L L     L L
L   L   L   L   L   L   L   L
L L L L L L L L L L L L L L L L
'''.strip()
assert sierpinski(3) == level3
print(sierpinski(3))