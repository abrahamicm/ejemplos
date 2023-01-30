<?php
//$crud = new CRUD('mysql:host=localhost;dbname=testdb', 'user', 'password');
class CRUD {
    private $pdo;

    public function __construct($dsn, $user, $password) {
        $this->pdo = new PDO($dsn, $user, $password);
    }

    public function create($table, $data) {
        $columns = implode(', ', array_keys($data));
        $values = ':' . implode(', :', array_keys($data));
        $sql = "INSERT INTO $table ($columns) VALUES ($values)";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute($data);
    }

    public function read($table, $id = null) {
        if ($id) {
            $sql = "SELECT * FROM $table WHERE id = :id";
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['id' => $id]);
            return $stmt->fetch();
        }
        $sql = "SELECT * FROM $table";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function update($table, $id, $data) {
        $set = implode(' = :', array_keys($data)) . ' = :' . implode(', ', array_keys($data));
        $sql = "UPDATE $table SET $set WHERE id = :id";
        $data['id'] = $id;
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute($data);
    }

    public function delete($table, $id) {
        $sql = "DELETE FROM $table WHERE id = :id";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute(['id' => $id]);
    }
}