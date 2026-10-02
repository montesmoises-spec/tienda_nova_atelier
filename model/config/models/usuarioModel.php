<?php
require_once __DIR__ . '/../config/database.php';

class UsuarioModel {
    private $conn;
    private $table_name = "usuarios";

    public function __construct() {
        $database = new Database();
        $this->conn = $database->getConnection();
    }

    // 1. CREAR (Create)
    public function crear($nombre, $email) {
        $query = "INSERT INTO " . $this->table_name . " (nombre, email) VALUES (:nombre, :email)";
        $stmt = $this->conn->prepare($query);

        $stmt->bindParam(":nombre", $nombre);
        $stmt->bindParam(":email", $email);

        return $stmt->execute();
    }

    // 2. LEER TODOS (Read)
    public function obtenerTodos() {
        $query = "SELECT * FROM " . $this->table_name . " ORDER BY id DESC";
        $stmt = $this->conn->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // LEER UNO POR ID
    public function obtenerPorId($id) {
        $query = "SELECT * FROM " . $this->table_name . " WHERE id = :id LIMIT 1";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(":id", $id);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    // 3. ACTUALIZAR (Update)
    public function actualizar($id, $nombre, $email) {
        $query = "UPDATE " . $this->table_name . " SET nombre = :nombre, email = :email WHERE id = :id";
        $stmt = $this->conn->prepare($query);

        $stmt->bindParam(":id", $id);
        $stmt->bindParam(":nombre", $nombre);
        $stmt->bindParam(":email", $email);

        return $stmt->execute();
    }

    // 4. BORRAR (Delete)
    public function eliminar($id) {
        $query = "DELETE FROM " . $this->table_name . " WHERE id = :id";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(":id", $id);

        return $stmt->execute();
    }
}
?>