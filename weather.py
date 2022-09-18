import python_weather
import asyncio
import os


async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(format=python_weather.METRIC) as client:

        # fetch a weather forecast from a city
        weather = await client.get("Минск")

        # returns the current day's forecast temperature (int)
        print(f"{weather.current.temperature}°C, {weather.nearest_area.name}, {weather.nearest_area.country}")

        # get the weather forecast for a few days
        for forecast in weather.forecasts:
            print(forecast.date)

            for hourly in forecast.hourly:
                print(f'Время: {hourly.time}, Температура {hourly.temperature}°C, {hourly.type}')
                print(f'Скорость ветра: {round(hourly.wind_speed * 0.2777)} м/c, '
                      f'Вероятность дождя: {hourly.chance_of_rain}%')
            break


if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
