from .engine import FIR_LPF_Config as ProcessorConfig
from .engine import FIR_Low_Pass_Filter as Processor

try:
    from .gui import FIR_LPF_ConfigWidget as ProcessorConfigurationWidget
except ImportError:
    ProcessorConfigurationWidget = None

__all__ = ["ProcessorConfig", "Processor", "ProcessorConfigurationWidget"]