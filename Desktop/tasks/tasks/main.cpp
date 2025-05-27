void insertBPlusSimple(Node* leaf, int key) {
    // Предполагаем, что leaf — это лист и в нём есть место
    int i = leaf->n - 1;
    while (i >= 0 && leaf->keys[i] > key) {
        leaf->keys[i + 1] = leaf->keys[i];
        --i;
    }
    leaf->keys[i + 1] = key;
    leaf->n++;
}
