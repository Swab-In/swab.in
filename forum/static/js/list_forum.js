// $(document).ready(function () {
//     $("#addThreadForm").submit(function (e) {
//         e.preventDefault();
//         var image = $('#image').val()
//         var title = $('#title').val()
//         var message = $('#message').val()
//         $.ajax({ 
//         type: "POST",
//         url: window.location.href,
//         data: {
//             image :image,
//             title :title,
//             message :message,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 
//         },
//         success: function (hasil) {
//             console.log('success');
//             for(i=0; i < hasil.length; i++){
//                 var temp = "<div class='card'><div class='crd-header'><div class='pImage'><img src="+hasil[i].fields.image+"alt=></div>" +
//                 "<div class='pInformation' id='desc'><h5>"+hasil[i].fields.title+"</h5><h7>Ditulis oleh:" +hasil[i].fields.writer+ " </h7></div></div>" +
//                 "<div class='crd-description'><p>"+hasil[i].fields.message+"</p></div><div class='crd-btn'><a href=>Read More</h6></a></div></div>";    
//                 $(".cards").append(temp);
//             }
//         }
//         });
//     });
// });