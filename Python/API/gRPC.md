# gRCP

https://grpc.io/docs/languages/python/basics/

install packages
```sh
pip install grpcio grpcio-tools googleapis-common-protos
```

compile protocols
```sh
python -m grpc_tools.protoc -I definitions/ --python_out=definitions/builds/ --grpc_python_out=definitions/builds/ definitions/service.proto
```

## comparison between gRCP and FastAPI
https://alek-cora-glez.medium.com/my-next-api-grpc-restful-5d888289acd

https://betterprogramming.pub/grpc-file-upload-and-download-in-python-910cc645bcf0

## FastAPI and gRPC
https://dev.to/ankitbrijwasi/connect-fastapi-golang-services-using-grpc-4k3d

## gRPC api
https://medium.com/google-cloud/building-apis-with-grpc-continued-f53b5a5ab850
