# Quotes Rest API
---

### This REST API is created to use with my portfolio site.
---

### Docs
---

#### Available Routes (Public)
	GET
	* /quotes
	* /quote/id
	* /quote/random

#### Available Routes (Protected)
	POST
	* /quotes - Creates a new quote, required: quote_description, quote_author
	* /register - Registers a new user, required: username,password
	
	PUT
	* /quotes/id - Updates or Creates a quote, required: quote_description, quote_author
	
	DELETE
	* /post/id

#### Auth Routes
	POST
	* /login - Returns access_token, required: username, password
	* Use in format: Authorization: Bearer access_token

