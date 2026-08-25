Hangman Bot

Goals:
1. Create a library of valid words, cutting out words with punctuation, abbreviation, profanity, etc.
2. Create an algorithm to weigh letters based on the following:
	a. Frequency of letter in any position
	b. Frequency of letter in certain positions
3. Using the weights from #2, construct a binary search tree for each word length (2, 3, 4...)
4. Reverse engineer this to find the most difficult word to solve based on its logic
   (to be used when bot is playing as the hangman) 
5. Make pretty U.I.
6. Create user input to allow the user to play either side of the game
7. Profit???


Sort trimmed-dict into length-based subdicts
Options:
1. For each word, store length of word and append word to subdict
	a. Windows: use "for line in f:"
