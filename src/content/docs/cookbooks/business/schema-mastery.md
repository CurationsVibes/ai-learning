---
title: 🗺️ Schema.org Mastery
---

**Your machine-readable DNA - make AI systems understand you perfectly**

---

## What Is Schema.org?

**Schema.org is a vocabulary for structured data on the web.**

Translation: It's how you tell machines (search engines, AI agents, crawlers) EXACTLY what your content means.

**Without Schema:**
```html
<p>Basecamp costs $299</p>
```

Machine reads: "Some text about numbers"

**With Schema:**
```json
{
  "@type": "SoftwareApplication",
  "offers": {
    "@type": "Offer",
    "price": "299",
    "priceCurrency": "USD"
  }
}
```

Machine reads: "This is software. It costs $299 USD."

**The difference:** Ambiguous text vs. structured, queryable data.

---

## Why Schema Matters for AI

**AI systems need structure:**

**Without Schema, AI must:**
- Parse unstructured HTML
- Guess at meaning
- Infer relationships
- Hope for accuracy

**With Schema, AI can:**
- Read structured data directly
- Understand precisely
- Extract facts confidently
- Cite accurately

**Result:** Schemaed content is **10-100x more likely** to be understood and cited by AI.

---

## The Three Implementation Methods

### 1. JSON-LD (Recommended)
**JavaScript Object Notation for Linked Data**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Basecamp"
}
</script>
```

**Pros:**
- ✅ Clean, separate from HTML
- ✅ Easy to generate programmatically
- ✅ Doesn't affect page rendering
- ✅ Recommended by Google
- ✅ Best for AI parsing

**Cons:**
- ❌ Requires JavaScript support (minimal concern)

**Use this 95% of the time.**

### 2. Microdata
**Inline HTML attributes**

```html
<div itemscope itemtype="https://schema.org/Organization">
  <span itemprop="name">Basecamp</span>
</div>
```

**Pros:**
- ✅ Tightly coupled to visible content
- ✅ No duplication

**Cons:**
- ❌ Clutters HTML
- ❌ Harder to maintain
- ❌ Less flexible

**Use when:** You need HTML validation or can't use JSON-LD.

### 3. RDFa
**Resource Description Framework in Attributes**

```html
<div vocab="https://schema.org/" typeof="Organization">
  <span property="name">Basecamp</span>
</div>
```

**Pros:**
- ✅ W3C standard
- ✅ Powerful for complex data

**Cons:**
- ❌ More complex
- ❌ Less common
- ❌ Overkill for most use cases

**Use when:** You have complex linked data requirements (rare).

---

## Core Schema Types for Business

### 1. Organization

**Use for:** Company homepage, about page

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Basecamp",
  "url": "https://basecamp.com",
  "logo": "https://basecamp.com/logo.png",
  "description": "Project management software for remote teams",
  "foundingDate": "2004",
  "founder": [
    {
      "@type": "Person",
      "name": "Jason Fried"
    },
    {
      "@type": "Person",
      "name": "David Heinemeier Hansson"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Chicago",
    "addressRegion": "IL",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-312-123-4567",
    "contactType": "customer support",
    "email": "support@basecamp.com"
  },
  "sameAs": [
    "https://twitter.com/basecamp",
    "https://linkedin.com/company/basecamp"
  ]
}
```

**What AI learns:**
- Company name and URL
- What they do
- When founded, by whom
- Where located
- How to contact
- Social presence

### 2. SoftwareApplication

**Use for:** Product pages for software

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Basecamp",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, iOS, Android",
  "offers": {
    "@type": "Offer",
    "price": "299",
    "priceCurrency": "USD",
    "priceValidUntil": "2025-12-31",
    "availability": "https://schema.org/InStock",
    "url": "https://basecamp.com/pricing"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "12453",
    "bestRating": "5",
    "worstRating": "1"
  },
  "screenshot": "https://basecamp.com/screenshot.png",
  "featureList": [
    "Unlimited projects",
    "Unlimited users",
    "Message boards",
    "To-do lists",
    "File storage"
  ],
  "author": {
    "@type": "Organization",
    "name": "37signals"
  }
}
```

**What AI learns:**
- It's business software
- Platforms supported
- Exact pricing
- User ratings
- Key features
- Who makes it

### 3. Article / BlogPosting

**Use for:** Blog posts, articles, guides

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The State of Remote Work in 2025",
  "description": "Analysis of remote work trends based on survey of 10,000 workers",
  "image": "https://example.com/article-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Sarah Chen",
    "jobTitle": "Remote Work Researcher",
    "url": "https://example.com/authors/sarah-chen"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Basecamp",
    "logo": {
      "@type": "ImageObject",
      "url": "https://basecamp.com/logo.png"
    }
  },
  "datePublished": "2025-01-15",
  "dateModified": "2025-03-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://basecamp.com/blog/remote-work-2025"
  }
}
```

**What AI learns:**
- Article title
- Author credentials
- Publishing date
- Last update
- Publisher
- Article URL

### 4. Product (Physical goods)

**Use for:** E-commerce product pages

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Wireless Bluetooth Headphones",
  "image": [
    "https://example.com/headphones-1.jpg",
    "https://example.com/headphones-2.jpg"
  ],
  "description": "Premium wireless headphones with active noise cancellation",
  "brand": {
    "@type": "Brand",
    "name": "AudioTech"
  },
  "offers": {
    "@type": "Offer",
    "price": "299.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "AudioTech Store"
    },
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingDestination": {
        "@type": "DefinedRegion",
        "addressCountry": "US"
      },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "businessDays": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
          ]
        },
        "cutoffTime": "17:00:00",
        "handlingTime": {
          "@type": "QuantitativeValue",
          "minValue": 0,
          "maxValue": 1,
          "unitCode": "DAY"
        },
        "transitTime": {
          "@type": "QuantitativeValue",
          "minValue": 2,
          "maxValue": 5,
          "unitCode": "DAY"
        }
      }
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.7",
    "reviewCount": "892"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "John Doe"
      },
      "reviewBody": "Amazing sound quality and comfortable for long use."
    }
  ]
}
```

### 5. FAQPage

**Use for:** FAQ pages

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does Basecamp cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Basecamp costs $299/month for unlimited users and unlimited projects. No per-user fees."
      }
    },
    {
      "@type": "Question",
      "name": "Can I try Basecamp for free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, we offer a 30-day free trial. No credit card required to start."
      }
    },
    {
      "@type": "Question",
      "name": "What's included in the price?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Everything is included: unlimited projects, unlimited users, 500GB storage, priority support, and all features."
      }
    }
  ]
}
```

**Why this is powerful for AI:**
- AI can extract Q&A pairs directly
- Perfect for voice assistants
- Easy to cite in responses

---

## Implementation by Page Type

### Homepage Implementation

**Goal:** Tell AI who you are, what you do, where you are

```html
<!DOCTYPE html>
<html>
<head>
  <title>Basecamp - Project Management for Remote Teams</title>

  <!-- JSON-LD for Organization -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Basecamp",
    "alternateName": "37signals Basecamp",
    "url": "https://basecamp.com",
    "logo": "https://basecamp.com/assets/logo.png",
    "description": "Project management and team communication software for remote teams",
    "foundingDate": "2004",
    "founders": [
      {
        "@type": "Person",
        "name": "Jason Fried",
        "jobTitle": "Co-Founder & CEO"
      },
      {
        "@type": "Person",
        "name": "David Heinemeier Hansson",
        "jobTitle": "Co-Founder & CTO"
      }
    ],
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "30 North LaSalle Street",
      "addressLocality": "Chicago",
      "addressRegion": "IL",
      "postalCode": "60602",
      "addressCountry": "US"
    },
    "contactPoint": [
      {
        "@type": "ContactPoint",
        "telephone": "+1-312-555-1212",
        "contactType": "customer support",
        "email": "support@basecamp.com",
        "availableLanguage": ["English"]
      }
    ],
    "sameAs": [
      "https://twitter.com/basecamp",
      "https://www.facebook.com/basecamp",
      "https://www.linkedin.com/company/basecamp",
      "https://www.youtube.com/basecamp"
    ]
  }
  </script>

  <!-- JSON-LD for Product (if homepage features product) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Basecamp",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web, iOS, Android, macOS, Windows",
    "offers": {
      "@type": "Offer",
      "price": "299",
      "priceCurrency": "USD",
      "priceValidUntil": "2025-12-31"
    }
  }
  </script>
</head>
<body>
  <!-- Your homepage content -->
</body>
</html>
```

### Product Page Implementation

```html
<!DOCTYPE html>
<html>
<head>
  <title>Basecamp Pricing - $299/month unlimited</title>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Basecamp",
    "description": "All-in-one project management and team communication tool",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web, iOS, Android, macOS, Windows",
    "offers": {
      "@type": "Offer",
      "price": "299",
      "priceCurrency": "USD",
      "priceValidUntil": "2025-12-31",
      "availability": "https://schema.org/InStock",
      "url": "https://basecamp.com/pricing",
      "eligibleRegion": {
        "@type": "Place",
        "name": "Worldwide"
      }
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.5",
      "reviewCount": "12453",
      "bestRating": "5",
      "worstRating": "1"
    },
    "screenshot": [
      "https://basecamp.com/screenshots/dashboard.png",
      "https://basecamp.com/screenshots/todo.png"
    ],
    "featureList": [
      "Message Boards",
      "To-do Lists",
      "Schedules",
      "Docs & Files",
      "Real-time Chat",
      "Automatic Check-ins",
      "Card Table",
      "Email Forwarding"
    ],
    "author": {
      "@type": "Organization",
      "name": "37signals"
    }
  }
  </script>
</head>
<body>
  <!-- Product page content -->
</body>
</html>
```

### Blog Post Implementation

```html
<!DOCTYPE html>
<html>
<head>
  <title>The State of Remote Work in 2025</title>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "The State of Remote Work in 2025",
    "alternativeHeadline": "Remote Work Trends and Statistics for 2025",
    "description": "Comprehensive analysis of remote work trends based on survey of 10,000 workers across 20 industries",
    "image": "https://basecamp.com/blog/images/remote-work-2025.jpg",
    "author": {
      "@type": "Person",
      "name": "Sarah Chen",
      "jobTitle": "Remote Work Researcher",
      "url": "https://basecamp.com/authors/sarah-chen",
      "sameAs": [
        "https://twitter.com/sarahchen",
        "https://linkedin.com/in/sarahchen"
      ]
    },
    "publisher": {
      "@type": "Organization",
      "name": "Basecamp",
      "logo": {
        "@type": "ImageObject",
        "url": "https://basecamp.com/logo.png",
        "width": 600,
        "height": 60
      }
    },
    "datePublished": "2025-01-15T08:00:00+00:00",
    "dateModified": "2025-03-01T10:30:00+00:00",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://basecamp.com/blog/remote-work-2025"
    },
    "wordCount": 2500,
    "keywords": ["remote work", "distributed teams", "work from home", "2025 trends"],
    "articleSection": "Research",
    "inLanguage": "en-US"
  }
  </script>
</head>
<body>
  <article>
    <h1>The State of Remote Work in 2025</h1>
    <p>By Sarah Chen | Published Jan 15, 2025 | Updated Mar 1, 2025</p>
    <!-- Article content -->
  </article>
</body>
</html>
```

---

## Advanced Patterns

### 1. Multiple Types (Combined Schema)

**Use when:** A page represents multiple things

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "name": "Basecamp",
      "@id": "https://basecamp.com/#organization"
    },
    {
      "@type": "WebSite",
      "name": "Basecamp",
      "url": "https://basecamp.com",
      "publisher": {
        "@id": "https://basecamp.com/#organization"
      },
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://basecamp.com/search?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "SoftwareApplication",
      "name": "Basecamp",
      "publisher": {
        "@id": "https://basecamp.com/#organization"
      }
    }
  ]
}
```

**Why:** Establishes relationships between entities

### 2. Nested Entities

**Product with Reviews:**

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Basecamp",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "12453"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      },
      "author": {
        "@type": "Person",
        "name": "Jane Doe"
      },
      "datePublished": "2025-02-15",
      "reviewBody": "Best project management tool we've ever used. Simple and effective."
    },
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "4",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "John Smith"
      },
      "datePublished": "2025-02-10",
      "reviewBody": "Great for remote teams. A few features we'd like to see added."
    }
  ]
}
```

### 3. BreadcrumbList

**For site navigation:**

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://basecamp.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Features",
      "item": "https://basecamp.com/features"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Message Boards",
      "item": "https://basecamp.com/features/message-boards"
    }
  ]
}
```

### 4. VideoObject

**For video content:**

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to Set Up Your First Basecamp Project",
  "description": "A step-by-step tutorial on setting up your first project in Basecamp",
  "thumbnailUrl": "https://basecamp.com/videos/setup-thumb.jpg",
  "uploadDate": "2025-01-20T08:00:00+00:00",
  "duration": "PT5M30S",
  "contentUrl": "https://basecamp.com/videos/setup-project.mp4",
  "embedUrl": "https://basecamp.com/videos/embed/setup-project",
  "publisher": {
    "@type": "Organization",
    "name": "Basecamp",
    "logo": {
      "@type": "ImageObject",
      "url": "https://basecamp.com/logo.png"
    }
  }
}
```

### 5. HowTo

**For tutorials and guides:**

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Create a Project in Basecamp",
  "description": "Step-by-step guide to creating your first project",
  "image": "https://basecamp.com/guides/create-project.jpg",
  "totalTime": "PT5M",
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Basecamp account"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Sign in to Basecamp",
      "text": "Navigate to basecamp.com and sign in with your credentials",
      "image": "https://basecamp.com/guides/step1.jpg"
    },
    {
      "@type": "HowToStep",
      "name": "Click 'New Project'",
      "text": "Click the 'New Project' button in the top right corner",
      "image": "https://basecamp.com/guides/step2.jpg"
    },
    {
      "@type": "HowToStep",
      "name": "Enter project details",
      "text": "Enter a project name and description, then click 'Create Project'",
      "image": "https://basecamp.com/guides/step3.jpg"
    }
  ]
}
```

---

## Testing and Validation

### Tools

1. **Google Rich Results Test**
   - URL: https://search.google.com/test/rich-results
   - Tests: Google's understanding of your schema
   - Shows: How it will appear in search

2. **Schema.org Validator**
   - URL: https://validator.schema.org
   - Tests: Schema syntax validity
   - Shows: Warnings and errors

3. **JSON-LD Playground**
   - URL: https://json-ld.org/playground
   - Tests: JSON-LD structure
   - Shows: Expanded form

### Validation Checklist

```
✅ Valid JSON syntax (no trailing commas, proper quotes)
✅ Correct @context (https://schema.org)
✅ Appropriate @type for content
✅ Required properties present
✅ URLs are absolute (not relative)
✅ Dates in ISO 8601 format (YYYY-MM-DD)
✅ Prices as strings (not numbers)
✅ Images include full URLs
✅ No broken references
```

---

## Common Mistakes

### ❌ Mistake 1: Missing @context

**Wrong:**
```json
{
  "@type": "Organization",
  "name": "Basecamp"
}
```

**Right:**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Basecamp"
}
```

### ❌ Mistake 2: Relative URLs

**Wrong:**
```json
{
  "url": "/products/basecamp"
}
```

**Right:**
```json
{
  "url": "https://basecamp.com/products/basecamp"
}
```

### ❌ Mistake 3: Wrong Data Types

**Wrong:**
```json
{
  "price": 299,
  "priceCurrency": "$"
}
```

**Right:**
```json
{
  "price": "299",
  "priceCurrency": "USD"
}
```

### ❌ Mistake 4: Invalid Dates

**Wrong:**
```json
{
  "datePublished": "01/15/2025"
}
```

**Right:**
```json
{
  "datePublished": "2025-01-15"
}
```

### ❌ Mistake 5: Missing Required Properties

**Wrong (missing offers for Product):**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Basecamp"
}
```

**Right:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Basecamp",
  "offers": {
    "@type": "Offer",
    "price": "299",
    "priceCurrency": "USD"
  }
}
```

---

## Dynamic Schema (For Developers)

### Server-Side Generation (Node.js/Express)

```javascript
app.get('/product/:id', async (req, res) => {
  const product = await getProduct(req.params.id);

  const schema = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": product.name,
    "description": product.description,
    "offers": {
      "@type": "Offer",
      "price": product.price.toString(),
      "priceCurrency": "USD"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": product.avgRating.toString(),
      "reviewCount": product.reviewCount.toString()
    }
  };

  res.render('product', {
    product,
    schema: JSON.stringify(schema)
  });
});
```

**Template (EJS/Handlebars):**
```html
<script type="application/ld+json">
  {{{schema}}}
</script>
```

### React/Next.js

```jsx
import Head from 'next/head';

function ProductPage({ product }) {
  const schema = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": product.name,
    "offers": {
      "@type": "Offer",
      "price": product.price.toString(),
      "priceCurrency": "USD"
    }
  };

  return (
    <>
      <Head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
        />
      </Head>
      <div>
        {/* Product content */}
      </div>
    </>
  );
}
```

---

## Schema Priority by Page Type

### Must-Have Schema

**Every site needs:**

1. **Homepage:**
   - Organization schema
   - WebSite schema (with SearchAction if you have search)

2. **Product/Service pages:**
   - SoftwareApplication or Product schema
   - Offers with pricing
   - AggregateRating if you have reviews

3. **Blog posts:**
   - Article/BlogPosting schema
   - Author (Person schema)
   - Publisher (Organization schema)
   - datePublished and dateModified

4. **About page:**
   - Organization schema with full details
   - Founders (Person schema)
   - Contact information

### Nice-to-Have Schema

**Add if applicable:**

- FAQPage for FAQ sections
- HowTo for tutorials
- VideoObject for video content
- BreadcrumbList for navigation
- Review schema for testimonials
- Event schema for webinars/conferences
- JobPosting for careers page

---

## Best Practices

### ✅ DO:
- Use JSON-LD (easiest to maintain)
- Include all recommended properties
- Keep schema updated with content
- Use absolute URLs
- Validate before deploying
- Add schema to ALL key pages
- Use specific types (not generic "Thing")
- Include images with full URLs
- Add dates (published, modified)
- Include author info

### ❌ DON'T:
- Add schema for content not on page
- Use schema to manipulate rankings
- Include spam or irrelevant data
- Use outdated schema types
- Forget to update prices/dates
- Mix multiple schema methods
- Use relative URLs
- Forget @context
- Leave out required properties
- Add schema without validation

---

## Measuring Impact

**Track:**

1. **Google Search Console**
   - Rich results report
   - Enhancement reports
   - Coverage issues

2. **AI Citation Rate**
   - Ask ChatGPT about your content
   - Check Perplexity citations
   - Monitor if AI understands correctly

3. **CTR Improvements**
   - Rich snippets often improve CTR
   - Monitor before/after schema implementation

4. **Validation Clean-Ups**
   - Regular validation checks
   - Fix warnings and errors
   - Keep schema current

---

## Quick Implementation Guide

**15-Minute Schema Setup:**

1. **Homepage (5 min):**
   - Add Organization schema
   - Include contact info
   - Add social links

2. **Product/Service Pages (5 min):**
   - Add SoftwareApplication or Product schema
   - Include pricing
   - Add key features

3. **Blog (5 min):**
   - Create Article schema template
   - Add author information
   - Include publish dates

4. **Validate:**
   - Run through Google Rich Results Test
   - Fix any errors
   - Deploy

**You now have basic machine-readable structure.**

---

## The Future of Schema

**2025:** Schema becomes expected for AAO

**2026:** AI agents rely heavily on schema for citations

**2027:** Voice assistants pull directly from schema

**2028:** Schema.org expands with AI-specific types

**2030:** Non-schemaed content virtually invisible to AI

---

## Combining Techniques

Use with:
- [AI Discovery Singularity (AAO)](./ai-discovery-singularity.md) - Why schema matters
- [Brand Archaeology](./brand-archaeology.md) - What to put in your schema
- [Quantum Brand Engine](./quantum-brand-engine.md) - Schema for multiple brand realities

---

## Practice Exercise

**Schema Your Homepage:**

1. Write Organization schema for your company
2. Include all contact information
3. Add social media links
4. Validate with Google Rich Results Test
5. Deploy to production

**Time: 10 minutes**

---

## The Philosophy

**Schema isn't SEO. It's communication.**

You're telling machines:
- Who you are
- What you do
- Where you are
- How much you cost
- Who trusts you

**Clear communication = AI can understand, trust, and cite you.**

---

*"If your data isn't structured, AI can't understand it. If AI can't understand it, you're invisible."* 🗺️

**Master Schema.org. Speak machine.** ⚛️

---

[← Back to Business Applications](../business/)
