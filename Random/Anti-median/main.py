# Compute the factorial of a number using dynamic programming.
def factorial(n):
    # Store the factorials in a dictionary for memoization.
    factorials = {}

    # Compute the factorial of the given number.
    result = 1
    for i in range(2, n + 1):
        if i not in factorials:
            factorials[i] = i * factorials[i - 1]
        result *= factorials[i]

    # Return the result.
    return result

# Compute the number of anti-median permutations for the given permutation.
def anti_median_permutation(n, p):
    # Compute the number of permutations of length n without any constraints,
    # which is n!
    result = factorial(n)

    # Iterate over all possible starting and ending indices of subarrays of
    # odd length >= 3 in the permutation and check if the subarray contains
    # the given values. If the subarray contains the given values, add it to
    # the list of subarrays that contain the given values.
    subarrays = []
    for i in range(1, n - 2):
        for j in range(i + 2, n):
            if all(p[k] != -1 for k in range(i, j + 1)):
                subarrays.append((i, j))

    # For each subarray that contains the given values, compute the number of
    # permutations that contain the given subarray and satisfy the anti-median
    # condition.
    for i, j in subarrays:
        # Compute the number of permutations that contain the given subarray,
        # but don't necessarily satisfy the anti-median condition. This can
        # be done by computing the number of ways to fill in the remaining
        # values in the permutation such that the given subarray is preserved.
        k = n - (j - i + 1)
        subarray_permutations = factorial(k)

        # Compute the number of permutations that contain the given subarray
        # and satisfy the anti-median condition. For this, compute the number
        # of ways to fill in the remaining values in the permutation such
        # that the given subarray is preserved and the median of the subarray
        # is the middle element of the subarray.
        if p[i + (j - i + 1) // 2] != -1:
            # If the middle element of the subarray is given, then the number
            # of permutations that contain the given subarray and satisfy the
            # anti-median condition is equal to the number of permutations
            # that contain the given subarray.
            median_permutations = subarray_permutations
        else:
            # If the middle element of the subarray is unknown, then we need
            # to compute the number of permutations that contain the given
            # subarray and satisfy the anti-median condition. This can be done
            # by computing the number of ways to fill in the remaining values
            # in the permutation such that the given subarray is preserved
            # and the median of the subarray is the middle element of the
            # subarray.
            median_permutations = subarray_permutations // 2

        # Subtract the number of permutations that contain the given subarray
        # from the total number of permutations.
        result -= median_permutations

    # Add the number of permutations that contain the given values and satisfy
    # the anti-median condition.
    result += factorial(n - sum(p[i] != -1 for i in range(n)))