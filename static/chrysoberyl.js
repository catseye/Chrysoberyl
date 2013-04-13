/*
 * Should be loaded at the bottom of the page.
 */

/*
 * Given a CSS class and local URL prefix, apply the class to all links
 * ('a' tags) on the page which are considered external.
 * A link is considered external if it begins with "http://" or "https://"
 * and does not begin with the local URL prefix.
 */
function addClassToExternalLinks(cssClass, localUrlPrefix) {
  var anchors = document.getElementsByTagName('a');
  for (var i = 0; i < anchors.length; i++) {
    var elem = anchors[i];
    var href = elem.href;
    if (href.substring(0, 16) == "http://127.0.0.1") continue;
    if (href.substring(0, 7) == "http://" || href.substring(0, 8) == "https://") {
      var prefix = href.substring(0, localUrlPrefix.length);
      if (prefix != localUrlPrefix) {
        elem.className += elem.className ? (' ' + cssClass) : cssClass;
      }
    }
  }
}

/*
 * Given two block elements, expand the first so that the second takes up
 * the remaining height of the visible document.
 * This is aesthetically nice for pushing footers down to the bottom of the
 * page, on short pages.
 * This is designed to only be run once, at window load time, because as
 * they say, browser resizing is a developer activity.
 */
function expandElementToFillDocument(article, footer) {
  extra_room =
      (document.documentElement.clientHeight - footer.clientHeight) -
      footer.offsetTop;
  newHeight = (article.clientHeight + extra_room) + "px";
  if (extra_room > 0) {
    article.style.height = newHeight;
  }
}

addClassToExternalLinks('external', "http://catseye.tc");
expandElementToFillDocument(
  document.getElementsByTagName('article')[0],
  document.getElementsByTagName('footer')[0]
);
