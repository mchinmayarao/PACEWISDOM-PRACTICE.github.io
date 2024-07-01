// Question 3: River Sizes 

// You get a two-dimensional table (matrix) that can have different heights and widths and contains only 0 and 1. Each 0 represents land and each 1 represents part of a river. A river consists of any number of rivers that are either horizontally or vertically contiguous (but not diagonally contiguous). The number of contiguous units that make up a river determines its size. 

// Note that the river can bend. In other words, it does not have to be a straight vertical line or a straight horizontal line; it can be, for example, L-shaped. 

// Write a function that returns a table of the sizes of all the rivers represented in the input matrix. The sizes do not have to be in any particular order. 

// Sample Input 

// matrix = [ 

// [1, 0, 0, 1, 0], 

// [1, 0, 1, 0, 0], 

// [0, 0, 1, 0, 1], 

// [1, 0, 1, 0, 1], 

// [1, 0, 1, 1, 0], 

// ] 

// Sample Output 

// [1, 2, 2, 2, 5] 
// The numbers could be ordered differently. 

// The rivers can be clearly seen here: 

// [ 

// [1, , , 1, ], 

// [1, , 1, , ], 

// [ , , 1, , 1], 

// [1, , 1, , 1], 

// [1,, 1, 1, ], 

// ] 



function river_size(matrix){

    let height = matrix.length;
    let width = matrix[0].length;

    // creating the visted matrix
    let visited = new Array(height).fill().map(() => new Array(width).fill(false));
    sizes = [];

    // these are direction for the node to check i.e up, down, left , right
    // when adding these to the respective row and column index we get the direction index to explore
    let directions = [[-1,0],[1,0],[0,-1],[0,1]];


    function exploreRiver(row,col){
        size = 0;
        let stack = [[row,col]];

        while(stack.length > 0){
            let [r,c] = stack.pop();

            if (visited[r][c]) continue;
            visited[r][c] = true;

            if (visited[r][c] == 1){
                size++;

                // explore up, down, left and right
                for(const [dr,dc] of directions){
                    nr = r + dr;
                    nc = c + dc;

                    if(nr >= 0 && nr <height && nc >= 0 && nc < width ){
                        if(!visited[nr][nc] && matrix[nr][nc] ==1){
                            stack.push([nr,nc])
                        }
                    }
                }
            }
        }
        
        return size;
    }

    // exploring all the nodes if it is already visited or 0 we dont explore the node
    for(let i =0; i<height; i++){
        for(let j=0; j<width; j++){
            if(!visited[i][j] && matrix[i][j] ==1){
                const riverSize = exploreRiver(i,j);
                sizes.push(riverSize)
            }

        }
    }

    return sizes;
    


}

// Example usage:
const matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0],
];

console.log(river_size(matrix)); // Output: [1, 2, 2, 2, 5]
