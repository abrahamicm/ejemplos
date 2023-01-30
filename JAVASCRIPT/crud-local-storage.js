class LocalStorageCRUD {
    constructor(key) {
      this.key = key;
    }
  
    create(value) {
      const items = this.getAll();
      items.push(value);
      this.saveAll(items);
    }
  
    read(id) {
      return this.getAll().find(item => item.id === id);
    }
  
    update(id, value) {
      const items = this.getAll();
      const index = items.findIndex(item => item.id === id);
      items[index] = { ...items[index], ...value };
      this.saveAll(items);
    }
  
    delete(id) {
      const items = this.getAll().filter(item => item.id !== id);
      this.saveAll(items);
    }
  
    getAll() {
      return JSON.parse(localStorage.getItem(this.key)) || [];
    }
  
    saveAll(items) {
      localStorage.setItem(this.key, JSON.stringify(items));
    }
  }
  
  const crud = new LocalStorageCRUD("myKey");
  
  crud.create({ id: 1, name: "John Doe" });
  crud.create({ id: 2, name: "Jane Doe" });
  console.log(crud.getAll());
  // [{ id: 1, name: "John Doe" }, { id: 2, name: "Jane Doe" }]
  crud.update(1, { name: "John Doe Updated" });
  console.log(crud.getAll());
  // [{ id: 1, name: "John Doe Updated" }, { id: 2, name: "Jane Doe" }]
  crud.delete(2);
  console.log(crud.getAll());
  // [{ id: 1, name: "John Doe Updated" }]