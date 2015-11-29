
$(function() {
  $( "#searchuser" ).autocomplete({
    source: function(request, response) {
      $.ajax({
          url: "/api/searchuser",
          data: { query: $("#searchuser").val()},
          dataType: "json",
          type: "GET",
          success: function(data) {
              console.log(data);
              response($.map(data['users'], function(obj) {
                  return {
                    label: obj.name,
                    value: obj.name,
                    id: obj.user_id
                  };
              }));
          }
      });
    },
    select: function(event, ui) {
      //need to fill in input value
      $("#inviteuser").val(ui.item.id);
      console.log(ui.item.id);
      //$("#searchForm").submit();
    }
  });
})

/*


$('#selector').autocomplete({
  source: url,
  select: function (event, ui) {
      $("#txtAllowSearch").val(ui.item.label); // display the selected text
      $("#txtAllowSearchID").val(ui.item.value); // save selected id to hidden input
  }
});

$('#button').click(function() {
    alert($("#txtAllowSearchID").val()); // get the id from the hidden input
});
*/
