import time

SECRET_KEY = bytes.fromhex("b2c439e8e7c98c0166be57ae5f4c1b80c0c9360d33ac29fba0e40fd4978b7eec2f41b767bbac8d0cd5c1a4db90cd335dcfd8925ee52f8860192711c53786e6cf")
time_offset = -3

def generate_seed() -> int:
    """Get the current time for offset seed."""
    return int(time.time())


def decode_bytes(byte_data: bytes) -> str:
    """Convert bytes to a UTF-8 string."""
    return byte_data.decode("utf-8")


def xor_layer(data: bytes, seed: int) -> bytes:
    """Apply XOR using the SECRET_KEY and a seed value for offset."""
    return bytes(
        byte ^ SECRET_KEY[(i + seed) % len(SECRET_KEY)] for i, byte in enumerate(data)
    )


def deobfuscate(hex_encoded: bytes, seed: int) -> bytes:
    """Convert a hex-encoded byte string back to original bytes using XOR decryption."""
    hex_str = decode_bytes(hex_encoded)
    if hex_str[0] == '"':
        hex_str = hex_str[1:-1]

    byte_data = bytes.fromhex(hex_str)

    return xor_layer(byte_data, seed + time_offset)


def obfuscate(data: bytes, seed: int) -> str:
    """Convert data to a hex-encoded string after XOR encryption."""
    encrypted_bytes = xor_layer(data, seed + time_offset)

    return f'"{encrypted_bytes.hex()}"'
