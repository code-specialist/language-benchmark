import java.util.Arrays;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

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
        String numbersFilename = args[0];
        int[] numbers = new int[Integer.parseInt(args[1])];

        BufferedReader reader;

		try {
			reader = new BufferedReader(new FileReader(numbersFilename));
			String line = reader.readLine();

            for(int i = 0; i < numbers.length; i++) {
                numbers[i] = Integer.parseInt(reader.readLine());
            }

			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

        sort(numbers);
    }
}