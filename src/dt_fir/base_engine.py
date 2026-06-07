import numpy as np
from scipy.signal import lfilter, lfilter_zi
from dataclasses import dataclass, replace

from dt_core.templates.processing import Processing, ProcessingConfig
from dt_core.structures.messages import DataPacket

class BaseFIRProcessor(Processing):
    """Shared execution logic for all Scipy-based FIR filters."""
    
    def process(self, packet: DataPacket) -> DataPacket:
        # --- PREVENT CRASH: Force data into a numpy matrix ---
        np_data = np.asarray(packet.data)
        
        if getattr(self, 'state', None) is None:
            base_zi = lfilter_zi(self.taps, 1.0)
            # Now the ellipsis indexing will work perfectly!
            initial_values = np_data[..., 0:1] 
            self.state = base_zi * initial_values

        filtered_data, self.state = lfilter(self.taps, 1.0, np_data, zi=self.state)
        
        return replace(packet, data=filtered_data)