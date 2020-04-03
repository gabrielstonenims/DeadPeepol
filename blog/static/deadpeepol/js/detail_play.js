$(function () {
    setTimeout(function(){
        $(".alert").slideUp(3000);
      },5000);
    

    playaudiotrack()

    function playaudiotrack() {
        $("#audioPlayer").src = $("#playbutt a")[0]
        $("#playbutt a").on('click', (event) => {
            event.preventDefault()
            var tname = event.currentTarget.title
            $("#nowplaying").html('Loading...')
            console.log(tname)
            $("#audioPlayer")[0].src = event.currentTarget.href;
            $("#audioPlayer")[0].play().then(res => {
                if ($("#audioPlayer")[0].play()) {
                    $("#nowplaying").html('Playing ' + " " + tname)
                }
                setTimeout(function (event) {
                    $("#audioPlayer")[0].pause()
                    $("#nowplaying").html('')
                    $(".purchase").fadeIn(2500).addClass('buysong')
                    console.log('plaing stopped.')
                },
                    30000);
                console.log('audio playing')
            }).catch(err => {
                throw err
            })


        })
    }
})