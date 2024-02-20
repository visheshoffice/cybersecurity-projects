import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Block {
    private String data;
    private String previousHash;
    private String hash;

    public Block(String data, String previousHash) throws NoSuchAlgorithmException {
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
            String data = "Vishesh Singh Aditya Narayan Harmeek Singh Saurav Bishnoi";
            String previousHash = "00000000000000000000000000000000"; // Previous hash for the genesis block
            Block genesisBlock = new Block(data, previousHash);
            System.out.println("Hash of the genesis block: " + genesisBlock.hash);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}
