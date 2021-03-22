# Udo
A todo site project.

## API

To signup: https://udo.pythonanywhere.com/signup
To login: http://udo.pythonanywhere.com/api/login
To view todos: https://udo.pythonanywhere.com/api/todos
To view completed todos: https://udo.pythonanywhere.com/api/todos/completed
To mark a todo complete: https://udo.pythonanywhere.com/api/todos/<id>/complete

## How to curl?
Note: Below instructions are for localhost:8000
### To signup through curl
curl -H "Content-Type: application/json" -X POST http://localhost:8000/api/signup -d "{\"username\":\"<username>\", \"password\":\"<password>\"}"

### To login through curl
curl -H "Content-Type: application/json" -X POST http://localhost:8000/api/login -d "{\"username\":\"<username>\", \"password\":\"<password>\"}"

### Adding a todo to complete
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Token <token_value>" http://localhost:8000/api/todos/7/complete

### To access todos of a tokened user through curl
curl http://localhost:8000/api/todos/ -H "Authorization: Token <token_value>"
