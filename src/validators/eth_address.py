"""ETH Address."""

# standard
import re

# local
from .utils import validator

@validator
def eth_address(value: str, /):
    """Return whether or not given value is a valid Ethereum address.

    Examples:
        >>> eth_address(
        ...     '0x71C7656EC7ab88b098defB751B7401B5f6d8976F'
        ... )
        # Output: True
        >>> eth_address('900zz11')
        # Output: ValidationError(func=eth_address, args={'value': '900zz11'})

    Args:
        value:
            Ethereum address string to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid Ethereum address.
        (ValidationError):
            If `value` is an invalid Ethereum address.

    > *New in version VER*
    """
    return re.match(r"^0x[a-f0-9]{40}$", value, re.IGNORECASE) if value else False