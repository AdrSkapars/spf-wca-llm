package own;

import gov.nasa.jpf.symbc.Debug;

import java.util.Arrays;

class HashTable {
    private int size;
    private Entry[] table;

    public HashTable(int size) {
        this.size = size;
        this.table = new Entry[size];
    }

    private int hash(char[] key) {
        int hash = 0;
        for (char c : key) {
            hash += c;
        }
        return hash % size;
    }

    public void put(char[] key, String value) {
        int index = hash(key);
        Entry entry = new Entry(key, value);

        if (table[index] == null) {
            table[index] = entry;
        } else {
            Entry current = table[index];
            while (current.next != null) {
                current = current.next;
            }
            current.next = entry;
        }
    }

    public String get(char[] key) {
        int index = hash(key);
        Entry current = table[index];

        while (current != null) {
            if (Arrays.equals(current.key, key)) {
                return current.value;
            }
            current = current.next;
        }

        return null;
    }

    private static class Entry {
        char[] key;
        String value;
        Entry next;

        Entry(char[] key, String value) {
            this.key = key;
            this.value = value;
            this.next = null;
        }
    }
}

public class BadgerHash {
    public static void main(String[] args) {
        final int N = Integer.parseInt(args[0]);

        int table_size = N;
        int key_amount = N;
        int key_length = 2;

        HashTable hashTable = new HashTable(table_size);

        for (int i=0;i<key_amount;i++){
            char[] key = new char[key_length];
            for (int j=0;j<key_length;j++)
                key[j]=Debug.makeSymbolicChar("put"+i+"_"+j);
            hashTable.put(key, "value");
        }

        char[] key = new char[key_length];
        for (int j=0;j<key_length;j++)
            key[j]=Debug.makeSymbolicChar("get"+j);
        hashTable.get(key);
        
    }
}
