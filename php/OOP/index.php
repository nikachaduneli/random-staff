<?php
$servername = "localhost";
$database = "bitoid";
$username = "root";
$password = "root";

// Create connection

$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection

if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
exit;
}

$query = 'CREATE TABLE IF NOT EXISTS MyGuests (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)';
$ins = 'insert into MyGuests (firstname,lastname,email)
        values ("nika", "chaduneli", "chaduasdasadnelinika15@gmail.com")';
$sel = 'SELECT * FROM MyGuests;';

$conn->query($query);
$conn->query($ins);
$result = $conn->query($sel);

if ($result->num_rows > 0){
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. " Email: ".$row['email']. "<br>";
    }
}
echo "Connected successfully";

mysqli_close($conn);

?>

