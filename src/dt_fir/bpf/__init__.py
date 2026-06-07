from .engine import FIR_BPF_Config as ProcessorConfig
from .engine import FIR_Band_Pass_Filter as Processor

try:
    from .gui import FIR_BPF_ConfigWidget as ProcessorConfigurationWidget
except ImportError:
    ProcessorConfigurationWidget = None

__all__ = ["ProcessorConfig", "Processor", "ProcessorConfigurationWidget"]