# Meal Planner

Food tracker, recipe database, meal planner and shopping list in one app.

## Apps

Here is a description of the various Django apps in this project.

### [`food`](food)

This stores all raw types of food that the app knows about. Everything from "Orange" to "Tesco Margarita Pizza".

### [`planner`](planner)

This stores meals and plan for when the user wants to eat them, using recipes from the `recipes` app.

### [`recipes`](recipes)

This stores all the recipes that the app know about, using ingredients from the `food` app.

### [`shopping`](shopping)

This stores all the shopping lists generated from the `planner` app or custom lists created by the user. It interacts with the supermarket APIs to automatically find prices and make orders.
