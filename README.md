# Simple Automatic WhatsApp Responder with Twilio (Docker)

## Overview

This project is a straightforward, automated responder designed to notify customers that we have moved to a new phone number via WhatsApp messages. It utilizes Twilio's API to listen for incoming WhatsApp messages and automatically responds with a predefined message indicating the new contact number. This solution is containerized using Docker, ensuring easy deployment and scalability.

## Features

- **Automatic Response**: Automatically replies to incoming WhatsApp messages.
- **Twilio Integration**: Leverages Twilio's powerful API for WhatsApp communication.
- **Dockerized Application**: Containerized for easy setup and scalability.
- **Customizable Message**: Easily change the auto-response message to fit your needs.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- Docker and Docker Compose installed on your machine.
- A Twilio account with WhatsApp messaging capabilities set up.
- Your Twilio Account SID and Auth Token.

### Installation

**Clone the Repository**

   Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

### Environment Setup

Before running the application, create a `.env` file in the project root directory with the necessary environment variables:

```plaintext
ACCOUNT_SID=your_account_sid_here
AUTH_TOKEN=your_auth_token_here
```

### Running the Application

To build the Docker image and start the container in detached mode (running in the background), execute the following command from the root directory of the project:
   ```bash
   docker-compose up --build -d
   ```