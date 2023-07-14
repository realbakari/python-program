Here is the detailed algorithm to solve the problem:

For each test case, do the following:
Compute the number of permutations of length 𝑛 without any constraints, which is 𝑛!.

Iterate over all possible starting and ending indices of subarrays of odd length ≥3 in the permutation and check if the subarray contains the given values. If the subarray contains the given values, add it to the list of subarrays that contain the given values.

For each subarray that contains the given values, do the following:

Compute the number of permutations that contain the given subarray, but don't necessarily satisfy the anti-median condition. This can be done by computing the number of ways to fill in the remaining values in the permutation such that the given subarray is preserved.

Compute the number of permutations that contain the given subarray and satisfy the anti-median condition. For this, compute the number of ways to fill in the remaining values in the permutation such that the given subarray is preserved and the median of the subarray is the middle element of the subarray.

Subtract the sum of the number of permutations that contain each of the subarrays that contain the given values from the total number of permutations of length 𝑛 without any constraints.

Add the number of permutations that contain the given values and satisfy 
the anti-median condition.

Return the result modulo 109+7.

The above algorithm has time complexity O(𝑛^2), since we need to iterate over all possible subarrays of odd length ≥3 in the permutation and compute the number of permutations that contain each of these subarrays. This should be efficient enough to solve the problem within the given time limits.