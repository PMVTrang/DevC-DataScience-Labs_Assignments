#task1
if __name__ == '__main__':
    n = int(input())
    # your code here
    if n % 2 == 0:
      if n in range(2, 6) or n > 20:
        print("Not Weird")
      elif n in range(6, 21):
        print("Weird")
    else:
      print("Weird")

#task2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    # your code here
    print(a + b, a - b, a * b, sep = "\n")

#task3
if __name__ == '__main__':
    n = int(input())
    # your code here
    for i in range(n):
        print (i * i)

#task4
def is_leap(y):
	if(y % 4 == 0):
		if(y % 100 == 0):
			if(y % 400 == 0):
				return True
			else:
				return False
	return False

#task5
if __name__ == '__main__':#runner-up score == the second highest score
	n = int(input())
	a = []
	for i in range(n):
		a.append(int(input()))
	a.sort()
	#print(a[-2]) -> wont work if the first and second place are equal
	#the highest score appears a.count(a[-1]) times
	print(a[-a.count(a[-1]) - 1])
