#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = emergency_planner
DIR_NAME = practical
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python

SUBMISSION_NAME = SheenaLang_AntonioLoboSantos_ZacharyParent_MaríaDelCarmenRamirezTrujillo_BrunoSánchezGómez_$(PROJECT_NAME)
ZIP_NAME = $(SUBMISSION_NAME).zip

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "cache" -delete
	find . -type d -name "*.egg-info" -delete

## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 src
	isort --check --diff --profile black src
	black --check --config pyproject.toml src

## Format source code with black
.PHONY: format
format:
	black --config pyproject.toml src

.PHONY: remove-zip
remove-zip:
	rm -f ${ZIP_NAME}

.PHONY: zip
zip: remove-zip ${ZIP_NAME}

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

${ZIP_NAME}:
	cd .. && \
	mkdir -p $(SUBMISSION_NAME) && \
	cp -r $(DIR_NAME) $(SUBMISSION_NAME) && \
	zip -r $(ZIP_NAME) $(SUBMISSION_NAME) \
		-x "*/__pycache__/*" "*.pyc" "*/*.egg-info/*" "*/cache/*" \
		"*.aux" "*.log" "*.out" "*.toc" "*.bbl" "*.blg" \
		"*.fls" "*.nav" "*.snm" "*.vrb" "*.fdb_latexmk" "*.synctex.gz" \
		"*/.venv/*" "*/.git/*" "*.lock" && \
	rm -rf $(SUBMISSION_NAME) && \
	mv ${ZIP_NAME} ${DIR_NAME}/


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
