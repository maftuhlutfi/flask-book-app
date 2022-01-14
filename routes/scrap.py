from app import app
from models.scrap import Scrap

@app.route('/scrap', methods=['POST'])
def scrap():
  return Scrap().scrap()