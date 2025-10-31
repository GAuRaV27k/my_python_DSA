def iterate_2d_array(arr):
    for row in arr:
        for item in row:
            yield item

if __name__ == '__main__':
    for x in iterate_2d_array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        print(x)

'''🍳 1️⃣ Normally: return gives one value and ends

When you use return, the function stops forever.

Example:

def numbers():
    return 1
    return 2  # ❌ never runs


Output:

print(numbers())  # → 1


It just returns once and dies.

⚙️ 2️⃣ But yield is special

When you use yield, your function becomes a generator —
it remembers where it left off, and you can get the next value later.

Example:

def numbers():
    yield 1
    yield 2
    yield 3


Now you can do:

for x in numbers():
    print(x)


Output:

1
2
3

🔁 3️⃣ It doesn’t end — it pauses

Each time you call next() on it, it continues from where it paused.

t = numbers()
next(t)  # 1
next(t)  # 2
next(t)  # 3
next(t)  # ❌ StopIteration (done)

💡 4️⃣ Why it’s used here

In your class:

for row in self.matrix:
    yield from row


This means:

For each row, go through every element inside it,
and yield one number at a time.

So instead of returning a big list, it gives you values one-by-one when needed.

✅ Advantage:

Uses less memory (no full list stored)

You can loop, sum, or sort directly

It works like a stream of values

🧠 5️⃣ Quick analogy

Think of:

return = “Give everything now and quit.”

yield = “Give one thing at a time, I’ll wait for you to ask for the next.”'''