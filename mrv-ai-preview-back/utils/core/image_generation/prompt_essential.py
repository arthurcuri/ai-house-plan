# PROMPTS ESSENTIAL - Basic and functional MRV standard

# QUARTO PEQUENO ESSENTIAL
def quarto_pequeno_essential(comodo):
    return f"""
Create a photorealistic 3D image of a small bedroom with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV ESSENTIAL standard, focusing on functionality and simple finishes. Consider the following features observed in the reference images:

- Single beds: one or two, side by side or bunk bed, with neutral bedding and light or grayish quilts.
- Simple MDF wardrobes in white or wood tones, built-in or with plain doors.
- Compact desk or study bench under the window, with a simple chair (office style or white Eames).
- Discreet children/teen decoration: shelves with books, toys, themed paintings (animals, quotes).
- Walls with two-tone paint (light green, gray or beige) or polka dot wallpaper.
- Generous natural lighting coming from a side window with blind or light curtain.
- Light-colored or soft wood vinyl/laminate flooring.

The environment should convey practicality and comfort, ideal for children or teenagers, with functional furniture and economical decoration.
"""

# QUARTO CASAL ESSENTIAL
def quarto_casal_essential(comodo):
    return f"""
Create a realistic 3D image of a master bedroom with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with simple, comfortable and functional decoration. Consider the following elements based on the reference images:

- Double bed centered, with upholstered or slatted headboard in green, beige or rattan tones.
- Light bedding, layered blankets (olive green, nude, beige).
- Built-in MDF wardrobe in wood tones with plain or slatted doors.
- Long, thin curtains in off-white tones.
- Neutral walls or two-tone paint (e.g., moss green, terracotta, light beige).
- TV on the wall opposite the bed, shelves or niches with light decoration.
- Light wood vinyl or laminate flooring.
- Ample natural lighting with side light entry.

The decoration should be economical, cozy and consistent with MRV’s most basic finish standard, prioritizing practicality and soft aesthetics.
"""

# SALA ESSENTIAL
def sala_essential(comodo):
    return f"""
Create a realistic 3D image of an integrated living and dining room with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The decoration must follow the MRV ESSENTIAL standard, focusing on simple, cozy and functional environments. Base it on the following references:

- Straight sofa with 2 to 3 seats, in light tones (beige, sand or gray), with earthy or green cushions.
- TV panel or simple wood MDF rack.
- Light and plain rug, partially covering the living area.
- Flat-screen TV installed on the wall opposite the sofa.
- Compact dining table for 2 or 4 seats, with wood or straw chairs.
- Background wall in neutral or accent color (moss green, terracotta, gray).
- Light decoration with plant pots, corner lamp, mirrors or decorative niches.
- Light-colored wood vinyl or laminate flooring.
- Abundant natural lighting coming from windows with translucent curtains.

The proposal should convey a contemporary, functional and well-lit space, suitable for MRV’s economical finish standard.
"""

# ÁREA PRIVATIVA ESSENTIAL
def area_privativa_essential(comodo):
    return f"""
Create a photorealistic 3D image of a private outdoor area with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located outside the apartment, following the MRV ESSENTIAL standard.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

Consider the following references from the images:

- Partially grassed floor (natural or synthetic) with concrete areas.
- Small round table with 2 to 4 simple chairs, in metal, plastic or wood.
- Decorative plants in pots in the corners or along the walls.
- Plain background wall in sand or white tones, with simple finish.
- Generous natural lighting and, if nighttime, include garden spotlights or a modern outdoor post.
- Simple decorative items: wooden bench with cushions, poufs, loungers or doghouse.
- Organized, functional and inviting appearance, without excess.

The environment should convey an intimate and economical leisure area, ideal for relaxing or small outdoor moments.
"""

# BANHEIRO ESSENTIAL
def banheiro_essential(comodo):
    return f"""
Create a photorealistic 3D image of a bathroom with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with simple and functional finishes:

- Conventional white toilet, with attached tank.
- Simple white porcelain sink with basic granite or marble countertop.
- Shower with simple control, no shower head or hydromassage.
- Basic finish: white or beige tiles up to mid-height, paint above.
- Neutral-toned (white, beige, light gray) non-slip ceramic flooring.
- Simple rectangular mirror above the sink.
- Basic lighting with central lamp or simple wall sconce.
- Light-colored towels, liquid soap, toilet paper.

The environment must be clean, functional and economical, without unnecessary luxuries.
"""

# COZINHA ESSENTIAL
def cozinha_essential(comodo):
    return f"""
Create a photorealistic 3D image of a kitchen with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with basic furniture and appliances:

- MDF cabinets in white or wood tones, with plain doors and simple handles.
- Granite or formica countertop, in white or beige.
- Simple 4-burner stove, basic white refrigerator, microwave.
- Simple stainless steel sink with conventional faucet.
- White tile backsplash on the sink wall.
- Light-colored, non-slip ceramic flooring.
- Lighting with central lamp and under-cabinet lights (optional).
- Basic utensils: pots, plates, some spices, dish towel.

The environment must be practical, clean and functional, suitable for everyday life.
"""

# VARANDA ESSENTIAL
def varanda_essential(comodo):
    return f"""
Create a photorealistic 3D image of a balcony with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ESSENTIAL standard, focusing on practicality and comfort:

- Small set of table and chairs in synthetic fiber or aluminum in neutral tones (beige, gray).
- Planter or pots with small, low-maintenance plants.
- Light-toned non-slip ceramic flooring.
- Aluminum and tempered glass railing.
- Spot or simple wall sconce lighting.
- External blind-type curtain (optional).
- Simple rubber mat (optional).
- Minimalist decoration with one or two decorative elements.

The environment should be cozy and functional, ideal for outdoor relaxation, while maintaining MRV’s economical Essential line.
"""

# GENÉRICO ESSENTIAL
def generico_essential(comodo):
    return f"""
Create a generic 3D image for the room '{comodo['nome']}' with dimensions {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

Simple decoration in MRV ESSENTIAL standard:
- Functional furniture in white or wood MDF
- Neutral colors (white, beige, light gray)
- Basic natural and artificial lighting
- Economical and practical finish
- Clean and organized environment
"""


# LAVANDERIA ESSENTIAL
def lavanderia_essential(comodo):
    return f"""
Create a photorealistic 3D image of a laundry room with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with simple and functional finishes:

- Washing machine and dryer side by side or stacked, in white or light gray.
- Utility sink with storage below, simple white porcelain or stainless steel.
- Wall-mounted cabinets in white MDF for detergents and cleaning supplies.
- Drying rack or retractable clothesline on the wall.
- Simple white tiles on walls, easy to clean.
- Non-slip ceramic flooring in light tones (white, beige, light gray).
- Basic lighting with central lamp or simple wall sconce.
- Simple organization: baskets, hangers, ironing board storage.
- Functional and organized appearance, maximizing space efficiency.

The environment must be practical, clean and functional, suitable for daily laundry tasks.
"""

# ESCRITÓRIO ESSENTIAL
def escritorio_essential(comodo):
    return f"""
Create a photorealistic 3D image of a home office with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, focusing on functionality and simple finishes:

- Simple desk in white MDF or light wood, with drawers.
- Ergonomic office chair in neutral tones (black, gray, beige).
- Wall-mounted shelves in white MDF for books and files.
- Basic desk lamp for task lighting.
- Neutral walls (white, light gray, beige) or two-tone paint.
- Light wood vinyl or laminate flooring.
- Natural lighting from window with simple curtain or blind.
- Minimal decoration: calendar, plant, simple storage boxes.
- Organized and functional workspace appearance.

The environment should convey practicality and comfort, ideal for work or study, with functional furniture and economical decoration.
"""

# CLOSET ESSENTIAL
def closet_essential(comodo):
    return f"""
Create a photorealistic 3D image of a walk-in closet with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with simple and functional organization:

- Built-in MDF wardrobes in white or light wood tones, with plain doors or sliding doors.
- Hanging rods at different heights for shirts and pants.
- Shelves for folded clothes and accessories.
- Simple drawers for small items.
- Basic lighting with LED strips under shelves or central lamp.
- Light-colored flooring (vinyl, laminate or ceramic).
- Simple mirror on door or wall.
- Basic organization: hangers, storage boxes, shoe rack.
- Functional and organized appearance, maximizing storage space.

The environment must be practical and organized, suitable for storing clothes and accessories efficiently.
"""

# SUITE ESSENTIAL
def suite_essential(comodo):
    return f"""
Create a photorealistic 3D image of a master suite (bedroom with private bathroom) with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with simple, comfortable and functional decoration:

- Double bed centered, with upholstered or slatted headboard in green, beige or rattan tones.
- Light bedding, layered blankets (olive green, nude, beige).
- Built-in MDF wardrobe in wood tones with plain or slatted doors.
- Private bathroom access visible or integrated.
- Long, thin curtains in off-white tones.
- Neutral walls or two-tone paint (e.g., moss green, terracotta, light beige).
- TV on the wall opposite the bed, shelves or niches with light decoration.
- Light wood vinyl or laminate flooring.
- Ample natural lighting with side light entry.

The decoration should be economical, cozy and consistent with MRV's most basic finish standard, prioritizing practicality and soft aesthetics with the convenience of a private bathroom.
"""

# CORREDOR ESSENTIAL
def corredor_essential(comodo):
    return f"""
Create a photorealistic 3D image of a corridor/hallway with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ESSENTIAL standard, focusing on functionality and circulation:

- Light-colored walls (white, beige, light gray) or two-tone paint.
- Simple wall-mounted lighting (sconces or LED strips).
- Light wood vinyl or laminate flooring, or light ceramic tiles.
- Minimal decoration: simple wall art, mirror, or small shelf.
- Functional elements: coat hooks, small console table (if space allows).
- Clean and uncluttered appearance, prioritizing circulation flow.
- Natural lighting from adjacent rooms or windows if available.

The environment should be functional and welcoming, facilitating movement between rooms without visual clutter.
"""

# HALL ESSENTIAL
def hall_essential(comodo):
    return f"""
Create a photorealistic 3D image of an entrance hall with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ESSENTIAL standard, focusing on functionality and welcoming appearance:

- Simple console table or small bench in white MDF or light wood.
- Wall mirror above console, simple rectangular or round frame.
- Coat hooks or small coat rack for outerwear.
- Light-colored walls (white, beige, light gray) or accent wall.
- Light wood vinyl or laminate flooring, or light ceramic tiles.
- Basic lighting with central lamp or wall sconces.
- Minimal decoration: small plant, key holder, simple wall art.
- Shoe storage: simple rack or small cabinet.
- Clean and organized appearance, creating a welcoming first impression.

The environment should be functional and inviting, suitable for receiving guests and organizing daily items.
"""

# SACADA ESSENTIAL
def sacada_essential(comodo):
    return f"""
Create a photorealistic 3D image of a balcony/sacada with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV ESSENTIAL standard, focusing on practicality and comfort:

- Small set of table and chairs in synthetic fiber or aluminum in neutral tones (beige, gray).
- Planter or pots with small, low-maintenance plants.
- Light-toned non-slip ceramic flooring.
- Aluminum and tempered glass railing.
- Spot or simple wall sconce lighting.
- External blind-type curtain (optional).
- Simple rubber mat (optional).
- Minimalist decoration with one or two decorative elements.
- Functional storage: small outdoor cabinet or bench with storage.

The environment should be cozy and functional, ideal for outdoor relaxation, while maintaining MRV's economical Essential line.
"""

# ÁREA GOURMET ESSENTIAL
def area_gourmet_essential(comodo):
    return f"""
Create a photorealistic 3D image of a gourmet area with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, with functional outdoor cooking and dining area:

- Simple barbecue grill or built-in barbecue in basic finish.
- Counter or table for food preparation, in granite or formica.
- Dining table for 4 to 6 people, in wood or synthetic material.
- Simple chairs in synthetic fiber or aluminum, weather-resistant.
- Basic storage: simple cabinet for utensils and supplies.
- Light-toned non-slip ceramic flooring.
- Basic lighting: wall sconces or spotlights.
- Simple decoration: plants in pots, basic outdoor accessories.
- Functional and inviting appearance, suitable for outdoor dining and socializing.

The environment must be practical and functional, ideal for outdoor cooking and dining, maintaining MRV's economical finish standard.
"""

# HOME OFFICE ESSENTIAL
def home_office_essential(comodo):
    return f"""
Create a photorealistic 3D image of a home office with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV ESSENTIAL standard, focusing on functionality and simple finishes:

- Simple desk in white MDF or light wood, with drawers for storage.
- Ergonomic office chair in neutral tones (black, gray, beige).
- Wall-mounted shelves in white MDF for books, files and office supplies.
- Basic desk lamp for task lighting.
- Neutral walls (white, light gray, beige) or two-tone paint.
- Light wood vinyl or laminate flooring.
- Natural lighting from window with simple curtain or blind.
- Minimal decoration: calendar, small plant, simple storage boxes, whiteboard.
- Organized and functional workspace appearance.

The environment should convey practicality and comfort, ideal for remote work or study, with functional furniture and economical decoration.
"""