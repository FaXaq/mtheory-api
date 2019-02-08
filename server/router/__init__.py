from .. import controllers

def route(api):
    """
    Define all routes and assign them to resources
    """

    # user
    api.add_resource(controllers.user.Create, '/users')
    api.add_resource(controllers.user.Read, '/users')

    #auth
    api.add_resource(controllers.auth.Login, '/login')
    api.add_resource(controllers.auth.LogoutAccess, '/logout')
    api.add_resource(controllers.auth.LogoutRefresh, '/logout/refresh')
    api.add_resource(controllers.auth.TokenRefresh, '/token')

    # resources
    api.add_resource(controllers.SecretResource, '/secret')