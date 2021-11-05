$(function () {

    var view = $('.list_komentar');
    // view.empty();

    $.ajax({
        type: 'GET',
        url: '/artikel/json',
        success: function (data) {

           //grep id from last character url
            var $id = $(location).attr('href').substr(-1);

            console.log("dataadalah:"+ data)

            for (let i = 0; i < data.length; i++) {
                console.log("MASUK SINII DONGG")

                console.log(data[i])

                if(data[i].fields.post_id === Number($id)){
                    console.log("yey dh masuk")
                    
                    view.append( '<div class="comments-list"><div class="media"><div class="media-body"><h4 class="media-heading user_name">' + data[i].fields.user_id +'</h4> <p>' + data[i].fields.komen + ' </p></div></div></div>');
                }
            }
        }
    });
});
