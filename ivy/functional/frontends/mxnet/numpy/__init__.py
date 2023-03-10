# flake8: noqa
import ivy
from . import random
from . import ndarray
from . import linalg
from .linalg import *
from . import mathematical_functions
from .mathematical_functions import *
from . import creation
from .creation import *
from . import symbol
from .symbol import *


mxnet_promotion_table = {
    (ivy.bool, ivy.bool): ivy.bool,
    (ivy.bool, ivy.int8): ivy.int8,
    (ivy.bool, ivy.int16): ivy.int16,
    (ivy.bool, ivy.int32): ivy.int32,
    (ivy.bool, ivy.int64): ivy.int64,
    (ivy.bool, ivy.uint8): ivy.uint8,
    (ivy.bool, ivy.uint16): ivy.uint16,
    (ivy.bool, ivy.uint32): ivy.uint32,
    (ivy.bool, ivy.uint64): ivy.uint64,
    (ivy.bool, ivy.bfloat16): ivy.bfloat16,
    (ivy.bool, ivy.float16): ivy.float16,
    (ivy.bool, ivy.float32): ivy.float32,
    (ivy.bool, ivy.float64): ivy.float64,
    (ivy.bool, ivy.complex64): ivy.complex64,
    (ivy.bool, ivy.complex128): ivy.complex128,
    (ivy.bool, ivy.bool): ivy.bool,
    (ivy.int8, ivy.bool): ivy.int8,
    (ivy.int8, ivy.int8): ivy.int8,
    (ivy.int8, ivy.int16): ivy.int16,
    (ivy.int8, ivy.int32): ivy.int32,
    (ivy.int8, ivy.int64): ivy.int64,
    (ivy.int16, ivy.bool): ivy.int16,
    (ivy.int16, ivy.int8): ivy.int16,
    (ivy.int16, ivy.int16): ivy.int16,
    (ivy.int16, ivy.int32): ivy.int32,
    (ivy.int16, ivy.int64): ivy.int64,
    (ivy.int32, ivy.bool): ivy.int32,
    (ivy.int32, ivy.int8): ivy.int32,
    (ivy.int32, ivy.int16): ivy.int32,
    (ivy.int32, ivy.int32): ivy.int32,
    (ivy.int32, ivy.int64): ivy.int64,
    (ivy.int64, ivy.bool): ivy.int64,
    (ivy.int64, ivy.int8): ivy.int64,
    (ivy.int64, ivy.int16): ivy.int64,
    (ivy.int64, ivy.int32): ivy.int64,
    (ivy.int64, ivy.int64): ivy.int64,
    (ivy.uint8, ivy.bool): ivy.uint8,
    (ivy.uint8, ivy.uint8): ivy.uint8,
    (ivy.uint8, ivy.uint16): ivy.uint16,
    (ivy.uint8, ivy.uint32): ivy.uint32,
    (ivy.uint8, ivy.uint64): ivy.uint64,
    (ivy.uint16, ivy.bool): ivy.uint16,
    (ivy.uint16, ivy.uint8): ivy.uint16,
    (ivy.uint16, ivy.uint16): ivy.uint16,
    (ivy.uint16, ivy.uint32): ivy.uint32,
    (ivy.uint16, ivy.uint64): ivy.uint64,
    (ivy.uint32, ivy.bool): ivy.uint32,
    (ivy.uint32, ivy.uint8): ivy.uint32,
    (ivy.uint32, ivy.uint16): ivy.uint32,
    (ivy.uint32, ivy.uint32): ivy.uint32,
    (ivy.uint32, ivy.uint64): ivy.uint64,
    (ivy.uint64, ivy.bool): ivy.uint64,
    (ivy.uint64, ivy.uint8): ivy.uint64,
    (ivy.uint64, ivy.uint16): ivy.uint64,
    (ivy.uint64, ivy.uint32): ivy.uint64,
    (ivy.uint64, ivy.uint64): ivy.uint64,
    (ivy.int8, ivy.uint8): ivy.int16,
    (ivy.int8, ivy.uint16): ivy.int32,
    (ivy.int8, ivy.uint32): ivy.int64,
    (ivy.int16, ivy.uint8): ivy.int16,
    (ivy.int16, ivy.uint16): ivy.int32,
    (ivy.int16, ivy.uint32): ivy.int64,
    (ivy.int32, ivy.uint8): ivy.int32,
    (ivy.int32, ivy.uint16): ivy.int32,
    (ivy.int32, ivy.uint32): ivy.int64,
    (ivy.int64, ivy.uint8): ivy.int64,
    (ivy.int64, ivy.uint16): ivy.int64,
    (ivy.int64, ivy.uint32): ivy.int64,
    (ivy.uint8, ivy.int8): ivy.int16,
    (ivy.uint16, ivy.int8): ivy.int32,
    (ivy.uint32, ivy.int8): ivy.int64,
    (ivy.uint8, ivy.int16): ivy.int16,
    (ivy.uint16, ivy.int16): ivy.int32,
    (ivy.uint32, ivy.int16): ivy.int64,
    (ivy.uint8, ivy.int32): ivy.int32,
    (ivy.uint16, ivy.int32): ivy.int32,
    (ivy.uint32, ivy.int32): ivy.int64,
    (ivy.uint8, ivy.int64): ivy.int64,
    (ivy.uint16, ivy.int64): ivy.int64,
    (ivy.uint32, ivy.int64): ivy.int64,
    (ivy.float16, ivy.bool): ivy.float16,
    (ivy.float16, ivy.float16): ivy.float16,
    (ivy.float16, ivy.float32): ivy.float32,
    (ivy.float16, ivy.float64): ivy.float64,
    (ivy.float32, ivy.bool): ivy.float32,
    (ivy.float32, ivy.float16): ivy.float32,
    (ivy.float32, ivy.float32): ivy.float32,
    (ivy.float32, ivy.float64): ivy.float64,
    (ivy.float64, ivy.bool): ivy.float64,
    (ivy.float64, ivy.float16): ivy.float64,
    (ivy.float64, ivy.float32): ivy.float64,
    (ivy.float64, ivy.float64): ivy.float64,
    (ivy.uint64, ivy.int8): ivy.float64,
    (ivy.int8, ivy.uint64): ivy.float64,
    (ivy.uint64, ivy.int16): ivy.float64,
    (ivy.int16, ivy.uint64): ivy.float64,
    (ivy.uint64, ivy.int32): ivy.float64,
    (ivy.int32, ivy.uint64): ivy.float64,
    (ivy.uint64, ivy.int64): ivy.float64,
    (ivy.int64, ivy.uint64): ivy.float64,
    (ivy.int8, ivy.float16): ivy.float16,
    (ivy.float16, ivy.int8): ivy.float16,
    (ivy.int8, ivy.float32): ivy.float32,
    (ivy.float32, ivy.int8): ivy.float32,
    (ivy.int8, ivy.float64): ivy.float64,
    (ivy.float64, ivy.int8): ivy.float64,
    (ivy.int16, ivy.float16): ivy.float32,
    (ivy.float16, ivy.int16): ivy.float32,
    (ivy.int16, ivy.float32): ivy.float32,
    (ivy.float32, ivy.int16): ivy.float32,
    (ivy.int16, ivy.float64): ivy.float64,
    (ivy.float64, ivy.int16): ivy.float64,
    (ivy.int32, ivy.float16): ivy.float64,
    (ivy.float16, ivy.int32): ivy.float64,
    (ivy.int32, ivy.float32): ivy.float64,
    (ivy.float32, ivy.int32): ivy.float64,
    (ivy.int32, ivy.float64): ivy.float64,
    (ivy.float64, ivy.int32): ivy.float64,
    (ivy.int64, ivy.float16): ivy.float64,
    (ivy.float16, ivy.int64): ivy.float64,
    (ivy.int64, ivy.float32): ivy.float64,
    (ivy.float32, ivy.int64): ivy.float64,
    (ivy.int64, ivy.float64): ivy.float64,
    (ivy.float64, ivy.int64): ivy.float64,
    (ivy.uint8, ivy.float16): ivy.float16,
    (ivy.float16, ivy.uint8): ivy.float16,
    (ivy.uint8, ivy.float32): ivy.float32,
    (ivy.float32, ivy.uint8): ivy.float32,
    (ivy.uint8, ivy.float64): ivy.float64,
    (ivy.float64, ivy.uint8): ivy.float64,
    (ivy.uint16, ivy.float16): ivy.float32,
    (ivy.float16, ivy.uint16): ivy.float32,
    (ivy.uint16, ivy.float32): ivy.float32,
    (ivy.float32, ivy.uint16): ivy.float32,
    (ivy.uint16, ivy.float64): ivy.float64,
    (ivy.float64, ivy.uint16): ivy.float64,
    (ivy.uint32, ivy.float16): ivy.float64,
    (ivy.float16, ivy.uint32): ivy.float64,
    (ivy.uint32, ivy.float32): ivy.float64,
    (ivy.float32, ivy.uint32): ivy.float64,
    (ivy.uint32, ivy.float64): ivy.float64,
    (ivy.float64, ivy.uint32): ivy.float64,
    (ivy.uint64, ivy.float16): ivy.float64,
    (ivy.float16, ivy.uint64): ivy.float64,
    (ivy.uint64, ivy.float32): ivy.float64,
    (ivy.float32, ivy.uint64): ivy.float64,
    (ivy.uint64, ivy.float64): ivy.float64,
    (ivy.float64, ivy.uint64): ivy.float64,
    (ivy.bfloat16, ivy.bfloat16): ivy.bfloat16,
    (ivy.bfloat16, ivy.uint8): ivy.bfloat16,
    (ivy.uint8, ivy.bfloat16): ivy.bfloat16,
    (ivy.bfloat16, ivy.int8): ivy.bfloat16,
    (ivy.int8, ivy.bfloat16): ivy.bfloat16,
    (ivy.bfloat16, ivy.float32): ivy.float32,
    (ivy.float32, ivy.bfloat16): ivy.float32,
    (ivy.bfloat16, ivy.float64): ivy.float64,
    (ivy.float64, ivy.bfloat16): ivy.float64,
    (ivy.complex64, ivy.bool): ivy.complex64,
    (ivy.complex64, ivy.int8): ivy.complex64,
    (ivy.complex64, ivy.int16): ivy.complex64,
    (ivy.complex64, ivy.int32): ivy.complex128,
    (ivy.complex64, ivy.int64): ivy.complex128,
    (ivy.complex64, ivy.uint8): ivy.complex64,
    (ivy.complex64, ivy.uint16): ivy.complex64,
    (ivy.complex64, ivy.uint32): ivy.complex128,
    (ivy.complex64, ivy.uint64): ivy.complex128,
    (ivy.complex64, ivy.float16): ivy.complex64,
    (ivy.complex64, ivy.float32): ivy.complex64,
    (ivy.complex64, ivy.float64): ivy.complex128,
    (ivy.complex64, ivy.bfloat16): ivy.complex64,
    (ivy.complex64, ivy.complex64): ivy.complex64,
    (ivy.complex64, ivy.complex128): ivy.complex128,
    (ivy.complex128, ivy.bool): ivy.complex128,
    (ivy.complex128, ivy.int8): ivy.complex128,
    (ivy.complex128, ivy.int16): ivy.complex128,
    (ivy.complex128, ivy.int32): ivy.complex128,
    (ivy.complex128, ivy.int64): ivy.complex128,
    (ivy.complex128, ivy.uint8): ivy.complex128,
    (ivy.complex128, ivy.uint16): ivy.complex128,
    (ivy.complex128, ivy.uint32): ivy.complex128,
    (ivy.complex128, ivy.uint64): ivy.complex128,
    (ivy.complex128, ivy.float16): ivy.complex128,
    (ivy.complex128, ivy.float32): ivy.complex128,
    (ivy.complex128, ivy.float64): ivy.complex128,
    (ivy.complex128, ivy.bfloat16): ivy.complex128,
    (ivy.complex128, ivy.complex64): ivy.complex128,
    (ivy.complex128, ivy.complex128): ivy.complex128,
    (ivy.int8, ivy.complex64): ivy.complex64,
    (ivy.int16, ivy.complex64): ivy.complex64,
    (ivy.int32, ivy.complex64): ivy.complex128,
    (ivy.int64, ivy.complex64): ivy.complex128,
    (ivy.uint8, ivy.complex64): ivy.complex64,
    (ivy.uint16, ivy.complex64): ivy.complex64,
    (ivy.uint32, ivy.complex64): ivy.complex128,
    (ivy.uint64, ivy.complex64): ivy.complex128,
    (ivy.float16, ivy.complex64): ivy.complex64,
    (ivy.float32, ivy.complex64): ivy.complex64,
    (ivy.float64, ivy.complex64): ivy.complex128,
    (ivy.bfloat16, ivy.complex64): ivy.complex64,
    (ivy.int8, ivy.complex128): ivy.complex128,
    (ivy.int16, ivy.complex128): ivy.complex128,
    (ivy.int32, ivy.complex128): ivy.complex128,
    (ivy.int64, ivy.complex128): ivy.complex128,
    (ivy.uint8, ivy.complex128): ivy.complex128,
    (ivy.uint16, ivy.complex128): ivy.complex128,
    (ivy.uint32, ivy.complex128): ivy.complex128,
    (ivy.uint64, ivy.complex128): ivy.complex128,
    (ivy.float16, ivy.complex128): ivy.complex128,
    (ivy.float32, ivy.complex128): ivy.complex128,
    (ivy.float64, ivy.complex128): ivy.complex128,
    (ivy.bfloat16, ivy.complex128): ivy.complex128,
}
