# Problem Statement 
**URL : [Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/7088c9ab-9067-4fa9-a55d-a3592164a940)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/a75dac63-2d11-447e-bbcb-393e726575de)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/845a6ac1-f11d-464a-bc38-a1ab92f5bf1a)



# Problem Solution 
```
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
```

### Code Explanation

This code generates a pattern using the letter 'H'. The pattern consists of a top cone, top pillars, a middle belt, bottom pillars, and a bottom cone. The alignment is done using the `rjust`, `ljust`, and `center` methods in Python.

#### Input

```
thickness = int(input()) # This must be an odd number
c = 'H'
``` 

-   `thickness`: The thickness of the pattern. It must be an odd number to ensure symmetry.
-   `c`: The character used to create the pattern, which is 'H'.

#### Top Cone


```
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
``` 

-   **Explanation**: This loop creates the top cone part of the pattern.
-   **Details**:
    -   `c*i`: Repeats the character `c`, `i` times.
    -   `.rjust(thickness-1)`: Right-aligns the repeated characters within a field width of `thickness-1`.
    -   `c`: Adds a single `c` in the middle.
    -   `.ljust(thickness-1)`: Left-aligns the repeated characters within a field width of `thickness-1`.
-   **Result**: This creates a triangle shape that grows in width with each iteration.

#### Top Pillars


```
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
```

-   **Explanation**: This loop creates the top pillars of the pattern.
-   **Details**:
    -   `c*thickness`: Repeats the character `c`, `thickness` times.
    -   `.center(thickness*2)`: Centers the repeated characters within a field width of `thickness*2`.
    -   `.center(thickness*6)`: Centers the repeated characters within a field width of `thickness*6`.
-   **Result**: This creates two columns of 'H' that are centered and have space between them.

#### Middle Belt


```
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
``` 

-   **Explanation**: This loop creates the middle belt of the pattern.
-   **Details**:
    -   `c*thickness*5`: Repeats the character `c`, `thickness*5` times.
    -   `.center(thickness*6)`: Centers the repeated characters within a field width of `thickness*6`.
-   **Result**: This creates a solid belt of 'H' characters in the middle.

#### Bottom Pillars


```
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
``` 

-   **Explanation**: This loop creates the bottom pillars of the pattern, similar to the top pillars.
-   **Details**:
    -   Same as the top pillars.
-   **Result**: This creates two columns of 'H' that are centered and have space between them.

#### Bottom Cone


```
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
``` 

-   **Explanation**: This loop creates the bottom cone of the pattern.
-   **Details**:
    -   `c*(thickness-i-1)`: Repeats the character `c`, `thickness-i-1` times.
    -   `.rjust(thickness)`: Right-aligns the repeated characters within a field width of `thickness`.
    -   `c`: Adds a single `c` in the middle.
    -   `.ljust(thickness)`: Left-aligns the repeated characters within a field width of `thickness`.
    -   The entire result is right-aligned again within a field width of `thickness*6`.
-   **Result**: This creates an inverted triangle shape that shrinks in width with each iteration, forming the bottom part of the pattern.

