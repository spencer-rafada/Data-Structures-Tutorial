# Trees

TODO: Insert Circuit with Turns Pictures

In Formula 1, there are different racing circuits they race on every weekend. In 2021, they raced on 21 circuits. Each circuits are unique. No turn is the same as the other! A lap is one full circuit in a race. Racers drive for a certain number of lap to finish the race.

In programming, similar to driving around a circuit, there is a technique we can use wherein a function calls itself. This is **recursion**.
```python
def drive_around():
    print("I feel the need, the Need for Speed.")
    drive_around()
```

However, this function will not stop calling itself and will print "I feel the needm the Need for Speed." forever. Python will eventually stop with a **RecursionError** because the function was called too many times. 

> Remember: In software, when a function is called, it is put in a [stack](1-queue.md). The stack is used to keep track of what function to go back to when the function finishes. In recursion, the stack piles up.

Recursion is a good technique to use without the use of loops. However, we have to avoid calling the function forever. There are two rules we have to follow to avoid calling the function forever.

1. Smaller Problem - we only call the function recursively on a smaller problem. Without this, our function will run forever.
2. Base Case - as we continue to call our function on a smaller problem, there must be a place to stop.

Applying these rules to the **drive_around** function, we have the modified code to keep track of how much laps are left to drive around the circuit:

```python
def drive_around(lap_count):
    if lap_count <= 36:
        print("Keep pushing.")
        print("Lap:", count+1)
