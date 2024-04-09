from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return HttpResponse(
        """
        <h1>Welcome to Home Page</h1>

        <p>This is the home page</p>

        <a href="/about">About</a>

        <a href="/contact">Contact</a>
        """
        
    
    )

def about(request):
    return HttpResponse(
        """
        <p>This is the about page</p>

        <a href="/">Home</a>

        <a href="/contact">Contact</a>
        """
    )

def contact(request):
    return HttpResponse(
        """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contacto</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #F4F4F4;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    width: 80%;
                    margin: 50px auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                }
                .form-group {
                    margin-bottom: 20px;
                }
                label {
                    display: block;
                    margin-bottom: 5px;
                }
                input[type="text"],
                input[type="email"],
                textarea {
                    width: calc(100% - 10px);
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 3px;
                }
                button {
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: #fff;
                    border: none;
                    border-radius: 3px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056B3;
                }
                button:focus {
                    outline: none;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Contacto</h1>
                <form action="#" method="post">
                    <div class="form-group">
                        <label for="nombre">Nombre:</label>
                        <input type="text" id="nombre" name="nombre" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email:</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="mensaje">Mensaje:</label>
                        <textarea id="mensaje" name="mensaje" rows="4" required></textarea>
                    </div>
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </body>
        </html>
        """
    )