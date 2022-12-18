const fs = require('fs');
const assert = require('assert');

function bubbleSort(array) {
    let hasSwapped = false;
    let outerLoopIterationCount = 0;

    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length - i; j++) {
            if (array[j] > array[j + 1]) {
                hasSwapped = true;
                let tmp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = tmp;
            }
        }

        if (!hasSwapped) {
            return outerLoopIterationCount;
        }

        hasSwapped = false
        outerLoopIterationCount++;
    }
    return outerLoopIterationCount;
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
