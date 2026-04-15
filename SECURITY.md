# Política de Segurança

## Reportando vulnerabilidades

Se você encontrar uma vulnerabilidade de segurança, **não abra uma issue pública** com detalhes de exploração.

Preferência de reporte:

1. **GitHub Security Advisories**: use “Security” → “Report a vulnerability” (se disponível neste repositório).
2. Se não estiver disponível, abra uma issue com o título **`[SECURITY]`** e descreva apenas o impacto em alto nível (sem PoC/exploit), solicitando um canal privado.

## Boas práticas adotadas

- **TrustedHostMiddleware** com allowlist configurável (`TRUSTED_HOSTS`)
- **CORS restritivo** com allowlist configurável (`CORS_ALLOWED_ORIGINS`)
- **Headers de segurança** em todas as respostas
- **Erros internos sanitizados**: respostas `500` não vazam stack traces/detalhes

