/*
 * Requires jQuery.
 */

/*
 * First, trick older IE into letting us style HTML5 elements.
 */
document.createElement('header');
document.createElement('nav');
document.createElement('article');
document.createElement('footer');
document.createElement('aside');

/*
 * Given a CSS class and local URL prefix, apply the class to all links on
 * the page which are considered external.
 * A link is considered external if it begins with "http://" or "https://"
 * and does not begin with the local URL prefix.
 */
function add_class_to_external_links(css_class, local_url_prefix) {
  $('a').each(function (i) {
    var href = $(this).attr('href');
    if (href.substring(0, 7) == "http://" || href.substring(0, 8) == "https://") {
      if (href.substring(0, local_url_prefix.length) != local_url_prefix) {
        $(this).addClass(css_class);
      }
    }
  });
}

/*
 * Given a block element specifier, expand it do that the height of
 * the body matches the height of the displayed page.
 * This is aesthetically nice for pushing footers down to the bottom of the
 * page, on short pages.
 */
var initial_element_height = 0;
function expand_element(element) {
  if (initial_element_height == 0) {
    initial_element_height = $(element).height();
  }
  var extra_room = $(document).height() - $('body').height();
  if (extra_room > 0) {
    $(element).height(initial_element_height + extra_room);
  }
}

/*
 * Given a function and a delay in milliseconds, run the function after
 * that many milliseconds, but *only* if this function has not been called
 * before that time.
 */
var hysteresis = function(fun, delay) {
  var executionTimer;
  return function() {
    if (!!executionTimer) {
      clearTimeout(executionTimer);
    }
    executionTimer = setTimeout(fun, delay);
  };
}();

$(window).load(function() {
  add_class_to_external_links('external', "http://catseye.tc");
  expand_element('article');
});

$(window).resize(function() {
  hysteresis(function() { expand_element('article'); }, 200);
});
