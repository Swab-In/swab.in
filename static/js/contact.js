$(function () {
    var container = $('#container');

    $.ajax({
        type: 'GET',
        url: '/about/json',
        success: function (data) {
            $.each(data, function (index, dictionary) {
                var message = dictionary['fields'];
                container.append(`
                <tr>
                    <td>${message["first"]}</td>
                    <td>${message["last"]}</td>
                    <td>${message["email"]}</td>
                    <td>${message["no_hp"]}</td>
                    <td>${message["message"]}</td>
                </tr>
            `);
            })
        }
    })
})

$('#tomboladmin').click(function () {
    redirect();
})

function redirect() {
    window.location.replace("list-message");
}