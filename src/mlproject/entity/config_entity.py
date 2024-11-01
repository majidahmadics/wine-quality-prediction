from dataclasses import dataclass
from pathlib import Path

# Data Ingestion Entity, which contains the configuration for data ingestion

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

# Data Validation Entity, which contains the configuration for data validation

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict