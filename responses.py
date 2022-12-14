# Copyright Beyond ML and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import requests
import settings


QUERY = """
fragment DaypartFragment on Daypart {
  temperature
  icon(format: CODE)
}

query ($lat: Float!, $lon: Float!) {
  weather: weatherByPoint(request: { lat: $lat, lon: $lon }) {
    now {
      temperature
      icon(format: CODE)
    }

    forecast {
      days(limit: 2) {
        parts {
          morning { ...DaypartFragment }
          day { ...DaypartFragment }
          evening { ...DaypartFragment }
          night { ...DaypartFragment }
        }
      }
    }
  }
}
"""

ICON_TO_EMOJI = {
    "skc_d": "☀️",
    "skc_n": "🌙",
    "bkn_d": "🌤️",
    "bkn_n": "☁️",
    "bkn_-ra_d": "🌦️",
    "bkn_-ra_n": "🌧️",
    "bkn_-sn_d": "🌨️",
    "bkn_-sn_n": "🌨️",
    "bkn_ra_d": "🌧️",
    "bkn_ra_n": "🌧️",
    "bkn_sn_d": "🌨️",
    "bkn_sn_n": "🌨️",
    "bkn_+ra_d": "🌧️",
    "bkn_+ra_n": "🌧️",
    "bkn_+sn_d": "🌨️",
    "bkn_+sn_n": "🌨️",
    "ovc_ts": "🌩️",
    "ovc_ts_ra": "⛈️",
    "ovc_ts_ha": "⛈️",
    "ovc": "☁️",
    "ovc_-ra": "🌧️",
    "ovc_-sn": "🌨️",
    "ovc_ra": "🌧️",
    "ovc_sn": "🌨️",
    "ovc_+ra": "🌧️",
    "ovc_+sn": "🌨️",
    "ovc_ra_sn": "🌨️",
    "ovc_ha": "🌨️",
}


def format_temperature(temperature: int) -> str:
    if temperature == 0:
        return "0"

    return f"{'+' if temperature > 0 else '−'}{abs(temperature)}°"


def format_part(part: dict) -> str:
    return f"{format_temperature(part['temperature'])}{ICON_TO_EMOJI[part['icon']]}"


def get_weather(lat: float, lon: float) -> str:
    response = requests.post(
        "https://api.meteum.ai/graphql/query",
        headers={"X-Meteum-API-Key": settings.API_TOKEN},
        json={"query": QUERY, "variables": {"lat": lat, "lon": lon}},
    ).json()

    weather: dict = response["data"]["weather"]
    days: list[dict] = weather["forecast"]["days"]
    now: dict = weather["now"]
    morning: dict = days[0]["parts"]["morning"]
    day: dict = days[0]["parts"]["day"]
    evening: dict = days[0]["parts"]["evening"]
    night: dict = days[-1]["parts"]["night"]

    return f"""```
Weather now: {format_part(now)}

Today morning:   {format_part(morning)}
Today afternoon: {format_part(day)}
Today evening:   {format_part(evening)}
Today night:     {format_part(night)}
```
Find out more on [meteum.ai](https://meteum.ai/?lat={lat}&lon={lon}&utm_source=telegram&utm_campaign=bot)!
"""
