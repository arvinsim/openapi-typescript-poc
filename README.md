# OpenAPI Typescript Proof of Concept

## Goals

## Setup

### OpenAPI Typescript

**Installing OpenAPI**

```shell
npm i -D openapi-typescript@next typescript
```
### Server(FastAPI)

[Reference](https://fastapi.tiangolo.com/#installation)

**Installing dependencies**

```shell
pip3 install -r requirements.txt
```

**Running the server**

```shell
uvicorn main:app --reload
```

**Accessing the API docs**

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Process

**Generate Typescript schema from local schema**

```shell
npx openapi-typescript ./schema/car.yaml -o ./types/car.d.ts
```

**Generate Typescript schema from remote schema(FastAPI)**

```shell
npx openapi-typescript https://127.0.0.1:8000/openapi.yaml -o ./types/api/users.d.ts
```
