import java.util.Arrays;

public class BubbleSort {

    static void sort(int [] array){
      int lastSwap = array.length - 1;
      for (int i = 1; i < array.length; i++) {
          boolean is_sorted = true;
          int currentSwap = -1;
          for (int j = 0; j < lastSwap; j++) {
              if (array[j] > array[j + 1]) {
                  int temp = array[j];
                  array[j] = array[j + 1];
                  array[j + 1] = temp;
                  is_sorted = false;
                  currentSwap = j;
              }
          }
          if (is_sorted) return;
          lastSwap = currentSwap;
      }
    }

    public static void main(String[] args) {
        int[] numbers = new int[args.length];
        for (int i = 0; i < args.length; i++) {
           numbers[i] = Integer.parseInt(args[i]);
        }
        sort(numbers);
    }
}