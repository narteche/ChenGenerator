# ======================================= QUABS ==================================== #
echo === QUABS 1 ===
time python3 solver_test_QUABS.py
mv ./output_files/quabs_times1.txt ./output_files/quabs_times3.txt
clear
# ================================================================================== #
echo === QUABS 2 ===
time python3 solver_test_QUABS.py
mv ./output_files/quabs_times1.txt ./output_files/quabs_times2.txt
clear
# ================================================================================== #
echo === QUABS 3 ===
time python3 solver_test_QUABS.py
clear
# ================================================================================== #
# ================================================================================== #


# ======================================= CQESTO =================================== #
echo === CQESTO 1 ===
time python3 solver_test_CQESTO.py
mv ./output_files/cqesto_times1.txt ./output_files/cqesto_times3.txt
clear
# ================================================================================== #
echo === CQESTO 2 ===
time python3 solver_test_CQESTO.py
mv ./output_files/cqesto_times1.txt ./output_files/cqesto_times2.txt
clear
# ================================================================================== #
echo === CQESTO 3 ===
time python3 solver_test_CQESTO.py
clear
# ================================================================================== #
# ================================================================================== #


# ======================================= DEPQBF =================================== #
echo === DEPQBF 1 ===
time python3 solver_test_DEPQBF.py
mv ./output_files/depqbf_new_times1.txt ./output_files/depqbf_new_times3.txt
clear
# ================================================================================== #
echo === DEPQBF 2 ===
time python3 solver_test_DEPQBF.py
mv ./output_files/depqbf_new_times1.txt ./output_files/depqbf_new_times2.txt
clear
# ================================================================================== #
echo === CQESTO 3 ===
time python3 solver_test_DEPQBF.py
clear
# ================================================================================== #
# ================================================================================== #