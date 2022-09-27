from typing import Optional
from fastapi import APIRouter, status, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['phone', 'laptop', 'headphones']

@router.get('/all')
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[str] = Header(None)):
    return products

@router.get('/{id}', responses={
    200 : {
        "content":{
            "text/html":{
               "example": "<div>Product</div>"
            }
        },
        "description" : "Returns the HTML for an object"
    },
    400: {
          "content":{
            "text/plain":{
                "example":"Product not available"
            }
        },
        "description" : "A cleartext error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=status.HTTP_404_NOT_FOUND, content=out, media_type="plain/text")
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
                .product {{
                    width:500px;
                    height:30px;
                    border: 2px inset green;
                    background-color: lightblue;
                    text-align: center
                }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")