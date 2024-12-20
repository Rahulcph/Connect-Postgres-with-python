from app import app, db

with app.app_context():
    # Perform database operations here
    db.create_all()
    print("Database tables created successfully.")
