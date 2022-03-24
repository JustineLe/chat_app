const roomName = JSON.parse($('#room_name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

// on message - An event listener to be called when a message is received from the server
chatSocket.onmessage = function(e) {
    // JSON.parse() convert the JSON object back into the original object,
    // then examine and act upon its contents.
    const data = JSON.parse(e.data);
    $('#chat-log').value += (data.message + '\n')
};

// on close - An event listener to be called when the connection is closed.
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

$('#chat-message-input').focus();
$('#chat-message-input').keyup = function(e) {
    if (e.keyCode === 13) {
        $('#chat-message-submit').click();
    }
};

$('#chat-message-submit').click = function(e) {
    const messageInputDom = $('#chat-message-input');
    const message = messageInputDom.value;

    // Send the msg object as a JSON-formatted string
    chatSocket.send(JSON.stringify({
        'message': message
    }));

    // Blank the text input element, ready to receive the next line of chat
    messageInputDom.value = '';
};
