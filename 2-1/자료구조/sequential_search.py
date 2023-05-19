def sequential_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1


if __name__ == "__main__":
    lst = [65, 22, 38, 4, 75, 6, 17, 8, 93, 10]
    x = 4
    result = sequential_search(lst, x)
    if result != -1:
        print(f"Found {x} at index {result}")
    else:
        print(f"{x} not found")

def ordered_sequential_search(lst, x):
    for i in range(len(lst)):
        if lst[i]==x:
            return i
        elif lst[i]>x:
            return -1
    return -1


if __name__ == "__main__":
  lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
  x = 5
  result = ordered_sequential_search(lst, x)
  if result != -1:
      print(f"Found {x} at index {result}")
  else:
      print(f"{x} not found")

