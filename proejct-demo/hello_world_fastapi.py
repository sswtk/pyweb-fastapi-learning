# -*- coding: utf-8 -*-
# @Author  : RoninssWang
# @Time    : 2021/7/10 5:22 下午
# @FileName: hello_world_fastapi.py.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class CityInfo(BaseModel):
    city: str
    country: str
    is_affected: Optional[bool] = None

city_data = {
    "city": "anqing",
    "country": "mafaf"
}

# =========非异步方式=======================


@app.get('/')
def hello_world():
    return {"FASTAPI": "Hello World"}


@app.get('/city/{city}')
def get_city_info(city: str, q: Optional[str] = None):
    return {"city": city, "q": q}


@app.post('/city/{city}')
def add_city_info(city: str, city_info: CityInfo):
    return {"city": city, "country": city_info.country, "is_affected": city_info.is_affected}


# =========异步方式=======================
@app.get('/')
async def hello_world():
    return {"FASTAPI": "Hello World"}


@app.get('/city/{city}')
async def get_city_info(city: str, q: Optional[str] = None):
    return {"city": city, "q": q}


@app.post('/city/{city}')
async def add_city_info(city: str, city_info: CityInfo):
    return {"city": city, "country": city_info.country, "is_affected": city_info.is_affected}