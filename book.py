from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

@app.route("/")
def Greeting():
    return"<h1>Welcome Book API!</h1>"

# Create (POST) operation สร้างBook
@app.route('/books', methods=['POST'])#ส่งออกมาเป็นpost 
def create_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book), 201 #create 201

# Read (GET) operation - Get all books
@app.route('/books', methods=['GET']) #รีเควสผ่านbooks -> /books
def get_all_books():
    return jsonify({"books": books}) #http://158.108.97.166:5000/books

# Read (GET) operation - Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404
    
# Update (PUT) operation
@app.route('/books/<int:book_id>', methods=['PUT']) #การupdate เรียกว่า PUT->แก้ไขทั้งหมด
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None) #search book ที่มีID Client
    if book:
        data = request.get_json()
        book.update(data) #หนังสือใหม่มาทำการ Update 
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404 #หาไม่เจอ
    
# Delete operation
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id] #อันไหนตรง = เอาออก // ถ้าไม่ตรง = เก็บไว้
    return jsonify({"message": "Book deleted successfully"})
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)