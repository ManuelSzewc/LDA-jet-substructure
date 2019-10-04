# number of background events
Nb=450

# S/B fraction
sb=0.1

# number of signal events
Ns=round(sb*Nb)

#Set Multicore to 1 for Multicore (less time, more cores involved)
Multicore=1
# gensim parameters for Multicore LDA (keep the format as a string here)
gensim_parameters_Multicore="num_topics=2,alpha=[2.727,0.273],passes=300,iterations=100,gamma_threshold=0.00000001,eval_every=10,workers=2,chunksize=10000,offset=1000.0"
# gensim parameters for old LDA (keep the format as a string here)
gensim_parameters="num_topics=2,alpha=[0.9,0.1],passes=20,iterations=100,gamma_threshold=0.00000001,eval_every=10,update_every=1,chunksize=1,decay=0.5, offset=1000.0"
# the alpha parameters are the hyper-parameters that determine the topic concentrations in the docs and in the corpus
# the passes is how many times you train over the whole dataset
# for details on other parameters we refer the reader to the gensim webpage

# bin sizes for the observables, should match what was used in the parser
sj_bin_size=10
md_bin_size=0.05
pmr_bin_size=0.1
kt_bin_size=0.1
ha_bin_size=0.1

# max for subjet mass histogram axes
sj_min_bin=30
sj_max_bin=200
