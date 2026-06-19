document.addEventListener('DOMContentLoaded', () => {
    const checkBtn = document.getElementById('checkBtn');
    const messageInput = document.getElementById('messageInput');
    const resultContainer = document.getElementById('resultContainer');
    const resultLabel = document.getElementById('resultLabel');
    const probabilityBadge = document.getElementById('probabilityBadge');
    const progressBar = document.getElementById('progressBar');
    const resultText = document.getElementById('resultText');
    const spinner = document.getElementById('spinner');
    const btnText = checkBtn.querySelector('span');

    checkBtn.addEventListener('click', async () => {
        const text = messageInput.value.trim();
        
        if (!text) {
            messageInput.style.transform = 'translateX(5px)';
            setTimeout(() => messageInput.style.transform = 'translateX(-5px)', 100);
            setTimeout(() => messageInput.style.transform = 'translateX(0)', 200);
            return;
        }

        resultContainer.classList.add('hidden');
        document.body.className = ''; 
        progressBar.style.width = '0%';
        
        checkBtn.disabled = true;
        btnText.textContent = 'Analyzing...';
        spinner.classList.remove('hidden');

        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            resultContainer.classList.remove('hidden');
            
            setTimeout(() => {
                if (data.prediction === 1) {
                    document.body.classList.add('theme-spam');
                    resultLabel.textContent = 'High Risk Detected';
                    probabilityBadge.textContent = `${data.spam_probability}% Spam`;
                    progressBar.style.width = `${data.spam_probability}%`;
                    resultText.textContent = `Caution! Our AI is highly confident that this message is a scam or spam. Do not click any links or send money.`;
                } else {
                    document.body.classList.add('theme-ham');
                    resultLabel.textContent = 'Appears Safe';
                    probabilityBadge.textContent = `${data.ham_probability}% Safe`;
                    progressBar.style.width = `${data.ham_probability}%`;
                    resultText.textContent = `This message seems to be a normal communication. However, always stay alert with unknown senders.`;
                }
            }, 50);

        } catch (error) {
            console.error('Error:', error);
            resultContainer.classList.remove('hidden');
            resultLabel.textContent = 'Connection Error';
            probabilityBadge.textContent = 'N/A';
            progressBar.style.width = '0%';
            resultText.textContent = 'Make sure your Python server is running (python app.py).';
        } finally {
            checkBtn.disabled = false;
            btnText.textContent = 'Analyze Message';
            spinner.classList.add('hidden');
        }
    });
});
