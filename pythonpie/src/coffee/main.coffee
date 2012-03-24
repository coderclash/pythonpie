$(document).ready ->
  editor = ace.edit 'editor'
  editor.setTheme 'ace/theme/twilight'
  PythonMode = require('ace/mode/python').Mode
  editor.getSession().setMode new PythonMode()

  $('.btn-submit').click ->
    code = editor.getSession().getValue()
    $.ajax
      type: 'POST'
      url: '/v1/python/2.7.1'
      data: JSON.stringify {code: code}
      contentType: "application/json; charset=utf-8",
      success: (data, textStatus, jqXHR) ->
        console.log data, textStatus, jqXHR
        console.log data.results
        $('#results').text data.results
