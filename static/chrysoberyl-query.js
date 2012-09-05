/* Chrysoberyl query functionality */
$(window).load(function() {
  $('#button').click(function() {
    $.ajax({
      url: "chrysoberyl.json",
      cache: false,
      dataType: 'json'
    }).done(function(json) {
      $('#button').html("Click me again");
      var results = "";
      $.each(json, function(key, val) {
        results += "<p>" + key + " " + val + "</p>";
      });
      $('#results').html(results);
    });
    $('#button').html("Please wait...");
    $('#results').html("");
  });
});
