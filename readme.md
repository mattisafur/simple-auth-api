# Simple Authenticated REST-ful API

## Overview

This API lets users store information as a string through a simple RESTful interface. Users are managed by the api.  
The program uses a postgresql database to store user authentication information and user data.

## Environment Variables

- `DATABASE_HOST` database host address
- `DATABASE_POST` port database is accessible on
- `DATABASE_USERNAME` username for accessing the database with
- `DATABASE_PASSWORD` password of database access user
- `DATABASE_NAME` name of the database on the server

## Database Schema

### users

| Column          | Type  | Constraints           |
| --------------- | ----- | --------------------- |
| `username`      | CITEX | Primary Key, Not null |
| `email`         | CITEX | Unique, Not null      |
| `password_hash` | BYTEA | Not null              |

### tokens

| Column       | Type        | Constraints                             |
| ------------ | ----------- | --------------------------------------- |
| `token`      | VARCHAR     | Primary Key                             |
| `username`   | CITEX       | Foreign Key, Not null                   |
| `created_at` | TIMESTAMPTZ | Not null, automatically set by database |
| `expires_at` | TIMESTAMPTZ | Not null, automatically set by database |

### user_data

| Column       | Type    | Constraints              |
| ------------ | ------- | ------------------------ |
| `username` ` | CITEX   | Primary Key, Foreign Key |
| `data`       | VARCHAR | Not null                 |
