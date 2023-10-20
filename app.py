from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        else:
            return False

    def return_book(self):
        self.copies += 1

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        return user  # Return the user object

    def display_books(self):
        return self.books

    def borrow_book(self, user_name, title):
        user = self.find_user(user_name)
        if not user:
            raise ValueError("User not found.")
        for book in self.books:
            if book.title == title:
                user.borrow_book(book)
                return True
        raise ValueError("Book not found.")

    def return_book(self, user_name, title):
        user = self.find_user(user_name)
        if not user:
            raise ValueError("User not found.")
        for book in user.borrowed_books:
            if book.title == title:
                user.return_book(book)
                return True
        raise ValueError("Book not found.")

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

library = Library()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        try:
            user = library.register_user(name)
            return redirect(url_for('user_profile', user_name=user.name))
        except ValueError as e:
            return render_template('error.html', error=str(e))
    return render_template('register.html')

@app.route('/user_profile/<user_name>')
def user_profile(user_name):
    user = library.find_user(user_name)
    if user:
        return render_template('user_profile.html', user_name=user.name, borrowed_books=user.borrowed_books)
    return render_template('error.html', error="User not found.")

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        copies = int(request.form['copies'])
        library.add_book(title, author, copies)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/display_books')
def display_books():
    books = library.display_books()
    return render_template('display_books.html', books=books)

@app.route('/borrow_book', methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        user_name = request.form['user_name']
        title = request.form['title']
        try:
            if library.borrow_book(user_name, title):
                return redirect(url_for('index'))
        except ValueError as e:
            return render_template('error.html', error=str(e))
    return render_template('borrow_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        user_name = request.form['user_name']
        title = request.form['title']
        try:
            if library.return_book(user_name, title):
                return redirect(url_for('index'))
        except ValueError as e:
            return render_template('error.html', error=str(e))
    return render_template('return_book.html')

if __name__ == '__main__':
    app.run(debug=True)
