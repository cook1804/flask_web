from flask import Flask ,  render_template, request ,redirect
from data import Articles
import pymysql


app = Flask(__name__)

app.debug = True  #오류 메세지를 보기위해 True 로 함. 디폴트는 False

db = pymysql.connect(             
    host ='localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan' 
)



@app.route('/' , methods=['GET']) # 데코레이터(@)    # method =['GET'] 이 디폴트 이다.
def index():
    # return "Hello World"
    return render_template("index.html", data="KIM")               # data, hello, articles, article 보다 = 다음이 중요하다.

@app.route('/about')                                     
def about():
    return render_template("about.html",hello = "Gary Kim")        #서버는 1개 라우팅을 2개 한것 /data, /about

@app.route('/articles')                                     
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    # print(topics)
    # articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html",articles = topics)

@app.route('/article/<int:id>')
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topics = cursor.fetchone()
    print(topics)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html",article = topics)

@app.route('/add_articles', methods = ["GET","POST"])               # GET
def add_articles():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc ,author]
        print(author, title, desc )
        
        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()
        return redirect("/articles")
    
    else:
        return render_template("add_articles.html")

@app.route('/delete/<int:id>', methods = ['POST'])
def delete(id):
    cursor = db.cursor()
    # sql = 'DELETE FROM topic WHERE id = %s;'                    #위     # 위에꺼랑 밑에꺼랑 같다. 
    # id = [id]
    # cursor.execute(sql,id)
    sql = 'DELETE FROM topic WHERE id = {};'.format(id)           #밑
    cursor.execute(sql)
    db.commit()

    return redirect("/articles")


if __name__ == '__main__':   # 여기서 부터 시작.
    app.run()