/*
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].


*/
const _ = require("underscore");

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
};


if (typeof module != 'undefined' && !module.parent) {
    const test_cases = [
        [[[2, 7, 11, 15], 9], [0, 1]],
        [[[2, 7, 11, 15], 17], [0, 3]]];
    for (let case_ of test_cases) {
        let args = case_[0];
        let out = case_[1];
        console.log(args, out);
        let result = twoSum( ...args );
        console.log(result);
        console.assert(_.isEqual(result, out));
    }
}
