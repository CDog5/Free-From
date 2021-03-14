from flask import Flask,redirect,url_for,render_template,request,session,send_file
import json,random,uuid
from flask_restful import Api, reqparse,Resource







app = Flask(__name__)



@app.route('/')
def home():
    with open('recipes.json') as f:
        facts = json.load(f)
        facts = facts["recipes"]
    return render_template("index.html",recipes=facts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route('/recipejson/<id>/',methods=['POST','GET'])
def recipejson(id):
    with open('recipes.json') as f:
        facts = json.load(f)
        facts = facts["recipes"]
    for i in range(len(facts)):
        if facts[i]["id"] == id:
            recipe = facts[i]
    return recipe
@app.route('/recipe/<id>/',methods=['POST','GET'])
def recipe(id):
    with open('recipes.json') as f:
        facts = json.load(f)
        facts = facts["recipes"]
    for i in range(len(facts)):
        if facts[i]["id"] == id:
            recipe = facts[i]
    #return "<h1>Added Todo</h1><br><p>Title: {}</p><p> Description: {}</p>".format(title,desc)
    return render_template("recipe.html",recipe=recipe)

app.run("0.0.0.0")
