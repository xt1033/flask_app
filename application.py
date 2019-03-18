from flask import Flask, jsonify, request
from tester import insertion_into_psql, post_new, get_feed, del_post,update, robject
import psycopg2
import psycopg2.extras

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Called resource not found."})


@app.errorhandler(500)
def not_found_error(error):
    return jsonify({"error": "INTERNAL ERROR"})


@app.route('/signup', methods=['POST'])
def signup_table():
    try:
        inp = request.json
        name = inp["name"]
        username = inp["username"]
        email = inp["email"]
        res = insertion_into_psql(username, name, email)
        return jsonify({"message" : res})
    except Exception as e:
        return jsonify({"error": "error :: {}".format(e)})


@app.route("/posts", methods=['POST'])
def create_post():
    try:
        inp = request.json
        user_id = inp["user_id"]
        descreption = inp["descreption"]
        res = post_new(user_id, descreption)
        return jsonify({"message": res})
    except psycopg2.Error as e:
        return jsonify({"error": "{}".format(e)})
    except Exception as e:
        return jsonify({"error": "error :: {}".format(e)})


@app.route("/posts/<int:post_id>", methods=['DELETE'])
def delete_post(post_id):
    try:
        res = del_post(post_id)
        return jsonify({"message": res})
    except psycopg2.Error as e:
        return jsonify({"error": "{}".format(e)})
    except Exception as e:
        return jsonify({"error": "error :: {}".format(e)})


@app.route("/posts", methods=['GET'])
def get_post():
    try:
        res = get_feed()
        return jsonify({"message": res})
    except psycopg2.Error as e:
        return jsonify({"error": "{}".format(e)})
    except Exception as e:
        return jsonify({"error": "error :: {}".format(e)})


@app.route("/posts/<int:post_id>", methods=['PUT'])
def update_post(post_id):
    try:
        inp=request.json
        descreption=inp["descreption"]
        res = update(post_id, descreption)
        return jsonify({"message": res})
    except psycopg2.Error as e:
        return jsonify({"error": "{}".format(e)})
    except Exception as e:
        return jsonify({"error": "Request format is incorrect."})

'''
@app.route("/count/<string:query>", methods=['GET'])
def count_of_hits(query):
    if query == "insert":
        return jsonify({"Count is": robject.get('insert_table').decode('utf-8')})
    elif query == "show":
        return jsonify({"Count is": robject.get('get_post').decode('utf-8')})
    elif query == "post":
        return jsonify({"Count is": robject.get('post_feed').decode('utf-8')})
    elif query == "delete":
        return jsonify({"Count is": robject.get('delete_post').decode('utf-8')})
    elif query == "update":
        return jsonify({"Count is": robject.get('update_post').decode('utf-8')})
    else:
        return jsonify({"Invalid query"})
'''

if __name__ == '__main__':
    app.run(debug=True)
