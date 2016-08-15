$('#submit').click(function(){
    grabData();
})
function grabData(){
    var name=$('#name').val();
    $.ajax({
        type: "GET",
        dataType: "JSON",
        url: 'http://www.khanacademy.org/api/v1/topictree?kind=Topic',
        success: function(result){
        console.log(result);
        $('#content').text('');
        console.log(result);
        
        }
})                


        }
    


$('#submit').click(function(){
    grabData();
})