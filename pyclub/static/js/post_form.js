var languageOverrides = {
  js: 'javascript',
  html: 'xml',
  htmlmixed: 'xml'
};

var md = markdownit({
  html: true,
  highlight: function(code, lang) {
    if (languageOverrides[lang]) {
      lang = languageOverrides[lang];
    }
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(lang, code).value;
    }

    return '';
  }
});

emojify.setConfig({
  img_dir: '/static/emojify.js/dist/images/basic'
});

function update(editor) {
  var out = document.getElementById('out');
  var old = out.cloneNode(true);

  out.innerHTML = md.render(editor.getValue());
  emojify.run(out);

  var allold = old.getElementsByTagName('*');
  if (allold === undefined) {
    return;
  }

  var allnew = out.getElementsByTagName('*');
  if (allnew === undefined) {
    return;
  }

  for (var i = 0, max = Math.min(allold.length, allnew.length); i < max; i++) {
    if (!allold[i].isEqualNode(allnew[i])) {
      out.scrollTop = allnew[i].offsetTop;
      return;
    }
  }
}

var editor = CodeMirror.fromTextArea(document.getElementById('id_body'), {
  mode: 'gfm',
  lineNumbers: false,
  matchBracket: true,
  lineWrapping: true,
  theme: 'base16-light',
  extraKeys: {"Enter": "newlineAndIndentContinueMarkdownList"}
});

editor.on('change', update);
update(editor);
editor.focus;
