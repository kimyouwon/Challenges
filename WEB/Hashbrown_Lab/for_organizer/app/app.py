import os
import redis
import random
import string
from flask import Flask, request, render_template
from hash import hashbrown

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_USERNAME = os.getenv("REDIS_USERNAME", "gamja")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

r = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
    decode_responses=True
)

HASH, BROWN = hashbrown()

key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

random_fields = {
    ''.join(random.choices(string.ascii_letters + string.digits, k=32)): ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    for _ in range(20)
}

for field, value in random_fields.items():
    r.hset("hashbrown_recipe", field, value)

# Flag is here
r.hset("hashbrown_recipe", f"{key}_HASH", HASH)
r.hset("hashbrown_recipe", f"{key}_BROWN", BROWN)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        cmd = request.form.get("cmd", "").strip()

        try:
            response = r.execute_command(cmd)
            result = f"{response}"
        except Exception as e:
            result = f"E: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)