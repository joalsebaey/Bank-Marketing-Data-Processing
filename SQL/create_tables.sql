- Create database schema for bank marketing data

-- Client table
CREATE TABLE IF NOT EXISTS client (
    client_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    job VARCHAR(50),
    marital VARCHAR(20),
    education VARCHAR(30),
    credit_default BOOLEAN,
    mortgage BOOLEAN
);

-- Campaign table
CREATE TABLE IF NOT EXISTS campaign (
    client_id INTEGER PRIMARY KEY,
    number_contacts INTEGER,
    contact_duration INTEGER,
    previous_campaign_contacts INTEGER,
    previous_outcome BOOLEAN,
    campaign_outcome BOOLEAN,
    last_contact_date DATE,
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

-- Economics table
CREATE TABLE IF NOT EXISTS economics (
    client_id INTEGER PRIMARY KEY,
    cons_price_idx FLOAT,
    euribor_three_months FLOAT,
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_client_credit_default ON client(credit_default);
CREATE INDEX IF NOT EXISTS idx_client_mortgage ON client(mortgage);
CREATE INDEX IF NOT EXISTS idx_campaign_outcome ON campaign(campaign_outcome);
CREATE INDEX IF NOT EXISTS idx_campaign_date ON campaign(last_contact_date);

-- Sample queries for data validation
-- COMMENT OUT in production environment

-- SELECT COUNT(*) FROM client;
-- SELECT COUNT(*) FROM campaign;
-- SELECT COUNT(*) FROM economics;

-- SELECT * FROM client LIMIT 5;
-- SELECT * FROM campaign LIMIT 5;
-- SELECT * FROM economics LIMIT 5;
