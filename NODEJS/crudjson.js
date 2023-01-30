const fs = require('fs');

class CRUD {
  constructor(filePath) {
    this.filePath = filePath;
  }

  async create(data) {
    let records = await this.getAll();
    records.push(data);
    fs.writeFileSync(this.filePath, JSON.stringify(records));
  }

  async read(id) {
    let records = await this.getAll();
    return records.find(record => record.id === id);
  }

  async update(id, data) {
    let records = await this.getAll();
    let recordIndex = records.findIndex(record => record.id === id);
    records[recordIndex] = { ...records[recordIndex], ...data };
    fs.writeFileSync(this.filePath, JSON.stringify(records));
  }

  async delete(id) {
    let records = await this.getAll();
    let filteredRecords = records.filter(record => record.id !== id);
    fs.writeFileSync(this.filePath, JSON.stringify(filteredRecords));
  }

  async getAll() {
    return JSON.parse(fs.readFileSync(this.filePath, 'utf-8')) || [];
  }
}

module.exports = CRUD;
