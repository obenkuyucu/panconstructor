# panconstructor
Constructing a PAN with first 6, last 4 and few digits of MD5 hash

This is my very first python script, so any feedback is highly appreciated. I have very limited developing knowledge and experience, so most of the credit should go to my dear friend [Fatih Tuna](https://github.com/ftuna), who helps me with all of my projects.

PANConstructor constructs the PAN (Primary Account Number) with first 6, last 4 and first few digits of the MD5 value. PCI DSS (Payment Card Industry Data Security Standard) mandates that they should not exist together in the same environment (Requirement 3.4.e), and this script is to prove why, even with the first digits of the hash data.

It creates 1M possibilities of cards with the given digits, creates the MD5 hashes and compares with the given hash string. It also checks for Luhn algorithm. It is as simple as this. Again, I’m not a developer, just an information security enthusiast with some PCI DSS knowledge.

# Usage

<code>python3 panconstructor.py</code>

It will ask for first 6, last 4 digits and any strings of MD5 hash from the beginning. Output would be the constructed PAN(s) with Luhn checked.

# Credits
* [Fatih Tuna](https://github.com/ftuna)
* Virgilio Viegas
* And the “PCI DSS compliant” third party payment gateway who has all three in their environment.
