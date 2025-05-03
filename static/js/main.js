document.body.addEventListener('htmx:afterRequest', function(evt) {
    if (evt.detail.successful) {
        const response = JSON.parse(evt.detail.xhr.responseText);
        
        // エラーメッセージの更新
        const errorMessageDiv = document.getElementById('error-message');
        if (response.error_message) {
            errorMessageDiv.innerHTML = response.error_message;
        } else {
            errorMessageDiv.innerHTML = '';
        }
        
        // ボタンの状態を更新
        if (response.success) {
            document.querySelectorAll('.preset-button').forEach(button => {
                button.classList.remove('active-preset');
                if (button.getAttribute('hx-vals').includes(response.current_preset)) {
                    button.classList.add('active-preset');
                }
            });
        }
    }
}); 