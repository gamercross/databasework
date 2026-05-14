from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # templates 폴더 안의 index.html을 읽어서 보여줍니다.
    return render_template('index.html')

if __name__ == '__main__':
    # 로컬에서 테스트 시 debug=True가 편리합니다.
    app.run(debug=True)