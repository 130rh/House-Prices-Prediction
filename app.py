import streamlit as st
import pandas as pd
import joblib

# Загрузка обученной модели
model = joblib.load("model.pkl")


# Заголовок страницы
st.title("🏡 Прогноз цены на дом")

# Описание
st.write("Введите характеристики дома, чтобы получить прогнозируемую цену на основе обученной модели.")

# Поля для ввода данных
overallqual = st.slider("Качество материалов (OverallQual)", 1, 10, 5)
grlivarea = st.number_input("Жилая площадь (GrLivArea)", value=1500)
garagecars = st.slider("Количество машиномест (GarageCars)", 0, 4, 2)
garagearea = st.number_input("Площадь гаража (GarageArea)", value=400)
totalbsmt = st.number_input("Площадь подвала (TotalBsmtSF)", value=800)
firstflr = st.number_input("Площадь первого этажа (1stFlrSF)", value=1000)
fullbath = st.slider("Количество полных ванных комнат (FullBath)", 0, 3, 1)
totrms = st.slider("Количество комнат (TotRmsAbvGrd)", 2, 12, 6)
yearbuilt = st.slider("Год постройки (YearBuilt)", 1870, 2023, 2000)
yearremod = st.slider("Год реконструкции (YearRemodAdd)", 1950, 2023, 2005)

# Создание DataFrame из введённых данных
input_df = pd.DataFrame({
    'OverallQual': [overallqual],
    'GrLivArea': [grlivarea],
    'GarageCars': [garagecars],
    'GarageArea': [garagearea],
    'TotalBsmtSF': [totalbsmt],
    '1stFlrSF': [firstflr],
    'FullBath': [fullbath],
    'TotRmsAbvGrd': [totrms],
    'YearBuilt': [yearbuilt],
    'YearRemodAdd': [yearremod]
})

# Кнопка для предсказания
if st.button("🔮 Предсказать цену"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Прогнозируемая цена: ${prediction:,.0f}")
