all:
	$(MAKE) -C richdem/programs/parallel_d8_accum
	mv ./richdem/programs/parallel_d8_accum/parallel_d8_accum.exe ./