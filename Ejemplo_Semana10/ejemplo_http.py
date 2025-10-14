import json
import requests

#Simular peticiones con diferente código de status
#https://httpstatus.io/mocking-data
#Petición GET: https://httpstatus.io/mocking-data/#status
#Ejemplo (Petición tipo GET): https://httpstatus.io/mocking-data/300
#Ejemplo (Petición tipo GET): https://httpstatus.io/mocking-data/400

#Juego de códigos de status HTTP
#https://dev.to/jamesrmoro/the-status-rebellion-an-epic-game-about-http-codes-1p66


url_api = 'https://jsonplaceholder.typicode.com'

#Solicitud HTTP GET a la API
try:
    res = requests.get(f'{url_api}/users')
    print(res, type(res))

    if res.status_code == 200:
        empleados = res.json()
        print(empleados[0])
    else:
        print('No se pudieron obtener los empleados de la API.')
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud GET: {e}')




usuario_nuevo = {
    "name": "Estudiante IPC2",
    "username": "ipc2",
    "email": "estudiante.ipc2@example.com",
    "address": {
        "street": "Aguilar Batres",
        "city": "Guatemala"
    }
}

#Solicitud HTTP POST a la API
try:
    res_post = requests.post(f'{url_api}/users', json=usuario_nuevo)
    print(res_post)
    if res_post.status_code == 201:
        usuario_nuevo = res_post.json()
        print('Usuario creado exitosamente: ')
        print(json.dumps(usuario_nuevo, indent=4, ensure_ascii=False))
    else:
        print('No fue posible crear el usuario')
        
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud POST: {e}')

#Obtener los datos de una imagen
url_picsum = "https://picsum.photos/800/600"  #Imagen aleatoria de 800x600 píxeles
try:
    res_imagen = requests.get(url_picsum)
    
    if res_imagen.status_code == 200:
        #Descargar la imagen binaria
        with open('imagen.jpg', 'wb') as file:
            file.write(res_imagen.content)
        print('Foto de perfil descargada y guardada como "imagen.jpg"')
    else:
        print(f'No se pudo descargar la imagen')
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud a Lorem Picsum: {e}')
