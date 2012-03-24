
$(document).ready(function() {
  var PythonMode, editor;
  editor = ace.edit('editor');
  editor.setTheme('ace/theme/twilight');
  PythonMode = require('ace/mode/python').Mode;
  editor.getSession().setMode(new PythonMode());
  return $('.btn-submit').click(function() {
    var code;
    code = editor.getSession().getValue();
    return $.ajax({
      type: 'POST',
      url: '/v1/python/2.7.1',
      data: JSON.stringify({
        code: code
      }),
      contentType: "application/json; charset=utf-8",
      success: function(data, textStatus, jqXHR) {
        console.log(data, textStatus, jqXHR);
        console.log(data.results);
        return $('#results').text(data.results);
      }
    });
  });
});
