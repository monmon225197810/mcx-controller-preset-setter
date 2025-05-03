from flask import Flask, render_template, request, jsonify
from mcx_controller import MCXController
import threading
import time
import html

app = Flask(__name__)
mcx = MCXController()

def poll_current_preset():
    """定期的に現在のプリセット情報を取得"""
    while True:
        # ここでMCXコントローラーから現在のプリセット情報を取得する処理を実装
        time.sleep(int(mcx.config['MCX_CONTROLLER']['polling_interval']))

# ポーリングスレッドを開始
polling_thread = threading.Thread(target=poll_current_preset, daemon=True)
polling_thread.start()

@app.route('/')
def home():
    presets = mcx.get_preset_list()
    current_preset = mcx.get_current_preset()
    error_message = mcx.get_error_message()
    
    return render_template('index.html',
                         one_to_one_presets=presets['one_to_one'],
                         n_to_one_presets=presets['n_to_one'],
                         current_preset=current_preset,
                         error_message=error_message,
                         mcx=mcx)

@app.route('/load_preset', methods=['POST'])
def load_preset():
    preset_name = request.form.get('preset_name')
    if preset_name:
        success = mcx.load_preset(preset_name)
        error_message = mcx.get_error_message()
        
        if error_message:
            error_html = f'<div class="error-message alert alert-danger">{html.escape(error_message)}</div>'
        else:
            error_html = ''
            
        return jsonify({
            'success': success,
            'current_preset': mcx.get_current_preset(),
            'error_message': error_html
        })
    return jsonify({
        'success': False,
        'error_message': '<div class="error-message alert alert-danger">プリセット名が指定されていません</div>'
    })

if __name__ == '__main__':
    app.run(debug=True) 