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

function validateBST(tree){

    function maxValue(node){
        if(node == null){
            return Number.MIN_VALUE
        }

        let lmax = maxValue(node.left);
        let rmax = maxValue(node.right);

        return Math.max(node.data , Math.max(lmax,rmax))    
    }

    function minValue(node){
        if(node == null) {
            return Number.MAX_VALUE;
        }

        lmin = minValue(node.left);
        rmin = minValue(node.right);

        return Math.min(node.data, Math.min(lmin,rmin));
    }

    if(tree == null) return true;

    if( tree.left != null && maxValue(tree.left)>tree.data) return false;

    if(tree.right != null && minValue(tree.right)<tree.data) return false;

    return validateBST(tree.left) && validateBST(tree.left);
}

// Test Case 1: Empty Tree
let tree1 = null;
console.log(validateBST(tree1)); // true

// Test Case 2: Single Node Tree
let tree2 = newNode(10);
console.log(validateBST(tree2)); // true

// Test Case 3: Valid BST
let tree3 = newNode(10);
tree3.left = newNode(5);
tree3.right = newNode(15);
console.log(validateBST(tree3)); // true

// Test Case 4: Invalid BST (right child less than root)
let tree4 = newNode(10);
tree4.left = newNode(5);
tree4.right = newNode(7);
console.log(validateBST(tree4)); // false

// Test Case 5: Valid BST with more nodes
let tree5 = newNode(20);
tree5.left = newNode(10);
tree5.right = newNode(30);
tree5.left.left = newNode(5);
tree5.left.right = newNode(15);
tree5.right.left = newNode(25);
tree5.right.right = newNode(35);
console.log(validateBST(tree5)); // true

// Test Case 6: Invalid BST (left subtree with incorrect value)
let tree6 = newNode(20);
tree6.left = newNode(30); // Invalid because 30 > 20
tree6.right = newNode(40);
console.log(validateBST(tree6)); // false

// Test Case 7: Invalid BST (subtree with incorrect value)
let tree7 = newNode(20);
tree7.left = newNode(10);
tree7.right = newNode(30);
tree7.left.right = newNode(25); // Invalid because 25 > 20
console.log(validateBST(tree7)); // false

// Test Case 8: Large Valid BST
let tree8 = newNode(50);
tree8.left = newNode(30);
tree8.right = newNode(70);
tree8.left.left = newNode(20);
tree8.left.right = newNode(40);
tree8.right.left = newNode(60);
tree8.right.right = newNode(80);
console.log(validateBST(tree8)); // true




