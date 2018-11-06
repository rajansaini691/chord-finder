import pysox

# Takes in an input file
infile = pysox.CSoxStream('G.wav')

# Creates a new output file to be written to
outfile = pysox.CSoxStream('out.wav','w',infile.get_signal())

# Creates a new chain of effects
chain = pysox.CEffectsChain(infile, outfile)

# Creates a new effect
effect = pysox.CEffect("chorus", [b'0.7', b'0.9', b'55', b'0.4', b'0.25', b'2', b'-t'])

# Adds the created effect to the chain
chain.add_effect(effect)

# Writes all effects on the chain to the output file
chain.flow_effects()

# Ends the program
outfile.close()
