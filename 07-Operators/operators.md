In python Programming , operators are usually used to perform operations on variable and values.

-> Types of Operators in Python:

1. Arithmetic Operators -> + , - , /, \* , % .

2. Relational Operators -> <, > , <=, >=, == , !=, <>.

3. Logical Operators -> AND, OR, NOT.

4. Bitwise Operator -> &, ^, |, <<, >>, ~ .

5. Assignment Operator -> =, +=, -=, \*=, %=.

6. Identity Operators -> is, is not.

7. Membership Operators -> in, not in.

<!-- Precedency and Associativity of Operators -->

Operator Precedence:

This is used in an expression with more than one operator with different precedence to determine which operation to perform first.

🔥 Operator Precedence Order (High → Low):

1.  () # Parentheses
2.  \*\* # Power
3.  +x -x ~x # Unary operators
4.  - / // % # Multiply, Divide
5.  - -                  # Add, Subtract
6.  << >> # Bitwise Shift
7.  & # Bitwise AND
8.  ^ # Bitwise XOR
9.  | # Bitwise OR
10. == != > < >= <= # Comparison
11. not # Logical NOT
12. and # Logical AND
13. or # Logical OR
14. = += -= \*= ... # Assignment (lowest)

🔥 Super Short Trick

👉 Remember this sentence:

🧠 “B P U M A S B C L”

| Letter | Operator                 |     |
| ------ | ------------------------ | --- |
| **B**  | Brackets `()`            |     |
| **P**  | Power `**`               |     |
| **U**  | Unary `+ - ~`            |     |
| **M**  | Multiply `* / // %`      |     |
| **A**  | Add `+ -`                |     |
| **S**  | Shift `<< >>`            |     |
| **B**  | Bitwise `& ^             | `   |
| **C**  | Comparison               |     |
| **L**  | Logical `not → and → or` |     |

Operator Associativity:

If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. It can either be Left to Right or from Right to Left.

🔥 Associativity Rules
👉 Left to Right (most operators):

- - - / // % << >> & ^ | and or

👉 Right to Left:

\*\* # power
= += -= # assignment
not # logical NOT
