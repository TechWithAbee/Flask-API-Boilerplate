from flask import jsonify

def get_me_service():
    user = {"name": "Ibrohim Abdivokhidov", "website": "abdibrokhim.vercel.app"}
    return jsonify(user)