<?php
class UserDAO {
  private $pdo;

  public function __construct($pdo) {
    $this->pdo = $pdo;
  }

  public function getUserById($id) {
    $stmt = $this->pdo->prepare("SELECT * FROM users WHERE id = ?");
    $stmt->execute([$id]);
    return $stmt->fetch();
  }

  public function addUser($username, $email) {
    $stmt = $this->pdo->prepare("INSERT INTO users (username, email) VALUES (?, ?)");
    return $stmt->execute([$username, $email]);
  }

  public function updateUser($id, $username, $email) {
    $stmt = $this->pdo->prepare("UPDATE users SET username = ?, email = ? WHERE id = ?");
    return $stmt->execute([$username, $email, $id]);
  }

  public function deleteUser($id) {
    $stmt = $this->pdo->prepare("DELETE FROM users WHERE id = ?");
    return $stmt->execute([$id]);
  }
}

// Conexión a la base de datos
$pdo = new PDO("mysql:host=localhost;dbname=database", "username", "password");

// Instanciación de la clase UserDAO
$userDAO = new UserDAO($pdo);

// Ejemplos de uso de la clase UserDAO
$user = $userDAO->getUserById(1);
$userDAO->addUser("newuser", "newuser@example.com");
$userDAO->updateUser(1, "updateduser", "updateduser@example.com");
$userDAO->deleteUser(1);
