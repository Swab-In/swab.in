// $(function () {
//   var view = $(".komentar");
//   view.empty();

//   $.ajax({
//     type: "GET",
//     url: "/forum/json",
//     data: {
//       id: Number($(location).attr("href").substr(-1)),
//     },
//     success: function (data) {
//       // console.log("bajingan");
//       //grep id from last character url
//       var $id = $(location).attr("href").substr(-1);
//       console.log("dataadalah:" + data);
//       console.log(data.length)
//       for (let i = 0; i < data.length; i++) {
//         console.log()
//         view.append(
//           "<div class='row gx-4 gx-lg-5'> \
//             <div class='col-md-4 mb-3 w-100'> \
//               <div class='card h-100 border border-white'> \
//                 <div class='card-body rounded'> \
//                 <h4 class='card-text'>" + data[i].fields.user_id + "</h4>  \
//                   <p class='card-text'>" + data[i].fields.komentar + "</p> \
//                 </div> \
//               </div> \
//             </div> \
//           </div>"
//         );
//       }
//     },
//   });
// });

// {
//   /*  */
// }

$(function () {
  var view = $(".komentar");

  $.ajax({
      type: 'GET',
      url: '/forum/json',
      data: {
      id: Number($(location).attr("href").substr(-1)),
    },

      success: function (data) {
          $.each(data, function (index, dictionary) {
              var d = dictionary['fields'];
             view.append(`
               <div class='row gx-4 gx-lg-5'> \
              <div class='col-md-4 mb-3 w-100'> \
                <div class='card h-100 border border-white'> \
                 <div class='card-body rounded'> \
                  <h4 class='card-text'> ${d.user_id} </h4>  \
                   <p class='card-text'>" ${d.komentar} "</p> \
                 </div> \
               </div> \
             </div> \
           </div>
           `);
          })
      }
  })
})
