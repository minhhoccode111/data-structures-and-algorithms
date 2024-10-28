# Algorithmic Warmup

## Why study algorithms

- **Basic Idea**: Algorithms solve a range of computational problems, from straightforward tasks (like displaying text or copying files) to complex issues (like shortest path calculation).
- **Efficiency Importance**: Knowing the right algorithms improves program speed and usability, impacting how efficiently problems are solved.
- **Foundational Skills**: A strong understanding of algorithms is vital for tackling more advanced topics like AI, where solutions require both clarity and efficiency.
- **Mathematical Problem Solving**: Translating complex tasks into structured, solvable problems is a major component of algorithm design and analysis.

## Fibonacci numbers

#### Naive Algorithm

```
     | 0,                   n = 0,
Fn = | 1,                   n = 1,
     | F(n - 1) + F(n - 2), n > 1.
```

But this toooo slow because

If n = 100, then the callstack (`T(100)`) will be somewhere `2 * 10 ^ 20` to `2 * 10 ^ 30` (sextillion)

#### Efficient Algorithm

```
Imitate hand computation:
0, 1, 1, 2, 3, 5, 8 ...

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
...
```

This is more efficient because
If n = 100, then the callstack (`T(100)`) will be `202` (`T(100) = 2n + 2`)

## Greater Common Divisor

For integers, **a** and **b**, their _greatest common divisor_ or **gcd(a,b)** is the largest integer **d** so that **d** divides both **a** and **b**

#### Naive Algorithm

Runtime approximately a + b

Very slow for 20 digit numbers

```
best <- 0
for d from 1 to a + b:
    if d|a and d|b:
        best <- d
return best
```

#### Efficient Algorithm

Euclideam Algorithm

```
if b = 0
    return a
a' <- the remainder when a is divided by b
return EuclidGCD(b,a')
```

## Computing Runtimes

Problem

- Figuring out accurate runtime is a huge mess
- In practice, you might not even know some of these details

Goal

- Measure runtime without knowing these details
- Get results that work for large inputs

## Asymptotic notation

- Let us ignore messy details in analysis
- Produces clean answer
- Throws away a lot of practically useful information

## Big-O Notation

Common rules

- Multiplicative constants can be omitted
- Out of two polynomials, the one with larger degree grow faster
- Any polynomial grow slower than any exponential
- Any polylogarithm grow slower than any polynomial
- Smaller term can be ommited

## Algorithm Design is Hard

- Algorithms very general
- No generic procedure for designing good algorithms
- Finding good algorithms often required coming up with unique insights

## Levels of Design

- Naive Algorithm: Definition to algorithm. Slow
- Algorithm by the way of standard Tools: Standard techniques
- Optimize Algorithm: Improve existing algorithm
- Magic Algorithm: Unique insight
