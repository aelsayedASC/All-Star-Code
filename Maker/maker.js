var makerURL="https://maker.ifttt.com/trigger/playSong/with/key/cxyOctg62oGk0YEgKA8cFz";
function addSong(){
    var song=$("#song").val();
    var artist=$("#artist").val();
    
    var sendoff={
        "value1":song,
        "value2":artist,
    }
    $.post(makerURL,sendoff);
    
    $("#song").val("");
    $("#artist").val("");
}