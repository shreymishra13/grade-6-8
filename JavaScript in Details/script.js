const resultId = document.getElementById("result")


// function add(a,b){
//     return a+b
// }

const add = (a,b)=>a+b

function Printresult(a,b){
    let answer = add(a,b);
    resultId.innerHTML = answer
}