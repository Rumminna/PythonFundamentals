n = int(input())

positives = []
negatives = []

sum_negatives = 0

for _ in range(n):
    current_number = int(input())
    if current_number < 0:
        negatives.append(current_number)
        sum_negatives += current_number
    else:
        positives.append(current_number)

print(positives)
print(negatives)

print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

