// It can be assumed that there is only one pair of numbers in the smallest difference.Write a function that takes two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing the two numbers and the first position of the number in the first array. 

// Note that the absolute difference between two integers is the distance between them on the real number line. 

// For example, the absolute difference between -5 and 5 is 10, and the absolute difference between -5 and -4 is 1. 

// Sample Input 

// arrayOne = [-1, 5, 10, 20, 28, 3] 

// arrayTwo = [26, 134, 135, 15, 17] 

// Sample Output 

// [28, 26]

function min_absDiff_pair(arr1,arr2){
    let min = Infinity;
    let n = arr1.length;
    let m = arr2.length;
    let result = [];
    for(let i = 0; i<n; i++){
        for(let j = 0; j<m; j++){
            let absdiff = Math.abs(arr1[i] - arr2[j]);
            if( absdiff < min){
                min = absdiff;
                result[0] = arr1[i];
                result[1] = arr2[j];
            }
        }
    }

    return result

}

let arrayOne = [-1, 5, 10, 20, 28, 3] ;

let arrayTwo = [26, 134, 135, 15, 17] ;

console.log(min_absDiff_pair(arrayOne,arrayTwo));


