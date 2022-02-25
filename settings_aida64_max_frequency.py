from datetime import timedelta


# #####################  MUST SET THESE CORRECTLY  ###########################
necessary = {
    # name of process (could also be "cinebench")
    "process_to_switch": "aida_bench64.dll",

    # number of cores
    "core_num": 6,

    # True or False, whether your CPU has 2 threads per core (SMT is AMD word)
    "hyper_threading": True,
}
##############################################################################


# The below are optional
other_options = {
    # Set to a low time so that you can quickly assess max frequencies
    "switch_every": timedelta(minutes=1),
    # synchronize with wall time because prime95 only logs time in hh:mm
    "sync_on_clock_minute": True,
    # 1-indexed (1 is first, total number of cores is last index)
    # core number to start testing from
    "starting_core": 1
}


cfg = other_options | necessary
