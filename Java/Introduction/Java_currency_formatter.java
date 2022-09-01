import java.util.*;
import java.text.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        NumberFormat defaultFormat = NumberFormat.getCurrencyInstance();
        NumberFormat cn = NumberFormat.getCurrencyInstance(java.util.Locale.CHINA);
        NumberFormat fr = NumberFormat.getCurrencyInstance(java.util.Locale.FRANCE);
        NumberFormat inr = NumberFormat.getCurrencyInstance(new Locale("en", "in"));
        String us = defaultFormat.format(payment);
        String france = fr.format(payment);
        String china = cn.format(payment);
        String india = inr.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
        /*
        */
    }
}
