/* Chrysoberyl query functionality */
var chrysoberyl = null;

var selected_type = '(all)';
var selected_author = '(any)';

function draw_chart(dict) {
  if (!!document.createElement('canvas').getContext) {
      var mychart = new AwesomeChart('chart');
      mychart.chartType = "pie";
      mychart.title = "Breakdown";
      mychart.data = [];
      mychart.labels = [];
      $.each(dict, function(key, value) {
        mychart.labels.push(key);
        mychart.data.push(value);
      });
      var canvas = $('#chart').get(0);
      var context = canvas.getContext('2d');
      context.clearRect(0, 0, canvas.width, canvas.height);
      mychart.draw();
  }
}

function load_chrysoberyl_data() {
  $.ajax({
    url: "chrysoberyl.json",
    cache: false,
    dataType: 'json'
  }).done(function(json) {
    chrysoberyl = json;
    $('#status').html("Ready.");
  });
  $('#status').html("Please wait...");
  $('#results').html("");
}

function run_query() {
  var results = "";
  var licenses = {};
  if (chrysoberyl === null) return;
  $.each(chrysoberyl, function(key, node) {
    if (node['type'] === selected_type) {
      if (selected_author === '(any)' ||
          (node['authors'] !== undefined &&
           node['authors'].indexOf(selected_author) >= 0)) {
        results += "<p>" + key + "</p>";
        if (node['license'] !== undefined) {
          if (licenses[node['license']] === undefined) {
            licenses[node['license']] = 0;
          }
          licenses[node['license']] += 1;
        }
      }
    }
  });
  $('#results').html(results);
  draw_chart(licenses);
}

$(window).load(function() {
  load_chrysoberyl_data();  
  
  $('#type_selector').change(function() {
    selected_type = $('#type_selector option:selected').text();
    run_query();
  });

  $('#author_selector').change(function() {
    selected_author = $('#author_selector option:selected').text();
    run_query();
  });
});
