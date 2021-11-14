$(document).ready(function () {
    $('#thumbs img').click(function() {
        var thmb = this;
        var src = this.src;
        $('#bottlesWrapper img').fadeOut(400,function(){
            thmb.src = this.src;
            $(this).fadeIn(400)[0].src = src;
        });
    });
})