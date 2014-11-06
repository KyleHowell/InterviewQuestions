# An anagram is a word formed by rearranging the letters of another, like "topside" and "deposit". In some cases, there might be as many (or more) anagrams than there are characters, like "post", "spot", "stop" and "tops".
# Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and at least as many anagrams as there are letters.
# The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/share/dict/words.
# The output produced by your code should be in this format:
# emit, item, mite, time
# merit, miter, mitre, remit, timer
# reins, resin, rinse, risen, serin, siren
# inert, inter, niter, retin, trine
# inset, neist, snite, stein, stine, tsine

# To execute from command line:
# python anagrams.py /usr/share/dict/words 4
# To execute from interpreter:
# import anagrams
# anagrams.find_anagrams("/usr/share/dict/words", 4)

def find_anagrams(dictionary_path, word_length):
  from collections import defaultdict
  frequencies = defaultdict(list)
  with open(str(dictionary_path)) as file:
    for line in file:
      sorted_word = ''.join(sorted(line.lower().rstrip()))
      if len(sorted_word) >= word_length:
        frequencies[sorted_word].append(line.rstrip())
  for sorted_word, anagrams in frequencies.items():
    if len(anagrams) >= word_length:
      print ", ".join(anagrams)

if __name__ == "__main__":
    import sys
    find_anagrams(sys.argv[1], int(sys.argv[2]))
