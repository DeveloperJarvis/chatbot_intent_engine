@echo off

REM Root directory
@REM set ROOT=chatbot_intent_engine
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\chatbot"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\data"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\chatbot\engine"
call :create_folder "%ROOT%\chatbot\handlers"
call :create_folder "%ROOT%\chatbot\intents"
call :create_folder "%ROOT%\chatbot\patterns"
call :create_folder "%ROOT%\chatbot\preprocessing"
call :create_folder "%ROOT%\chatbot\rules"
call :create_folder "%ROOT%\chatbot\utils"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\chatbot\__init__.py"
call :create_py_file "%ROOT%\chatbot\engine\__init__.py"
call :create_py_file "%ROOT%\chatbot\engine\chatbot_engine.py"
call :create_py_file "%ROOT%\chatbot\engine\intent_classifier.py"
call :create_py_file "%ROOT%\chatbot\engine\intent_resolver.py"
call :create_py_file "%ROOT%\chatbot\engine\scorer.py"
call :create_py_file "%ROOT%\chatbot\handlers\__init__.py"
call :create_py_file "%ROOT%\chatbot\handlers\booking_handler.py"
call :create_py_file "%ROOT%\chatbot\handlers\fallback_handler.py"
call :create_py_file "%ROOT%\chatbot\handlers\order_handler.py"
call :create_py_file "%ROOT%\chatbot\intents\__init__.py"
call :create_py_file "%ROOT%\chatbot\intents\base_intent.py"
call :create_py_file "%ROOT%\chatbot\intents\book_flight_intent.py"
call :create_py_file "%ROOT%\chatbot\intents\cancel_order_intent.py"
call :create_py_file "%ROOT%\chatbot\intents\fallback_intent.py"
call :create_py_file "%ROOT%\chatbot\patterns\__init__.py"
call :create_py_file "%ROOT%\chatbot\patterns\keyword_matcher.py"
call :create_py_file "%ROOT%\chatbot\patterns\pattern_matcher.py"
call :create_py_file "%ROOT%\chatbot\patterns\regex_engine.py"
call :create_py_file "%ROOT%\chatbot\preprocessing\__init__.py"
call :create_py_file "%ROOT%\chatbot\preprocessing\cleaner.py"
call :create_py_file "%ROOT%\chatbot\preprocessing\entity_extractor.py"
call :create_py_file "%ROOT%\chatbot\preprocessing\normalizer.py"
call :create_py_file "%ROOT%\chatbot\preprocessing\tokenizer.py"
call :create_py_file "%ROOT%\chatbot\rules\__init__.py"
call :create_py_file "%ROOT%\chatbot\rules\mandatory_rule.py"
call :create_py_file "%ROOT%\chatbot\rules\negative_rule.py"
call :create_py_file "%ROOT%\chatbot\rules\priority_rule.py"
call :create_py_file "%ROOT%\chatbot\rules\rule_engine.py"
call :create_py_file "%ROOT%\chatbot\utils\__init__.py"
call :create_py_file "%ROOT%\chatbot\utils\contants.py"
call :create_py_file "%ROOT%\chatbot\utils\helpers.py"
call :create_py_file "%ROOT%\chatbot\utils\logger.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_intent_classifier.py"
call :create_py_file "%ROOT%\tests\test_pattern_matching.py"
call :create_py_file "%ROOT%\tests\test_preprocessing.py"
call :create_py_file "%ROOT%\tests\test_rule_engine.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\config\intents.yaml"
call :create_file "%ROOT%\config\rules.yaml"
call :create_file "%ROOT%\config\settings.yaml"

call :create_file "%ROOT%\data\sample_inputs.json"
call :create_file "%ROOT%\data\test_cases.json"

call :create_file "%ROOT%\logs\chatbot.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Chatbot Intent Engine Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Chatbot Intent Engine - Intent classification using rules and patterns
echo #      Skills: NLP, pattern matching
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b