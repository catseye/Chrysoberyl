document.createElement('header');
document.createElement('nav');
document.createElement('article');
document.createElement('footer');
document.createElement('aside');

$(window).load(function() {
  $('a').each(function (i) {
    var href = $(this).attr('href');
    if (href.substring(0, 7) == "http://" || href.substring(0, 8) == "https://") {
      if (href.substring(0, 17) != "http://catseye.tc") {
        $(this).addClass('external');
      }
    }
  });
});
