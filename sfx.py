import pysox

# Takes in an input file
infile = pysox.CSoxStream('G.wav')
outfile = pysox.CSoxStream('out.wav','w',infile.get_signal())

chain = pysox.CEffectsChain(infile, outfile)

effect = pysox.CEffect("chorus", [b'0.7', b'0.9', b'55', b'0.4', b'0.25', b'2', b'-t'])
chain.add_effect(effect)

chain.flow_effects()
outfile.close()
