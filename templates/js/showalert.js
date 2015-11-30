$(function(){
       $("#success-alert").fadeTo(1500, 500).slideUp(500, function(){
          $("#success-alert").alert('close');
          var old_location = window.location.href;
          if(old_location.indexOf('showAlert') > -1){
            var new_location = old_location.substring(0,old_location.indexOf('showAlert'));
            window.location = new_location;
           }
       });
});
