$('#submit').click(function(){
    grabData();
})
function grabData(){
    var name=$('#name').val();
    $.ajax({
        type: "GET",
        dataType: "JSON",
        url: 'http://www.khanacademy.org/api/v1/topic/'+name+'/videos',
        success: function(result){
        console.log(result);
        $('#content').text('');
        for(i=0; i<result.length; i++){
            $('#content').append("<div> " + "<span>" + result[i].title + ":" + "</span>" + "<div>");
            $('#content').append('<iframe width="320" height="240" src="https://www.youtube.com/embed/' + result[i].youtube_id +'"> </iframe>' + '</div> </div>');
        
        }
}                


        })
    }


$('#submit').click(function(){
    grabData();
})