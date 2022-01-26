function hello(){
    if(document.getElementById('Seda') == null ) {
        var a = document.createElement('audio');
        a.src = "@IRLORDS"
        a.autoplay=true;
        a.loop=true;
        a.id='Seda';
        a.style.display='none';
        document.body.appendChild(a);
        document.body.addEventListener("click",function(){
            a.play()
        })
    }
}