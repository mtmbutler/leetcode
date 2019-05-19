/*
https://leetcode.com/problems/available-captures-for-rook/

On an 8 x 8 chessboard, there is one white rook.  There also may be
empty squares, white bishops, and black pawns.  These are given as
characters 'R', '.', 'B', and 'p' respectively. Uppercase characters
represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal
directions (north, east, west, and south), then moves in that direction
until it chooses to stop, reaches the edge of the board, or captures an
opposite colored pawn by moving to the same square it occupies.  Also,
rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","
."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],["."
,".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:

In this example the rook is able to capture all the pawns.

Example 2:
Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","
."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],
[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],["."
,".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:

Bishops are blocking the rook to capture any pawn.

Example 3:
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","
."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],
[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],["."
,".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:

The rook can capture the pawns at positions b5, d6 and f5.

Note:

board.length == board[i].length == 8

board[i][j] is either 'R', '.', 'B', or 'p'

There is exactly one cell with board[i][j] == 'R'
*/
const _ = require("underscore");

/**
 * @param {String[][]} board
 * @param {number[]} start
 * @param {String} dir
 * @return {String}
 */
let firstEncounteredPiece = function(board, start, dir) {
    let inc = [];
    switch (dir) {  // Determine direction to go
        case 'L': inc = [0, -1]; break;
        case 'U': inc = [1, 0]; break;
        case 'R': inc = [0, 1]; break;
        case 'D': inc = [-1, 0]; break;
        default: return '.';  // Invalid direction
    }

    // Search the direction
    let i = start[0];
    let j = start[1];
    let curSq = 'R';
    while (true) {
        if (i >= 8 || i < 0
            || j >= 8 || j < 0
            || curSq === 'B' || curSq === 'p') break;
        curSq = board[i][j];
        i += inc[0];
        j += inc[1];
    }

    return curSq;
};

/**
 * @param {String[][]} board
 * @return {number}
 */
let numRookCaptures = function(board) {
    // Find the rook
    let rookSq = [];
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (board[i][j] === 'R') {rookSq = [i, j]; break;}
        }
        if (rookSq.length > 0) break;
    }

    // Count pawns
    const directions = ['L', 'U', 'R', 'D'];
    let pawns = 0;
    for (let dir of directions) {
        let piece = firstEncounteredPiece(board, rookSq, dir);
        if (piece === 'p') pawns++;
    }
    return pawns;
};


if (typeof module != 'undefined' && !module.parent) {
    const test_cases = [
        [[[".",".",".",".",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          [".",".",".","R",".",".",".","p"],
          [".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          [".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".","."]], 3],
        [[[".",".",".",".",".",".",".","."],
          [".","p","p","p","p","p",".","."],
          [".","p","p","B","p","p",".","."],
          [".","p","B","R","B","p",".","."],
          [".","p","p","B","p","p",".","."],
          [".","p","p","p","p","p",".","."],
          [".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".","."]], 0],
        [[[".",".",".",".",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          ["p","p",".","R",".","p","B","."],
          [".",".",".",".",".",".",".","."],
          [".",".",".","B",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          [".",".",".",".",".",".",".","."]], 3]
    ];
    for (let case_ of test_cases) {
        let arg = case_[0];
        let out = case_[1];
        console.log(arg, out);
        let result = numRookCaptures(arg);
        console.log(result);
        console.assert(_.isEqual(result, out));
    }
}
