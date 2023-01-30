class Database {
    constructor(dbName, storeName) {
      this.dbName = dbName;
      this.storeName = storeName;
    }
  
    openDB() {
      return new Promise((resolve, reject) => {
        const request = window.indexedDB.open(this.dbName, 1);
  
        request.onsuccess = (event) => {
          this.db = event.target.result;
          resolve(this.db);
        };
  
        request.onerror = (event) => {
          reject(event.target.error);
        };
  
        request.onupgradeneeded = (event) => {
          const db = event.target.result;
          db.createObjectStore(this.storeName, { keyPath: 'id', autoIncrement: true });
        };
      });
    }
  
    getAll() {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readonly');
        const store = transaction.objectStore(this.storeName);
        const request = store.getAll();
  
        request.onsuccess = (event) => {
          resolve(event.target.result);
        };
  
        request.onerror = (event) => {
          reject(event.target.error);
        };
      });
    }
  
    add(data) {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readwrite');
        const store = transaction.objectStore(this.storeName);
        const request = store.add(data);
  
        request.onsuccess = (event) => {
          resolve(event.target.result);
        };
  
        request.onerror = (event) => {
          reject(event.target.error);
        };
      });
    }
  
    update(data) {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readwrite');
        const store = transaction.objectStore(this.storeName);
        const request = store.put(data);
  
        request.onsuccess = (event) => {
          resolve(event.target.result);
        };
  
        request.onerror = (event) => {
          reject(event.target.error);
        };
      });
    }
  
    delete(id) {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readwrite');
        const store = transaction.objectStore(this.storeName);
        const request = store.delete(id);
  
        request.onsuccess = (event) => {
          resolve();
        };
  
        request.onerror = (event) => {
          reject(event.target.error);
        };
      });
    }
  }
  