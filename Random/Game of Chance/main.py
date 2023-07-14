# Read the input.
n = int(input())
a = list(map(int, input().split()))

# Compute the value of k.
k = 0
for i in range(1, n):
  if (n - i/2) & (i - 1) == 0:
    k = i
    break

# Simulate the tournament for each participant.
total_simulations = 0
wins = [0] * n

# Sort the participants by luckiness.
sorted_participants = sorted(range(k), key=lambda i: a[i], reverse=True)

# Simulate the tournament for the participants with the highest luckiness first.
for x in sorted_participants:
  # Compute the probability that the current participant wins the tournament.
  probability = 1.0
  for i in range(x + 1, k):
    a1 = a[sorted_participants[i]]
    a2 = a[sorted_participants[i - 1]]
    probability *= a1 / (a1 + a2)
  # Simulate the tournament until the probability is small enough.
  while probability >= 1e-9:
    total_simulations += 1
    if simulate_tournament(n, a, x):
      wins[x] += 1
    probability *= 0.5

# Print the probability of each participant winning the tournament.
for i in range(n):
  print(wins[i] / total_simulations)
