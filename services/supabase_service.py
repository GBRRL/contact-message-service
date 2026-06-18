from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
def buscar_contatos():
    response = (
        supabase
        .table("contatos")
        .select("*")
        .execute()
    )
    return response.data
