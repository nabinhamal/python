/**
 * This is an Immediately Invoked Function Expression (IIFE).
 * It runs as soon as it is defined.
 * 
 * WHY USE THIS?
 * 1. Encapsulation: It creates a private scope. Variables like 'count' and 'godown' 
 *    cannot be accessed or modified from outside.
 * 2. Avoiding Global Scope Pollution: It keeps the global namespace clean.
 * 3. Module Pattern: It defines a clear public API (the returned object) while 
 *    hiding implementation details.
 */
const kironstore = (function () {
  // Private variables (internal state)
  // These are hidden from the outside world.
  let count = 0;
  const godown: string[] = [];

  // The returned object is the "Public API"
  return {
    /**
     * Adds an item to the store and increments the count.
     */
    add(name: string) {
      count++;
      godown.push(name);
      return `Sharma stocker item : ${name}`;
    },

    /**
     * Returns the current count of items.
     */
    count() {
      return count;
    },

    /**
     * Returns a copy of the item list.
     * slice() is used to prevent the caller from modifying the original array.
     */
    list() {
      return godown.slice();
    },
  };
})();

// Usage examples
console.log(kironstore.add("atta 10 packs"));
console.log(kironstore.add("rice 20 packs"));
console.log(kironstore.add("dal 30 packs"));

console.log("Total items in kironstore : ", kironstore.count());
console.log("List of items in kironstore : ", kironstore.list());

// Demonstrating encapsulation:
// These will be undefined or the function itself, showing no direct access to variables.
console.log("Direct Godown access : ", (kironstore as any).godown); // undefined
console.log("Direct count access : ", (kironstore as any).count);   // function (since count() is a method)

