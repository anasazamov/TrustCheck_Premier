<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Django Loyihasi Dokumentatsiyasi</title>
</head>

<body>

  <h1>Django Loyihasi Dokumentatsiyasi</h1>

  <p>
    Bu dokumentatsiya <a href="https://www.djangoproject.com/" target="_blank">Django</a> loyihangizni tushunish va uni frontend qismiga ulash uchun muhim ma'lumotlar beradi.
  </p>

  <h2>Komponentlar</h2>

  <p>
    Bu qismda loyihada qo'llangan modellar, serializers, views, hamda boshqa komponentlar haqida ko'rsatmalar beriladi.
  </p>

  <h3>CreateProduct API</h3>

  <h4>Get Products</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>/api/create-product/</code></li>
    <li><strong>Method:</strong> GET</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 200 OK</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 19.99,
    "description": "Description 1",
    // ...
  },
  {
    "id": 2,
    "name": "Product 2",
    "price": 29.99,
    "description": "Description 2",
    // ...
  },
  // ...
]
  </code></pre>

  <h4>Create Product</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>/api/create-product/</code></li>
    <li><strong>Method:</strong> POST</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Request</h5>

  <ul>
    <li><strong>Data:</strong></li>
  </ul>

  <pre><code>
{
  "name": "New Product",
  "price": 24.99,
  "description": "New Description",
  "how_many": 3
}
  </code></pre>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 201 Created</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>
[
  {
    "id": 3,
    "name": "New Product",
    "price": 24.99,
    "description": "New Description",
    // ...
  },
  // ...
]
  </code></pre>

  <h4>Delete Product</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>/api/create-product/&lt;int:pk&gt;/</code></li>
    <li><strong>Method:</strong> DELETE</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 204 No Content</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>
{
  "id": 3,
  "name": "New Product",
  "price": 24.99,
  "description": "New Description",
  // ...
}
  </code></pre>

  <h3>Utilized Product API</h3>

  <h4>Get Utilized Products</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>/api/utilized-product/</code></li>
    <li><strong>Method:</strong> GET</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 200 OK</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>
[
  {
    "id": 1,
    "product": {
      "id": 1,
      "name": "Product Name 1",
      "price": 19.99,
      "description": "Product Description 1",
      // ...
    },
    "user": 1
  },
  {
    "id": 2,
    "product": {
      "id": 2,
      "name": "Product Name 2",
      "price": 29.99,
      "description": "Product Description 2",
      // ...
    },
    "user": 1
  },
  // ...
]
  </code></pre>

  <h3>Get All Users API</h3>

  <h4>Get All Users</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>/api/get-all-users/</code></li>
    <li><strong>Method:</strong> GET</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 200 OK</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "john_doe"
  },
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Doe",
    "username": "jane_doe"
  },
  // ...
]
  </code></pre>

</body>

</html>
