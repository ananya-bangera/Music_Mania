var a = document.getElementById("emo1");

a.addEventListener("click", fun1)
function fun1() {
    a.classList.toggle("classnew")
 

    b.classList.remove("classnew")
    c.classList.remove("classnew")
    d.classList.remove("classnew")
    e.classList.remove("classnew")
   
}

var b = document.getElementById("emo2");
b.addEventListener("click", fun2)
function fun2() {
    b.classList.toggle("classnew")
  

    a.classList.remove("classnew")
    c.classList.remove("classnew")
    d.classList.remove("classnew")
    e.classList.remove("classnew")
    
}


var c = document.getElementById("emo3");

c.addEventListener("click", fun3)
function fun3() {
    c.classList.toggle("classnew")
   

    a.classList.remove("classnew")
    b.classList.remove("classnew")
    d.classList.remove("classnew")
    e.classList.remove("classnew")
 
}


var d = document.getElementById("emo4");

d.addEventListener("click", fun4)
function fun4() {
    d.classList.toggle("classnew")
  
    a.classList.remove("classnew")
    c.classList.remove("classnew")
    c.classList.remove("classnew")
    e.classList.remove("classnew")
  
}



var e = document.getElementById("emo5");

e.addEventListener("click", fun5)
function fun5() {
    e.classList.toggle("classnew")

    a.classList.remove("classnew")
    c.classList.remove("classnew")
    d.classList.remove("classnew")
    b.classList.remove("classnew")
 
}