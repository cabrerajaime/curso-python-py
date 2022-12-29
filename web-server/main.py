import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Algo de HTML</title>
        </head>
        <body>
            <h1>Soy una Página de HTML!</h1>
            <p> Mi nombre es Jaime </p>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()