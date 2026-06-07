import numpy as np
from scipy.signal import lfilter, lfilter_zi
from dataclasses import dataclass, replace

from dt_core.templates.processing import Processing, ProcessingConfig
from dt_core.structures.messages import DataPacket

class BaseFIRProcessor(Processing):
    """Shared execution logic for all Scipy-based FIR filters."""
    
    def process(self, packet: DataPacket) -> DataPacket:
        # All filters share this exact stateful processing logic
        if getattr(self, 'state', None) is None:
            base_zi = lfilter_zi(self.taps, 1.0)
            initial_values = packet.data[..., 0:1] # Slice keeps dimensions for broadcasting
            self.state = base_zi * initial_values

        filtered_data, self.state = lfilter(self.taps, 1.0, packet.data, zi=self.state)
        return replace(packet, data=filtered_data)