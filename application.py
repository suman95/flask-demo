from flask import Flask
from neo4j import GraphDatabase

app = Flask(__name__)
driver = GraphDatabase.driver("bolt://localhost:7687", auth=('neo4j','pass'))

session = driver.session()

@app.route("/")
def test():
    return "Hello World"

if __name__ == "__main__":
    session.run()

    app.run(debug=True)