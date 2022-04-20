from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class WaveColors:
    gray: str = '#9E9E9E'
    red: str = '#F44336'
    tangerine: str = '#FF5722'
    brown: str = '#795548'
    orange: str = '#FF9800'
    amber: str = '#FFC107'
    yellow: str = '#FFEB3B'
    lime: str = '#CDDC39'
    green: str = '#8BC34A'
    mint: str = '#4CAF50'
    teal: str = '#009688'
    cyan: str = '#00BCD4'
    azure: str = '#03A9F4'
    blue: str = '#2196F3'
    indigo: str = '#3F51B5'
    violet: str = '#673AB7'
    purple: str = '#9C27B0'
    pink: str = '#E91E63'
    black: str = "#000000"
    h2o: str = "#FEC925"
    light_gray: str = "#0D0D0D"
    white: str = "#FFFFFF"
