import os
import requests
from flask import Flask, request
from google import genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

GEMINI_MODEL = "gemini-3.5-flash-lite"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Startup Shark Bot is running!", 200
    # tpc/ip
    # 1xx -информационные 
    # 100 - continue -> сервер получил начало запроса
    # и ждет остальную часть данных
    # 101 --> Switch Protocols --> червер готов сменить протокол
    # 2xx
    # 200 -> Ok --> успешный результат
    # 201 --> Created --> Запрос выполнен, создан новый ресурс
    # 202 --> Accepted --> Запрос принят в обработку, но еще завершен
    # 204 --> Not Content --> запрос выполнен, 
    # но тело ответа отсутствует
    # 3xx --> Перенаправления (редиректоры)
    # 302 --> Found --> временный перенос ресурса
    # 4xx --> Ошибки клиента
    # 400 --> Bad request --> некорректный запрос
    # 401 --> Unauthorized --> доступ к ресурсу запрещен
    # даже при наличии аутентификации
    # 404 --> Not Found --> запрошенный ресурс не найден
    # 408 --> Request Timeout --> сервер не дождался 
    # полного запроса от клиента за отведенное время
    # 429 --> Too Many Requests --> превышен лимит запросов
    # за единицу времени
    # 5xx --> Ошибки сервера
    # 500 --> Internal Server Error --> внутренняя ошибка сервера
    # 502 --> Bad Gateway --> шлюх получил некорректный ответ
    # от вышестоящего сервера
    # 503 --> Service Unavailable --> сервис временно недоступен
    # (техработы, перезагрузка сервиса)


class StartupPitch:
    def __init__(self, author, idea, score, verdict, comment):
        self.author = author
        self.idea = idea
        self.score = score
        self.verdict = verdict
        self.comment = comment
    def format_card(self):
        return (    
            f"СТАРТАП-ПИТЧ ОТ: {self.author}\n",
            f"Идея: {self.idea}\n\n"
            f"Оценка инвестора: {self.verdict}\n",
            f"Вердикт: {self.verdict}\n",
            f"Разбор от инвестора: {self.comment}"
        )
