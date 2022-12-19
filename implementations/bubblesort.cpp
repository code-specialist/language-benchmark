#include <iostream>
#include <fstream>
using namespace std;

void bubbleSort(int array[], int size) {
  bool swapNeeded = true;
  int i = 0;

  while(i < size - 1 && swapNeeded) {
    swapNeeded = false;
    for (int j = 1; j < size - i; j++) {
      if (array[j - 1] > array[j]) {
          int temp = array[j - 1];
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