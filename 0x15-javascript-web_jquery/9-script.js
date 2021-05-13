/*
   Fetches from URL and displays the value of hello from
   in the HTML’s tag DIV#hello
*/
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});