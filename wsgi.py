from blog.app import app
from blog.models.database import db
from blog.models.user import Role


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! creates users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin_role = Role(name='Admin')
    admin = User(username="admin", is_staff=True)
    james = User(username="james")
    newadmin1 = User(username='new_admin', is_staff=True)
    newadmin1.roles = [admin_role, ]
    db.session.add(admin)
    db.session.add(james)
    db.session.add(newadmin1)
    db.session.commit()
    print("done! created users:", admin, james, newadmin1)
