/*
 * Should be loaded at the bottom of the page.
 */

/*
 * Given a CSS class and list of internal URL prefixes, apply the class to
 * all links ('a' tags) in the document which are considered external.
 * A link is considered external if it begins with "http://" or "https://"
 * and does not begin with any of the internal URL prefixes.
 */
function addClassToExternalLinks(cssClass, internalPrefixes) {
  var anchors = document.getElementsByTagName('a');
  for (var i = 0; i < anchors.length; i++) {
    var elem = anchors[i];
    var href = elem.href;
    var decorate = true;
    for (var j = 0; j < internalPrefixes.length; j++) {
      var prefix = internalPrefixes[j];
      if (href.substring(0, prefix.length) === prefix) {
        decorate = false;
        break;
      }
    }
    if (decorate) {
      elem.className += elem.className ? (' ' + cssClass) : cssClass;
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

addClassToExternalLinks('external', [
  "http://catseye.tc",
  "http://www.catseye.tc",
  "http://127.0.0.1"
]);
expandElementToFillDocument(
  document.getElementsByTagName('article')[0],
  document.getElementsByTagName('footer')[0]
);
