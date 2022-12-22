n = int(input('Digite quantos números deseja na sequência: '))

def fibo(num):
  if num == 1 or num == 0:
    return 1
  else:
    result = fibo(num - 1) + fibo(num - 2)
    return result

for x in range(n):
  print(fibo(x))

