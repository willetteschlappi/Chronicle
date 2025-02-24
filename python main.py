
#### main.py

```python
#!/usr/bin/env python3
import random

subjects = ["A brave knight", "An adventurous explorer", "A mysterious stranger", "A clever detective"]
verbs = ["discovered", "encountered", "lost", "found"]
objects = ["an ancient artifact", "a secret passage", "a hidden city", "a magical creature"]

def generate_story():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."

def main():
    print("Welcome to the Chronicle Project!")
    print("Here's your random short story:")
    print(generate_story())

if __name__ == "__main__":
    main()
