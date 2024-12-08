

# WARNING
YOU WILL 99.99% GET BANNED FOR USING FURINALC, PROJECT MOON HAS ADDED A DETECTION FOR PRIVATE SERVER PLAYERS, IT IS RECOMMENDED THAT YOU WAIT FOR THE NEWEST VERSION OF THE ALTERNATIVE & BETTER PRIVATE SERVER [LETHE](https://lethelc.site) AS IT WILL BE ABLE TO BYPASS THE DETECTION. HOWEVER, IF YOU ARE ALREADY BANNED IN THE FIRST PLACE, OR IF YOU DON'T CARE ABOUT GETTING BANNED, ENJOY FURINALC!

-- --

# FurinaLC

**FurinaLC** is a server reimplementation for *Limbus Company*, named after the second-best girl from *Genshin Impact*. 

As stated in the license, there is no liability. This project obviously breaks Limbus Company's terms of service, so if anything happens, just remember that you have been warned.

Be sure to check out the [Frequently Asked Questions](https://github.com/LEAGUE-OF-NINE/FurinaLC/blob/main/FAQ.md).

## Getting Started

This guide is Windows-oriented. If you're using Linux, you probably already know how to set things up. (I use arch btw.)

### Requirements

~~Most important requirement: a brain.~~

- **uv (v0.4.22+)**  
  Install **uv** by running the following PowerShell command:
  ```bash
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
  Note: You might need to set up an environment variable for `uv`. By default, you can find `uv.exe` in `C:\Users\<username>\.local\bin`. If you're unsure how to do that, ask ChatGPT.

- **MongoDB (v8.0.3+)**  
  Download and install from [MongoDB's official website](https://www.mongodb.com/try/download/community-edition).

- **Git**  
  Install **Git** from [Git's official website](https://git-scm.com/downloads). This is required for cloning the repository.

- **FurinaLC.Tool.Proxy**  
  Download from [this link](https://github.com/yuvlian/FurinaLC.Tool.Proxy/releases/download/v2.0.1/FurinaLC.Tool.Proxy_win-x64.zip). Alternatively, you can use any HTTP proxy tool that allows modifying requests.

## Step-by-Step Setup

If you prefer a tutorial video, you can watch [this video](https://www.youtube.com/watch?v=gu6zE1KQyyE), made by Ishmael. It is kinda outdated, but you can simply skip the Python install step. And for the Fiddler install & setup, you should follow the Proxy guide in this README instead, as it's much easier to use.

### 1. **Setting Up MongoDB**

- **Install MongoDB**:  
  Follow the installation guide for your operating system from the [MongoDB installation page](https://www.mongodb.com/try/download/community-edition).

- **Configure MongoDB Connection**:  
  Once installed, connect to MongoDB using the following connection string:
  ```bash
  mongodb://127.0.0.1:27017
  ```

That's all for MongoDB setup!

### 2. **Setting Up FurinaLC.Tool.Proxy**

This proxy will redirect API requests to your local server. Follow these steps to configure it:

1. **Download FurinaLC.Tool.Proxy**:  
   Download it [here](https://github.com/yuvlian/FurinaLC.Tool.Proxy/releases/download/v2.0.1/FurinaLC.Tool.Proxy_win-x64.zip) and unzip it.

2. **Run FurinaLC.Tool.Proxy.exe**:  
   When prompted to install a certificate, allow it. We need it to decrypt HTTPS traffic. After this, the tool should automatically set itself as the system proxy (and revert this when you close it).

**Note:**

- If you're unable to browse the internet after using and closing this proxy, it might be due to Guardian failing to revert the proxy settings.
  
- If that happens, simply disable the proxy settings manually (Open windows search, then type "Proxy", the settings menu option should show up).

### 3. **Setting Up FurinaLC**

Now that MongoDB and FurinaLC.Tool.Proxy are configured, follow these steps to set up **FurinaLC**:

1. **Clone the Repository**:  
   Clone the repository to your machine using Git:
   ```bash
   git clone --recursive https://github.com/LEAGUE-OF-NINE/FurinaLC.git
   ```
   The `--recursive` flag is required for submodules. Be sure to sync the submodules every time the game updates if you want the latest identities and other content.

2. **Navigate to the Project Directory**:  
   ```bash
   cd FurinaLC
   ```

3. **Start the Server**:  
   Run the following command to start the server:
   ```bash
   uv run -m server
   ```

### 4. **Play the Game**

Once the server is running, you can launch **Limbus Company**. Ensure that the proxy is running and properly redirecting the API requests to your local server.
