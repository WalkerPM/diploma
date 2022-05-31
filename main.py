from flask import Flask, jsonify, request
import data_aggregation as dg
import cache

app = Flask(__name__)

@app.route("/")
def selftest():
    return jsonify()

@app.route("/api/get_info", methods=["POST"] )
def get_info():
    raw_body = request.json
    if 'uid' in raw_body:
        uid = raw_body['uid']
    if cache.get_data(uid) != None:
        data = cache.get_data(uid)
        data['from_cache'] = True
    else:
        data = dg.get_data(uid).__dict__
        del data['_sa_instance_state']
        cache.set_data(uid,data)
    return jsonify(data)

if __name__ == "__main__":
    app.run()