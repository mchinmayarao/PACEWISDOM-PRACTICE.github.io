// let a1 = [1,2,3,4];
// let a2 = [6,7,8,9];
// let a3 = Array()

// let i = 0;

// while(i<Math.min(a1.length , a2.length)){
//     a3.push(a1[i]);
//     a3.push(a2[i]);
//     i+=1;
// }

// while(i<a1.length){
//     a3.push(a1[i]);
//     i+=1;
// }

// while(i<a2.length){
//     a3.push(a2[i]);
//     i+=1;
// }
// // console.log(a3)

// function threeFive(start,end){
//     let arr = Array()
//     for(let i = start; i<= end; i++){
//         if(i%3==0 && i%5==0){
//             arr.push("fizzz")
//         }
//         else if(i%3==0){
//             arr.push("thriss")
//         }
//         else if(i%5==0){
//             arr.push("fiveess")
//         }
//         else {
//             arr.push(i)
//         }
//     }
//     return arr
// }

// a = threeFive(2,25)
// console.log(a)

prom = (condition) => {
    return new Promise((resolve,reject) =>{
        if(condition){
            resolve("success")
        }
        else{
            reject("unsuccess")
        }
    })
}

// prom(false).then((rr) => {console.log(rr)}).catch((rr) => {console.log(rr)})

async function func(){
    let res =  await prom(true).then((rr) => rr).catch((rr) => rr)
    console.log(res)
}

// func()


let myPromise = new Promise(function(myResolve, myReject) {
    setTimeout(function() { myResolve("resolved!"); }, 3000);
  });
  
// myPromise.then(function(value){console.log(value)});

// debounce 

function display(name){
    console.log(name)
}

function debouncer(func){
    let timer

    return function(name){
        clearTimeout(timer)

        timer = setTimeout(() => {
            display(name);
        },5000)
    }
}

let debounceDisplay = debouncer(display)

// debounceDisplay("chin")
// debounceDisplay("hen")
// debounceDisplay("shiv")
// debounceDisplay("mun")

let promise = (condition) => {
    return new Promise((resolve,reject) => {
        return condition?resolve("resolved"):reject("rejected")
    })
}
async function asyncEg(condition){
    let res = await promise(condition)
    
    return res
}




asyncEg(false).then(
    (res) => {
        console.log(res + " inside then")
    }
    ).catch(
        (res) => {
            console.log(res + " inside catch")
        }
    );

// clousers 

let a =( () =>{
    let counter = 0;
    return () => {
        counter +=1;
        return counter
    }
})();

