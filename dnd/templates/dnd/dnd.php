<!DOCTYPE html>
<html lang="en">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"> 
        <meta charset="utf-8">
        <title>Projects</title>
        <meta name="generator" content="Bootply" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <meta name="description" content="" />
        <link rel="stylesheet" type="text/css" href="style.css">
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
        
       
        <link rel="apple-touch-icon" href="/bootstrap/img/apple-touch-icon.png">
        <link rel="apple-touch-icon" sizes="72x72" href="/bootstrap/img/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="/bootstrap/img/apple-touch-icon-114x114.png">
        
        
    </head>
       

    <body style="background-color:#006666">        
  <?php
$servername = "ls-83b76412cfb19ce97b259074e362e7e2605c6a71.cmkceejlkolu.us-west-2.rds.amazonaws.com";
$username = "dbmasteruser";
$password = "P>wL5SB-;?ak&]U]xin47ZOy+|1&xml7";
$dbname = "dbmaster";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM 5E_CHAR";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row["NAME"]. " Level " . $row["LEVEL"]. " " . $row["RACE"]. " " . $row["CLASS"]. " STR[" . $row["STRENGTH"]. "] DEX[" . $row["DEXTERITY"]. "] CON[". $row["CONSTITUTION"]. "] INT[" . $row["INTELLIGENCE"]. "] WIS[" . $row["WISDOM"]. "] CHA[" . $row["CHARISMA"]. "] " . "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>

    </body>   
</html>