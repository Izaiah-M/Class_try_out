"""With our naive pattern search, we will:

-Iterate through each character of the text.
-For each character of the text, count the number of following characters that match the pattern.
-Check if that match count equals the length of the pattern.
-If the match count equals the length, then a pattern has been found!"""

def pattern_search(text, pattern):

  print("Input Text:", text, "Input Pattern:", pattern)

#   looping through the text
  for index in range(len(text)):
    print("Text Index:", index)

    match_count = 0

    # looping through the pattern
    for char in range(len(pattern)):
      print("Pattern Index:", char)

    #   Checking if the charchter at the given index of the pattern is equal to the character at the given index of the pattern
      if pattern[char] == text[index + char]:
        print("Matching index found")
        print("Match Count:", match_count)
        match_count += 1
      else:
        break

    # Checking if we have found the pattern by comparing the lengthn of the pattern to the match count
    if match_count == len(pattern):
      print(pattern, " found at index ", index)



text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)