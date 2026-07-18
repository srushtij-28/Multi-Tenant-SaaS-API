from flask import Flask, request, jsonify
from models import db, Customer

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///tenant.db"

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------- Add Customer ----------
@app.route("/customers", methods=["POST"])
def add_customer():

    data = request.get_json()

    customer = Customer(
        tenant_id=data["tenant_id"],
        name=data["name"]
    )

    db.session.add(customer)
    db.session.commit()

    return jsonify({
        "message": "Customer Added"
    })


# ---------- Get Customers by Tenant ----------
@app.route("/customers")
def get_customers():

    tenant = request.headers.get("X-Tenant-ID")

    customers = Customer.query.filter_by(
        tenant_id=tenant
    ).all()

    return jsonify([
        {
            "id": c.id,
            "name": c.name
        }
        for c in customers
    ])


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)
