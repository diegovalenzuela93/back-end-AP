from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'evaluacion1_app/index.html')

def consolas(request):
    data = {"tipo" : "consolas",
            "titulo" : "Consolas",
            "producto1" : "PlayStation 5",
            "producto2" : "Xbox One",
            "producto3" : "Nintendo Switch",
            "foto1" : "play.jpg",
            "foto2" : "xbox.png",
            "foto3" : "nintendo.jpg"}
    return render(request, 'evaluacion1_app/productos.html', data)

def pc(request):
    data = {"tipo" : "pc",
            "titulo" : "PC GAMERS",
            "producto1" : "HP OMEN 16-B1001LA",
            "producto2" : "ACER NITRO 5",
            "producto3" : "ASUS TUF GAMING F15 FX506HC",
            "foto1" : "hp_omen.jpg",
            "foto2" : "acer.jpg",
            "foto3" : "asus.jpg"}
    return render(request, 'evaluacion1_app/productos.html', data)

def accesorios(request):
    data = {"tipo" : "accesorios",
            "titulo" : "Accesorios",
            "producto1" : "Mouse Logitech G502X",
            "producto2" : "Teclado HyperX",
            "producto3" : "Joystick Xbox Stellar Shift",
            "foto1" : "mouse.jpg",
            "foto2" : "teclado.jpg",
            "foto3" : "joystick.jpg"}
    return render(request, 'evaluacion1_app/productos.html', data)

def descripcion_consolas(request, producto_id):
    data = {
        '1': {
            "nombre" : "PlayStation 5",
            "descripcion" : "G502 X PLUS es la última adición a la legendaria gama G502. Reinventado con nuestros primerísimos interruptores híbridos LIGHTFORCE, tecnología inalámbrica LIGHTSPEED de nivel profesional, RGB LIGHTSYNC, sensor HERO 25K, etc. ",
            "foto" : ""
        },
        '2' : {
            "nombre" : "Xbox One serie S",
            "descripcion" : "Rendimiento de última generación en la consola Xbox más pequeña de la historia: La consola Xbox Series S, totalmente digital, ofrece juegos de próxima generación a un precio accesible. Experimenta la velocidad y el rendimiento de próxima generación con la arquitectura Xbox Velocity, impulsada por un SSD personalizado y software integrado. Juega miles de títulos de cuatro generaciones de Xbox con compatibilidad con versiones anteriores, incluidos títulos optimizados con el lanzamiento. Descarga y juega más de 100 juegos de alta calidad, incluidos todos los títulos nuevos de Xbox Game Studios como Halo Infinite el día de su lanzamiento, con Xbox Game pass Ultimate (la membresía se vende por separado). Con la Entrega Inteligente garantizas que juegas la mejor versión disponible de tu juego sin importar en qué consola estés jugando. Halo Infinite: lanzamiento en 2021. Uso exclusivo con juegos digitales; la consola no reproduce discos físicos. Xbox Game Pass: el catálogo de juegos varía con el tiempo. (xbox.com/gamepass). Experimenta la velocidad y el rendimiento de una consola totalmente digital de próxima generación. Empieza con una biblioteca instantánea de más de 100 juegos de alta calidad, incluidos todos los títulos nuevos de Xbox Game Studios como Halo Infinite el día de su lanzamiento, cuando agregues Xbox Game Pass Ultimate (la membresía se vende por separado). *Alterna sin problemas entre varios juegos en un instante con Quick Resume. En el corazón de la Serie S se encuentra la Arquitectura Xbox Velocity, que combina un SSD personalizado con un software integrado para un juego más rápido y optimizado con tiempos de carga significativamente reducidos.*",
            "foto" : ""
        },
        '3' : {
            'nombre' : 'Nintendo Switch ',
            'descripcion' : 'Diseñado para juegos serios y con un estilo nuevo y elegante, TUF Gaming F15 es un portátil para juegos repleto de funciones con el poder de llevarte a la victoria. Con hasta GPU GeForce RTX ™ 3060 ofrece un juego fluido en una pantalla de hasta 240Hz con 100% sRGB, mientras que la potente hasta CPU Intel Core i5 se ve reforzada por una refrigeración mejorada que amplifica el rendimiento de la CPU y mantiene la acústica sigilosa. Una batería de 90 Wh de larga duración junto con la durabilidad de grado militar de TUF te mantiene en tu mejor juego en cualquier lugar.',
            'foto' : ''
        },
    }

    informacion_producto = data.get(producto_id)    
    return render(request, 'evaluacion1_app/descripcion.html', informacion_producto)

def descripcion_pc(request, producto_id):
    data = {
        '1': {
            "nombre" : "HP OMEN 16-B1001LA",
            "descripcion" : "Experimenta el rendimiento de alto nivel para juegos y productividad con la Notebook HP Omen Gaming 16-k0033dx. Esta laptop ofrece un procesador Core i9, 16 GB de RAM y una unidad de 1 TB SSD para un funcionamiento óptimo y fluida. Disfruta de experiencias gaming de alto nivel con excelentes gráficos y optimizaciones que te permiten jugar sin problemas.",

            "foto" : ""
        },
        '2' : {
            "nombre" : "ACER NITRO 5",
            "descripcion" : "El nuevo Nitro 5 te dará las herramientas necesarias para ganar en el campo de batalla: Incorpora procesador Intel de Séptima Generación, una tarjeta NVIDIA® GeForce® GTX serie 10 y sonido envolvente Dolby Audio™ Premium. El Notebook Gamer Acer Nitro 5 es un portátil con pantalla Full HD de 15,6 pulgadas y matriz IPS. Cuenta con 8 GB de memoria RAM DDR4 y una tarjeta gráfica dedicada NVIDIA GeForce GTX 1050 de 4GB GDDR5, todo lo necesario para un entretenimiento sin retrasos. Entre su conectividad encontramos un puerto RJ-45 Gigabit, un USB 3.1 Type-C, un USB 3.0 y dos USB 2.0, además de salida de vídeo HDMI. Así mismo, cuenta con WiFi 802.11ac con antena MIMO 2×2. Además integra teclado isla retro-iluminado de color rojo, ventiladores con tecnología Acer CoolBoost™ y Wi-Fi estable gracias a la antena MU-MIMO 802.11ac estratégicamente ubicada." ,
            "foto" : ""
        },
        '3' : {
            'nombre' : 'ASUS TUF GAMING F15',
            'descripcion' : 'Diseñado para juegos serios y con un estilo nuevo y elegante, TUF Gaming F15 es un portátil para juegos repleto de funciones con el poder de llevarte a la victoria. Con hasta GPU GeForce RTX ™ 3060 ofrece un juego fluido en una pantalla de hasta 240Hz con 100% sRGB, mientras que la potente hasta CPU Intel Core i5 se ve reforzada por una refrigeración mejorada que amplifica el rendimiento de la CPU y mantiene la acústica sigilosa. Una batería de 90 Wh de larga duración junto con la durabilidad de grado militar de TUF te mantiene en tu mejor juego en cualquier lugar.',
            'foto' : ''
        },
    }

    informacion_producto = data.get(producto_id)    
    return render(request, 'evaluacion1_app/descripcion.html', informacion_producto)

def descripcion_accesorios(request, producto_id):
    data = {
        '1': {
            "nombre" : "Mouse Logitech G502X",
            "descripcion" : "Play Has No Limits ™. PlayStation®5. La consola PS5 ™ da rienda suelta a nuevas posibilidades de juego que nunca anticipaste. Experimenta una carga ultrarrápida con un SSD de velocidad ultrarrápida, una inmersión más profunda con soporte para retroalimentación háptica, activadores adaptativos y audio 3D, y una nueva generación de increíbles juegos de PlayStation®. Velocidad de la luz: Aprovecha la potencia de una CPU, GPU y SSD personalizadas con E / S integradas que reescriben las reglas de lo que puede hacer una consola PlayStation®. Juegos impresionantes: Maravíllate con los gráficos increíbles y experimenta las nuevas funciones de PS5 ™. Inmersión impresionante: Descubra una experiencia de juego más profunda con soporte para retroalimentación háptica, activadores adaptativos y tecnología de audio 3D.",
            "foto" : ""
        },
        '2' : {
            "nombre" : "HyperX Alloy Origins 65",
            "descripcion" : "El teclado HyperX Alloy Origins 65 es un teclado que sabe combinar el tamaño con la funcionalidad sin ponerlas en riesgo. El formato 65 % lo hace más compacto que un teclado sin teclas numéricas incluso manteniendo las teclas de dirección. Cuenta con un cuerpo duradero totalmente de aluminio y con las teclas HyperX, diseñadas para resistir 80 millones de pulsaciones, que lo convierte en un teclado práctico y compacto. Las cubiertas de PBT de doble capa de las teclas llevan impresas funciones secundarias para que las puedas localizar con facilidad. Brillarás más que nunca con el llamativo diseño LED de las teclas HyperX y sus increíbles efectos luminosos. Saca partido al software HyperX NGENUITY y personaliza el teclado con macros, perfiles de iluminación específicos y mucho más.",
            "foto" : ""
        },
        '3' : {
            'nombre' : 'Xbox Stellar Shift Edición Especial',
            'descripcion' : 'Vive una experiencia surrealista con el control inalámbrico Xbox Stellar Shift Edición Especial, que cuenta con un acabado brillante azul y morado que cambia de color y agarres texturizados con espirales en color morado. Experimenta el agarre texturizado morado del espiral, el primero de su clase de Xbox con un patrón que hace que cada uno sea único por diseño. No pierdas el objetivo con el pad direccional híbrido y agarre texturizado en los gatillos, botones superiores y carcasa trasera. Conecta cualquier auricular compatible con la entrada de audio estéreo de 3.5mm. Incluye tecnología inalámbrica Xbox y Bluetooth® para jugar de forma inalámbrica en consolas compatibles, PC con Windows y dispositivos móviles Android y iOS.* Captura y comparte contenido fácilmente con el botón para Compartir. Configura los botones para personalizar el control con la aplicación de Accesorios de Xbox*. Conéctate usando el puerto USB-C® para conectarte y jugar directo en la consola y en la PC. El soporte para pilas AA está incluido en la parte trasera.',
            'foto' : ''
        },
    }

    informacion_producto = data.get(producto_id)    
    return render(request, 'evaluacion1_app/descripcion.html', informacion_producto)

def usuario(request):
    data = {'perfil' : 'perfil.png',
            'nombre' : 'Diego Valenzuela',
            'rut'   : '18484489-3',
            'direcc' : 'Calle Falsa 123',
            'contacto' : '56 9 4567 8464',
            'correo' : 'micorreo@dominio.cl'}
    return render(request, 'evaluacion1_app/user.html', data)