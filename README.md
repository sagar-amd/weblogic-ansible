# WebLogic Installation and Domain Creation using Ansible

This repository provides an automated way to install Oracle WebLogic Server and create a WebLogic domain using Ansible.

## 📦 Repository Structure

- `inventory/hosts` – Defines your WebLogic target servers.
- `playbooks/install_weblogic.yml` – Playbook to install Java and WebLogic.
- `playbooks/create_domain.yml` – Playbook to create a WebLogic domain.
- `roles/java` – Installs a specific JDK.
- `roles/weblogic_install` – Installs WebLogic silently.
- `roles/domain_create` – Creates a WebLogic domain using WLST.

## 🛠️ Prerequisites

- Ansible installed on the control machine.
- SSH access to the WebLogic server.
- JDK and WebLogic JARs hosted at accessible URLs.

## 🚀 Usage

### 1. Update Inventory

Edit `inventory/hosts` with your target WebLogic server.

\`\`\`ini
[weblogic_server]
192.168.1.100 ansible_user=oracle ansible_become=true
\`\`\`

### 2. Install Java and WebLogic

\`\`\`bash
ansible-playbook -i inventory/hosts playbooks/install_weblogic.yml
\`\`\`

### 3. Create WebLogic Domain

\`\`\`bash
ansible-playbook -i inventory/hosts playbooks/create_domain.yml
\`\`\`

## 📍 Output

After successful execution, you can access the WebLogic console at:

\`\`\`
http://<hostname>:8001/console
\`\`\`

Default credentials:
- Username: weblogic
- Password: Welcome1

## 🔐 Security Note

Always change the default password and restrict console access.
