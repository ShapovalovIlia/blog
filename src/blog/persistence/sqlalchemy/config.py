from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    url: str


def load_postgres_config_from_toml(path: str) -> PostgresConfig:
    toml_as_dict = .load(path)
    postgres_section_as_dict = toml_as_dict["postgres"]
    return PostgresConfig(url=postgres_section_as_dict["url"])
