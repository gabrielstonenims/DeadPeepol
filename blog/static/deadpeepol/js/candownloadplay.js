candownload();

function candownload() {
    var currentSong = 0
    // var is_playing = false
    $("#audioplayer").src = $("#candownload a")[0]
    $("#candownload a").on('click', function (event) {
        event.preventDefault()
        var tname = event.currentTarget.title
        $("#nowplaying").html('Loading...')

        $("#audioPlayer")[0].src = event.currentTarget.href;
        $("#audioPlayer")[0].play().then(res => {
            if ($("#audioPlayer")[0].play()) {
                $("#nowplaying").html('Playing ' + " " + tname)
            }
            console.log('audio playing')
        }).catch(err => {
            throw err
        })
    })

    $("#audioPlayer")[0].addEventListener("ended", function (event) {
        currentSong++;
        if (currentSong == $("#candownload a").length)
            currentSong = 0;
        $("#audioPlayer")[0].src = $("#candownload a")[currentSong].href;
        var name = $("#candownload a")[currentSong].title
        $("#audioPlayer")[0].play().then(res => {
            // console.log(res.text)
        }).catch(err => {
            throw err
        })
        $("#nowplaying").html('Playing ' + " " + name)
    })
}