import pysox

# Takes in an input file
infile = pysox.CSoxStream('G.wav')

# Creates a new output file to be written to
outfile = pysox.CSoxStream('G_Modified.wav','w',infile.get_signal())

# Creates a new chain of effects
chain = pysox.CEffectsChain(infile, outfile)

# Adds chorus 
chorus = pysox.CEffect("chorus", [b'0.7', b'0.9', b'55', b'0.4', b'0.25', b'2', b'-t'])
chain.add_effect(chorus)

# Adds reverb
reverb = pysox.CEffect("reverb", [b'50'])
chain.add_effect(reverb)

# Adds echo
echo = pysox.CEffect("echo", [b'0.8', b'0.88', b'1000', b'0.4'])
chain.add_effect(echo)

# Adds pitch bending (tremolo)
tremolo = pysox.CEffect("tremolo", [b'5', b'50'])
chain.add_effect(tremolo)

# Reverses the sound 
# reverse = pysox.CEffect("reverse", [])
# chain.add_effect(reverse)

# Writes all effects on the chain to the output file
chain.flow_effects()

# Ends the program
outfile.close()
