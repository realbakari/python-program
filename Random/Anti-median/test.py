# Author: Bakari Mustafa, contact@bakarimustafa.com

from main import anti_median_permutation


# Test case 1
# There is only one test case with n = 2.
# The permutation is given as [1, -1], which means that the first element
# is given and the second element is unknown.
# There is only one anti-median permutation in this case, which is [1, 2].
assert anti_median_permutation(2, [1, -1]) == 1

# Test case 2
# There are two test cases with n = 4.
# In the first test case, the permutation is given as [1, 2, -1, -1], which
# means that the first two elements are given and the last two elements are
# unknown.
# There are two anti-median permutations in this case, which are [1, 2, 3, 4]
# and [1, 2, 4, 3].
# In the second test case, the permutation is given as [-1, -1, -1, -1], which
# means that all elements are unknown.
# There are six anti-median permutations in this case, which are [1, 2, 3, 4],
# [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], and [1, 4, 3, 2].
assert anti_median_permutation(4, [1, 2, -1, -1]) == 2
assert anti_median_permutation(4, [-1, -1, -1, -1]) == 6

# Test case 3
# There is only one test case with n = 6.
# The permutation is given as [1, 2, 3, -1, -1, -1], which means that the
# first three elements are given and the last three elements are unknown.
# There are four anti-median permutations in this case, which are
# [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6, 5], [1, 2, 3, 5, 4, 6], and
# [1, 2, 3, 5, 6, 4].
assert anti_median_permutation(6, [1, 2, 3, -1, -1, -1]) == 4

