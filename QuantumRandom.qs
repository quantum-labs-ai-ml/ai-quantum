namespace QuantumRandomAI {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    // Operation to generate a single random bit using a qubit in superposition
    operation GenerateRandomBit() : Result {
        use q = Qubit(); // Allocate a qubit
        H(q); // Apply Hadamard gate to create superposition
        let result = M(q); // Measure the qubit
        Reset(q); // Reset qubit before releasing
        return result;
    }

    // Operation to generate an array of random bits
    operation GenerateRandomBits(count : Int) : Result[] {
        mutable results = [];
        for _ in 0..count-1 {
            let bit = GenerateRandomBit();
            set results += [bit];
        }
        return results;
    }
}
