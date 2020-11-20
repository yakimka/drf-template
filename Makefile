.PHONY: all
all: help

COMMITS_COUNT := 30

.PHONY: whats-new
whats-new: ## Get info about last tag
	$(eval LAST_TAG := $(shell git describe --abbrev=0 --tags))
	$(eval PREV_TAG := $(shell git describe --abbrev=0 --tags $(LAST_TAG)^ 2>/dev/null || [ ]))
	$(eval TAGS := $(if $(PREV_TAG),$(PREV_TAG)..$(LAST_TAG),$(LAST_TAG)))
	$(eval NUMBER_OF_COMMITS := $(shell git rev-list --count --no-merges $(TAGS)))
	@echo ""
	@echo "Since the last release there have been $(NUMBER_OF_COMMITS) commit(s). \
	The descriptions for the first (at most) $(COMMITS_COUNT) of these are as follows"
	@echo ""
	@git --no-pager log $(TAGS) --pretty=format:'- %s' --no-merges | head -n $(COMMITS_COUNT)
	@echo ""

.PHONY: flake
flake: ## Run flake8
	flake8 --statistics --count .

.PHONY: test
test: ## Run tests
	  # Running tests:
		DJANGO_ENV=testing pytest
		# Check dead or dup fixtures
		DJANGO_ENV=testing pytest --dead-fixtures --dup-fixtures

.PHONY: check
check: ## Run checks
		# Run checks to be sure we follow all django's best practices:
		python manage.py check --fail-level WARNING
		# Check that all migrations worked fine:
		python manage.py makemigrations --dry-run --check
		# Checking dependencies status:
		pip check

.PHONY: lint
lint: flake ## Run all linters

.PHONY: clean
clean: clean-dist clean-pyc  ## Clean project

.PHONY: clean-dist
clean-dist:  ## Clean dist files
	rm -fr *.egg-info dist build

.PHONY: clean-pyc
clean-pyc:  ## Clean pycache files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: installdev
installdev: clean  ## Install dev
	pip install -Ue '.[dev]'

.PHONY: sdist
sdist: clean  ## Create a source distribution
	python setup.py sdist

.PHONY: generate-django-secret-key
generate-django-secret-key:  ## Generate secret key for django deployment
	@python -c 'from django.utils.crypto import get_random_string; print(get_random_string(50))'

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
