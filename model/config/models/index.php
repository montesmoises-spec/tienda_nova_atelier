<?php
require_once 'models/UsuarioModel.php';

$usuarioModel = new UsuarioModel();

// Ejemplo de lectura:
$listaUsuarios = $usuarioModel->obtenerTodos();

// Ejemplo de inserción:
// $usuarioModel->crear("Juan Pérez", "juan@example.com");
?>