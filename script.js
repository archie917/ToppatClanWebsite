// script.js
function saveToFile() {
    const input = document.getElementById('userInput').value;
    const blob = new Blob([input], { type: 'text/plain' });
    const anchor = document.createElement('a');
    anchor.href = URL.createObjectURL(blob);
    anchor.download = 'input.txt';
    anchor.click();
    URL.revokeObjectURL(anchor.href);
}
