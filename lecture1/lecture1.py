def computeEditDistance(s,t):
	cache = {} # (m,n) => result
	def recurse(m,n):
		"""
		return the minimun edit distance between:
		- first m letters of s
		- first n letters of t
		"""
		
		if (m,n) in cache:
			return cache[(m,n)]
		if m == 0: # base case
			result = n
		elif n == 0: # base case
			result = n
		elif s[m-1] == t[n-1]: 
			result = recurse(m-1,n-1)
		else:
			subCost = 1 + recurse(m-1, n-1)
			delCost = 1 + recurse(m-1,n)
			insCost = 1 + recurse(m, n-1)
			result = min(subCost, delCost, insCost)
		cache[(m,n)] = result
		return result

	return recurse(len(s),len(t))

# print(computeEditDistance('a cat!' *10,'the cats!' * 10))

points = [(2,4), (4,2)]
def F(w):
	return sum((w * x -y) **2 for x, y in points)

def dF(w):
	return sum( 2 * (w * x -y)  * x for x, y in points)

w = 0
eta = 0.01
for t in range(1000):
	value = F(w)
	gradient = dF(w)
	w = w - eta * gradient
	print('interation {} : w = {}, F(w) = {}'.format(t, w, value))