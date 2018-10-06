# Casechek Coding Interview

### Install (Mac OSX)
1. Be sure to have homebrew installed:
```
$ xcode-select --install
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. `cd` into project and run `install.sh`:
```
$ cd casechek_coding_challenge; sh install.sh
```
This may take a few minutes.

### Run
1. run `start.sh`:
```
$ sh start.sh
```
This should start up the flask app on `localhost:5000` in the terminal window. You should see a message that the app has started.

### Specifications
This REST API allows interaction with the `hospitals` database. By default, it runs on `localhost:5000`. The supported routes are:
- `GET /hospitals/`: returns collection of all hospitals in database
- `GET /hospitals/<id>`: returns hospital corresponding to `id`
- `POST /hospitals`: inserts hospital entry into database
- `PUT /hospitals/<id>`: updates hospital entry corresponding to `id`
- `DELETE /hospitals/<id>`: deletes hospital corresponding to `id`

Filtering by field is supported for `GET` requests with the following syntax:

`localhost:5000/<resource>?filter=field1=val1`

To make a request using cURL, use the following template:
```
curl -X [GET|POST|PUT|DELETE] [-d arg1=val1 -d arg2=val2 ...] localhost:5000/<resource>/<id> 
```

Author: Tom Large (thomaslarge2019@u.northwestern.edu)