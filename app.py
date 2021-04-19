from flask import Flask ,  render_template
from data import Articles

app = Flask(__name__)

app.debug = True  #오류 메세지를 보기위해 True 로 함. 디폴트는 False

@app.route('/', methods=['GET']) # 데코레이터(@)
def index():
    # return "Hello World"
    return render_template("index.html", data="KIM")

@app.route('/about')                                     
def about():
    return render_template("about.html",hello = "Gary Kim")        #서버는 1개 라우팅을 2개 한것 /data, /about

@app.route('/articles')                                     
def articles():
    articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html",articles = articles)  

if __name__ == '__main__':   # 여기서 부터 시작.
    app.run()