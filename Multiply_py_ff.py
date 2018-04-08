import numpy
from gnuradio import gr

class multiply_py_ff(gr.sync_block):
    """
    docstring for block multiply_py_ff
    """
    def __init__(self, multiple):
	self.multiple = multiple
        gr.sync_block.__init__(self,
		name="multiply_py_ff",
		#in_sig=[numpy.float32],
		#out_sig=[numpy.float32])
		in_sig=[(numpy.float32,2)],
		out_sig=[(numpy.float32,2)])

    def work(self, input_items,output_items):
	#out1= in1+in1
	output_items[0][0][:]=input_items[0][0]*self.multiple
	output_items[0][1][:]=input_items[0][1]*self.multiple
	
        return len(output_items)
