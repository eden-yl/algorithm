import java.io.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            String[] arr = br.readLine().split(" ");
            double a = Double.parseDouble(arr[0]);
            double b = Double.parseDouble(arr[1]);
            System.out.println(a/b);
        } catch(IOException e) {

        }
    }
}