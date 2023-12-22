array =  [1,1,1,1,1]
sequence = [1, 1, 1]

def isValidSubsquence(array, sequence):
  
  # newarray=[]
  # for seq in sequence:
  #   for arr in array:
  #     if arr == seq:
  #       newarray.append(arr)
  #       array.remove(arr)
  #       break

  # return True if newarray == sequence else False

# array =  [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
  seq_index = 0

  for arr in array:
    if seq_index == len(sequence):
      break
    if arr == sequence[seq_index]:
      seq_index += 1

  return seq_index == len(sequence)
  
print(isValidSubsquence(array=array, sequence=sequence))
