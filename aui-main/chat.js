function escapeHtml(unsafe) {
    return unsafe
       // .replace(/&/g, "&amp;")
     // .replace(/"/g, "\"")
     // .replace(/'/g, "\'");
}

document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submission
        if (document.getElementsByClassName('dummy-entry').length > 0) return;
        document.getElementById('send-button').click(); // Trigger the button click
    }
});

document.getElementById('send-button').onclick = async function() {
    if (document.getElementsByClassName('dummy-entry').length > 0) return;

    const userInput = document.getElementById('user-input').value;
    newDummyEntry(userInput);
    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: escapeHtml(userInput) })
    });
    const data = await response.json();
    removeDummyEntry();

    newMessageEntry(data.prompt, data.message);
};


function newMessageEntry(highlightedPrompt, response) {
    let chatbox = document.getElementById('chatbox');

    let safeHighlightedPrompt = escapeHtml(highlightedPrompt);
    let safeResponse = escapeHtml(response);

    let chatMsg = `
        <li class="message-container right">
            <div class="message right">
                <img class="logo" src="nerd.png" alt="">
                <p>${safeHighlightedPrompt}</p>
            </div>
        </li>`;
    chatbox.innerHTML += chatMsg;

    chatMsg = `
        <li class="message-container left">
            <div class="message left">
                <img class="logo" src="ollama.png" alt="">
                <p>${safeResponse}</p>
            </div>
        </li>`;
    chatbox.innerHTML += chatMsg;


    // Scroll to the bottom of the chatbox
    chatbox.scrollTop = chatbox.scrollHeight;
}

function newDummyEntry(message) {
    let chatbox = document.getElementById('chatbox');

    let safeMessage = escapeHtml(message);

    let chatMsg = `
        <li class="message-container right dummy-entry">
            <div class="message right">
                <img class="logo" src="nerd.png" alt="">
                <p>${safeMessage}</p>
            </div>
        </li>`;
    chatbox.innerHTML += chatMsg;

    chatMsg = `
        <li class="message-container left dummy-entry">
            <div class="message left">
                <img class="logo" src="ollama.png" alt="">
                <div id="loading-icon" class="loading-icon" style="display: block;">
                    <img id="loading-img" src="loading.gif" alt="Loading...">
                </div>
            </div>
        </li>`;
    chatbox.innerHTML += chatMsg;

    document.getElementById('user-input').value = '';

    // Make the send button gray
    document.getElementById('send-button').style.backgroundColor = '#848484';

    // Scroll to the bottom of the chatbox
    chatbox.scrollTop = chatbox.scrollHeight;

}

function removeDummyEntry() {
    var toRemove = [];
    for (let i = 0; i < document.getElementsByClassName('dummy-entry').length; i++){
        toRemove.push(document.getElementsByClassName('dummy-entry')[i]);
    }
    for (let i = 0; i < toRemove.length; i++){
        toRemove[i].remove();
    }
    // make the button background-color: #007bff; again
    document.getElementById('send-button').style.backgroundColor = '#007bff';
}


window.newMessageEntry = newMessageEntry;
window.escapeHtml = escapeHtml;
window.newDummyEntry = newDummyEntry;
window.removeDummyEntry = removeDummyEntry;
export { newMessageEntry, escapeHtml, newDummyEntry, removeDummyEntry};
