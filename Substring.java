/*
For a given input string(str), write a function to print all the possible substrings.
 */

import java.util.Scanner;

public class Substrings {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Input String");
        String str = in.next();

        System.out.println("Substrings: ");
        printSubstrings(str);
    }

    public static void printSubstrings(String str){
        int n = str.length();

        for(int i = 0; i<n; ++i){
            for(int j = i; j<n; ++j){
                for(int k = i; k<=j; ++k){
                    System.out.print(str.charAt(k));
                }
                System.out.println();
            }
        }
    }
}
