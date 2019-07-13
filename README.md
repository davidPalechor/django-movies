# Django movies
A RESTful application built in Python 3.7 and Django 2.2

## Build and Run Docker Container
* `docker-compose build`
* `docker-compose up`

# To Apply Migrations
* `docker-compose exec web python manage.py migrate`
# To Create Superusers
* `docker-compose exec web python manage.py createsuperuser`
* Complete all blank fields.
* Go to `localhost:8000/admin` and you should be able to login.

## Using the App (web)
* go to `localhost:8000`

## Requesting the API
* *GET* `localhost:8000/api/movie/list_movies`
* *POST* `localhost:8000/api/movie/create_movie`

For POST method the test data is like:
```javascript
{
	"title": "The Shining",
	"director": "Stanley Kubrick",
	"writer": "same",
	"stars": "4",
	"summary": "Mad Mad at A Hotel",
	"year": "1976",
	"category": "thriller",
	"username": "serpalmop"
}
```

**All methods were tested via [postman](https://www.getpostman.com/)** except GET method, which you can test in your browser typing the link described previously.