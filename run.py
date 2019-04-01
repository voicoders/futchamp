from manage import app, migrate

if __name__ == '__main__':
    migrate.init_app(app)
    app.run()
