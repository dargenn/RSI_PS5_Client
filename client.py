from zeep import Client

client = Client('http://localhost:8080/unnamed/HelloWorldSuperService?wsdl')

with client.options(raw_response=True):
    response = client.service.superProductsGet()

    assert response.status_code == 200
    assert response.content

    print(response.content)