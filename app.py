from flask import Flask, render_template, request
from main import news_summarization

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")

        try:
            obj = news_summarization(url)
            obj.fetch_article()

            if hasattr(obj, "text") and obj.text.strip():
                obj.summarization()
                obj.cleaning()
                summary = obj.cleaned_summary
            else:
                error = "❌ Could not fetch article. Try another URL."

        except Exception as e:
            error = f"❌ Error: {str(e)}"

    return render_template("index.html", summary=summary, error=error)


if __name__ == "__main__":
    app.run(debug=True)