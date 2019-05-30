(function($){
    $(document).ready(function(){
        $('#enter').on("click", function() {
            var problem = $('#problem').val();
            var pp = $('#pp').children('option:selected').val();

            console.log(problem + "\n" + pp);

            sendRequest(problem, pp);
        });
    });
})(jQuery);