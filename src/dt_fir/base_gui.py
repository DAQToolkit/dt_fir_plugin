from PyQt6 import QtWidgets
from dt_gui.templates.processing import ProcessingConfigurationWidget

class Base_FIR_LPF_HPF_Widget(ProcessingConfigurationWidget):
    """Shared configuration widget for single-cutoff filters (LPF/HPF)."""
    
    def __init__(self, config_class, plugin_id: str, parent=None):
        super().__init__(parent)
        self.config_class = config_class
        self.plugin_id = plugin_id  
        self.current_process_id = None 

        layout = QtWidgets.QVBoxLayout(self)
        self.cutoff_box = QtWidgets.QDoubleSpinBox()
        self.cutoff_box.setValue(100.0)
        
        self.samplerate_box = QtWidgets.QDoubleSpinBox()
        self.samplerate_box.setValue(1000.0)
        
        self.taps_box = QtWidgets.QSpinBox()
        self.taps_box.setValue(101)

        layout.addWidget(QtWidgets.QLabel("Cutoff Frequency (Hz):"))
        layout.addWidget(self.cutoff_box)
        layout.addWidget(QtWidgets.QLabel("Sampling Rate (Hz):"))
        layout.addWidget(self.samplerate_box)
        layout.addWidget(QtWidgets.QLabel("Number of Taps (Filter Order):"))
        layout.addWidget(self.taps_box)

    def set_config(self, config):
        self.current_process_id = config.process_id
        self.cutoff_box.setValue(config.cutoff_freq)
        self.samplerate_box.setValue(config.sampling_rate)
        self.taps_box.setValue(config.num_taps)

    def get_config(self):
        kwargs = {
            "plugin_id": self.plugin_id,
            "cutoff_freq": self.cutoff_box.value(),
            "sampling_rate": self.samplerate_box.value(),
            "num_taps": self.taps_box.value()
        }
        if self.current_process_id:
            kwargs["process_id"] = self.current_process_id
            
        return self.config_class(**kwargs)