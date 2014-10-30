=begin
An anagram is a word formed by rearranging the letters of another, like "topside" and "deposit". In some cases, there might be as many (or more) anagrams than there are characters, like "post", "spot", "stop" and "tops".
Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and at least as many anagrams as there are letters.
The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/share/dict/words.

The output produced by your code should be in this format:
emit, item, mite, time
merit, miter, mitre, remit, timer
reins, resin, rinse, risen, serin, siren
inert, inter, niter, retin, trine
inset, neist, snite, stein, stine, tsine

The first argument on the command line will be the path to your word list file. I would run this program like:
$ ruby anagram_solution.rb /usr/share/dict/words
=end

sorted_words = Hash.new{|hash, key| hash[key] = Array.new}
File.open(ARGV[0]).each_line do |word|
  sorted_words[word.delete("\n").downcase.chars.sort.join] << word.delete("\n") if word.delete("\n").length > 3
end

sorted_words.each do |sorted_word, anagrams|
  if (anagrams.length >= sorted_word.length)
    anagrams.each{|word| print "#{word} "}
    print "\n"
  end
end
