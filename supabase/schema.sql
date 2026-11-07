-- Vailongara Kalari website: enquiry form table.
-- Run once in Supabase: SQL Editor -> New query -> paste -> Run.

create table if not exists public.enquiries (
  id          bigint generated always as identity primary key,
  created_at  timestamptz not null default now(),
  name        text not null check (char_length(name) between 1 and 120),
  phone       text not null check (char_length(phone) between 5 and 30),
  topic       text check (char_length(topic) <= 60),
  message     text not null check (char_length(message) between 1 and 2000),
  status      text not null default 'NEW'      -- office can set: NEW / CONTACTED / CLOSED
);

alter table public.enquiries enable row level security;

-- The public website (anon key) may only ADD enquiries. It can never read, change or delete them.
drop policy if exists "website can insert enquiries" on public.enquiries;
create policy "website can insert enquiries"
  on public.enquiries for insert
  to anon
  with check (status = 'NEW');

-- Office staff read enquiries in the Supabase dashboard (Table Editor), which bypasses these rules.
