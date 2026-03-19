import React, { useState, useMemo } from 'react';

/**
 * React Implementation of the Module Pattern (IIFE concept)
 * 
 * WHY? 
 * In React, we want 'state' to trigger re-renders. A plain IIFE object 
 * won't tell React to update the UI when variables change.
 */

// 1. Custom Hook Approach (The "React Way")
function useKironStore() {
  const [items, setItems] = useState<string[]>([]);
  
  // Encapsulated logic
  const store = useMemo(() => ({
    add: (name: string) => {
      setItems(prev => [...prev, name]);
      return `Added: ${name}`;
    },
    count: () => items.length,
    list: () => [...items]
  }), [items]); // Re-calculates if items change

  return store;
}

// 2. Component using the store
export const KironStoreComponent: React.FC = () => {
  const store = useKironStore();
  const [itemName, setItemName] = useState("");

  const handleAdd = () => {
    if (itemName) {
      store.add(itemName);
      setItemName("");
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Sharma Kiron Store (React Version)</h2>
      
      <input 
        value={itemName} 
        onChange={(e) => setItemName(e.target.value)} 
        placeholder="Enter item name"
      />
      <button onClick={handleAdd}>Add Item</button>

      <h3>Total Items: {store.count()}</h3>
      <ul>
        {store.list().map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default KironStoreComponent;
