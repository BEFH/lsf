class CookieCutter:
    """
    Cookie Cutter wrapper
    """

    @staticmethod
    def get_default_mem_mb() -> int:
        return int("4096")

    @staticmethod
    def get_log_dir() -> str:
        return "logs/cluster"

    @staticmethod
    def get_default_queue() -> str:
        return "premium"

    @staticmethod
    def get_default_project() -> str:
        return "acc_LOAD"

    @staticmethod
    def get_lsf_unit_for_limits() -> str:
        return "MB"

    @staticmethod
    def get_unknwn_behaviour() -> str:
        return "wait"

    @staticmethod
    def get_zombi_behaviour() -> str:
        return "ignore"

    @staticmethod
    def get_latency_wait() -> float:
        return float("10")
