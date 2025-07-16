from flask import Flask

app = Flask(__name__)

# Dictionary of animal facts
animal_facts = {
    "elephant": "Elephants use their trunks to snorkel while swimming!",
    "giraffe": "A giraffe’s neck can be up to 6 feet long — same as a tall human!",
    "penguin": "Penguins propose to their mates with pebbles!",
    "octopus": "Octopuses have three hearts and blue blood!",
    "koala": "Koalas sleep up to 18–22 hours a day!"
}

@app.route("/fact/<animal>")
def fact_by_animal(animal):
    print(f"Accessed: /fact/{animal}")
    fact = animal_facts.get(animal.lower())
    if fact:
        return f"""
        <html>
        <head>
            <title>{animal.capitalize()} Fact</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 40px; background: #fff8e1; }}
                h1 {{ color: #4e342e; }}
                p {{ font-size: 1.3em; color: #6d4c41; }}
            </style>
        </head>
        <body>
            <h1>Did You Know?</h1>
            <p>{fact}</p>
        </body>
        </html>
        """
    else:
        return f"<h2>Sorry, no facts found for '{animal}'. Try <a href='/fact/list'>/fact/list</a></h2>"

@app.route("/fact/list")
def list_animals():
    print("Accessed: /fact/list")
    list_items = "".join([f"<li>{name.capitalize()}</li>" for name in animal_facts.keys()])
    return f"""
    <html>
    <head>
        <title>Available Animals</title>
        <style>
            body {{ font-family: Verdana, sans-serif; padding: 30px; background: #e1f5fe; }}
            h2 {{ color: #01579b; }}
            ul {{ font-size: 1.2em; color: #0277bd; }}
        </style>
    </head>
    <body>
        <h2>Animals with Fun Facts:</h2>
        <ul>
            {list_items}
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)