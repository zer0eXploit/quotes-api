# Quotes REST API

This REST API is created to feed my portfolio with programming quotes.

### Docs

#### Available Routes (Public)
	GET
	* /quotes
	* /quote/id
	* /quote/random

#### Available Routes (Protected)
	POST
	* /quotes - Creates a new quote, required: quote_description, quote_author
	* /register - Registers a new user, required: username, password
	
	PUT
	* /quotes/id - Updates or Creates a quote, required: quote_description, quote_author
	
	DELETE
	* /post/id

#### Auth Routes
	POST
	* /login - Returns access_token, required: username, password
	* Supply in header - Authorization: Bearer access_token
#### Run
	Please install requirements first.
	Please also supply your own environment variables.
	1. DB_URL
	2. APP_SECRET
	```python
	python3 app.py
	```

#### Live Demo
[quotes.yanwaipann.tech](https://quotes.yanwaipann.tech/quotes)
