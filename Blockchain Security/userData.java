import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class userData {
    public static String generateSHA256Hash(String gmail, String username, String password) throws NoSuchAlgorithmException 
    {
        // Combine user data into a single string
        String userData = gmail + username + password;
        
        // Create a SHA-256 hash of the combined user data
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = md.digest(userData.getBytes());
        
        // Convert the byte array to a hexadecimal representation
        StringBuilder hexHash = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xFF & b);
            if (hex.length() == 1) {
                hexHash.append('0'); // Ensure two digits
            }
            hexHash.append(hex);
        }
        
        return hexHash.toString();
    }

    public static void main(String[] args) throws NoSuchAlgorithmException 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Your Mail ID: ");
        String gmail = sc.nextLine();
        System.out.println("Enter Your Username: ");
        String username = sc.nextLine();
        System.out.println("Enter Your Password: ");
        String password = sc.nextLine();
        
        String hashValue = generateSHA256Hash(gmail, username, password);
        System.out.println("Generated SHA-256 Hash: " + hashValue);
    }
}
