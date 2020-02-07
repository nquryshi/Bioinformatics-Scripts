# Paste the sequence you want to work with here
myStr = 'GTTTCACAATTTTTCAAGCAAGGAAACGGGCTCGGAGGTCTTGAACACCTGCTACCCAATAGCAGAACAGCTACTGGAACTAAAATCCTCTGATTTCAAATAACAGCCCCGCCCACTACCAC TAAGTGAAGTCATCCACAACCACACACCGACCACTCTAAGCTTTTGTAAGATCGGCTCGCTTTG GGGAACAGGTCTTGAGAGAACATCCCTTTTAAGGTCAGAACAAAGGTATTTCATAGGTCCCAG GTCGTGTCCCGAGGGCGCCCACCCAAACATGAGCTGGAGCAAAAAGAAAGGGATGGGGGACTTGGAGTAGGCATAGGGGCGGAGGGTGGCCTGGGACTCTTAAGGGTCAGCGAGAAGAGAACACACACTCCAG'

################################################################################
# REVERSE COMPLEMENT FUNCTION - GENERATES REVERSE COMPLEMENT OF DNA SEQUENCE

alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

def reverse_complement(seq):    
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases

################################################################################

PrimerARV = reverse_complement('AGCCCGTTTCCTTGCTTG')
PrimerBRV = reverse_complement('TAAGGTCAGAACAAAGGTA')
PrimerCRV = reverse_complement('CTTAAGAGTCCCAGGCCAC')
PrimerDRV = reverse_complement('GAGGTCTTGAACACCTGC')

PrimerA = 'AGCCCGTTTCCTTGCTTG'
PrimerB = 'TAAGGTCAGAACAAAGGTA'
PrimerC = 'CTTAAGAGTCCCAGGCCAC'
PrimerD = 'GAGGTCTTGAACACCTGC'

result1 = myStr.find(PrimerARV)
result2 = myStr.find(PrimerBRV)
result3 = myStr.find(PrimerCRV)
result4 = myStr.find(PrimerDRV)

print(result1)
print(result2)
print(result3)
print(result4)
