<!DOCTYPE html>
<html>
<head>
    <title>Full Report </title>
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
        td {
            padding: 15px;
            background-color:white;
        }
        .main-block {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background: #1c87c9;
        }
        th{
            padding: 20px;
            background: #1c87c9;
        }


    </style>
</head>
<body>
<?php
$conn = new mysqli("mars.cs.qc.cuny.edu", "yawe8598", "23548598", "yawe8598");
$sourceID_Query = "SELECT * FROM source";
$source_ID_Result = mysqli_query($conn,$sourceID_Query);
$source_ID_Array = [];
//store data to array used for finding frequency list
while($row = mysqli_fetch_array($source_ID_Result)){
     $source_ID_Array[] = $row['source_id'];
}
// selecting source_id and source_name storing them into associative array for book name lookup
$book_name_query ="SELECT source_id, source_name FROM source";
$book_name_result = mysqli_query($conn,$book_name_query);
$output = mysqli_fetch_all($book_name_result);
$book_arr = array();
for($x=0; $x<sizeof($output); $x++){
    $book_arr[$output[$x][1]] =  $output[$x][0];
}

// This loop will generate amount of book in database from source_ID length
for ($i =0; $i <sizeof($source_ID_Array); $i++)
{
    // select frequency and word by looking up it's source_ID to the current source_id in this loop
    $sql = "SELECT * FROM occurrence WHERE source_id = $source_ID_Array[$i] ORDER BY freq DESC";
    $result = mysqli_query($conn,$sql);


    $totalRowQuery = "SELECT SUM(freq) FROM occurrence WHERE source_id = $source_ID_Array[$i]";
    $totalRowResult = mysqli_query($conn,$totalRowQuery);
    $totalRowOutput = mysqli_fetch_all($totalRowResult);


    // searching the hashmap for the name that matches current source_id
    $book_name = array_search($source_ID_Array[$i],$book_arr);
    echo
    "<h1>Full Report Of Parsed Text</h1>
<h1>$book_name</h1>
    <table border='1'>
    <tr>
    <th>word</th>
    <th>frequency</th>
    <th>percentage</th>
    </tr>";
    // assigning occurrence data to html table
    while($row=$result->fetch_assoc()) {
        $percentage =  100 * $row['freq'] /$totalRowOutput[0][0];
        echo "<tr>";
        echo "<td>" . $row['word'] . "</td>";
        echo "<td>" . $row['freq'] . "</td>";
        echo "<td>" . number_format($percentage,3) . "%". "</td>";
        echo "</tr>";
    }

    echo"</table>";
}

?>

</body>
</html>