{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "snap-analog Log Analysis Output",
  "type": "object",

  "properties": {
    "summary": {
      "type": "object",
      "properties": {
        "total_lines": { "type": "integer", "minimum": 0 },
        "total_requests": { "type": "integer", "minimum": 0 },
        "memory_mode": { "type": "string" },
        "file": { "type": "string" },
        "processing_time": { "type": "number", "minimum": 0 }
      },
      "required": ["total_lines", "total_requests", "memory_mode", "file"]
    },

    "health_metrics": {
      "type": "object",
      "properties": {
        "success_rate_2xx_3xx": { "type": "string", "pattern": "^[0-9.]+%$" },
        "client_error_rate_4xx": { "type": "string", "pattern": "^[0-9.]+%$" },
        "server_error_rate_5xx": { "type": "string", "pattern": "^[0-9.]+%$" },

        "status_groups": {
          "type": "object",
          "additionalProperties": { "type": "integer", "minimum": 0 }
        }
      },
      "required": [
        "success_rate_2xx_3xx",
        "client_error_rate_4xx",
        "server_error_rate_5xx",
        "status_groups"
      ]
    },

    "traffic_analysis": {
      "type": "object",
      "properties": {
        "top_ips": {
          "type": "array",
          "items": {
            "type": "array",
            "items": [
              { "type": "string" },
              { "type": "integer", "minimum": 0 }
            ],
            "minItems": 2,
            "maxItems": 2
          }
        },

        "top_urls": {
          "type": "array",
          "items": {
            "type": "array",
            "items": [
              { "type": "string" },
              { "type": "integer", "minimum": 0 }
            ],
            "minItems": 2,
            "maxItems": 2
          }
        },

        "top_minutes": {
          "type": "array",
          "items": {
            "type": "array",
            "items": [
              { "type": "string" },
              { "type": "integer", "minimum": 0 }
            ],
            "minItems": 2,
            "maxItems": 2
          }
        },

        "methods": {
          "type": "object",
          "additionalProperties": { "type": "integer", "minimum": 0 }
        }
      },
      "required": ["top_ips", "top_urls", "methods"]
    },

    "memory_optimization": {
      "type": "object",
      "properties": {
        "tracker_stats": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "properties": {
              "unique_items": { "type": "integer", "minimum": 0 },
              "mode": { "type": "string" }
            },
            "required": ["unique_items"]
          }
        }
      },
      "required": ["tracker_stats"]
    },

    "invalid_lines": {
      "type": "integer",
      "minimum": 0
    },

    "elapsed_time": {
      "type": "number",
      "minimum": 0
    }
  },

  "required": [
    "summary",
    "health_metrics",
    "traffic_analysis",
    "memory_optimization",
    "elapsed_time"
  ]
}

