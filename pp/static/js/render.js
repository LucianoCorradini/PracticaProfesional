
function render (container_id, template_id, data) {
    var template = $(template_id)[0].text;
    var html = _.template(template, data);
    $(container_id).html(html);
}
