$(function () {

    var view = $('.cols');
    // view.empty();

    $.ajax({
        type: 'GET',
        url: '/artikel/json',
        success: function (data) {

           //grep id from last character url
            var $id = $(location).attr('href').substr(-1);

            for (let i = 0; i < data.length; i++) {
                console.log("MASUK SINII DONGG")

                console.log(data[i])

                if(data[i].fields.post_id === Number($id)){
                    console.log("yey dh masuk")
                    // data[i].fields.user_id data[i].fields.komen
                    view.append(' <div class="w-full pb-4" style=min-width:24rem"><div class="kotak"><h4>'+ data[i].fields.user_id + ' </h4><br><p>'+ data[i].fields.komen + '</p></div></div> ');
                }
            }
        }
    });
});