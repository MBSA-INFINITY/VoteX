from app import app
import os
ENVIRONMENT = os.environ['ENVIRONMENT']
if __name__ == '__main__':
    if ENVIRONMENT == "dev":
        app.run(debug=True,port=5500)
    else:
        app.run()
