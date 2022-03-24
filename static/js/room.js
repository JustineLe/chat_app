const roomName = JSON.parse(document.getElementById('room_name').textContent);

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
    document.querySelector('#chat-log').value += (data.message + '\n')
};

// on close - An event listener to be called when the connection is closed.
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    // Send the msg object as a JSON-formatted string
    chatSocket.send(JSON.stringify({
        'message': message
    }));

    // Blank the text input element, ready to receive the next line of chat
    messageInputDom.value = '';
};
