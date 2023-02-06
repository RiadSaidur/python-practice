def multiply(num1: str, num2: str) -> str:
  if '0' in [num1, num2]:
    return '0'

  result = [0] * (len(num1) + len(num2))
  num1, num2 = num1[::-1], num2[::-1]

  for i1 in range(len(num1)):
    for i2 in range(len(num2)):
      digit = int(num1[i1]) * int(num2[i2])
      result[i1+i2] += digit
      result[i1+i2+1] += result[i1+i2] // 10
      result[i1+i2] = result[i1+i2] % 10

  result, start = result[::-1], 0
  
  while start < len(result) and result[start] == 0:
    start += 1
  
  result = map(str, result[start:])

  return "".join(result)
  

# print(multiply(num1 = "2", num2 = "3"))
print(multiply(num1 = "123", num2 = "456"))