from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # templates 폴더 안의 index.html을 읽어서 보여줍니다.
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    # 폼에서 제출된 데이터를 받습니다
    submitted_data = {
        'username': request.form.get('username'),
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'name': request.form.get('name'),
        'address': request.form.get('address'),
        'phone': request.form.get('phone'),
        'previousUsageDate': request.form.get('previousUsageDate'),
        'previousCampingCarType': request.form.get('previousCampingCarType')
    }
    
    # 데이터를 signup_result.html에 전달합니다
    return render_template('signup_result.html', submittedData=submitted_data)

if __name__ == '__main__':
    # 로컬에서 테스트 시 debug=True가 편리합니다.
    app.run(debug=True)