import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.19368, 0.09208).lineTo(0.19368, 0.09208).lineTo(0.19368, -0.09208).lineTo(-0.19368, -0.09208).lineTo(-0.19368, 0.09208).close()
solid=wp_sketch0.add(loop0).extrude(-0.6235889494832736)
