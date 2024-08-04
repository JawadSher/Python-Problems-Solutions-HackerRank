# Problem Statement
**URL** : [The Minion Game](https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/f4d02b1a-4e45-4410-95df-a64df419ed5e)
![image](https://github.com/user-attachments/assets/57b33f93-5398-4281-a5c5-ed0c94a1122a)
![image](https://github.com/user-attachments/assets/093e0caf-e649-496b-a566-f4c0a99d91db)

# Problem Solution
```
def minion_game(string):
    vowels = "AEIOU"
    Kevin_score = 0
    Stuart_score = 0
    
    s_length = len(string)
    
    for i in range(s_length):
        if string[i] in vowels:
            Kevin_score += s_length - i
        else:
            Stuart_score += s_length - i
    
    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Kevin_score < Stuart_score:
        print("Stuart", Stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
```
## Source Code Explanation
1.  **Defining the Game Function**:
    

    
    `def minion_game(string):` 
    
2.  **Initialize Variables**:

    
    ```
    vowels = "AEIOU"
    Kevin_score = 0
    Stuart_score = 0
    ``` 
    
    -   `vowels`: A string containing all uppercase vowels.
    -   `Kevin_score`: Keeps track of Kevin's score.
    -   `Stuart_score`: Keeps track of Stuart's score.
3.  **Determine the Length of the Input String**:
    
   
    
    `s_length = len(string)` 
    
4.  **Calculate Scores**:

    
    ```
    for i in range(s_length):
        if string[i] in vowels:
            Kevin_score += s_length - i
        else:
            Stuart_score += s_length - i
       ``` 
    
    -   Iterate through each character in the string.
    -   If the character is a vowel, add the number of possible substrings starting with this character to Kevin's score.
    -   Otherwise, add the number of possible substrings starting with this character to Stuart's score.
5.  **Determine and Print the Winner**:

    
    ```
    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Kevin_score < Stuart_score:
        print("Stuart", Stuart_score)
    else:
        print("Draw")
	``` 
    
    -   Compare Kevin's and Stuart's scores.
    -   Print the winner and their score, or "Draw" if the scores are equal.
6.  **Main Function Execution**:
    

    
    ```
    if __name__ == '__main__':
        s = input()
        minion_game(s)
      ``` 
    
    -   This part ensures that the code runs when the script is executed directly.
    -   It takes input from the user and calls the `minion_game` function with that input.

## Example Output

For the input string `BANANA`:

-   Substrings starting with vowels: A, AN, ANA, ANAN, ANANA (Kevin's score).
-   Substrings starting with consonants: B, BA, BAN, BANA, BANAN, BANANA, N, NA, NAN, NANA (Stuart's score).

**Kevin's score**: 9
** Stuart's score**: 12

**Output**: `Stuart 12`

### Key Concepts for DSA Students

-   **String Manipulation**: Understanding how to work with strings and their indices.
-   **Counting Substrings**: Calculating the number of substrings starting with a specific character.
-   **Looping and Conditions**: Using loops and conditional statements to iterate through strings and make decisions based on character types (vowels or consonants).

This code provides a practical example of combining basic programming constructs to solve a problem involving strings, which is common in algorithm challenges.
