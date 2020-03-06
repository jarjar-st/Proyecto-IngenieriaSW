(function($,window){
    var arrowWidth = 30;
    $.fn.resizeSelect = function(settings){
        return this.each(function(){
            $(this).change(function(){
                var $this = $(this);
                var text = $this.find("option:selected").text();
                var $test = $("<span>").html(text);
                $test.appendTo('body');
                var width = $test.width();
                $test.remove();
                $this.width(width+arrowWidth);
            }).change();
        });  
    };
    $("select.resize-select").resizeSelect();
})(jQuery, window);