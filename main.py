from flask import Flask, request, render_template

# Hjaelper builder til at finde routes
app = Flask(__name__)

# This routes different pages in your App using python functions
# @ signifies a decorator - a way to wrap a function and modifying its behavior
@app.route("/")  # root dir
def hello_flask():
    return "Hello Flask!"

@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)  # hver side skal have en return

# Tuna page
@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

# Profile pages with custom names
@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

# use Integer with pages in url
@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>Post ID is %s" % post_id

@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)

# checks if we only run the app/server when this python file is called
if __name__ == "__main__":
    app.run(debug=True)