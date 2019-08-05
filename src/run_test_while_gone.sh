# ======================================= GENERATE ==================================== #
echo GENERATING
time python3 simple_generator.py

# ======================================= DEBQBF ==================================== #
echo === DEPQBF 1 ===
time python3 solver_test_DEPQBF.py
mv ./output_files/depqbf_t2_times1.txt ./output_files/depqbf_t2_times3.txt

# ================================================================================== #
echo === DEPQBF 2 ===
time python3 solver_test_DEPQBF.py
mv ./output_files/depqbf_t2_times1.txt ./output_files/depqbf_t2_times2.txt

# ================================================================================== #
echo === DEPQBF 3 ===
time python3 solver_test_DEPQBF.py

# ================================================================================== #
# ================================================================================== #


# ======================================= CAQE ==================================== #
echo === CAQE 1 ===
time python3 solver_test_CAQE.py
mv ./output_files/caqe_t2_times1.txt ./output_files/caqe_t2_times3.txt

# ================================================================================== #
echo === CAQE 2 ===
time python3 solver_test_CAQE.py
mv ./output_files/caqe_t2_times1.txt ./output_files/caqe_t2_times2.txt

# ================================================================================== #
echo === CAQE 3 ===
time python3 solver_test_CAQE.py

# ================================================================================== #
# ================================================================================== #

