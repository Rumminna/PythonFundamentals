n = int(input())
searched_word = input()

all_words = []
matches_words = []

for _ in range(n):
    current_word = input()
    all_words.append(current_word)
    if searched_word in current_word:
        matches_words.append(current_word)

print(all_words)
print(matches_words)

