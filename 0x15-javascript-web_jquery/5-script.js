const $ = window.$;

const item = $('UL.my_list').html('<li>Item</li>');
$('DIV#add_item').on('click', function () {
  $(this).append(item);
});
