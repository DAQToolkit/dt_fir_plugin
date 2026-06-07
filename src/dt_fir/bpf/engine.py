from scipy.signal import firwin
from dataclasses import dataclass
from dt_core.templates.processing import ProcessingConfig
from dt_fir.base_engine import BaseFIRProcessor

@dataclass(kw_only=True)
class FIR_BPF_Config(ProcessingConfig):
    plugin_id: str = "fir_bpf"
    low_cutoff_freq: float = 50.0
    high_cutoff_freq: float = 150.0
    sampling_rate: float = 1000.0
    num_taps: int = 101

class FIR_Band_Pass_Filter(BaseFIRProcessor):
    config: FIR_BPF_Config

    def initialize(self):
        self.taps = firwin(
            numtaps=self.config.num_taps, 
            cutoff=[self.config.low_cutoff_freq, self.config.high_cutoff_freq], 
            pass_zero=False, 
            fs=self.config.sampling_rate
        )
        self.state = None