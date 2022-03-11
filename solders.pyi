from typing import List, Union

def is_on_curve(_bytes: bytes) -> bool: ...

class Pubkey:
    LENGTH: int
    def __init__(self, pubkey_bytes: bytes) -> None: ...
    @staticmethod
    def new_unique() -> "Pubkey": ...
    @staticmethod
    def default() -> "Pubkey": ...
    @staticmethod
    def from_string(s: str) -> "Pubkey": ...
    @staticmethod
    def create_with_seed(
        from_public_key: "Pubkey", seed: str, program_id: "Pubkey"
    ) -> "Pubkey": ...
    @staticmethod
    def create_program_address(seeds: List[bytes]) -> "Pubkey": ...
    @staticmethod
    def find_program_address(seeds: List[bytes], program_id: "Pubkey") -> "Pubkey": ...
    def is_on_curve(self) -> bool: ...
    def string(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def __richcmp__(self, other: "Pubkey", op: int) -> bool: ...
    def __hash__(self) -> int: ...

class Keypair:
    def __init__(self) -> None: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "Keypair": ...
    @staticmethod
    def from_seed(seed: bytes) -> "Keypair": ...
    @staticmethod
    def from_base58_string(s: str) -> "Keypair": ...
    @staticmethod
    def from_seed_phrase_and_passphrase(
        seed_phrase: str, passphrase: str
    ) -> "Keypair": ...
    def secret(self) -> bytes: ...
    def pubkey(self) -> Pubkey: ...
    def sign_message(self, message: bytes) -> Signature: ...
    def to_bytes_array(self) -> List[int]: ...
    def to_base58_string(self) -> str: ...
    def __str__(self) -> str: ...
    def __bytes__(self) -> str: ...
    def __richcmp__(self, other: "Keypair", op: int) -> bool: ...
    def __hash__(self) -> int: ...

class Signature:
    def __init__(self, signature_slice: bytes) -> None: ...
    @staticmethod
    def new_unique() -> "Signature": ...
    @staticmethod
    def default() -> "Signature": ...
    @staticmethod
    def from_string(s: str) -> "Signature": ...
    def verify(self, pubkey_bytes: bytes, message_bytes: bytes) -> bool: ...
    def to_bytes_array(self) -> List[int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def to_string(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "Signature", op: int) -> bool: ...
    def __hash__(self) -> int: ...

class AccountMeta:
    def __init__(self, pubkey: Pubkey, is_signer: bool, is_writable: bool) -> None: ...
    @property
    def pubkey(self) -> Pubkey: ...
    @property
    def is_signer(self) -> bool: ...
    @property
    def is_writable(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "AccountMeta", op: int) -> bool: ...

class Instruction:
    def __init__(
        self, program_id: Pubkey, data: bytes, accounts: List[AccountMeta]
    ) -> None: ...
    @property
    def program_id(self) -> Pubkey: ...
    @property
    def data(self) -> bytes: ...
    @property
    def accounts(self) -> list[AccountMeta]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "Instruction", op: int) -> bool: ...

class Hash:
    def __init__(self, hash_bytes: Union[bytes, List[int]]) -> None: ...
    def to_string(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def from_string(s: str) -> "Hash": ...
    @staticmethod
    def new_unique() -> "Hash": ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def __richcmp__(self, other: "Hash", op: int) -> bool: ...

def decode_length(raw_bytes: bytes) -> tuple[int, int]: ...
def encode_length(value: int) -> list[int]: ...
