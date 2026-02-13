
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Naty ❤️</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #1a1a1a; /* Fondo oscuro elegante */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
        }

        .container {
            text-align: center;
        }

        /* El Corazón */
        .heart {
            position: relative;
            width: 100px;
            height: 100px;
            background-color: #e74c3c;
            margin: 0 auto;
            transform: rotate(-45deg);
            animation: beat 1.2s infinite; /* Animación de latido */
            cursor: pointer;
            transition: transform 0.5s ease;
        }

        .heart::before,
        .heart::after {
            content: "";
            position: absolute;
            width: 100px;
            height: 100px;
            background-color: #e74c3c;
            border-radius: 50%;
        }

        .heart::before {
            top: -50px;
            left: 0;
        }

        .heart::after {
            top: 0;
            left: 50px;
        }

        /* Animación Latido */
        @keyframes beat {
            0% { transform: scale(1) rotate(-45deg); }
            15% { transform: scale(1.2) rotate(-45deg); }
            30% { transform: scale(1) rotate(-45deg); }
            45% { transform: scale(1.15) rotate(-45deg); }
            60% { transform: scale(1) rotate(-45deg); }
        }

        /* Mensaje Oculto */
        .message {
            margin-top: 80px;
            color: white;
            opacity: 0;
            transition: opacity 1s ease;
        }

        .heart:hover + .message, .heart:active + .message {
            opacity: 1;
        }

        h1 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1.1rem;
            color: #bdc3c7;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="heart"></div>
        <div class="message">
            <h1>¡Feliz San Valentín, Naty!</h1>
            <p>Aunque esté entre códigos y obras, mi corazón siempre compila contigo.</p>
            <p><strong>Te amo.</strong></p>
        </div>
    </div>

</body>
</html>