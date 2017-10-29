vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")

complete = False
while complete == False:
  print("")       
  words = input("Enter a sentence or a word:\n").lower().strip()
       
  number_of_consonants = sum(words.count(c) for c in consonants)
  number_of_vowels = sum(words.count(c) for c in vowels)    
  print("The String is" ,str(words).upper())
  print("")
  print(" Number of  Vowels     : ",number_of_vowels)
  print(" Number of  Consonants : ",number_of_consonants)
  break
