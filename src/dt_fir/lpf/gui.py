from dt_fir.base_gui import Base_FIR_LPF_HPF_Widget
from .engine import FIR_LPF_Config

class FIR_LPF_ConfigWidget(Base_FIR_LPF_HPF_Widget):
    def __init__(self, parent=None):
        super().__init__(config_class=FIR_LPF_Config, plugin_id="fir_lpf", parent=parent)