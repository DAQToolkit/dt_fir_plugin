from .engine import FIR_HPF_Config as ProcessorConfig
from .engine import FIR_High_Pass_Filter as Processor

try:
    from .gui import FIR_HPF_ConfigWidget as ProcessorConfigurationWidget
except ImportError:
    ProcessorConfigurationWidget = None

__all__ = ["ProcessorConfig", "Processor", "ProcessorConfigurationWidget"]