# PROMPTS CLASS - Premium and sophisticated MRV standard

# SMALL BEDROOM CLASS
def quarto_pequeno_class(comodo):
    return f"""
Create a photorealistic 3D image of a small bedroom CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV CLASS standard, with premium finish and sophisticated design:

- Single beds in noble wood (cherry, mahogany) with premium upholstery.
- Bedding in noble fabrics: Egyptian percale, silk, premium linen (sophisticated colors).
- Planned wardrobes in noble wood with glossy lacquered finish, noble metal handles.
- Executive-style desk in solid wood, premium ergonomic chair.
- Sophisticated decoration: framed paintings, awards, art objects, classic books.
- Walls with textured wallpaper, decorative moldings or noble wood panels.
- Smart lighting: directional spots, designer table lamps, controllable RGB LED.
- Flooring in noble wood (oak, tauari) or premium porcelain with marble finish.
- Motorized curtains in noble fabrics with integrated blackout.
- Integrated technology: smart TV, ambient sound system, temperature control.

The environment should convey sophistication, premium comfort and cutting-edge technology.
"""

# MASTER BEDROOM CLASS
def quarto_casal_class(comodo):
    return f"""
Create a realistic 3D image of a master bedroom CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with maximum refinement and comfort:

- King-size bed in noble wood with premium upholstered headboard (Italian leather or velvet).
- Bedding in luxurious fabrics: silk, Egyptian percale, Belgian linen (sophisticated tones).
- Integrated walk-in closet in noble wood with internal LED lighting and mirrors.
- Master suite with hydromassage bathtub visible through glass wall.
- Walls with premium finish: imported wallpaper, 3D panel or noble wood.
- Motorized curtains with imported fabrics, blackout system and remote control.
- Scenic lighting: designer chandelier, RGB spots, perimeter indirect lighting.
- Flooring in noble wood or Italian porcelain with natural veins.
- Premium technology: retractable OLED TV, surround sound system, smart climate control.
- Designer furniture: leather armchair, marble side table, art objects.

The environment should be a luxury refuge with 5-star hotel comfort.
"""

# LIVING ROOM CLASS
def sala_class(comodo):
    return f"""
Create a realistic 3D image of an integrated living and dining room CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The decoration must follow the MRV CLASS standard, with maximum refinement and sophistication:

- Premium modular sofa in Italian leather or imported fabric, velvet cushions.
- Complete home theater: 75" OLED TV, 7.1 surround sound system, retractable projector.
- Dining table in noble wood or Carrara marble with designer upholstered chairs.
- TV panel in noble wood with piano lacquer, integrated LED lighting.
- Persian or Italian designer rug, noble materials (silk, premium wool).
- Walls with premium finish: imported wallpaper, 3D panel, natural marble.
- Scenic lighting: crystal chandelier, directional spots, controllable perimeter RGB LED.
- Flooring in noble wood (tauari, ipê) or premium Italian porcelain.
- Integrated bar with climate-controlled wine cellar, marble counter, premium coffee machine.
- Art objects: sculptures, original paintings, Murano crystal vases, expensive ornamental plants.
- Integrated technology: home automation, motorized curtains, individual climate control.

The environment should rival luxury penthouses, with imported materials and finishes.
"""

# PRIVATE AREA CLASS
def area_privativa_class(comodo):
    return f"""
Create a photorealistic 3D image of a private outdoor area CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located outside the apartment, following the MRV CLASS standard.

Premium terrace characteristics:

- Deck in noble wood (teak, cumaru) with resistant naval finish.
- Premium outdoor furniture: modular sofas in luxury synthetic fiber, designer waterproof cushions.
- Gourmet barbecue in stainless steel with hood, integrated sink and marble counter.
- Landscaped garden: expensive ornamental plants, palm trees, automated irrigation system.
- Scenic lighting: spots embedded in deck, phytotecs for plants, perimeter RGB lighting.
- Pergola in noble wood with motorized retractable curtains.
- Mini-pool or spa with hydromassage, wet deck in natural stone.
- Outdoor ambient sound system, USB outlets integrated in furniture.
- Wall finish in natural stone or large format porcelain.
- Luxurious elements: ecological fireplace, wet bar, integrated wine cooler.
- Landscaping with rare plants and automatic misting system.

The environment should simulate a luxury hotel rooftop with panoramic view.
"""

# BATHROOM CLASS
def banheiro_class(comodo):
    return f"""
Create a photorealistic 3D image of a bathroom CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with premium spa finish:

- Wall-hung smart toilet with electronic bidet and seat heating.
- Double vanity in Carrara marble with premium porcelain or natural stone basins.
- Shower with 10mm tempered glass, ceiling rain shower + side shower + chromotherapy.
- Hydromassage bathtub in marble or premium fiber with integrated LED lighting.
- Finish in natural marble or large format porcelain with glossy finish.
- Heated floor in premium non-slip porcelain with marble pattern.
- Mirrors with perimeter LED lighting, anti-fog function and touch screen.
- Scenic lighting: directional spots, RGB LED for chromotherapy, premium chandelier.
- Planned furniture in noble wood or glossy lacquer with golden handles.
- Premium accessories: heated towel racks, automatic soap dispensers, golden faucets.
- Technology: Bluetooth sound system, radiant floor heating, silent exhaust fans.

The environment should rival 5-star resort spas.
"""

# KITCHEN CLASS
def cozinha_class(comodo):
    return f"""
Create a photorealistic 3D image of a kitchen CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with premium gourmet kitchen pattern:

- Planned cabinets in noble wood (cherry, freijó) with lacquered finish, golden handles.
- Central island in Carrara marble with induction cooktop, premium suspended stainless steel hood.
- Premium appliances: side-by-side stainless steel refrigerator, combination oven, built-in microwave.
- Countertop in natural marble or imported quartz with polished finish.
- Integrated climate-controlled wine cellar with glass door and internal LED lighting.
- Finish in large format porcelain or premium subway tiles with fine grout.
- Flooring in Italian porcelain or treated non-slip noble wood.
- Gourmet lighting: directional spots over countertop, LED under cabinets, designer pendants.
- Premium sink in stainless steel or granite with gourmet table faucet, integrated filter.
- Integrated pantry with organizing shelves, internal LED lighting.
- Technology: silent exhaust system, USB outlets, ambient temperature control.

The environment should rival professional gastronomic program kitchens.
"""

# LAUNDRY CLASS
def lavanderia_class(comodo):
    return f"""
Create a photorealistic 3D image of a laundry room CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with premium and functional finish:

- Side-by-side or stacked washing machine and dryer, premium models with smart features.
- Utility sink with premium countertop in marble or natural stone, storage below.
- Wall-mounted cabinets in noble wood with lacquered finish for detergents and supplies.
- Retractable drying rack or premium clothesline system.
- Premium finish: large format porcelain tiles or natural stone, easy to clean.
- Heated floor in premium non-slip porcelain.
- Smart lighting with LED strips under cabinets or premium central fixture with motion sensor.
- Premium organization: designer baskets, wooden hangers, integrated ironing board storage.
- Integrated technology: smart appliance control, humidity sensors, automated systems.

The environment must be practical, luxurious and functional, suitable for premium laundry tasks.
"""

# OFFICE CLASS
def escritorio_class(comodo):
    return f"""
Create a photorealistic 3D image of a home office CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV CLASS standard, with premium executive finish:

- Executive desk in noble wood (cherry, mahogany) with drawers and premium organization.
- Premium ergonomic chair in Italian leather or designer fabric.
- Wall-mounted shelves in noble wood with piano lacquer for books and files.
- Designer desk lamp in premium materials with adjustable LED lighting.
- Walls with premium finish: imported textured wallpaper, decorative moldings or noble wood panels.
- Flooring in noble wood (oak, tauari) or premium Italian porcelain.
- Motorized curtains with imported fabrics, blackout system and remote control.
- Premium decoration: original art, designer objects, classic books, luxury accessories.
- Integrated technology: smart lighting control, ambient sound system, climate control.
- Premium organization: leather organizers, designer storage boxes, premium filing systems.

The environment should convey executive sophistication, premium comfort and cutting-edge technology.
"""

# CLOSET CLASS
def closet_class(comodo):
    return f"""
Create a photorealistic 3D image of a walk-in closet CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with premium organization:

- Planned built-in wardrobes in noble wood with glossy lacquered finish, sliding or hinged doors.
- Hanging rods at different heights in premium materials, with integrated LED lighting.
- Shelves in noble wood with premium organization systems for folded clothes and accessories.
- Premium drawers in noble wood with soft-close mechanisms and golden handles.
- Integrated LED lighting system under shelves and in wardrobe interiors.
- Flooring in noble wood or premium porcelain.
- Full-length mirrors with perimeter LED lighting and anti-fog function.
- Premium organization: designer hangers, luxury storage boxes, premium shoe racks.
- Integrated seating area with designer bench or armchair.
- Smart technology: automated lighting, climate control, integrated sound system.

The environment must be luxurious and organized, maximizing storage space with premium materials and finishes.
"""

# SUITE CLASS
def suite_class(comodo):
    return f"""
Create a realistic 3D image of a master suite CLASS (bedroom with private bathroom) with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with maximum refinement and comfort:

- King-size bed in noble wood with premium upholstered headboard (Italian leather or velvet).
- Bedding in luxurious fabrics: silk, Egyptian percale, Belgian linen (sophisticated tones).
- Integrated walk-in closet in noble wood with internal LED lighting and mirrors.
- Private bathroom access visible or integrated with premium spa features.
- Walls with premium finish: imported wallpaper, 3D panel or noble wood.
- Motorized curtains with imported fabrics, blackout system and remote control.
- Scenic lighting: designer chandelier, RGB spots, perimeter indirect lighting.
- Flooring in noble wood or Italian porcelain with natural veins.
- Premium technology: retractable OLED TV, surround sound system, smart climate control.
- Designer furniture: leather armchair, marble side table, art objects.

The environment should be a luxury refuge with 5-star hotel comfort, with the convenience of a private premium bathroom integrated with spa features.
"""

# HALLWAY CLASS
def corredor_class(comodo):
    return f"""
Create a photorealistic 3D image of a hallway CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV CLASS standard, focusing on circulation and sophistication:

- Walls with premium finish: imported textured wallpaper, decorative moldings or noble wood panels.
- Smart LED lighting (sconces or LED strips) with motion sensors and dimming control.
- Flooring in noble wood (oak, tauari) or premium Italian porcelain.
- Minimalist premium decoration: original art, designer mirrors, small console table in noble wood.
- Functional elements: premium coat hooks, designer console table (if space allows).
- Premium organization: designer storage solutions, luxury accessories.
- Clean and uncluttered appearance, prioritizing circulation flow.
- Natural lighting from adjacent rooms or windows, if available.

The environment should be functional and sophisticated, facilitating movement between rooms with premium finishes.
"""

# ENTRANCE HALL CLASS
def hall_class(comodo):
    return f"""
Create a photorealistic 3D image of an entrance hall CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV CLASS standard, focusing on functionality and sophisticated welcome:

- Console table or designer bench in noble wood or marble.
- Designer mirror above console, with premium frame in noble wood or metal.
- Premium coat hooks or designer coat rack in noble materials.
- Walls with premium finish: imported wallpaper, decorative moldings or noble wood panels.
- Flooring in noble wood, premium porcelain or natural stone.
- Smart LED lighting with motion sensors (premium central fixture or designer sconces).
- Premium decoration: designer art, luxury accessories, premium key holder.
- Premium shoe storage: designer rack or small cabinet in noble wood.
- Premium rug in noble materials (silk, premium wool).

The environment should be functional and sophisticated, creating a luxury first impression with premium finishes.
"""

# BALCONY CLASS
def sacada_class(comodo):
    return f"""
Create a photorealistic 3D image of a balcony CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV CLASS standard, focusing on sophistication and premium outdoor comfort:

- Premium outdoor furniture: designer table and chairs in weather-resistant luxury materials.
- Designer planters with expensive ornamental plants and premium landscaping.
- Premium non-slip porcelain flooring or noble wood deck.
- Premium railing in stainless steel or aluminum with tempered glass.
- Smart outdoor lighting with RGB LED control and motion sensors.
- Motorized outdoor curtains in premium weather-resistant fabrics.
- Premium decorative elements: designer accessories, luxury outdoor rugs.
- Integrated technology: outdoor sound system, USB outlets, climate control.

The environment should be sophisticated and functional, ideal for premium outdoor relaxation, maintaining MRV's luxury CLASS line.
"""

# GOURMET AREA CLASS
def area_gourmet_class(comodo):
    return f"""
Create a photorealistic 3D image of a gourmet area CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The room must follow the MRV CLASS standard, with premium outdoor cooking and dining area:

- Gourmet barbecue in premium stainless steel with integrated hood and premium finish.
- Premium counter or table for food preparation, in Carrara marble or natural stone.
- Designer dining table for 4 to 6 people, in noble wood or premium materials.
- Premium designer chairs in weather-resistant luxury materials.
- Premium storage: designer cabinet in noble wood for utensils and supplies.
- Premium non-slip porcelain flooring or noble wood deck.
- Smart outdoor lighting: designer sconces or premium spotlights with RGB control.
- Premium decoration: designer planters, luxury outdoor accessories, premium landscaping.
- Integrated technology: outdoor sound system, USB outlets, climate control, automated systems.

The environment must be sophisticated and functional, ideal for premium outdoor cooking and dining, maintaining MRV's luxury finish standard.
"""

# HOME OFFICE CLASS
def home_office_class(comodo):
    return f"""
Create a photorealistic 3D image of a home office CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

This room must follow the MRV CLASS standard, with premium executive finish:

- Executive desk in noble wood (cherry, mahogany) with premium drawers and organization.
- Premium ergonomic chair in Italian leather or designer fabric.
- Wall-mounted shelves in noble wood with piano lacquer for books, files and office supplies.
- Designer desk lamp in premium materials with adjustable LED lighting.
- Walls with premium finish: imported textured wallpaper, decorative moldings or noble wood panels.
- Flooring in noble wood (oak, tauari) or premium Italian porcelain.
- Motorized curtains with imported fabrics, blackout system and remote control.
- Premium decoration: original art, designer objects, luxury accessories, premium whiteboard.
- Integrated technology: smart lighting control, ambient sound system, climate control, automation.
- Premium organization: designer storage boxes, luxury filing systems, premium organizers.

The environment should convey executive sophistication and premium comfort, ideal for remote work or study with luxury finishes and cutting-edge technology.
"""

# BALCONY/VARANDA CLASS
def varanda_class(comodo):
    return f"""
Create a photorealistic 3D image of a balcony CLASS with approximately {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

The environment must follow the MRV CLASS standard, focusing on sophistication and premium outdoor comfort:

- Premium outdoor furniture: designer table and chairs in weather-resistant luxury materials (teak, premium synthetic fiber).
- Designer planters with expensive ornamental plants and premium landscaping.
- Premium non-slip porcelain flooring or noble wood deck (teak, cumaru).
- Premium railing in stainless steel or aluminum with tempered glass.
- Smart outdoor lighting with RGB LED control and motion sensors.
- Motorized outdoor curtains in premium weather-resistant fabrics.
- Premium decorative elements: designer accessories, luxury outdoor rugs, premium planters.
- Integrated technology: outdoor sound system, USB outlets, climate control.

The environment should be sophisticated and functional, ideal for premium outdoor relaxation, maintaining MRV's luxury CLASS line with panoramic views.
"""

# GENERIC CLASS
def generico_class(comodo):
    return f"""
Create a generic 3D image for the room '{comodo['nome']}' with dimensions {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, located in the {comodo['localização']} area of the floor plan.

Below, the indication of the furniture, their respective arrangements and decorations observed in the plan. This information will be useful to compose the image more precisely: {comodo.get('notas')}.

Premium decoration in MRV CLASS standard:
- Furniture in noble wood with lacquered finish
- Premium materials: marble, Italian leather, imported fabrics
- Smart scenic lighting (RGB LED, directional spots)
- Integrated technology and home automation
- Art objects and designer decoration
- Luxury finish comparable to 5-star hotels
"""