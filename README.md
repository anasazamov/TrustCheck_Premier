<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>

<body>
<h1>Django Loyihasi Dokumentatsiyasi</h1>

<h2>BASE_URL =  trustcheck.pythonanywhere.com</h2>

  <h2>Django Loyihasi Dokumentatsiyasi</h2>

  <p>
    Bu dokumentatsiya <a href="https://www.djangoproject.com/" target="_blank">Django</a> loyihamni tushunish va uni frontend qismiga ulash uchun muhim ma'lumotlar beradi.
  </p>

  <h1>TrustCheck Premier Web</h1>

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
{
    "count": 3800,
    "next": "http://127.0.0.1:8000/api/create-product/?page=2",
    "previous": null,
    "results": [
        {
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
        },
        {
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
        },
       //...
    ]
}
  </code></pre>
  <h4>Get Products by ID</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>/api/create-product/<int:ID></code></li>
    <li><strong>Method:</strong> GET</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 200 OK</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>

        {
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
        }
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
    "name": "Oil",
    "made_in": "uzbekistan",
    "description": "The best oil",
    "end_date": "2023-12-12",
    "product_seria_num": 4200126161
}
  </code></pre>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 200 OK</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>
{
    "count": 300,
    "next": "http://127.0.0.1:8000/api/create-product/?page=2",
    "previous": null,
    "results": [
        {
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
        },
        //...
    ]
}
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
    "message": "product has been deleted",
    "product": {
        "id": null,
        "name": "1",
        "description": "1",
        "created": "2024-01-18T22:32:19.746470+05:00",
        "end_date": "2023-12-12",
        "utilized": true,
        "utilized_date": "2024-01-18"
    }
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
{
    "count": 0,
    "next": null,
    "previous": null,
    "results":
[
  {
    "id": 1,{
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
        },
    "user": 1
  },
  {
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
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
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "password": "pbkdf2_sha256$600000$uraQHYDDX1A5UlpciZWCpq$2mpjqC/4Bxk1NDeT3VO9I1wzodTNqvW1ZTkywgSoln8=",
            "last_login": null,
            "is_superuser": false,
            "username": "+998991234567",
            "first_name": "Anas",
            "last_name": "Azamov",
            "email": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-11-28T05:26:16.752801+05:00",
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 3,
            "password": "pbkdf2_sha256$600000$NL5wLStKjmrUpgqmN9hCRR$34Fjl+YUKNoYy6Fdx+x226TbKeZXRXGRpIuGXKjZVmY=",
            "last_login": null,
            "is_superuser": false,
            "username": "+998330751735",
            "first_name": "",
            "last_name": "",
            "email": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-12-11T19:53:42.833150+05:00",
            "groups": [],
            "user_permissions": []
        }
    ]
    // ...
}
  </code></pre>


  <h3>Get Create products by User Table</h3>

  <h4>Get All CreateProduct</h4>

  <ul>
    <li><strong>Endpoint:</strong> <code>api/create-product-table/</code></li>
    <li><strong>Method:</strong> GET</li>
    <li><strong>Permissions:</strong> Session Authentication, Basic Authentication</li>
  </ul>

  <h5>Response</h5>

  <ul>
    <li><strong>Success Code:</strong> 200 OK</li>
    <li><strong>Success Response:</strong></li>
  </ul>

  <pre><code>

{
    "count": 4103,
    "next": "http://127.0.0.1:8000/api/create-product-table/?page=2",
    "previous": null,
    "results":
[
    {
        "id": 6103,
        "product": {
            "id": 167967,
            "name": "1",
            "product_hash": "c804dce280cf1f12b7fe4f5a79a19700e0ec5d187b9601ee21dbfd30eb802403",
            "product_seria_num":1656465
            "made_in": "uzbekistan",
            "description": "1",
            "created": "2023-12-17T11:02:48.166186+05:00",
            "end_date": "2023-12-12",
            "utilized_date": "2023-12-12",
            "utilized": false
        },
        "user": {
            "id": 2,
            "password": "pbkdf2_sha256$600000$M6fKbQrfK6kp8y6eW5hRiG$ez+9USQ3lab0wBNZKPuCLAp4+l7QcAZWWf2Hq5plRic=",
            "last_login": "2023-12-11T23:40:16.822206+05:00",
            "is_superuser": true,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2023-11-28T05:32:14.898669+05:00",
            "groups": [],
            "user_permissions": []
        }
    }
    // ...
]
}
  </code></pre>


<h1>TrustCheck Premier App</h1>
</body>

</html>

## Send Otp code

register a phone number

**`post /userverification/send-otp/`**

**Reuest body**

``` json
{"phone_number":"+998XXXXXXXXX"}

 ```

**Response**

``` json
{"message": "OTP code sent successfully"}

 ```

## Verify Phone number

verify phone number

`post` **`/userverification/verify-otp/`**

**Request body**

``` json
{
"phone_number":"+998XXXXXXXXX",
"otp_code":"XXXXXX"
}

 ```

**Response**

``` json
{
    "token": "{token}"
}

 ```

## Get user info

get **`/userverification/put-user/`**

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Response**

``` json
{
    "first_name": "Name1",
    "last_name": "Name2",
    "phone_number": "+998XXXXXXXXX"
}

 ```

## Edit name or add name

`put` **`/userverification/put-user/`**

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Request Body**

``` json
{
"first_name" : "Name1",
"last_name": "Name2"
}

 ```

**Response**

``` json
{
    "first_name": "Anas2",
    "last_name": "Azamov",
    "phone_number": "+998990751735"
}

 ```

## Edit phone number

## `put` **`/userverification/put-user/`**

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Request Body**

``` json
{
"phone_number": "+998XXXXXXXXX"
}

 ```

**Response**

``` json
{
    "first_name": "Anas2",
    "last_name": "Azamov",
    "phone_number": "+998990751735"
}

 ```

## Change Phone number

Confirmation of phone number change

## `put` **`/userverification/put-user/`**

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Request Body**

``` json
{
"phone_number": "+998XXXXXXXXX"
}

 ```

**Response**

``` json
{
    "phone_number": "+998990751735",
    "otp_code": "XXXXXX"
}

 ```

## Get product

get info product

`get` `/qrcode/products/`

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Response**

``` json
{
    "id": 3315,
    "name": "1",
    "product_seria_num": 4200126161,
    "made_in": "uzbekistan",
    "description": "1",
    "created": "2024-01-18T22:32:19.746470+05:00",
    "end_date": "2023-12-12",
    "utilized_date": null,
    "utilized": false
}

 ```

## Get all product

get all info product

`get` `/qrcode`

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Response**

``` json
[
    {
        "id": 3315,
        "name": "1",
        "product_seria_num": 4200126161,
        "made_in": "uzbekistan",
        "description": "1",
        "created": "2024-01-18T22:32:19.746470+05:00",
        "end_date": "2023-12-12",
        "utilized_date": "2024-01-18",
        "utilized": true
    }
// ...
]

 ```

## Get product by id

get info product by id

`get` `/qrcode/id/`

**Request Header**

``` json
{
"Authorization":"Token {token}"
"Content-Type":"application/json"
}

 ```

**Response**

``` json
{
    "id": 3315,
    "name": "1",
    "product_seria_num": 4200126161,
    "made_in": "uzbekistan",
    "description": "1",
    "created": "2024-01-18T22:32:19.746470+05:00",
    "end_date": "2023-12-12",
    "utilized_date": null,
    "utilized": false
}

 ```
