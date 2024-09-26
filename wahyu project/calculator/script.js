function appendToDisplay(value) {
    document.getElementById('display').innerText += value;
}

function clearDisplay() {
    document.getElementById('display').innerText = '';
}

function deleteLast() {
    let currentText = document.getElementById('display').innerText;
    document.getElementById('display').innerText = currentText.slice(0, -1);
}

function calculate() {
    try {
        let result = eval(document.getElementById('display').innerText);
        document.getElementById('display').innerText = result;
    } catch (error) {
        document.getElementById('display').innerText = 'Error';
    }
}
