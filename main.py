# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Chatbot Intent Engine Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Chatbot Intent Engine - Intent classification using rules and patterns
#      Skills: NLP, pattern matching
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# main MODULE
# --------------------------------------------------
"""
Main entry point for Chatbot Intent ENgine
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import sys
import logging
from pathlib import Path

from chatbot.engine.chatbot_engine import ChatbotEngine
from config.config import AppConfig


# --------------------------------------------------
# Logging Setup
# --------------------------------------------------
def setup_logging(config: AppConfig) -> None:
    """
    Configure application logging based on AppConfig
    """
    log_level = getattr(logging, config.log_level.upper(),
                        logging.INFO)
    
    handlers = [logging.StreamHandler(sys.stdout)]

    if config.log_to_file:
        log_path = Path(config.log_file_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_path))
    
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=handlers,
    )

# --------------------------------------------------
# Main Application Bootstrap
# --------------------------------------------------
def main():
    """
    Application bootstrap
    """
    try:
        # Load configuration
        config = AppConfig()

        # Setup logging
        setup_logging(config)

        logger = logging.getLogger("chatbot.main")
        logger.info("Starting Chatbot Engine")

        # Initialize chatbot engine
        chatbot = ChatbotEngine(config=config)

        print("=" * 50)
        print(f"{config.app_name} v{config.version}")
        print("Type 'exit' to quit")
        print("=" * 50)

        # REPL Loop
        while True:
            try:
                user_input = input("\nYou: ")

                if not user_input:
                    continue
                
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting chatbot. Goodbye!")
                    logger.info("Chatbot session ended by user.")
                    break

                response = chatbot.handle_message(user_input)

                print(f"Bot: {response}")
            
            except KeyboardInterrupt:
                print("\nInterrupted. Exiting...")
                logger.info("Chatbot interrupted by user (Ctrl+C).")
                break
            
            except Exception as e:
                logger.exception(
                    f"Runtime error during message handling: {e}"
                )
                print(f"Error: {e}")

        logger.info("Chatbot shutdown cleanly.")
        sys.exit(0)

    except Exception as startup_error:
        print(f"Fatal startup error: {startup_error}")
        logger.exception(
            f"Fatal startup error: {startup_error}"
        )
        sys.exit(1)


# --------------------------------------------------
# Entry point
# --------------------------------------------------
if __name__ == "__main__":
    main()
