def windowMax(l, k):
	max = 0
	for i in range(len(l) - k + 1):
		max = l[i]
		for j in range(1, k):
			if l[i + j] > max:
				max = l[i + j]
		print(str(max) + " ", end="")

if __name__ == "__main__":
	l = list(map(int, input().split()))
	k = int(input())
	windowMax(l, k)