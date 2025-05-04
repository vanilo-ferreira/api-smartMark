from fastapi import FastAPI
from app.api import category_router, product_router, sale_router
from app.database.session import engine
from app.models import category, product, sale

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI CRUD Project")

origins = [
    "http://localhost:5173", 
    "http://127.0.0.1:5173",
    "https://desafio-smart-mark.vercel.app",
    "https://desafio-smart-mark-45x734f0z-vaniloferreiras-projects.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

category.Base.metadata.create_all(bind=engine)
product.Base.metadata.create_all(bind=engine)
sale.Base.metadata.create_all(bind=engine)

app.include_router(category_router.router, prefix="/categories", tags=["Categories"])
app.include_router(product_router.router, prefix="/products", tags=["Products"])
app.include_router(sale_router.router, prefix="/sales", tags=["Sales"])

if __name__ == "__main__":
    import uvicorn
    import os

    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))