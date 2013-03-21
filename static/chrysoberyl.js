/*
 * Requires jQuery.
 * Can be loaded at the bottom of the page.
 */

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
 * Given a block element specifier, expand it so that the height of
 * the body matches the height of the displayed page.
 * This is aesthetically nice for pushing footers down to the bottom of the
 * page, on short pages.
 * This is designed to only be run once, at window load time, because as
 * they say, browser resizing is a developer activity.
 */
function expand_element(element) {
  var extra_room = $(window).height() - $('body').height();
  if (extra_room > 0) {
    $(element).height($(element).height() + extra_room);
  }
}

$(window).load(function() {
  add_class_to_external_links('external', "http://catseye.tc");
  expand_element('article');
});
