<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Students</title>
</head>
<body>
    <h2>Search Students by Last Name</h2>
    <form action="/search" method="post">
        <p>Last Name: <input name="last_name" required/></p>
        <p><button type="submit">Search</button></p>
    </form>
    <hr/>
    <a href="/list">Back to List</a>
    <hr/>
</body>
</html>
