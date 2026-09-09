temperature = 28

if temperature > 35:
    print("It's scorching outside!")
elif temperature >= 25:
    print("It's a warm, sunny day.")  # This executes, skipping the rest
elif temperature >= 15:
    print("It's a bit cool.")
else:
    print("Brr, it's freezing!")