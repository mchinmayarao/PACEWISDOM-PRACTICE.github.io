var arrray = ['hello', 'world', 'in', 'a', 'frame'];

function arrayInFrame(array){
    var lengths = array.map(function(word){
        return word.length

       }) 
       
       maxLength = Math.max(...lengths) + 4;
      // console.log(maxLength);

       console.log("*".repeat(maxLength));
       array.forEach(element => {

        console.log("* " + element + " ".repeat(maxLength - element.length -3) + "*");
        
       });
       console.log("*".repeat(maxLength));



}
arrayInFrame(arrray);