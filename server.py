from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    #return redirect("result.html")
    #print(request.form)
    return render_template("result.html")

@app.route("/danger")
def danger():
    print("*" * 42)
    print("***** A user accessed 'danger' page! *****")
    print("*" * 42)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
