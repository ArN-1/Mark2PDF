from flask import Flask, render_template, request, send_file
import markdown2
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    markdown_text = request.form['markdown_text']
    html_content = markdown2.markdown(markdown_text)
    return render_template('preview.html', html_content=html_content)

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    markdown_text = request.form['markdown_text']
    html_content = markdown2.markdown(markdown_text)
    pdf = HTML(string=html_content).write_pdf()
    return send_file(pdf, as_attachment=True, download_name='output.pdf')

if __name__ == '__main__':
    app.run(debug=True)
