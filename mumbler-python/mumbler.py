def mumble_letters(letters):
  input = letters.strip()
  if len(input) == 0:
    return input
  i = 0
  output = input[i].upper()
  i += 1
  while i < len(input):
    output += "-"
    output += input[i].upper() + input[i].lower() * i
    i += 1
  return output
