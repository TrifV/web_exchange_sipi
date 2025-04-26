"""
Модуль с маршрутизацией приложения: определяет обработчики URL.
"""
from flask import Blueprint, render_template, request
import requests
import plotly.graph_objects as go
import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Обрабатывает запрос к главной странице.

    Получает список тикеров, запрашивает их котировки с API Московской биржи,
    рассчитывает волатильность, строит свечные графики через Plotly
    и возвращает HTML-шаблон с интерактивными графиками.

    GET-параметры:
        sort (str): 'volatility_desc' или 'volatility_asc' — сортировка списка по волатильности.

    Returns:
        Response: рендер шаблона 'index.html' с данными графиков.
    """
    securities = ["GAZP", "SBER", "LKOH", "MGNT", "ALRS", "CHMF"]
    from_date = "2024-03-01"
    till_date = "2025-03-14"
    interval = 24
    charts = []

    for security in securities:
        url = (
            f"https://iss.moex.com/iss/engines/stock/markets/shares/"
            f"securities/{security}/candles.json?from={from_date}"
            f"&till={till_date}&interval={interval}&start=0"
        )
        resp = requests.get(url)
        data = resp.json()
        cols = data['candles']['columns']
        rows = data['candles']['data']

        if not rows:
            charts.append({'security': security, 'volatility': None, 'graph_html': None})
            continue

        # Извлечение данных
        dates, opens, highs, lows, closes = [], [], [], [], []
        for row in rows:
            r = dict(zip(cols, row))
            dt = datetime.datetime.strptime(r['begin'][:10], '%Y-%m-%d')
            dates.append(dt.strftime('%d.%m.%Y'))
            opens.append(r['open'])
            highs.append(r['high'])
            lows.append(r['low'])
            closes.append(r['close'])

        # Расчёт волатильности
        volatility = ((max(highs) - min(lows)) / opens[0] * 100) if opens[0] else 0

        # Построение графика
        fig = go.Figure(data=[
            go.Candlestick(
                x=dates,
                open=opens,
                high=highs,
                low=lows,
                close=closes,
                increasing_line_color='green',
                decreasing_line_color='red'
            )
        ])
        fig.update_layout(
            title=f'График {security} (Волатильность: {volatility:.2f}%)',
            xaxis_title='Дата',
            yaxis_title='Цена (руб.)',
            xaxis_rangeslider_visible=False,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        fig.update_xaxes(gridcolor='lightgray')
        fig.update_yaxes(gridcolor='lightgray')

        graph_html = fig.to_html(full_html=False)
        charts.append({'security': security, 'volatility': volatility, 'graph_html': graph_html})

    # Сортировка
    sort_order = request.args.get('sort')
    if sort_order == 'volatility_desc':
        charts.sort(key=lambda x: x['volatility'] or 0, reverse=True)
    elif sort_order == 'volatility_asc':
        charts.sort(key=lambda x: x['volatility'] or 0)

    return render_template('index.html', charts=charts)

@main.route('/settings')
def settings():
    """
    Обрабатывает запрос к странице 'Подбор настроек'.

    В текущей реализации возвращает шаблон-заглушку. В дальнейшем
    сюда будет перенесён интерфейс выбора пресетов и фильтров.

    Returns:
        Response: рендер шаблона 'settings.html'.
    """
    return render_template('settings.html')