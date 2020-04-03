audioPlayer();

function audioPlayer(){
    var currentSong = 0;
    $("#audioPlayer")[0].src = $("#playlist li a")[0];
    $("#playlist li a").on('click',function(event){
        event.preventDefault();
       
        var tname = event.currentTarget.title;
        $("#audioPlayer")[0].src = this;
        $("#audioPlayer")[0].play(); 
        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " + tname)
        });
    $("#audioPlayer")[0].addEventListener("ended",function(event){
       currentSong++;
       if(currentSong == $("#playlist li a").length)
        currentSong = 0;
       $("#audioPlayer")[0].src = $("#playlist li a")[currentSong].href;
       var name= $("#playlist li a")[currentSong].title
       $("#audioPlayer")[0].play(); 
       $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " +name)


    });
    $("#forward").on('click',function(event){
        currentSong++;
        if(currentSong > $("#playlist li a").length)
            currentSong = 0;
        $("#audioPlayer")[0].src = $("#playlist li a")[currentSong].href;
        var name= $("#playlist li a ")[currentSong].title
        $("#audioPlayer")[0].play();
        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " +name)

        console.log("forward is clicked")

    })
    $("#back").on('click',function(event){
        currentSong--;
        if(currentSong < 0)
            currentSong = 0;
        $("#audioPlayer")[0].src = $("#playlist li a")[currentSong].href;
        var name= $("#playlist li a ")[currentSong].title
        $("#audioPlayer")[0].play();
        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " +name)

    })
}

