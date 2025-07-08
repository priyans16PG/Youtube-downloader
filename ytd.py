from flask import Flask, render_template_string, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)
status_message = ""

# HTML Templates
FORM_HTML = '''
<!doctype html><html><head><title>YouTube Downloader</title>
<style>
body { font-family: sans-serif; padding: 30px; background: #f9f9f9; }
.container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
input, select, button { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
button { background: #007bff; color: white; font-weight: bold; }
</style>
</head><body>
<div class="container">
  <h2>🎥 YouTube Downloader</h2>
  <form method="POST" action="/start">
    <input name="url" placeholder="YouTube URL" required>
    <select name="quality">
      <option value="low">Low (240p)</option>
      <option value="mid" selected>Mid (480p)</option>
      <option value="high">High (1080p)</option>
    </select>
    <button type="submit">⬇️ Download</button>
  </form>
  {% if message %}
    <p><b>{{ message }}</b></p>
  {% endif %}
</div></body></html>
'''

LOADING_HTML = '''
<!doctype html><html><head><title>Downloading...</title>
<meta http-equiv="refresh" content="5;URL=/">
<style>
body { font-family: sans-serif; text-align: center; padding: 50px; }
.loader {
  border: 6px solid #f3f3f3; border-top: 6px solid #3498db;
  border-radius: 50%; width: 50px; height: 50px;
  animation: spin 1s linear infinite; margin: auto;
}
@keyframes spin { 100% { transform: rotate(360deg); } }
</style></head><body>
<h2>📥 Download in Progress...</h2>
<div class="loader"></div>
<p>You will be redirected when done.</p>
</body></html>
'''

def get_quality_format(choice):
    presets = {
        "low": ("bestvideo[height<=240]+bestaudio/best", "240p"),
        "mid": ("bestvideo[height<=480]+bestaudio/best", "480p"),
        "high": ("bestvideo[height<=1080]+bestaudio/best", "1080p"),
    }
    return presets.get(choice, presets["mid"])

@app.route('/')
def index():
    global status_message
    msg = status_message
    status_message = ""
    return render_template_string(FORM_HTML, message=msg)

@app.route('/start', methods=['POST'])
def start_download():
    url = request.form['url']
    choice = request.form['quality']
    quality_format, label = get_quality_format(choice)

    # Save the download job and redirect
    download_video(url, quality_format, label)
    return render_template_string(LOADING_HTML)

def download_video(url, quality_format, label):
    global status_message
    save_path = "/storage/4A0D-AC71/Movies/yt"
    os.makedirs(save_path, exist_ok=True)
    try:
        subprocess.run([
            "yt-dlp",
            "-f", quality_format,
            "-S", "res:1080,ext:mp4",
            "--merge-output-format", "mp4",
            "-o", os.path.join(save_path, "%(title)s.%(ext)s"),
            url
        ])
        status_message = f"✅ Downloaded in {label} to {save_path}"
    except Exception as e:
        status_message = f"❌ Download failed: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)