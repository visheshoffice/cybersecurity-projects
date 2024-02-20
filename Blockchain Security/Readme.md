# Blockchain Security

## Overview

Blockchain Security is a Java-based project that demonstrates the implementation of a simple blockchain and user authentication system. The project consists of three main classes: `Block.java`, `Blockchain.java`, and `userData.java`. 

## Classes

### Block.java

The `Block.java` class represents a single block in the blockchain. Each block contains the following attributes:

- `data`: The data stored in the block.
- `previousHash`: The hash of the previous block in the chain.
- `hash`: The hash of the current block.

The `Block.java` class provides a constructor to create a new block and a method `calculateHash()` to calculate the hash of the block based on its data and previous hash.

### Blockchain.java

The `Blockchain.java` class represents the entire blockchain. It contains a list of blocks and provides methods to add new blocks to the chain and validate the integrity of the chain.

The `Blockchain.java` class provides a constructor to create a new blockchain with a genesis block and a method `addBlock()` to add a new block to the chain. It also provides a method `isValid()` to validate the integrity of the chain by checking the hashes of all blocks.

### userData.java

The `userData.java` class represents a user's data for authentication purposes. It contains a method `generateSHA256Hash()` to generate a SHA-256 hash of the user's data (Gmail, username, and password).

## Usage

To use the Blockchain Security project, follow these steps:

1. Clone the repository to your local machine.
2. Compile the Java files using a Java compiler.
3. Run the `Blockchain.java` class to create a new blockchain and add blocks to it.
4. Run the `userData.java` class to generate a SHA-256 hash of a user's data.

## Dependencies

The project requires Java 8 or higher to compile and run. It uses the `MessageDigest` class from the `java.security` package to calculate SHA-256 hashes.

## Contributing

Contributions to the Blockchain Security project are welcome. To contribute, fork the repository, make your changes, and submit a pull request.

## License

The Blockchain Security project is open-source and licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

For any questions or issues, please contact the project maintainer at https://www.linkedin.com/in/visheshoffice/.

## Acknowledgements

The Blockchain Security project was inspired by [Blockchain Technology](https://en.wikipedia.org/wiki/Blockchain) and [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hashing algorithm.

## References

- [Java MessageDigest](https://docs.oracle.com/javase/8/docs/api/java/security/MessageDigest.html)
- [SHA-256 Hashing Algorithm](https://en.wikipedia.org/wiki/SHA-2)

## Conclusion

Blockchain Security is a simple yet powerful demonstration of blockchain technology and user authentication using SHA-256 hashing. The project can be used as a learning tool for understanding the basics of blockchain and cryptography.

Feel free to modify and extend the project to suit your needs. Happy coding!
