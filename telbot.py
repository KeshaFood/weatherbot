import logging
from aiogram import Bot, Dispatcher, types, executor
import python_weather

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5652314122:AAGPVZZV8mLhHPrESrrnYDyqmSTQCulQjE4")
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    async with python_weather.Client(format=python_weather.METRIC) as client:
        weather = await client.get(message.text)
        answer_text = f"{weather.current.temperature}°C, {weather.nearest_area.name}, {weather.nearest_area.country}"
        for forecast in weather.forecasts:
            answer_text += f"\n{forecast.date.day}-{forecast.date.month}-{forecast.date.year}"

            for hourly in forecast.hourly:
                answer_text += f'\nВремя: {hourly.time}, Температура {hourly.temperature}°C, {hourly.type}'
                answer_text += f'\nСкорость ветра: {round(hourly.wind_speed * 0.2777)} м/c, ' \
                               f'Вероятность дождя: {hourly.chance_of_rain}%'
            break
    await message.answer(answer_text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
