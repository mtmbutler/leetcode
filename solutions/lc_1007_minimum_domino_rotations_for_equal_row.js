/*
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

In a row of dominoes, A[i] and B[i] represent the top and bottom halves
of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 -
one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are
the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:

The first figure represents the dominoes as given by A and B: before we
do any rotations.

If we rotate the second and fourth dominoes, we can make every value in
the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:

In this case, it is not possible to rotate the dominoes to make one row
of values equal.

Note:

1 <= A[i], B[i] <= 6

2 <= A.length == B.length <= 20000
*/
const _ = require("underscore");

let rotsToMatchFirstVal = function(A, B) {
  let val = A[0];
  let switches = 0;  // Dominoes to rotate
  for (let i = 1; i < A.length; i++) {
    if (A[i] === val) {}
    else if (B[i] === val) switches++;
    else {
      return -1;
    }
  }
  return switches;
};

/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
let minDominoRotations = function(A, B) {
  /**
   * There are four ways to iterate:
   *  1. Rotate into A to match first value of A
   *  2. Rotate into B to match first value of B
   *  3. Swap A[0] with B[0], then #1
   *  4. Swap A[0] with B[0], then #2
   */
  let a = rotsToMatchFirstVal(A, B);
  let b = rotsToMatchFirstVal(B, A);
  let temp = A[0]; A[0] = B[0]; B[0] = temp;  // Swap first elements
  let c = rotsToMatchFirstVal(A, B);
  let d = rotsToMatchFirstVal(B, A);

  // Adjust c and d to account for first rotation
  if (c !== -1) c++;
  if (d !== -1) d++;
  let li = [a, b, c, d];  // Store results for each method

  // Filter out -1's
  for (let ix = li.indexOf(-1); ix !== -1; ix = li.indexOf(-1)) {
      li.splice(ix, 1);
  }
  if (li.length === 0) return -1;
  return Math.min(...li);

};


if (typeof module != 'undefined' && !module.parent) {
  const test_cases = [
    [[[2,1,2,4,2,2], [5,2,6,2,3,2]], 2],
    [[[3,5,1,2,3], [3,6,3,3,4]], -1],
    [[[1, 2, 1, 2, 2], [1, 1, 2, 1, 1]], 1],
    [[[1,1,1,2,1,1,1,2,1,1],
      [2,1,1,1,1,1,1,1,1,1]],
      1]
  ];
  for (let case_ of test_cases) {
    let args = case_[0];
    let out = case_[1];
    console.log(args, out);
    let result = minDominoRotations(...args);
    console.log(result);
    console.assert(_.isEqual(result, out));
  }
}
