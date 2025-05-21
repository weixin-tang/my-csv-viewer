from fastapi import FastAPI, HTTPException , Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uvicorn
from fastapi.responses import FileResponse


app = FastAPI()

# 添加CORS中间件，允许前端与后端通信
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境下应该指定确切的源，而不是"*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/csv-render")
async def get_index():
    return FileResponse("static/index.html")

# @app.get("/csv-render/api/get_csv")
@app.post("/csv-render/api/get_csv")
async def get_csv( dataUrl : str ):
    async with httpx.AsyncClient() as client:
        response = await client.get( dataUrl )
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail="Failed to fetch data")
        csv_data = str(response.text)
        return {"csv_data" : csv_data }

# 添加一个新的API端点，直接返回JSON数据
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8092, reload=True)