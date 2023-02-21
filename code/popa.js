let i = 1
let j =1
const btnNext = document.querySelector('.next')
btnNext.addEventListener('click', next)
function next(){
    const elem = document.querySelector('.img')
    elem.classList.add('img'+i) 
    i++
    
}

const btnPrev = document.querySelector('.prev')
btnPrev.addEventListener('click', prev)
function prev(){
    const elem = document.querySelector('.img')
    elem.classList.remove('img'+i)
    i--
    
   
}