from scipy.signal import firwin
from dataclasses import dataclass
from dt_core.templates.processing import ProcessingConfig
from dt_fir.base_engine import BaseFIRProcessor

@dataclass(kw_only=True)
class FIR_HPF_Config(ProcessingConfig):
    plugin_id: str = "fir_hpf"
    cutoff_freq: float = 100.0
    sampling_rate: float = 1000.0
    num_taps: int = 101

class FIR_High_Pass_Filter(BaseFIRProcessor):
    config: FIR_HPF_Config

    def initialize(self):
        self.taps = firwin(
            numtaps=self.config.num_taps, 
            cutoff=self.config.cutoff_freq, 
            pass_zero=False, 
            fs=self.config.sampling_rate
        )
        self.state = None