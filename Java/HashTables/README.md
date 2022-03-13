## HashTables

### HashTable
- Abstract data type
- Provide access to data using keys
- Key doesn't have to be an integer; it could be a string
- Consists of key/value pairs - data types don't have to match for the key and value.
- Optimized for retrieval (when you know the key)
- Associative array is one type of the hash table

### Hashing
- Maps keys of any data type to an integer
- Hash function maps keys to int
- In Java, hash function is Ob ject.hashCode()
- Collision occurs when more than one value has the same hashed value

### Load Factor
- Tells us how full a hash table is
- Load factor = # of items / capacity = size / capacity
- Load factor is used to decide when to resize the array backing the hash table
- Don't want load factor to be too low (lots of empty space)
- Don't want load factor to be too high (will increase the likelihood of collision)
- Can play a role in determining the time complexity for retrieval

### Add to a Hash Table backed by an Array
1. Provide a key/value pair
2. Use a hash function to hash the key to an int value
3. Store the value at the hashed key value - this is the index into the array

### Add "Jane Jones" with the key of "Jones"
1. Use a hash function to map "Jones" to an integer - let's assume we get the value 4
2. Store "Jane Jones" at index 4 of the array (i.e. array[4] = "Jane Jones")

### Retrieve the employee with key "Jones"
1. Provide the key "Jones"
2. Use the same hash function to map "Jones" to an integer - let's asume we get the value 4
3. Retrieve the value at index 4. array[4] -> "Jane Jones"

