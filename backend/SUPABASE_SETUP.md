# Supabase Integration Guide

This guide will help you connect your Python backend to Supabase.

## Step 1: Create a Supabase Project

1. Go to [https://supabase.com](https://supabase.com)
2. Sign up or log in
3. Click "New Project"
4. Fill in your project details and create the project
5. Wait for the project to be provisioned (takes ~2 minutes)

## Step 2: Get Your Supabase Credentials

### Database Connection String (Required)

1. Go to your Supabase Dashboard
2. Click on **Project Settings** (gear icon in sidebar)
3. Navigate to **Database** section
4. Find **Connection String** and select **URI**
5. Copy the connection string (it looks like this):
   \`\`\`
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxxx.supabase.co:5432/postgres
   \`\`\`
6. Replace `[YOUR-PASSWORD]` with your actual database password

### API Keys (Optional - for Supabase client features)

1. In Project Settings, navigate to **API** section
2. Copy the following:
   - **Project URL** (SUPABASE_URL)
   - **anon public** key (SUPABASE_KEY)
   - **service_role** key (SUPABASE_SERVICE_KEY) - Keep this secret!

## Step 3: Configure Your Backend

1. Copy `.env.example` to `.env`:
   \`\`\`bash
   cp .env.example .env
   \`\`\`

2. Update your `.env` file with Supabase credentials:
   \`\`\`env
   # Replace with your Supabase PostgreSQL connection string
   DATABASE_URL=postgresql://postgres:your-password@db.xxxxxxxxxxxxx.supabase.co:5432/postgres
   
   # Optional: Add these for Supabase client features
   SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co
   SUPABASE_KEY=your-anon-public-key
   SUPABASE_SERVICE_KEY=your-service-role-key
   
   # Generate a secure secret key
   SECRET_KEY=your-secret-key-here
   \`\`\`

## Step 4: Create Database Tables

Run the Python backend to automatically create all tables:

\`\`\`bash
python main.py
\`\`\`

The SQLAlchemy models will automatically create the necessary tables in your Supabase PostgreSQL database.

## Step 5: (Optional) Set Up Row Level Security (RLS)

For production, you should enable RLS on your tables:

1. Go to Supabase Dashboard > **Table Editor**
2. For each table (users, tallies), click the table name
3. Click **RLS** tab and enable Row Level Security
4. Add policies based on your security requirements

Example policy for tallies table:
\`\`\`sql
-- Allow authenticated users to read tallies
CREATE POLICY "Users can view tallies"
ON tallies FOR SELECT
TO authenticated
USING (true);

-- Allow coordinators and admins to insert tallies
CREATE POLICY "Coordinators can insert tallies"
ON tallies FOR INSERT
TO authenticated
WITH CHECK (
  EXISTS (
    SELECT 1 FROM users
    WHERE users.id = auth.uid()
    AND users.role IN ('admin', 'coordinator')
  )
);
\`\`\`

## What You Get with Supabase

- **PostgreSQL Database**: Production-ready, scalable database
- **Auto-generated REST API**: Access your data via REST (optional)
- **Realtime Subscriptions**: Get live updates when data changes
- **Authentication**: Built-in auth system (can integrate with your JWT)
- **Storage**: File storage for images, documents, etc.
- **Row Level Security**: Database-level security policies

## Using Supabase Client Features

The backend includes `supabase_client.py` for accessing Supabase-specific features:

\`\`\`python
from supabase_client import get_supabase_client

# Example: Upload a file to Supabase Storage
supabase = get_supabase_client()
supabase.storage.from_('avatars').upload('user1.png', file_data)

# Example: Subscribe to realtime changes
supabase.table('tallies').on('INSERT', handle_new_tally).subscribe()
\`\`\`

## Troubleshooting

**Connection Error**: Make sure your IP is allowed in Supabase. By default, Supabase allows all IPs, but check Project Settings > Database > Connection Pooling.

**Authentication Issues**: If using Supabase Auth, make sure your JWT secret matches between your backend and Supabase.

**Table Not Found**: Run `python main.py` to create tables automatically via SQLAlchemy.
