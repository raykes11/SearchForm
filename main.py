import uvicorn
from fastapi import FastAPI, Request

from my_pydantic.def_pydantic import identify_model, all_pydantic_model

app = FastAPI()
all_model = all_pydantic_model()


@app.get("/")
async def parser_json():
    return {"massage": "Hello index!"}


@app.post("/")
async def parser_json(request: Request):
    request = await request.json()
    return identify_model(data=request, models=all_model)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
