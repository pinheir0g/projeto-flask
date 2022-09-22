def init_app(app):

    @app.before_first_request
    def init_everything():
        print('Isso roda sempre antes do primeiro request')