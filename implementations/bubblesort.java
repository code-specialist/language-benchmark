import java.util.Arrays;

public class BubbleSort {

    static void sort(int[] arr) {
        int i = 0, n = arr.length;
        boolean swapNeeded = true;
        while (i < n - 1 && swapNeeded) {
            swapNeeded = false;
            for (int j = 1; j < n - i; j++) {
                if (arr[j - 1] > arr[j]) {
                    int temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                    swapNeeded = true;
                }
            }
            if(!swapNeeded) {
                break;
            }
            i++;
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