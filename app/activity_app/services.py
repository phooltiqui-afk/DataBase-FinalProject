from app.database import db

# Colecciones
searches_collection = db["busqueda"]
likes_collection = db["likecontenido"]
playback_collection = db["reproduccion"]


async def get_all_searches():
    return await searches_collection.find().to_list(100)


async def get_all_likes():
    return await likes_collection.find().to_list(100)


async def get_all_playbacks():
    return await playback_collection.find().to_list(100)
