# Wordplease

## Diego Alvarado

### Practica de Back End Avanzado

-> Incluyo db.sqlite y carpeta media para poder probar la plataforma


## Usuarios

    diego (superuser)
    presi
    Mario
    ApiTest

    contrasena comun: Supersegura



## URLS

    '': Home, Listado de posts publicados
    'blogs/<str:account>/<int:pk>', Detalle de post 'pk' de usuario 'account'
    'blogs/<str:account>/<str:blogname>', Listado de posts en el blog 'blogname' del usuario 'account'    
    'blogs/<str:account>', Listado de blogs del usuario 'account'    
    'blogs', Listado de blogs de usuarios
    'my-posts', Listado de posts del usuario autenticado
    'my-blogs', Listado de blogs del usuario autenticado
    'new-post', Nuevo post del usuario autenticado
    'new-blog', Nuevo blog del usuario autenticado
    'admin', Panel de administrador 
    'signup', Registro de nuevo usuario
    'login', Formulario de login
    'logout', Logout

## API

    'api/my-posts', API para posts del usuario autenticado
    'api/blogs', API para consulta de blogs
    'api/blogposts, API para consulta de posts
    'api/blogposts/pk, API para operar sobre el post 'pk'
    'api/users', API para consulta de usuarios
    'api/users/pk', API para operar sobre el usuario 'pk'