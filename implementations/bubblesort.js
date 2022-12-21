const fs = require('fs');
const assert = require('assert');

function bubbleSort(array) {
    const n = array.length;
    let swapNeeded = true;
    let i = 0;

    while (i < n - 1 && swapNeeded) {
        swapNeeded = false;
        for (let j = 1; j < n - i; j++) {
            if (array[j - 1] > array[j]) {
                const temp = array[j - 1];
                array[j - 1] = array[j];
                array[j] = temp;
                swapNeeded = true;
            }
        }
        if(!swapNeeded) {
            break;
        }
        i++;
    }
}

try {
    const filename = process.argv[2]
    const listLength = parseInt(process.argv[3]);

    const data = fs.readFileSync(filename, 'utf8');
    const numbers = data.split('\n').slice(0, listLength).map(input => parseInt(input))

    bubbleSort(numbers)
} catch (err) {
    console.error(err);
}
