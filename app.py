# Импорт необходимых библиотек
import pickle
import numpy as np
from flask import Flask, request, jsonify

# Загрузка обученной модели из файла
model = pickle.load(open("model.pkl", "rb"))

# Создание Flask-приложения
app = Flask(__name__)

# Главная страница — для проверки, что сервер работает
@app.route("/")
def home():
    return "✅ API работает! Отправьте POST-запрос на /predict"

# Маршрут для предсказаний
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # Получаем входные данные в формате JSON

    try:
        # Извлекаем признаки и преобразуем в нужную форму
        features = np.array(data["features"]).reshape(1, -1)

        # Выполняем предсказание модели
        prediction = model.predict(features)

        # Возвращаем результат в формате JSON
        return jsonify({"prediction": float(prediction[0])})
    except:
        # В случае ошибки возвращаем сообщение
        return jsonify({"error": "Убедитесь, что вход содержит ключ 'features' с числовыми значениями в списке."})

# Запуск приложения
if __name__ == "__main__":
    # Хост 0.0.0.0 делает API доступным извне (не только с localhost)
    app.run(host="0.0.0.0", port=5000)
