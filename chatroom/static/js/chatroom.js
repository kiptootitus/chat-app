// Connect to websocket
const chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + roomName + '/');

// When the websocket is opened
chatSocket.onopen = function (event) {
    console.log('Websocket connected.')
}

// When the websocket receives a message
chatSocket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    const message = data['message'];
    const sender = data['sender'];
    const timestamp = data['timestamp'];
    
    // Display the message in the chatroom
    const messageElement = document.createElement('div');
    messageElement.innerHTML = '<strong>' + sender + '</strong>: ' + message + ' <small>(' + timestamp + ')</small>';
    document.querySelector('#chat-log').appendChild(messageElement);
}

// When the form is submitted
document.querySelector('#chat-message-input').onsubmit = function (event) {
    event.preventDefault();
    const messageInputDom = document.querySelector('#chat-message-input input[name="message"]');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
}
