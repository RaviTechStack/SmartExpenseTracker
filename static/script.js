let cover = document.querySelector(".cover");
let move = document.querySelector(".move");
let text = document.querySelector(".cover-text")
move.addEventListener("click", ()=>{
    if(move.innerHTML == "signUp"){
        text.innerHTML = " Already have an Account ?"
        move.innerHTML = "Login"
        cover.style.transform = "translateX(-100%)"
        
    }
    else{
        text.innerHTML = " Don't have an Account ?"
        move.innerHTML = "signUp"
        cover.style.transform = "translateX(0%)"
        
    }
})

