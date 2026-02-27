from fastapi import FastAPI,status

app = FastAPI(title='LPU')

@app.get("/",tags=['main'],status_code=status.HTTP_200_OK)
def LPU():
    return {
        "msg":'Hello'
    }

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/students/{students_id}')
def view():
    data=load_data()
    return data