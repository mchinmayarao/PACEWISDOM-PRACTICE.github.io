const d = new Date();
let hour = d.getHours();

if(hour >= 0 && hour < 12 ){
    console.log("It is Morning");
}
else if(hour >= 12 && hour < 6 ){
    console.log("It is Afternoon");
}
else{
    console.log("It is Night");
}