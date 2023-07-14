Let's call an array 𝑎 of odd length 2𝑚+1 (with 𝑚≥1) bad, if element 𝑎𝑚+1 is equal to the median of this array. In other words, the array is bad if, after sorting it, the element at 𝑚+1-st position remains the same.

Let's call a permutation 𝑝 of integers from 1 to 𝑛 anti-median, if every its subarray of odd length ≥3 is not bad.

You are already given values of some elements of the permutation. Find the number of ways to set unknown values to obtain an anti-median permutation. As this number can be very large, find it modulo 109+7.

Input
The first line contains a single integer 𝑡 (1≤𝑡≤104)  — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer 𝑛 (2≤𝑛≤106)  — the length of the permutation.

The second line of each test case contains 𝑛 integers 𝑝1,𝑝2,…,𝑝𝑛 (1≤𝑝𝑖≤𝑛, or 𝑝𝑖=−1)  — the elements of the permutation. If 𝑝𝑖≠−1, it's given, else it's unknown. It's guaranteed that if for some 𝑖≠𝑗 holds 𝑝𝑖≠−1,𝑝𝑗≠−1, then 𝑝𝑖≠𝑝𝑗.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 106.

Output
For each test case, output a single integer  — the number of ways to set unknown values to obtain an anti-median permutation, modulo 109+7.

Example

input
5
2
-1 -1
3
-1 -1 -1
4
1 2 3 4
6
-1 -1 3 4 -1 -1
8
-1 -1 -1 -1 -1 -1 -1 -1
output
2
4
0
1
316

Note
In the first test case, both [1,2] and [2,1] are anti-median.

In the second test case, permutations [1,3,2],[2,1,3],[2,3,1],[3,1,2] are anti-median. The remaining two permutations, [1,2,3], [3,2,1], are bad arrays on their own, as their median, 2, is in their middle.

In the third test case, [1,2,3,4] isn't anti-median, as it contains bad subarray [1,2,3].

In the fourth test case, the only anti-median array you can get is [5,6,3,4,1,2].