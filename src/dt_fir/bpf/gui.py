from PyQt6 import QtWidgets
from dt_gui.templates.processing import ProcessingConfigurationWidget
from .engine import FIR_BPF_Config

class FIR_BPF_ConfigWidget(ProcessingConfigurationWidget):
    """Configuration widget for dual-cutoff filters (Band-Pass)."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_process_id = None

        layout = QtWidgets.QVBoxLayout(self)
        self.low_cutoff_box = QtWidgets.QDoubleSpinBox()
        self.low_cutoff_box.setValue(50.0)

        self.high_cutoff_box = QtWidgets.QDoubleSpinBox()
        self.high_cutoff_box.setValue(150.0)
        
        self.samplerate_box = QtWidgets.QDoubleSpinBox()
        self.samplerate_box.setValue(1000.0)
        
        self.taps_box = QtWidgets.QSpinBox()
        self.taps_box.setValue(101)

        layout.addWidget(QtWidgets.QLabel("Low Cutoff Frequency (Hz):"))
        layout.addWidget(self.low_cutoff_box)
        layout.addWidget(QtWidgets.QLabel("High Cutoff Frequency (Hz):"))
        layout.addWidget(self.high_cutoff_box)
        layout.addWidget(QtWidgets.QLabel("Sampling Rate (Hz):"))
        layout.addWidget(self.samplerate_box)
        layout.addWidget(QtWidgets.QLabel("Number of Taps (Filter Order):"))
        layout.addWidget(self.taps_box)
        
    def set_config(self, config: FIR_BPF_Config):
        self.current_process_id = config.process_id
        self.low_cutoff_box.setValue(config.low_cutoff_freq)
        self.high_cutoff_box.setValue(config.high_cutoff_freq)
        self.samplerate_box.setValue(config.sampling_rate)
        self.taps_box.setValue(config.num_taps)

    def get_config(self) -> FIR_BPF_Config:
        kwargs = {
            "plugin_id": "fir_bpf",
            "low_cutoff_freq": self.low_cutoff_box.value(),
            "high_cutoff_freq": self.high_cutoff_box.value(),
            "sampling_rate": self.samplerate_box.value(),
            "num_taps": self.taps_box.value()
        }
        if self.current_process_id:
            kwargs["process_id"] = self.current_process_id
            
        return FIR_BPF_Config(**kwargs)