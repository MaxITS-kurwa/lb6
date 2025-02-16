word = input("Введите слово: ")

s = int(input("Введите индекс s (s < k): "))
k = int(input("Введите индекс k (k > s): "))

modified_word = word[:s] + word[s+1:k] + word[s] + word[k+1:]

print("Измененное слово:", modified_word)