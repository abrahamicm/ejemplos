<?php

/**
 * Para usar la clase, primero debes crear una instancia y proporcionar el nombre del archivo JSON donde se guardare la informacion:
 *php
 *$crud = new CRUD('data.json');
 *Luego, puedes llamar a los metodos create, read, update y delete en la instancia $crud para realizar las operaciones CRUD correspondientes.
 *Regenerate response
 */
class CRUD
{
    private $filename;

    public function __construct($filename)
    {
        $this->filename = $filename;
    }

    public function create($data)
    {
        $records = $this->read();
        $records[] = $data;
        $this->write($records);
    }

    public function read()
    {
        if (file_exists($this->filename)) {
            return json_decode(file_get_contents($this->filename), true);
        }
        return [];
    }

    public function update($id, $data)
    {
        $records = $this->read();
        foreach ($records as &$record) {
            if ($record['id'] == $id) {
                $record = array_merge($record, $data);
                break;
            }
        }
        $this->write($records);
    }

    public function delete($id)
    {
        $records = $this->read();
        $records = array_filter($records, function ($record) use ($id) {
            return $record['id'] != $id;
        });
        $this->write($records);
    }

    private function write($records)
    {
        file_put_contents($this->filename, json_encode($records));
    }
}
