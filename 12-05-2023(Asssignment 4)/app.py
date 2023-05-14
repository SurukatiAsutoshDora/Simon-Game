import uvicorn

if __name__ == "__main__":
    while True:
        uvicorn.run("main:app", reload=True)