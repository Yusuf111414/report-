from flask import Flask, request, jsonify
from info import User, Gender

app = Flask(__name__)


db: list[User] = [
    User(
        first_name="yusuf",
        last_name="sobhy",
        id=42023232,
        gender=Gender.MALE
    )
]

@app.route('/', methods=['GET'])
def saying_hi():
    return "hi, userrrrr"

@app.route("/", methods=['POST'])
def getting_user_info(): 
    data = request.get_json()
    user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        id=data["id"],
        gender=Gender(data["gender"])
    )
    db.append(user)
    return jsonify({"message": "User added successfully!"})

@app.route("/api", methods=["GET"])
def show_users():
    return jsonify([user.__dict__ for user in db])

if __name__ == "__main__":
    app.run(debug=True)
