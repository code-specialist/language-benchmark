#include <iostream>
#include <fstream>
using namespace std;

void bubbleSort(int array[], int size) {
  for (int step = 0; step < (size-1); ++step) {
    int swapped = 0;

    for (int i = 0; i < (size-step-1); ++i) {
      if (array[i] > array[i + 1]) {
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        swapped = 1;
      }
    }

    if (swapped == 0)
      break;
  }
}

int main(int argc, char** argv) {
    string filename = argv[1];
    int listLength = stoi(argv[2]);
    int numbers[listLength];

    ifstream numbersFile;
    numbersFile.open(filename);

    for (int i = 0; i < listLength; i++) {
        numbersFile >> numbers[i];
    }

    bubbleSort(numbers, listLength);

    return 0;
}