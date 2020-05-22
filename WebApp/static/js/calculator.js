alert("this is calculator");

var result = document.getElementById('result');

function inputDigit(x){
    if(result.innerText.length >= 14) return;

    if (result.innerText == '0'){
        result.innerText = x;
    }else{
        result.innerText += x;
    }
}