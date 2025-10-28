-- Database schema for Nashville Public Safety project
CREATE TABLE IF NOT EXISTS calls (
    call_id BIGINT PRIMARY KEY,
    call_datetime TIMESTAMP NOT NULL,
    call_type TEXT,
    zip TEXT
);

CREATE TABLE IF NOT EXISTS incidents (
    incident_id BIGINT PRIMARY KEY,
    call_id BIGINT,
    confirmed_type TEXT,
    occurred_at TIMESTAMP,
    zip TEXT
);
