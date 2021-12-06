$(document).ready(function () {
    $(function () {
        var swab = $(".cards");
      
        $.ajax({
            type: 'GET',
            url: '/swab-vaksin/json-swab',
      
            success: function (data) {
                var $id = $(location).attr('href').substr(-1);
                console.log('success');
                for (let i = 0; i < data.length; i++) {
                    if(data[i].fields.swab_id === Number($id)){
                      console.log(data[i])
                      swab.append(`
                        <div class='card'>
                          <div class='crd-description'>
                            <p>` + data[i].fields.pengalamanSwab + `</p>
                          </div>
                          <div class='pInformation' id='desc'>
                            <h6>` + data[i].fields.penulis + `</h6>
                          </div>
                      </div>
                        `);
                    }
                }
                
            }
        })
      })
})