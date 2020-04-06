from flask import Flask,jsonify, request, Response,json

app = Flask(__name__)

books =[
        {
            'name':'Green Eggs and Ham',
            'price':7.99,
            'isbn':978839400165
            },
        {
            'name':'The Cat In The Hat',
            'price':6.99,
            'isbn':9782371000193
            }
        ]
def validBook(bookObject):#sanitizing data
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False
#GET /books
@app.route('/books')
def get_books ():
    return jsonify({'books':books})
''' POST /books
{
  'name':'ABC', 'price':0.0,'isbn':numeric
}'''

@app.route('/books',methods=['POST'])
def add_books():
    request_data = request.get_json()
    if(validBook(request_data)):
        newBook={
        "name":request_data["name"],
        "price":request_data["price"],
        "isbn":request_data["isbn"]

        }
        books.insert(0, newBook)
        response = Response("",201,mimetype="application/json")
        response.headers['LOcation'] = '/books/'+str(newBook["isbn"])
        return response
    else:
        InvalidBookError = {
            "error":"Invalid Book Object passed in request",
            "help":"Valid Data is similar to this{'name':'bookname','price':7.39,'isbn':12345678910}"
            }
        response = Response(json.dumps(InvalidBookError),status=400,mimetype="application/json")
        return response

@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):  
    return_value ={}
    for book in books:
        if book['isbn'] == isbn:
           return_value={
               'name':book["name"],
               'price':book['price']
             }
    return jsonify(return_value)



            

app.run()
