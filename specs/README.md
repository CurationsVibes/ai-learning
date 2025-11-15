# OpenAPI Specifications

This directory contains OpenAPI specifications for the project's APIs. These specifications follow the Docs-as-Code workflow, where API documentation is version-controlled alongside the code.

## Directory Structure

```
specs/
├── README.md           # This file
└── example-api.yaml    # Example OpenAPI specification (replace with your own)
```

## Adding Your OpenAPI Specifications

1. Create your OpenAPI specification file (`.yaml`, `.yml`, or `.json` format)
2. Place it in this `specs/` directory
3. Commit and push your changes
4. The automated workflow will validate your specification

## OpenAPI Specification Guidelines

- Use OpenAPI 3.0.0 or later
- Include comprehensive descriptions for all endpoints
- Define reusable components in the `components` section
- Add examples for request/response bodies
- Tag endpoints for better organization
- Document all required and optional parameters

## File Naming Conventions

- Use lowercase with hyphens: `my-api.yaml`
- Be descriptive: `payment-service-api.yaml` instead of `api.yaml`
- Include version if maintaining multiple versions: `my-api-v1.yaml`, `my-api-v2.yaml`

## Validation

All OpenAPI specifications are automatically validated when:
- Changes are pushed to the `main` branch
- Pull requests are created or updated

The workflow uses `@apidevtools/swagger-cli` to validate specifications against the OpenAPI standard.

## Optional: SDK Generation with Stainless

If you want to generate SDKs from your OpenAPI specifications:

1. Set up a [Stainless](https://stainless.com/) account
2. Configure the Stainless project settings
3. Uncomment the `upload-to-stainless` job in `.github/workflows/openapi-spec-workflow.yml`
4. Add your Stainless project name and configure authentication (OIDC or API key)

See the [Stainless documentation](https://www.stainless.com/docs/guides/automate-updates) for more details.

## Resources

- [OpenAPI Specification](https://spec.openapis.org/oas/v3.0.0)
- [OpenAPI Examples](https://github.com/OAI/OpenAPI-Specification/tree/main/examples)
- [Swagger Editor](https://editor.swagger.io/) - Online OpenAPI editor
- [Stoplight Studio](https://stoplight.io/studio) - Visual OpenAPI editor
