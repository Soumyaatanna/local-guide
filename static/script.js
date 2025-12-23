document.addEventListener('DOMContentLoaded', function() {
    const userInput = document.getElementById('user-input');
    const submitBtn = document.getElementById('submit-btn');
    const responseArea = document.getElementById('response-area');
    const queryButtons = document.querySelectorAll('.query-btn');

    // Handle submit button click
    submitBtn.addEventListener('click', handleSubmit);
    
    // Handle enter key press
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            handleSubmit();
        }
    });

    // Handle example query button clicks
    queryButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const query = this.getAttribute('data-query');
            userInput.value = query;
            handleSubmit();
        });
    });

    function handleSubmit() {
        const query = userInput.value.trim();
        if (!query) return;

        // Show user query
        displayUserQuery(query);
        
        // Clear input and show loading
        userInput.value = '';
        setLoadingState(true);

        // Send request to Flask backend
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: query })
        })
        .then(response => response.json())
        .then(data => {
            displayResponse(data);
        })
        .catch(error => {
            console.error('Error:', error);
            displayError('Sorry, I encountered an error. Please try again.');
        })
        .finally(() => {
            setLoadingState(false);
        });
    }

    function displayUserQuery(query) {
        // Clear welcome message if it exists
        const welcomeMessage = responseArea.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        const queryDiv = document.createElement('div');
        queryDiv.className = 'response-message user-query';
        queryDiv.innerHTML = `<strong>You asked:</strong> ${query}`;
        
        responseArea.appendChild(queryDiv);
        responseArea.scrollTop = responseArea.scrollHeight;
    }

    function displayResponse(data) {
        const responseDiv = document.createElement('div');
        responseDiv.className = 'response-message';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'response-content';
        contentDiv.textContent = data.response || 'No response received.';
        
        const sourceDiv = document.createElement('div');
        sourceDiv.className = 'response-source';
        sourceDiv.textContent = data.source || 'Source: Local Guide';
        
        responseDiv.appendChild(contentDiv);
        responseDiv.appendChild(sourceDiv);
        responseArea.appendChild(responseDiv);
        
        responseArea.scrollTop = responseArea.scrollHeight;
    }

    function displayError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'response-message';
        errorDiv.style.borderLeftColor = '#e74c3c';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'response-content';
        contentDiv.textContent = message;
        contentDiv.style.color = '#e74c3c';
        
        errorDiv.appendChild(contentDiv);
        responseArea.appendChild(errorDiv);
        
        responseArea.scrollTop = responseArea.scrollHeight;
    }

    function setLoadingState(loading) {
        if (loading) {
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Thinking...';
            submitBtn.classList.add('loading');
            submitBtn.disabled = true;
        } else {
            submitBtn.innerHTML = 'Ask';
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
        }
    }

    // Add some interactive feedback
    userInput.addEventListener('input', function() {
        if (this.value.trim()) {
            submitBtn.style.background = 'linear-gradient(135deg, #667eea, #764ba2)';
        } else {
            submitBtn.style.background = 'linear-gradient(135deg, #95a5a6, #7f8c8d)';
        }
    });

    // Focus on input when page loads
    userInput.focus();
});