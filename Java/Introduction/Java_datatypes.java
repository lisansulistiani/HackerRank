import java.util.*;
import java.io.*;



class Solution{
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-Math.pow(2,(Byte.SIZE)-1) && x<Math.pow(2,(Byte.SIZE)-1)){
                    System.out.println("* byte");
                }
                if(x>=-Math.pow(2,(Short.SIZE)-1) && x<Math.pow(2,(Short.SIZE)-1)){
                    System.out.println("* short");
                }
                if(x>=-Math.pow(2,(Integer.SIZE)-1) && x<Math.pow(2,(Integer.SIZE)-1)){
                    System.out.println(("* int"));
                }
                if(x>=-Math.pow(2,(Long.SIZE)-1) && x<=Math.pow(2,(Long.SIZE)-1)){
                    System.out.println(("* long"));
                }
                //Complete the code
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}



