<?php
$host = 'datenbank'; // Der Service-Name aus der docker-compose.yml
$db   = 'adressen';
$user = 'root';
$pass = 'DAA';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
     $pdo = new PDO($dsn, $user, $pass, $options);
     echo "<h1>Erfolg!</h1>";
     echo "<p>Die Verbindung zur MariaDB-Datenbank '<strong>$db</strong>' wurde erfolgreich hergestellt.</p>";
} catch (\PDOException $e) {
     echo "<h1>Verbindungsfehler</h1>";
     echo "<p>Fehlermeldung: " . $e->getMessage() . "</p>";
}
?>