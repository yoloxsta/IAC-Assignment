<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>
        <?php
        echo 'We are running PHP, version: ' . phpversion();
        ?>
    </p>

    <?php
    $database = "mydb";
    $user = "root";
    $password = "secret";
    $host = "mysql";

    try {
        $connection = new PDO("mysql:host={$host};dbname={$database};charset=utf8", $user, $password);
        $connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $query = $connection->query("SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='{$database}'");
        $tables = $query->fetchAll(PDO::FETCH_COLUMN);

        if (empty($tables)) {
            echo "<p>There are no tables in database \"{$database}\".</p>";
        } else {
            echo "<p>Database \"{$database}\" has the following tables:</p>";
            echo "<ul>";
            foreach ($tables as $table) {
                echo "<li>{$table}</li>";
            }
            echo "</ul>";
        }
    } catch (PDOException $e) {
        echo "<p style='color: red;'>Database connection failed: " . htmlspecialchars($e->getMessage()) . "</p>";
    }
    ?>
</body>
</html>
