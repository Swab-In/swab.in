$(function () {
  console.log("testt");
  var view = $(".info-wrapper");
  // console.log('testt')
  let loc = $(location).attr("href").split("/");

  $.ajax({
    type: "GET",
    url: "/lokasi/json",
    data: {
      id: Number(loc[loc.length - 1]),
    },

    success: function (data) {
      $.each(data, function (index, dictionary) {
        var d = dictionary["fields"];
             view.append(`
             <div class='iImage'><img src=" ${d.lokasi_pic} " alt=""></div>
                <div class='iDescription'>
                    <div class='info-lokasi'>
                        <h3>${d.lokasi}</h3>
                        <p>${d.detail}</p>
                    </div>
                </div>
           `);
      });
    },
  });
});
