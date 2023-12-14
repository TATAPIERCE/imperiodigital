function toggleChat() {
    var chatContainer = document.getElementById('chat-container');
    chatContainer.style.display = chatContainer.style.display === 'none' ? 'block' : 'none';
}

function sendMessage() {
    var userMessage = document.getElementById('user-input').value.trim();
    if (userMessage === '') {
        return;
    }

    appendMessage('user', userMessage);

    var botResponse = getBotResponse(userMessage);
    appendMessage('bot', botResponse);

    document.getElementById('user-input').value = '';
}

function appendMessage(sender, message) {
    var chatbox = document.getElementById('chatbox');
    var senderClass = sender === 'user' ? 'user-message' : 'bot-message';
    var messageElement = document.createElement('div');
    messageElement.className = senderClass;
    messageElement.textContent = message;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}


function getBotResponse(userMessage) {
    console.log('Mensaje del usuario:', userMessage);

    const lowerCaseMessage = userMessage.toLowerCase();
    console.log('Mensaje convertido a minúsculas:', lowerCaseMessage);

    switch (lowerCaseMessage) {
        case 'hola':
            return '¡Hola! ¿En qué puedo ayudarte?';
        case 'tengo una duda sobre las agendas':
            return '¿Qué dudas tienes?';
        case 'como agendo una hora?':
            return 'En la barra de navegacion puedes ver la opcion de servicios, si le das click te llevara a los servicios y le debas dar click en el boton de agendar, completas el formulario y listo';
        case 'muchas gracias':
            return 'De nada, estoy para ayudar';
        case 'hola necesito ayuda con mi computador':
            return '¡Hola! ¿En qué puedo ayudarte?';
        case 'no enciende desde ayer que me puedes recomendar ?':
            return 'Te recomiendo escoger la opcion de reparación, esto se demora entre 1 a 2 días dependiendo del estado en que se encuentre';
        case 'hola mi computador esta lento':
            return 'Hola estimado cliente, deberias utilizar la opcion de reparacion, esto tarda de 3 a 4 horas dependiendo del estado en el que se encuentre';
        case 'cuanto debo pagar ?':
            return 'Primero debemos ver si es reutilizable el disco duro de su computadora para luego cotizarle uno nuevo, el valor varia entre 20.000 mil a 50.000 mil pesos.';
        case 'muchas gracias':
            return 'De nada, estoy para ayudar';
        default:
            return 'No entiendo. ¿Puedes preguntar de otra manera?';
    }
}