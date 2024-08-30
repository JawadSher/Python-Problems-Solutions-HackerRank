<h1 align='center'>Words - Score</h1>

## Problem Statement

**Problem URL :** [Words Score](https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/b4a70b73-09e7-4435-8dc0-4e6552acf966)
![image](https://github.com/user-attachments/assets/7a1f21fb-5e02-40bf-a2a0-ed559ba6590b)

## Problem Solution
```py
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))

```

## Problem Solution Explanation

Let's go through the code step by step:

### 1. `def is_vowel(letter):`
This line defines a function named `is_vowel` that takes a single parameter `letter`. The purpose of this function is to check whether a given letter is a vowel.

### 2. `return letter in ['a', 'e', 'i', 'o', 'u', 'y']`
This line returns a boolean value (`True` or `False`). It checks if the `letter` passed to the function is one of the vowels listed in the array `['a', 'e', 'i', 'o', 'u', 'y']`. If the letter is found in this list, the function returns `True`, indicating that the letter is a vowel; otherwise, it returns `False`.

### 3. `def score_words(words):`
This line defines another function called `score_words` that takes one parameter `words`. This parameter is expected to be a list of words (strings). The purpose of this function is to calculate and return a score based on the number of vowels in each word.

### 4. `score = 0`
Here, the variable `score` is initialized to `0`. This variable will be used to accumulate the total score for all the words in the list.

### 5. `for word in words:`
This is the start of a loop that iterates over each word in the list `words`. For each iteration, the current word is assigned to the variable `word`.

### 6. `num_vowels = 0`
Inside the loop, `num_vowels` is initialized to `0` for each word. This variable will be used to count the number of vowels in the current word.

### 7. `for letter in word:`
This is another loop that iterates over each letter in the current `word`. The loop assigns the current letter to the variable `letter`.

### 8. `if is_vowel(letter):`
This line checks if the current `letter` is a vowel by calling the `is_vowel` function defined earlier. If the letter is a vowel (`True`), the code inside the `if` block is executed.

### 9. `num_vowels += 1`
If the `letter` is a vowel, the `num_vowels` variable is incremented by 1. This counts the total number of vowels in the current word.

### 10. `if num_vowels % 2 == 0:`
After counting the vowels in the word, this line checks if the number of vowels is even. It does so by using the modulo operator (`%`), which returns the remainder when `num_vowels` is divided by 2. If the remainder is `0`, the number is even.

### 11. `score += 2`
If the number of vowels is even, `2` is added to the `score`.

### 12. `else:`
If the number of vowels is not even (i.e., odd), the code inside the `else` block is executed.

### 13. `score += 1`
If the number of vowels is odd, `1` is added to the `score`.

### 14. `return score`
After processing all the words in the list, the total `score` is returned as the output of the `score_words` function.

### 15. `n = int(input())`
This line reads an integer input from the user (presumably the number of words) and converts it from a string to an integer using `int()`. The integer is stored in the variable `n`, but in this particular code, `n` is not actually used.

### 16. `words = input().split()`
This line reads a line of input from the user, which is expected to be a series of words separated by spaces. The `split()` method splits the input string into a list of words, which is then stored in the variable `words`.

### 17. `print(score_words(words))`
Finally, this line calls the `score_words` function with the list `words` as an argument. The resulting score is printed to the console.
