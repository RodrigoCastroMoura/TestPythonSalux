-- Create logs table if it doesn't exist
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    level VARCHAR(10) NOT NULL CHECK (level IN ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')),
    message TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index on timestamp for better query performance
CREATE INDEX IF NOT EXISTS idx_logs_timestamp ON logs(timestamp);

-- Create index on level for filtering
CREATE INDEX IF NOT EXISTS idx_logs_level ON logs(level);
