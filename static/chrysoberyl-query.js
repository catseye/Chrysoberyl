/* Chrysoberyl query functionality */
var chrysoberyl = null;
var selected_type = "Programming Language";
$(window).load(function() {
  
  $('#load_button').click(function() {
    $.ajax({
      url: "chrysoberyl.json",
      cache: false,
      dataType: 'json'
    }).done(function(json) {
      chrysoberyl = json;
      $('#load_button').html("Reload");
    });
    $('#load_button').html("Please wait...");
    $('#results').html("");
  });
  
  $('#query_button').click(function() {
    var results = "";
    if (chrysoberyl === null) return;
    $.each(chrysoberyl, function(key, val) {
      if (val['type'] === selected_type) {
        results += "<p>" + key + "</p>";
      }
    });
    $('#results').html(results);
  });
  
  $('#type_selector').change(function() {
    selected_type = $('#type_selector option:selected').text();
  });
});
