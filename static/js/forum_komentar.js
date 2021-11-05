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
               <div class='bg-light text-dark row gx-4 gx-lg-5 pt-4 rounded'> \
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
