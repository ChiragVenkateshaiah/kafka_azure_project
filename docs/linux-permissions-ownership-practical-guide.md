# Linux File Permissions & Ownership - Practical Guide

This document explains **how Linux file permissions, ownership, and groups work in practice**, with a focus on **real-world engineering use cases** such as Kafka, Python applications, and server administration.

It is written as a **learning + reference guide** and can be reused across projects.

---

## 1. Why permissions Matter (Engineering Context)

On Linux servers:

* Applications **do not run as root**
* Services (Kafka, Spark, Airflow, etc.) run under **dedicated users**
* Multiple engineers may manage the same directories

Incorrect permissions cause:

* `Permission denied` errors
* Services failing at startup
* Forced use of `sudo` (bad practice)

Correct permissions enable:

* Secure access
* Clean automation
* Production-grade setups

---

## 2. Linux Permission Model (Core Concepts)

Every file/directory has:

* **Owner (user)**
* **Groups**
* **Others**

Permission are represented as:

```
drwxrwx---
```
| Position | Meaning            |
| -------- | ------------------ |
| d        | directory          |
| rwx      | owner permissions  |
| rwx      | group permissions  |
| ---      | others permissions |

---

## 3. Permission Types Explained

### Read (`r`)

* File: view contents
* Directory: list files

### Write (`w`)

* File: modify contents
* Directory: create/delete files

### Execute (`x`)

* File: run as program
* Directory: **enter/traverse directory**

> **Important**: To create a file in a directory, you need **write + execute** on that directory

---

## 4. Ownership Commands

### Check ownership and permissions

```bash
ls -ld /path/to/dir
```

### Change owner and group

```bash
sudo chown user:group /path/to/dir
```

### Change ownership recursively

```bash
sudo chown -R user:group /path/to/dir
```

## 5. chmod - Changing Permissions

### Numeric permission mapping

| Number | Permission |
| ------ | ---------- |
| 7      | rwx        |
| 6      | rw-        |
| 5      | r-x        |
| 4      | r--        |

Example:

```bash
chmod 770 /opt/python_pro
```

Meaning:

* Owner -> rwx
* Group -> rwx
* Others -> no access

---

## 6. Groups - The Correct Way to Share Access

### Why groups are important

* Avoid changing ownership repeatedly
* Avoid using `sudo` for normal work
* Enable collaboration

### Add user to group

```bash
sudo usermod -aG kafka ubuntu
```

> **Log out and log back in after this.**

Verify:

```bash
groups
```

---

## 7. Recommended Permission Patterns (Best Practices)

### Shared service directories (Kafka, Python apps)

```bash
Owner: kafka
Group: kafka
Permissions: 770
```

Command:
```bash
sudo chown -R kafka:kafka /opt/python_pro
sudo chmod 770 /opt/python_pro
```

This allows:

* Kafka service to read/write
* Admin users (in kafka group) to manage files
* No access for others

---

## 8. Common Permission Problems & Fixes

### Problem: Permission denied on file upload (WinSCP)

**Cause**: Directory owned by root or another user

**Fix**:

* Add user to group
* Grant group write permission

---

### Problem: `touch` fails even after group add

**Cause**: Directory permission is `750`

**Fix**:
```bash
chmod 770 directory_name
```

----

### Problem: Access blocked despite correct permissions

**Cause**: Parent directories missing execute (`x`) permission

**Debug command**:
```bash
namei -l /path/to/dir
```

---

## 9. What NOT to Do (Anti-Patterns)

* `chmod 777` (security risk)
* Running services as `root`
* Using `sudo` inside applications
* Changing ownership repeatedly instead of using groups

---

## 10. Standard Kafka Permissions:

Kafka directories should be:
```bash
/opt/kafka      -> kafka:kafka 755
/var/lib/kafka  -> kafka:kafka 770
/var/log/kafka  -> kafka:kafka 770
```

Kafka runs as:
```bash
User=kafka
Group=kafka
```

## 11. My Debug Checklist
```bash
whoami
groups
ls -ld /target/dir
namei -l /target/dir
```

If all look correct, permissions will work.

---

## 12. Key Takeways for me

* Ownership controls **who** owns files
* Permissions control **what** actions are allowed
* Groups enable **clean multi-user access**
* `770` is the most common production-safe directory permission

---

## 13. Summary Rule (Golden Rule)
> **If multiple trusted users or services need write access -> use groups + 770**

## 14. To check whether the user & group already present
```bash
id kafka
```
if not present:
```bash
id: 'kafka': no such user
```
## 15. Check if a group exists
```bash
getent group kafka
```
