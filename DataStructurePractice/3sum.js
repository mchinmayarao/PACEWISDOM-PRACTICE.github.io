

function threeSum(arr, target) {
    let n = arr.length;
    let res = [];
    arr.sort((a, b) => a - b); // Sorting the array for two-pointer technique

    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && arr[i] === arr[i - 1]) continue; // Avoid duplicates

        let start = i + 1;
        let end = n - 1;

        while (start < end) {
            let sum = arr[i] + arr[start] + arr[end];
            if (sum === target) {
                res.push([arr[i], arr[start], arr[end]]);
                while (start < end && arr[start] === arr[start + 1]) start++; // Avoid duplicates
                while (start < end && arr[end] === arr[end - 1]) end--; // Avoid duplicates
                start++;
                end--;
            } else if (sum > target) {
                end--;
            } else {
                start++;
            }
        }
    }

    return res;
}

// Test Case 1: Basic case with positive numbers
let arr1 = [1, 2, 3, 4, 5];
let target1 = 9;
console.log(threeSum(arr1, target1)); // [[1, 3, 5], [2, 3, 4]]

// Test Case 2: Basic case with negative numbers
let arr2 = [-1, -2, -3, -4, -5];
let target2 = -9;
console.log(threeSum(arr2, target2)); // [[-1, -3, -5], [-2, -3, -4]]

// Test Case 3: Mixed positive and negative numbers
let arr3 = [-1, 0, 1, 2, -1, -4];
let target3 = 0;
console.log(threeSum(arr3, target3)); // [[-1, -1, 2], [-1, 0, 1]]

// Test Case 4: No triplet found
let arr4 = [1, 2, 3, 4, 5];
let target4 = 15;
console.log(threeSum(arr4, target4)); // []

// Test Case 5: All zeroes
let arr5 = [0, 0, 0, 0, 0];
let target5 = 0;
console.log(threeSum(arr5, target5)); // [[0, 0, 0]]

// Test Case 6: Duplicate elements
let arr6 = [1, 1, 2, 2, 3, 3];
let target6 = 6;
console.log(threeSum(arr6, target6)); // [[1, 2, 3]]

// Test Case 7: Large numbers
let arr7 = [1000000000, -1000000000, 0, 1, 2, -1];
let target7 = 1;
console.log(threeSum(arr7, target7)); // [[1000000000, -1000000000, 1], [2, -1, 0]]

// Test Case 8: Single triplet
let arr8 = [1, 2, 3];
let target8 = 6;
console.log(threeSum(arr8, target8)); // [[1, 2, 3]]

// Test Case 9: Empty array
let arr9 = [];
let target9 = 0;
console.log(threeSum(arr9, target9)); // []

// Test Case 10: Array with less than three elements
let arr10 = [1, 2];
let target10 = 3;
console.log(threeSum(arr10, target10)); // []
