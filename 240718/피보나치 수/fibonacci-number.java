import java.util.Arrays;
import java.util.Scanner;

public class Main{
    private static int[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        arr = new int[N + 1];
        Arrays.fill(arr, 0);
        arr[0] = 1;
        arr[1] = 1;
        arr[2] = 1;
        
        System.out.println(fibo(N));
    }

    private static int fibo(int n) {
        if (arr[n] != 0) return arr[n];

        arr[n] = fibo(n-2) + fibo(n-1);
        return arr[n];
    }
}