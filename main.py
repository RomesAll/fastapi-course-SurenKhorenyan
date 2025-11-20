from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_oauth2_redirect_html,
    get_swagger_ui_html
)
import uvicorn
'''
        Swagger UI и ReDoc — инструменты для автоматической документации API, встроенные в фреймворк FastAPI. 
        Они генерируют интерактивную документацию на основе стандарта OpenAPI (ранее Swagger).

        Адреса интерфейсов: по умолчанию FastAPI устанавливает Swagger UI по адресу /docs и ReDoc — /redoc. 
        Можно настроить эти адреса, если нужно. 

        Swagger UI — интерактивный интерфейс для изучения и тестирования конечных точек API. Позволяет: 
        - просматривать все доступные конечные точки и их описания;
        - тестировать запросы к API прямо из браузера;
        - понимать схемы запросов и ответов.

        Особенности:
        - отображает подробную информацию о каждой конечной точке, включая параметры, модели запросов и ответов, и примеры запросов;
        - есть кнопка «Попробовать» — позволяет отправлять запросы к API прямо из браузера и просматривать ответы в реальном времени.

        ReDoc — альтернативный интерфейс для документации API. Предлагает: 
        - чистый дизайн в три панели;
        - поддержку вложенных объектов;
        - улучшенную читаемость для больших API;
        - поддержку глубокой ссылки.

        Особенности:
        - автоматически генерирует документацию для API, включая название, описание и версию, 
            все конечные точки, организованные по тегам, параметры запросов и модели ответов;
        - позволяет настраивать документацию, например, добавлять метаданные в конструктор FastAPI.
'''
app = FastAPI(docs_url=None, redoc_url=None)

@app.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url= app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@2/bundles/redoc.standalone.js",
    )

@app.get('/home')
def get_home_page():
    return {'message': 'hello world'}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)