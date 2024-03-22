var array = [1,4,2,3,1,7];
var position = 5;
var arrayLength = array.length;
//console.log(arrayLength);

// var start = 0;
// var end = arrayLength-1;

var left = position -1;
var right = position + 1;
var flag = true;
while(flag){
    if(left>=0){
        if(array[left] > array[position] && array[left] > array[right] ){
            console.log(array[left]);
            return;
        }
        else{
            left = left -1;
        }
    }
    if(right <= arrayLength -1){
        if(array[right] > array[position]){
            console.log(array[right]);
            return;
        }
        else{
            right = right + 1;
        }
    }

    if(left == -1 && right == arrayLength){
        console.log("No larger element found.");
        return;
    }

}
