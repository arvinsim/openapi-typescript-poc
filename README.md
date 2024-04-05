# OpenAPI Typescript Proof of Concept

## Link

https://openapi-ts.pages.dev/

## Goals

Automate the creation of Typescript definitions from an OpenAPI compatible API endpoint.

These are the advantages of this approach
- Eliminate the tedious job of manually defining types
- Ensure that the types are in sync with the current types defined in the API endpoint

## Milestones

- [x] Setup Python server as mock OpenAPI compatible server
- [x] Generate types from local schema downloaded from documentation API
- [x] Generate types from remote schema using the mock server
- [ ] Generate types from remote schema with Authentication

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
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Commands

**Generate Typescript types from local schema**

```shell
npx openapi-typescript ./schema/car.yaml -o ./types/car.d.ts
```

**Generate Typescript types from local schema downloaded from documentation API**

```shell
npx openapi-typescript ./schema/users.json -o ./types/users.d.ts
```

**Generate Typescript types from remote schema(local development FastAPI server)**

```shell
npx openapi-typescript https://127.0.0.1:8000/openapi.json -o ./types/openapi.d.ts
```

**Generate Typescript types from remote schema(with authentication)**

1. Copy `redocly.template.yaml` to `redocly.yaml`
2. Configure it to point to the API you want and add authentication details if needed