$('.swab-btn').click(function() {
    state = 'swab';
    $('.vaksin-btn').css({'opacity' : '50%'});
    $('.swab-btn').css({'opacity' : '100%'});
    $('.swab-cards').css({display: 'block'});
    $('.vaksin-cards').css({display: 'none'});
});
  
$('.vaksin-btn').click(function() {
    state = 'vaksin';
    $('.vaksin-cards').css({display: 'block'});
    $('.swab-cards').css({display: 'none'});
    $('.swab-btn').css({'opacity' : '50%'});
    $('.vaksin-btn').css({'opacity' : '100%'});
});
