$('#zz').on( "click", function() {
    document.body.style.backgroundColor = "red";
});
var from = true;
var to = true;
var from_colour = '';
var to_colour = '';
var from_cor = '';
var to_cor= '';

function notify() {
  alert( "clicked" );
}
$(document).on( "click", '[name="field"]', function() {
    if (from) {
        from_colour = $( this ).css( "background-color" );
        from_cor = $(this).prop('id');
        $('#from').val(from_cor)
        $(this).css('background-color', 'yellow');
        from = false;
    } else if (to) {
        to_colour = $( this ).css( "background-color" );
        to_cor = $(this).prop('id');
        $('#to').val(to_cor)
        $(this).css('background-color', 'green');
        to = false;
    } else if ((from_cor == $(this).prop('id')) || (to_cor == $(this).prop('id'))) {
        $("#" + from_cor).css('background-color', from_colour);
        from_colour = '';
        from_cor = '';
        $('#from').val('')
        from = true;
        
        $("#" + to_cor).css('background-color', to_colour);
        to_colour = '';
        to_cor = '';
        $('#to').val('')
        to = true;
    }
   
} );

