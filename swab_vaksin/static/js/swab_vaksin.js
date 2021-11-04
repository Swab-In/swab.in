var state = 'swab';

$('.swab-btn').click(function() {
    state = 'swab';
    $('.vaksin-btn').css({'opacity' : '50%'});
    $('.swab-btn').css({'opacity' : '100%'});
    $('.swab-cards').css({display: 'block'});
    $('.vaksin-cards').css({display: 'none'});
    console.log(state)
});
  
$('.vaksin-btn').click(function() {
    state = 'vaksin';
    $('.vaksin-cards').css({display: 'block'});
    $('.swab-cards').css({display: 'none'});
    $('.swab-btn').css({'opacity' : '50%'});
    $('.vaksin-btn').css({'opacity' : '100%'});
    console.log(state)
});


if(state == 'swab') {
    $('.swab-info').css({display: 'block'});
    $('.vaksin-info').css({display: 'none'});
    $('.swab-experience').css({display: 'block'});
    $('.vaksin-experience').css({display: 'none'});
} else{
    $('.vaksin-info').css({display: 'block'});
    $('.swab-info').css({display: 'none'});
    $('.vaksin-experience').css({display: 'block'});
    $('.swab-experience').css({display: 'none'});
}
