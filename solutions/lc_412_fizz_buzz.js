/*
https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1
to n.

But for multiples of three it should output “Fizz” instead of the number
and for the multiples of five output “Buzz”. For numbers which are
multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
*/
const _ = require("underscore");

/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let li = [];
    for (let i = 1; i <= n; i++) {
        let fizz = ((i % 3) === 0) ? 'Fizz' : '';
        let buzz = ((i % 5) === 0) ? 'Buzz' : '';
        let s = fizz + buzz;
        li[li.length] = (s.length > 0) ? s : i.toString();
    }
    return li;
};


if (typeof module != 'undefined' && !module.parent) {
    const test_cases = [
        [15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
              "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]]
    ];
    for (let case_ of test_cases) {
        let arg = case_[0];
        let out = case_[1];
        console.log(arg, out);
        let result = fizzBuzz(arg);
        console.log(result);
        console.assert(_.isEqual(result, out));
    }
}
