# Flask-SQLAlchemy Lab 1 - Earthquake API

A small Flask backend for Seismic Analytics Co. that stores earthquake data in a
SQLite database and returns it as JSON. It replaces the old spreadsheet tracking
so frontend tools (maps, graphs, etc.) can pull earthquake records from an API.

## Features

- `Earthquake` model built with Flask-SQLAlchemy (id, magnitude, location, year)
- Database created and versioned with Flask-Migrate
- Seed script that loads 5 real earthquakes into the database
- Look up a single earthquake by its id
- Get every earthquake at or above a given magnitude, along with a count
- Returns a 404 JSON message when an earthquake id doesn't exist

## Screenshots

**Get an earthquake by id** - `GET /earthquakes/1`

![Earthquake found by id](assets/Screenshot%202026-11-10%20201855.png)

**Earthquake id not found (404)** - `GET /earthquakes/7`

![Earthquake not found](assets/Screenshot%202026-11-10%20201925.png)

**Get earthquakes by minimum magnitude** - `GET /earthquakes/magnitude/8`

![Earthquakes filtered by magnitude](assets/Screenshot%202026-11-10%20201825.png)

## Installation

Clone the repo, then install the dependencies and start the virtual environment:

```console
$ pipenv install
$ pipenv shell
```

Move into the `server` folder and set the Flask environment variables:

```console
$ cd server
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

Create the database and seed it:

```console
$ flask db upgrade head
$ python seed.py
```

## Usage

Start the server from the `server` folder:

```console
$ flask run
```

The API will be running at http://127.0.0.1:5555.

### Endpoints

| Method | Route | Description |
| ------ | ----- | ----------- |
| GET | `/` | Welcome message |
| GET | `/earthquakes/<id>` | Returns one earthquake by id, or a 404 message if it isn't found |
| GET | `/earthquakes/magnitude/<magnitude>` | Returns the count and list of earthquakes with a magnitude greater than or equal to the value |

### Example responses

`GET /earthquakes/2`

```json
{
  "id": 2,
  "location": "Alaska",
  "magnitude": 9.2,
  "year": 1964
}
```

`GET /earthquakes/9999` (404)

```json
{
  "message": "Earthquake 9999 not found."
}
```

`GET /earthquakes/magnitude/9.0`

```json
{
  "count": 2,
  "quakes": [
    {
      "id": 1,
      "location": "Chile",
      "magnitude": 9.5,
      "year": 1960
    },
    {
      "id": 2,
      "location": "Alaska",
      "magnitude": 9.2,
      "year": 1964
    }
  ]
}
```

If no earthquakes match, the count is `0` and `quakes` is an empty list.

## Running the Tests

From the `server` folder:

```console
$ pytest
```

Or run each test file on its own:

```console
$ pytest testing/models_test.py
$ pytest testing/app_earthquake_test.py
$ pytest testing/app_magnitude_test.py
```

## Built With

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Pytest

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE.md](LICENSE.md).
