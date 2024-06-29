document.getElementById('checkSpam').addEventListener('click', async () => {
    const email = document.getElementById('emailContent').value;
    const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email })
    });
    const data = await response.json();
    document.getElementById('result').innerText = data.prediction;
});
