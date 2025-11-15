<?php
class Database {
    private $dataFile = 'data.json';

    public function saveData($data) {
        $currentData = $this->getData();
        $currentData[] = $data;
        file_put_contents($this->dataFile, json_encode($currentData));
    }

    public function getData() {
        if (!file_exists($this->dataFile)) {
            return [];
        }
        $jsonData = file_get_contents($this->dataFile);
        return json_decode($jsonData, true);
    }

    public function clearData() {
        file_put_contents($this->dataFile, json_encode([]));
    }
}
?>