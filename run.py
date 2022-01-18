from frontend import create_app
import eel
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
