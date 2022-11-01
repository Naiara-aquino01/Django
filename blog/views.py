from django.forms import SlugField
from django.shortcuts import render
from datetime import date

post_cabina = {
    'titulo': 'Cabina para uñas UV Led+kit manicura',
    'precio': '$36.500',
    'marca': 'Gadnic',
    'resumen': 'SE ENTREGA CON: 1x Lámpara LED para uñas, 1x Fuente de alimentación 220v, 1x lima de brillo, 1x brocha, 1x lima porosa, 1x lima suave, 1x pinza para strass, 1x dootin tool, 1x repujador de cutícula, 1x pincel, 1x pinza para strass, 1x Manual en español',
    'contenido': 'Material: ABS de alta calidad, Cantidad de LED de alta potencia: 36, Vida útil: 50,000 hs, Potencia máxima 108w, Sensor de proximidad, Temporizador: 10s, 30s, 60s y 99s, Base imantada removible, Medidas: 28 x 20 x 9,5 [cm]',
    'imagen': 'blog/images/cabina.png',
    'slug': 'poducto-cabina'
}
post_dosemeline= {
    'titulo': 'Kit Meline 12 Esmaltes Semipermanente',
    'precio': '$20.000',
    'marca': 'Meline',
    'resumen': 'KIT 12 ESMALTES MELINÉ GEL COLOR PARA ESMALTADO SEMIPERMANENTE Esmalte color para uñas Meliné gel on-off para cabinas uv o led. CONSULTAR STOCK ANTES DE OFERTAR',
    'contenido': 'Esmalte Meliné de uso profesional próximos a vencer o vencidos (vto de tapa), El vencimiento corre una vez abiertos, 12 meses. PRECIO PROMOCIÓN, Curado en cabina uv: 2 minutos, Curado en cabina led: 30 a 60 segundos',
    'imagen': 'blog/images/dosemeline.png',
    'slug': 'producto-dosemeline'
}
post_adhere = {
    'titulo': 'Adhere+Primer sin acido',
    'precio': '$1.500',
    'marca': 'Cuvage',
    'resumen': 'Adhere Deshidratador Cuvage, Primer sin acido',
    'contenido': 'Producto para uso profesional para la construcción de uñas y esmaltado semipermanente. Recomendado como complemento al primer cuando la uña de la clienta presenta desprendimientos del producto aplicado a causa de la oleosidad de la uña o sudoración en las manos (hiperhidrosis). Adhere Cuvage es un deshidratador y nivelador de PH. Producto elaborado para eliminar oleosidad y humedad de la uña natural. Se utiliza después del pulido de las uñas y antes del primer con o sin ácido. Recomendado para construcción de uñas acrílicas y gelificadas así como esmaltado semipermanente',
    'imagen': 'blog/images/adhere.png',
    'slug': 'producto-adhere' 
}
post_topbase = {
    'titulo': 'Kit Base + Top Coat Meline',
    'precio': 'Meline',
    'marca': '$4.000',
    'resumen': 'Base Y Top Coat Esmalte Meliné Gel Led/uv Semipermanen',
    'contenido': 'Con este sistema de manicuría, las uñas permanecen esmaltadas y prolijas por hasta 15 días.',
    'imagen': 'blog/images/topbase.png',
    'slug': 'producto-topbase'
}
lista_posts = [
    post_cabina,
    post_dosemeline,
    post_adhere,
    post_topbase,
]

# Create your views here.
def starting_page(request):
    return render(request, 'blog/index.html' , {
        'producto':lista_posts [0:4]
    })

def posts(request):
    return render(request, 'blog/posts.html', {
        'producto':lista_posts
    })

def post_detail(request, slug):
    print ('slug' , slug)
    for producto in lista_posts:
        if slug == producto ['slug']:
            print ('producto', producto)
            return render(request, 'blog/post-detail.html', {
                'producto' : producto 
            })
