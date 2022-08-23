<!DOCTYPE html>
<html>
<head>
    <title>Parsed info</title>
    <style>
        html, body {
            min-height: 100%;
            padding: 0;
            margin: 0;
            font-family: Roboto, Arial, sans-serif;
            font-size: 14px;
            color: #666;

        }
        h1{
            color:dimgrey;
            text-align:center;
        }
        table {
            table-layout: fixed;
            width: 100%;
            border-collapse: collapse;
            border: 3px solid grey;
        }
        th, td {
            padding: 20px;
            background-color:white;
        }
        .main-block {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        th{
            background: #1c87c9;
        }

    </style>
</head>

<body>
<div class="main-block">

<h1>Parsing result</h1>
<?php
    $sql = "SELECT * FROM source";
    $conn = new mysqli("mars.cs.qc.cuny.edu", "yawe8598", "23548598", "yawe8598");
    $result = mysqli_query($conn,$sql);

    echo "<table border='1'>
    <tr>
    <th>source Id</th>
    <th>source Name</th>
    <th>source URL</th>
    <th>Time processed</th>
    <th>Begin text</th>
    <th>End text</th>
    <th>Words frequency list</th>
    </tr>";

        while($row = mysqli_fetch_array($result)) {
            echo "<tr>";
            echo "<td>" . $row['source_id'] . "</td>";
            echo "<td>" . $row['source_name'] . "</td>";
            echo "<td>" . "<a href='".$row['source_url']."'>link </a>" ."</td>";
            echo "<td>" . $row['process_dtm'] . "</td>";
            echo "<td>" . $row['source_begin'] . "</td>";
            echo "<td>" . $row['source_end'] . "</td>";
            $book_id_to_other = $row['source_id'];
            echo "<td>"."<a href='wordFrequencyList.php?idCantiere=$book_id_to_other'>link </>"."</td>";
            echo "</tr>";
        }

    echo"</table>";


?>
</div>

</body>


</html>