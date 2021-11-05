$(document).ready(function () {
    $("#buttonAdd").click(function (e) {
        e.preventDefault();
        $.ajax({ 
            url: window.location.href,
            success: function () {
                console.log('success');
                $('#addModal').modal('show');
            }
        });
    });

    $(function () {
        var forum = $(".cards");
      
        $.ajax({
            type: 'GET',
            url: '/lokasi/json',
      
            success: function (data) {
                var $id = $(location).attr('href').substr(-1);
                console.log('success');
                for (let i = 0; i < data.length; i++) {
                    if(data[i].fields.post_id === Number($id)){
                            forum.append(`<div class='card'> 
                            <div class='crd-header'> 
                                <div class='pImage'><img src="` + data[i].fields.image + `" alt=""></div> 
                                <div class='pInformation' id='desc'> 
                                    <h5 class="fw-bold">` + data[i].fields.title + `</h5>
                                    <h7>Ditulis oleh: ` + data[i].fields.writer + `</h7> 
                                </div> 
                            </div> 
                            <div class='crd-description'> 
                                <p>` + data[i].fields.message + `</p> 
                            </div> 
                            <div class='crd-btn'> 
                                <a href="{% url 'forum:forum-detail' ` + data[i].fields.pk + ` %}">Read More</h6></a> 
                            </div> 
                        </div>
                        `);
                    }
                }
                
            }
        })
      })
});

