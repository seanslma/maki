# Password 

## hash password
https://snyk.io/learn/password-storage-best-practices/
- generates a random value called a "salt"
- concatenates the user's password and the salt
- hash the combined value using argon2, bcrypt, scrypt
- store the hash and the salt in database, not the original password
- the generated hash is compared to the stored hash. If they match, the entered password is correct
