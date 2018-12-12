import pysox
import numpy as np
from scikits.audiolab import wavread, wavwrite

def lp_filter_helper(x, freq):
	return np.exp(-19*(x-0.2)**2)

lp_filter = np.vectorize(lp_filter_helper)

# Adds noise to the file at the beginning
data2, fs2, enc2 = wavread("0007/G.wav")
percent_noise = 0.05
noise = lp_filter(np.random.randn(*data2.shape), -0.5)
result = (3 - percent_noise) * data2 + percent_noise * noise

wavwrite(result, "G.wav", 44100)

# Takes in an input file
infile = pysox.CSoxStream('G.wav')

# Creates a new output file to be written to
outfile = pysox.CSoxStream('G_Modified.wav','w',infile.get_signal())

# Creates a new chain of effects
chain = pysox.CEffectsChain(infile, outfile)

# Adds chorus 
chorus = pysox.CEffect("chorus", [b'0.7', b'0.9', b'55', b'0.4', b'0.25', b'2', b'-t'])
chain.add_effect(chorus)

# Adds reverb to the file
reverb = pysox.CEffect("reverb", [b'100'])
chain.add_effect(reverb)

# Adds echo
echo = pysox.CEffect("echo", [b'0.8', b'0.88', b'1000', b'0.4'])
chain.add_effect(echo)

# Adds pitch bending (tremolo)
tremolo = pysox.CEffect("tremolo", [b'5', b'50'])
chain.add_effect(tremolo)

# Adds overdrive
overdrive = pysox.CEffect("overdrive", [b'50', b'0'])
chain.add_effect(overdrive)

# Writes all effects on the chain to the output file
chain.flow_effects()

# Ends the program
outfile.close()

