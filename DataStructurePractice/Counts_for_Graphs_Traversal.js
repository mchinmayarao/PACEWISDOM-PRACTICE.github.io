// Question 2: Counts for Graphs Traversal 

// Given the width and height of a rectangular grid, the task is to write a function that calculates the number of ways to reach the lower right corner of the grid, starting from the upper left corner. Each move can only be made by going down or right, and moving up or left is not allowed. 

// The function should return the count of all possible paths to reach the lower right corner. 

// For example, if the width is 2 and the height is 3, there are three possible ways to reach the lower right corner: 

// · Moving down, down, right. 

// · Moving right, down, down. 

// · Moving down, right, down. 

// It is important to note that the given width and height will always be such that the grid is larger than 1x1, satisfying the condition width * height >= 2. 

// Sample Input 

// width = 4 

// height = 3 

// Sample Output 

// 10 

function possiblePath(height,width){
    if(height == 1 || width ==1){
        return 1 
    }

    return possiblePath(height-1 , width) + possiblePath(height , width-1)
}




function possiblePath2(height,width){

    let arr  = Array(height).fill().map(() => Array(width).fill(1));
    
    for(let i = 1; i<height; i++){
        for(let j = 1; j<width; j++){
            arr[i][j] = arr[i-1][j] + arr[i][j-1];
        }
    }

    return arr[height-1][width-1];
}

console.log(possiblePath2(3,4))