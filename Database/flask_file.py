from flask import Flask, jsonify


class Food:
    """Represents a food item."""

    def __init__(self, food_id, name, price):
        self.food_id = food_id
        self.name = name
        self.price = price

    def to_dict(self):
        """Convert object to dictionary."""
        return {
            "id": self.food_id,
            "name": self.name,
            "price": self.price,
        }


app = Flask(__name__)


@app.route("/")
def home():
    """Home route."""
    return "Hello Flask!"


@app.route("/test")
def test():
    """Test route."""
    return "Test Method!"


@app.route("/displayItems")
def display_food_items():
    """Return list of food items."""
    food_items = [
        Food(101, "Burger", 100).to_dict(),
        Food(102, "Pizza", 200).to_dict(),
    ]
    return jsonify(food_items)


@app.route("/displayFood")
def display_food():
    """Return single food item."""
    food = Food(101, "Burger", 100)
    return jsonify(food.to_dict())


@app.route("/nums")
def nums():
    """Return list of numbers."""
    numbers = [10, 20, 30]
    return jsonify(numbers)


if __name__ == "__main__":
    app.run(debug=True)
