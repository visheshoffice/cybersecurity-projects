import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class Blockchain {
    private String data;
    private String previousHash;
    private String hash;

    public Blockchain(String data, String previousHash) throws NoSuchAlgorithmException {
        this.data = data;
        this.previousHash = previousHash;
        this.hash = calculateHash();
    }

    private String calculateHash() throws NoSuchAlgorithmException {
        String input = data + previousHash;
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = digest.digest(input.getBytes());

        // Convert the byte array to a hexadecimal representation
        StringBuilder hexHash = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = String.format("%02x", b);
            hexHash.append(hex);
        }

        return hexHash.toString();
    }

    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the first hash: ");
            String firstHash = scanner.nextLine();
            System.out.print("Enter the second hash: ");
            String secondHash = scanner.nextLine();

            // Combine the two hash values
            String combinedHash = firstHash + secondHash;

            // Assign the combined hash value to the genesis block of another blockchain
            Blockchain newBlockchain = new Blockchain("GenesisData", combinedHash);
            System.out.println("Hash of the Genesis Block of the New Blockchain: " + newBlockchain.hash);

            scanner.close();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}
