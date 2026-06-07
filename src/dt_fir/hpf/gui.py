from dt_fir.base_gui import Base_FIR_LPF_HPF_Widget
from .engine import FIR_HPF_Config

class FIR_HPF_ConfigWidget(Base_FIR_LPF_HPF_Widget):
    def __init__(self, parent=None):
        super().__init__(config_class=FIR_HPF_Config, plugin_id="fir_hpf", parent=parent)