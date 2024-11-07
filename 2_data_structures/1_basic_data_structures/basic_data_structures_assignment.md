# Basic Data Structures Assignment

1. Which of the basic data structures is the most suitable if you need to access its elements by their positions in O(1)O(1) time (this is called random access)?

- Array

2. Which of the basic data structures is the most suitable if you want to be able to insert elements in the middle in O(1)O(1)?

- List

Correct! Inserting an element after an existing element in a list is O(1)O(1), even if it is in the middle of the list.

3. Which of the basic data structures is the most suitable if you only need to insert the elements in the back and to extract elements from the front?

- Queue

4. Which of the basic data structures is the most suitable if you only need to implement recursion in a programming language? When you make a recursive call, you need to save the function you are currently in and its parameters values in some data structure, so that when you go out of the recursion you can restore the state. When you go out of the recursive call, you will always need to extract the last element that was put in the data structure.

- Stack

Correct! You put the function and its parameters values on the stack when you make recursive call, and you remove the top element of the stack when you go out of the recursive call. Stack is LIFO - last in first out, so you will always extract the last element that was put on the stack.
Status: [object Object]

5. Which of the basic data structures is the most suitable if you need to store the directory structure on your hard drive?

- Tree

Correct! The directory structure is a tree, so it is good to store it as a tree data structure.
