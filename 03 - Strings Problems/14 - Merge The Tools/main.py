  def merge_the_tools(string, k):
  n = len(string)
  
  for i in range(0, n, k):
    result = ""
    segment = string[i : i+k]
    for char in segment:
      if char not in result:
        result += char
    print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
