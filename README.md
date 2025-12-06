# My Tools Installer

A comprehensive and automated tool installer that simplifies the setup and configuration of essential development tools and utilities.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated Installation**: Quickly install multiple development tools with a single command
- **Cross-Platform Support**: Works seamlessly on Windows, macOS, and Linux
- **Dependency Management**: Automatically handles tool dependencies and version management
- **Verification**: Built-in verification to ensure all tools are correctly installed
- **Customizable**: Configure which tools to install based on your needs
- **Error Handling**: Robust error handling with detailed logging and troubleshooting information
- **Easy Rollback**: Simple rollback functionality to revert installations if needed
- **Regular Updates**: Keep your tools up-to-date with automated update checks

## Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+, CentOS 7+, etc.)
- **Python**: Python 3.7 or higher
- **Package Manager**: 
  - Windows: Chocolatey or Windows Package Manager (winget)
  - macOS: Homebrew
  - Linux: apt, yum, or pacman (depending on distribution)
- **Network Access**: Internet connection for downloading tools and packages
- **Disk Space**: Minimum 2GB free disk space for tool installations
- **Administrator/Sudo Access**: Required for system-level installations

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/nemaapdola-cmyk/my-tools-installer.git
cd my-tools-installer
```

### Step 2: Install Dependencies

```bash
# Windows
pip install -r requirements.txt

# macOS and Linux
pip3 install -r requirements.txt
```

### Step 3: Configure (Optional)

Edit the `config.yaml` file to customize which tools you want to install:

```yaml
tools:
  - git
  - node
  - python
  - docker
  - vscode
```

### Step 4: Run the Installer

```bash
# Windows
python installer.py

# macOS and Linux
python3 installer.py
```

## Usage

### Basic Usage

Run the installer with default configuration:

```bash
python installer.py
```

### Command-Line Options

```bash
# Display help information
python installer.py --help

# Specify a custom configuration file
python installer.py --config custom-config.yaml

# Verbose logging
python installer.py --verbose

# Verify installations without installing
python installer.py --verify-only

# Uninstall specific tools
python installer.py --uninstall git node

# Check for updates
python installer.py --check-updates
```

## Examples

### Example 1: Install Essential Development Tools

```bash
# Using default configuration
python installer.py
```

This installs the default set of tools: Git, Node.js, Python, Docker, and VS Code.

### Example 2: Custom Tool Selection

Create a custom configuration file `dev-config.yaml`:

```yaml
tools:
  - git
  - nodejs
  - npm
  - python
  - pip
  - vscode
  - postman
```

Then run:

```bash
python installer.py --config dev-config.yaml
```

### Example 3: Verify Installations

Check if all tools are properly installed without making changes:

```bash
python installer.py --verify-only
```

### Example 4: Uninstall Tools

Remove specific tools from your system:

```bash
python installer.py --uninstall docker nodejs
```

### Example 5: Verbose Output

Get detailed logging information during installation:

```bash
python installer.py --verbose
```

## Configuration

The `config.yaml` file controls which tools are installed. Each tool entry can include:

```yaml
tools:
  - name: git
    version: latest          # or specific version like "2.40.0"
    skip: false             # skip installation if true
  - name: nodejs
    version: "18.0.0"
  - name: docker
    version: latest
```

## Troubleshooting

### Issue: Permission Denied

**Solution**: Run with administrator/sudo privileges:

```bash
# Windows (Run as Administrator)
python installer.py

# Linux/macOS
sudo python3 installer.py
```

### Issue: Tool Not Found After Installation

**Solution**: Verify the installation and restart your terminal:

```bash
python installer.py --verify-only
```

Then close and reopen your terminal window to refresh environment variables.

### Issue: Network Timeout

**Solution**: Check your internet connection and try again with verbose logging:

```bash
python installer.py --verbose
```

### Issue: Conflicting Tool Versions

**Solution**: Specify compatible versions in `config.yaml` or use version management tools like nvm or pyenv.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/nemaapdola-cmyk/my-tools-installer/issues).

---

**Last Updated**: 2025-12-06
