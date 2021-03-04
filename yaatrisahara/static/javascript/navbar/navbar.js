
const menu=document.getElementById('mobile-menu');
const hambar=document.getElementById('hambar');
const prof=document.getElementById('profile-img');
const overlay=document.getElementById('profile-over');

hambar.addEventListener('click',(e)=>{

    menu.classList.toggle('animatednav')

})
prof.addEventListener('click',(e)=>{

    overlay.classList.toggle('d-block')

})
