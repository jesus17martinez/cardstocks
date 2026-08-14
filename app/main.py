from fastapi import FastAPI

app = FastAPI(title="VaultIQ")


@app.get("/")
def root():
    return {"message": "VaultIQ is running!"}

#Or
# from fastapi import FastAPI

# app = FastAPI(title="VaultIQ")

# def root():
#     return {"message": "VaultIQ is running"}

# app.get("/")(root)