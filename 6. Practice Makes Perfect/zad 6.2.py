# Counts vowels in the text using a while loop

text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

index = 0
while index < len(text):
    if text[index] in vowels:
        vowel_count += 1
    index += 1

print(f"The number of vowels in the text is: {vowel_count}")



#ustawienie indeksu index = 0
#pętla while index < len(text) → przechodzenie po każdym znaku
#sprawdzenie, czy text[index] jest samogłoską
#zwiększenie licznika vowel_count += 1
#przesunięcie indeksu index += 1