class Tree{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

function newNode(data){
    let node = new Tree(data);
    return node
}

function height(tree){
    if(tree == null) return 0;

    return 1 + Math.max(height(tree.left),height(tree.right))
}
function diameter(tree){
    if(tree == null) return 0;

    let lheight = height(tree.left);
    let rheight = height(tree.right);

    let ldia = diameter(tree.left);
    let rdia = diameter(tree.right);

    return Math.max(lheight + rheight + 1 , Math.max(ldia,rdia))

}

// Test Case 1: Empty Tree
let tree1 = null;
console.log(diameter(tree1)); // 0

// Test Case 2: Single Node Tree
let tree2 = newNode(10);
console.log(diameter(tree2)); // 1

// Test Case 3: Tree with two nodes
let tree3 = newNode(10);
tree3.left = newNode(5);
console.log(diameter(tree3)); // 2

// Test Case 4: Linear Tree (Left-skewed)
let tree4 = newNode(10);
tree4.left = newNode(9);
tree4.left.left = newNode(8);
tree4.left.left.left = newNode(7);
console.log(diameter(tree4)); // 4

// Test Case 5: Linear Tree (Right-skewed)
let tree5 = newNode(10);
tree5.right = newNode(11);
tree5.right.right = newNode(12);
tree5.right.right.right = newNode(13);
console.log(diameter(tree5)); // 4

// Test Case 6: Balanced Tree
let tree6 = newNode(10);
tree6.left = newNode(5);
tree6.right = newNode(15);
tree6.left.left = newNode(3);
tree6.left.right = newNode(7);
tree6.right.left = newNode(12);
tree6.right.right = newNode(18);
console.log(diameter(tree6)); // 5

// Test Case 7: Complete Binary Tree
let tree7 = newNode(1);
tree7.left = newNode(2);
tree7.right = newNode(3);
tree7.left.left = newNode(4);
tree7.left.right = newNode(5);
tree7.right.left = newNode(6);
tree7.right.right = newNode(7);
console.log(diameter(tree7)); // 5

// Test Case 8: Tree with varying branch lengths
let tree8 = newNode(1);
tree8.left = newNode(2);
tree8.left.left = newNode(4);
tree8.left.left.left = newNode(8);
tree8.right = newNode(3);
tree8.right.right = newNode(7);
console.log(diameter(tree8)); // 6

// Test Case 9: Larger Tree
let tree9 = newNode(1);
tree9.left = newNode(2);
tree9.right = newNode(3);
tree9.left.left = newNode(4);
tree9.left.right = newNode(5);
tree9.left.left.left = newNode(8);
tree9.left.left.right = newNode(9);
tree9.right.right = newNode(7);
tree9.right.right.right = newNode(10);
tree9.right.right.right.left = newNode(11);
console.log(diameter(tree9)); // 7
