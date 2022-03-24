$('#room-name-input').focus();
$('#room-name-input').keyup = function(e) {
    if (e.keyCode === 13) {
        $('#room-name-submit').click();
    }
};

$('#room-name-submit').click = function(e) {
    var roomName = $('#room-name-input').value;
    window.location.pathname = '/chat/' + roomName + '/';
};
