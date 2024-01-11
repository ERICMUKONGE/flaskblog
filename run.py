from flaskblog import app, db

if __name__ == "__main__":
    app.run(debug=True) 

@app.cli.command('db_create')
def db_create():
    with app.app_context():
        db.create_all()
        print('Database created') 