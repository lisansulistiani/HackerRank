import java.util.*;
import java.io.*;

class Solution{
    public static String hitung(int a, int b, int n){
        int s = a;
        int awal = 1;
        String hasil="";
        for(int i=0;i<n;i++){
            int ans = s+awal*b;
            awal = awal*2;
            s = ans;
            hasil+=ans+" ";
        }
        return hasil;
    }
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        int s = 0;
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            System.out.println(hitung(a, b, n));
        }
        in.close();
        
    }
}
