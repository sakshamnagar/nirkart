
let a = document.getElementById('avgrate').textContent;
let num = Number(a); //a is string. Hence converted it to number
let rating = Math.floor(num); //rounded to the smaller value
for (let i = 1; i <= rating; i++) {
    document.getElementById(i).classList.add('starrate');
  }

  
//var k = Array.from(document.getElementsByClassName('revrate')).map(el=>Number(el.innerText));
//console.log(k)

//for (i=0; i<=k.length; i++) {
  //for (j=1; j<= k[i]; j++) {
    //console.log(k[i]);
    //if (j === k[i]) {
      //document.getElementById('rate'+j).classList.add('star');
  //}
  //}
//}





